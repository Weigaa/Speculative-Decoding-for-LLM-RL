"""Weekly arXiv discovery. Hits stay pending until primary-source screening."""
import argparse
from datetime import datetime, timedelta, timezone
import time
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from library import ROOT, read_json, write_json, parse_atom, identities, arxiv_identity


def now_utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def fetch(url):
    for attempt in range(3):
        try:
            req = Request(url, headers={"User-Agent": "SpeculativeRolloutSurvey/1.0 (public scholarly metadata index)"})
            with urlopen(req, timeout=40) as response:
                return response.read()
        except Exception as exc:
            if attempt == 2:
                raise
            delay = 4 * (attempt + 1)
            if isinstance(exc, HTTPError) and exc.code == 429:
                retry_after = exc.headers.get("Retry-After", "") if exc.headers else ""
                if retry_after.isdigit() and int(retry_after) > 60:
                    raise  # Do not violate a long server-directed cooldown.
                delay = max(int(retry_after) if retry_after.isdigit() else 12, 12 * (attempt + 1))
            time.sleep(delay)


def merge_hits(hits, papers, queue, screening_log):
    known = {}
    for p in papers:
        for identity in identities(p):
            known[identity] = p
    excluded = set()
    for entry in screening_log:
        if entry.get("decision") == "excluded":
            excluded.update(entry.get("identities", []))
    pending = {c["arxiv_id"]: dict(c) for c in queue}
    versions = []
    added = 0
    for hit in hits:
        match = next((known[i] for i in identities(hit) if i in known), None)
        if match:
            if hit.get("version") and match.get("arxiv_id") == hit["arxiv_id"] and hit["version"] != match.get("reviewed_version", ""):
                versions.append({"id": match["id"], "reviewed_version": match.get("reviewed_version", ""),
                                 "observed_version": hit["version"], "url": hit["url"], "observed_at": hit["updated"]})
            continue
        if identities(hit) & excluded:
            continue
        current = pending.get(hit["arxiv_id"])
        if current:
            queries = sorted(set(current.get("queries", [])) | set(hit["queries"]))
            registry_hit = bool(hit.get("metadata_source"))
            registry_current = bool(current.get("metadata_source"))
            if (not registry_hit and registry_current) or (registry_hit == registry_current and hit["updated"] > current["updated"]):
                if not registry_hit:
                    current.pop("metadata_source", None)
                    current.pop("metadata_record_url", None)
                current.update(hit)
            current["queries"] = queries
        else:
            # Different identifiers with the same normalized title are consolidated.
            duplicate = next((q for q in pending.values() if identities(q) & identities(hit)), None)
            if duplicate:
                duplicate["queries"] = sorted(set(duplicate.get("queries", [])) | set(hit["queries"]))
                duplicate.setdefault("alternate_urls", []).append(hit["url"])
                continue
            pending[hit["arxiv_id"]] = {**hit, "status": "pending"}
            added += 1
    return sorted(pending.values(), key=lambda x: x["updated"], reverse=True), versions, added


def parse_datacite(data):
    payload = json.loads(data)
    if "data" not in payload or not isinstance(payload["data"], list):
        raise ValueError("Expected a DataCite DOI-list response")
    entries = []
    for record in payload["data"]:
        a = record["attributes"]
        doi = a.get("doi", "")
        if not doi.casefold().startswith("10.48550/arxiv."):
            continue
        aid = arxiv_identity(doi)
        if not aid or not a.get("updated") or not a.get("titles"):
            raise ValueError("Incomplete arXiv DOI metadata")
        abstract = next((d.get("description", "") for d in a.get("descriptions", []) if d.get("descriptionType") == "Abstract"), "")
        entries.append({"arxiv_id": aid, "doi": doi, "version": "", "title": a["titles"][0]["title"],
                        "authors": [c.get("name", "") for c in a.get("creators", [])],
                        "published": str(a.get("publicationYear", "")), "updated": a["updated"],
                        "abstract": abstract, "url": "https://arxiv.org/abs/" + aid,
                        "metadata_source": "DataCite arXiv DOI registry", "metadata_record_url": "https://api.datacite.org/dois/" + doi})
    return entries, payload.get("meta", {}).get("total", len(entries))


def merge_version_observations(prior, observed):
    """Keep curator reviews when a search encounters the same version again."""
    index = {(v["id"], v["observed_version"]): dict(v) for v in prior}
    for version in observed:
        key = (version["id"], version["observed_version"])
        index[key] = {**index.get(key, {}), **version}
    return sorted(index.values(), key=lambda v: (v["id"], v["observed_version"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lookback-days", type=int, default=14)
    ap.add_argument("--max-pages", type=int, default=10)
    args = ap.parse_args()
    state_path = ROOT / "data/update_state.json"
    state = read_json(state_path, {})
    timestamp = now_utc()
    default_since = datetime.now(timezone.utc) - timedelta(days=args.lookback_days)
    previous = state.get("last_successful_scan")
    if previous:
        # A failed weekly run must not create a gap. Retain a two-day overlap.
        default_since = min(default_since, datetime.fromisoformat(previous.replace("Z", "+00:00")) - timedelta(days=2))
    elif state.get("since") and state.get("status") == "incomplete":
        default_since = min(default_since, datetime.fromisoformat(state["since"].replace("Z", "+00:00")))
    since = default_since.isoformat(timespec="seconds").replace("+00:00", "Z")
    config = read_json(ROOT / "data/search_queries.json")
    hits, logs, failures = [], [], []
    arxiv_throttled = False
    for family in config["families"]:
        row = {"family": family["id"], "query": family["query"], "since": since, "urls": [], "records": 0}
        try:
            if arxiv_throttled:
                raise RuntimeError("Not attempted: arXiv requested cooldown earlier in this run")
            complete = False
            for page in range(args.max_pages):
                url = "https://export.arxiv.org/api/query?" + urlencode({
                    "search_query": family["query"], "start": page * 100, "max_results": 100,
                    "sortBy": "lastUpdatedDate", "sortOrder": "descending"})
                row["urls"].append(url)
                entries, total = parse_atom(fetch(url))
                for entry in entries:
                    if not entry["updated"]:
                        raise ValueError("Missing updated timestamp")
                    if entry["updated"] >= since:
                        hits.append({**entry, "queries": [family["id"]], "discovered_at": timestamp})
                        row["records"] += 1
                if not entries or len(entries) < 100 or (page + 1) * 100 >= total or entries[-1]["updated"] < since:
                    complete = True
                    break
                time.sleep(3.2)
            if not complete:
                raise RuntimeError("Result pagination limit reached before covering the date window")
            row["status"] = "success"
        except Exception as exc:
            row.update(status="incomplete", error=f"{type(exc).__name__}: {exc}")
            failures.append(family["id"])
            if isinstance(exc, HTTPError) and exc.code == 429:
                arxiv_throttled = True
        logs.append(row)
        print(f"{family['id']}: {row['status']} ({row['records']} recent records)", flush=True)
        time.sleep(3.2)
    # A second official metadata source supplies useful discovery during arXiv
    # outages. Registry update time is not an arXiv paper-version timestamp.
    for family in config["families"]:
        family_id = "datacite-" + family["id"]
        query = "(" + family["query"].replace("all:", "") + ") AND updated:[" + since + " TO *]"
        row = {"family": family_id, "source": "DataCite arXiv DOI registry", "query": query, "since": since, "urls": [], "records": 0}
        try:
            complete = False
            for page in range(args.max_pages):
                url = "https://api.datacite.org/dois?" + urlencode({"query": query, "prefix": "10.48550", "sort": "-updated", "page[size]": 100, "page[number]": page + 1})
                row["urls"].append(url)
                entries, total = parse_datacite(fetch(url))
                for entry in entries:
                    if entry["updated"] >= since:
                        hits.append({**entry, "queries": [family_id], "discovered_at": timestamp})
                        row["records"] += 1
                if len(entries) < 100 or (page + 1) * 100 >= total or entries[-1]["updated"] < since:
                    complete = True
                    break
                time.sleep(3.2)
            if not complete:
                raise RuntimeError("DataCite pagination limit reached")
            row["status"] = "success"
        except Exception as exc:
            row.update(status="incomplete", error=f"{type(exc).__name__}: {exc}")
            failures.append(family_id)
        logs.append(row)
        print(f"{family_id}: {row['status']} ({row['records']} recent metadata records)", flush=True)
        time.sleep(3.2)
    log_path = ROOT / "data/screening_log.jsonl"
    screened = [__import__("json").loads(x) for x in log_path.read_text().splitlines() if x.strip()] if log_path.exists() else []
    queue, observed, added = merge_hits(hits, read_json(ROOT / "data/papers.json"), read_json(ROOT / "data/inbox.json", []), screened)
    prior_versions = read_json(ROOT / "data/version_observations.json", [])
    write_json(ROOT / "data/inbox.json", queue)
    write_json(ROOT / "data/version_observations.json", merge_version_observations(prior_versions, observed))
    state.update(last_attempt=timestamp, status="incomplete" if failures else "success", since=since,
                 pending_candidates=len(queue), newly_discovered=added, failures=failures,
                 note="Automated arXiv and DataCite discovery. DataCite dates are registry-update dates, not paper-version dates. Hits require primary-source screening.")
    if not failures:
        state["last_successful_scan"] = timestamp
    write_json(state_path, state)
    stamp = timestamp.replace(":", "-")
    write_json(ROOT / f"updates/logs/{stamp}.json", {"timestamp": timestamp, "since": since, "status": state["status"], "queries": logs})
    if failures:
        raise SystemExit("Incomplete search: " + ", ".join(failures))


if __name__ == "__main__":
    main()
