"""Build the browsing views from the curated JSON library; no network access."""
import argparse
from collections import Counter
from pathlib import Path
from library import ROOT, read_json, md, checked_url

EVIDENCE = {
    "direct_rl": "Direct RL rollout / training",
    "serving_transfer": "Serving / inference — RL transfer potential",
    "contextual": "Contextual evidence",
    "supporting": "Background / related survey / infrastructure",
}


def build():
    records = read_json(ROOT / "data/papers.json")
    snapshot = read_json(ROOT / "data/manuscript_snapshot.json")
    taxonomy = read_json(ROOT / "data/taxonomy.json")
    out = {}
    core = [p for p in records if p["id"] in snapshot["core_ids"]]
    live = [p for p in records if p["id"] not in snapshot["bibliography_ids"]]
    counts = Counter(p["evidence"] for p in core)
    intro = (ROOT / "docs/readme_intro.md.in").read_text()
    lines = [intro.rstrip(), "", "## Library status", "",
             f"- Manuscript literature cutoff: **{snapshot['cutoff']}**.",
             f"- Frozen core: **{len(core)}** unique studies, including **{counts['direct_rl']}** with direct RL evidence and **{counts['serving_transfer']}** serving-origin transfer studies.",
             f"- Imported bibliography: **{len(snapshot['bibliography_ids'])}** records, of which **{len(snapshot['cited_ids'])}** appear in the manuscript PDF.",
             f"- Screened additions after the cutoff: **{len(live)}**. These do not alter the manuscript snapshot.",
             "", "## Browse by the manuscript taxonomy", "",
             "A study may appear under several dimensions. Every study has one canonical record and is counted once.", ""]
    for branch in taxonomy:
        selected = [p for p in core if set(p["dimensions"]) & {d["id"] for d in branch["dimensions"]}]
        lines += [f"### [{branch['title']}]({branch['path']}/README.md)", ""]
        btext = [f"# {branch['title']}", "", branch["description"], "", "[Back to index](../../README.md)", ""]
        for dimension in branch["dimensions"]:
            matches = [p for p in records if dimension["id"] in p["dimensions"]]
            dest = f"{branch['path']}/{dimension['id']}.md"
            lines.append(f"- [{dimension['title']}]({dest}) — {len(matches)} studies")
            btext.append(f"- [{dimension['title']}]({dimension['id']}.md)")
            content = [f"# {dimension['title']}", "", dimension["description"], "", "[Branch index](README.md)", "",
                       "| Study | Year | Evidence setting | Snapshot |", "|---|---|---|---|"]
            for p in matches:
                tag = "Manuscript core" if p["id"] in snapshot["core_ids"] else "Post-cutoff screened addition"
                content.append(f"| [{md(p['name'])}](../../papers/{p['id']}.md) | {p['year']} | {EVIDENCE[p['evidence']]} | {tag} |")
            out[dest] = "\n".join(content) + "\n"
        lines.append("")
        btext += ["", f"{len(selected)} distinct manuscript-core studies in this branch. Cross-branch totals must not be summed."]
        out[branch["path"] + "/README.md"] = "\n".join(btext) + "\n"
    lines += ["## Other reading lists", "",
              "- [Related surveys](supporting/related-surveys.md)",
              "- [Background, foundational methods, and infrastructure](supporting/background.md)",
              "- [Contextual evidence on actions, observations, and numerical fidelity](supporting/contextual-evidence.md)",
              "- [All records](docs/all-papers.md)",
              "- [New candidates awaiting screening](updates/candidates.md)",
              "- [Version observations](updates/versions.md)",
              "- [Manuscript snapshot](docs/manuscript-snapshot.md)",
              "- [Search and inclusion protocol](docs/search-protocol.md)",
              "- [Maintenance instructions](CONTRIBUTING.md)", "",
              "## Weekly updates", "",
              "GitHub Actions checks arXiv and its DataCite DOI registry every Monday at **08:17 Asia/Shanghai** (00:17 UTC). It deduplicates discoveries, records version changes, and commits the candidate queue and search log. You can also run it from the Actions tab. The workflow uses no paid API or secret.", "",
              "A separate weekly curator review is configured in the maintainer's Codex chat. Primary-source screening is required before a candidate enters the curated taxonomy. The hosted discovery job works independently of the maintainer's computer; the curator run requires its configured host to be available.", "",
              "A successful empty search is reported as such. Failed or truncated searches are recorded as incomplete and do not advance the last-success timestamp. Scheduled GitHub runs can be delayed, and GitHub may disable schedules in inactive public repositories.", "",
              "## Bibliography and citation", "",
              "- [All imported and curated references](bibliography/references.bib)",
              "- [The frozen 46-study core](bibliography/manuscript-core.bib)",
              "- [SCIS-compatible BibTeX](bibliography/references-scis.bib)", "",
              "BibTeX metadata was imported from the author's working bibliography. Field-level checks are recorded per paper; import does not imply that every author/venue field has been independently reverified. arXiv posting is not a peer-review certificate.", "",
              "The companion manuscript is **Speculative Decoding for LLM Reinforcement Learning: A Survey of Algorithms, Systems, and Training Semantics**. Its journal submission is in preparation. No acceptance, DOI, or publication date is claimed. Use [CITATION.cff](CITATION.cff) to cite this repository.", "",
              "## Rights", "",
              "Paper PDFs are linked from their original sources and are not redistributed here. Third-party articles and artifacts retain their original licenses. Repository scripts and original editorial notes are covered by the [MIT license](LICENSE)."]
    out["README.md"] = "\n".join(lines) + "\n"
    support = {
        "related-surveys": ("Related surveys", lambda p: p["role"] == "related_survey"),
        "background": ("Background and infrastructure", lambda p: p["role"] in {"background", "bibliography_only"}),
        "contextual-evidence": ("Contextual evidence", lambda p: p["evidence"] == "contextual"),
    }
    for slug, (title, predicate) in support.items():
        items = [f"# {title}", "", "These records are excluded from the 46-study taxonomy corpus.", "", "[Back to index](../README.md)", ""]
        items += [f"- [{md(p['title'])}](../papers/{p['id']}.md) ({p['year']})" for p in records if predicate(p)]
        out[f"supporting/{slug}.md"] = "\n".join(items) + "\n"
    all_lines = ["# All papers", "", "[Back to index](../README.md)", "", "| Key | Study | Role |", "|---|---|---|"]
    for p in records:
        dims = {d["id"]: d["title"] for b in taxonomy for d in b["dimensions"]}
        links = "\n".join(f"- {dims[d]}" for d in p["dimensions"]) or "Outside the core taxonomy."
        lines = [f"# {md(p['name'])}", "", f"**{md(p['title'])}**", "",
                 f"- Citation key: `{p['id']}`", f"- Authors: {md(p['authors'])}",
                 f"- Year: {p['year']}", f"- Bibliographic venue: {md(p['venue'])}",
                 f"- Source: [paper]({checked_url(p['url'])})", f"- Evidence setting: **{EVIDENCE[p['evidence']]}**",
                 f"- Library role: `{p['role']}`", f"- Cited in the manuscript PDF: {'yes' if p['manuscript_cited'] else 'no (bibliography-only import)'}",
                 f"- Reviewed arXiv version: {md(p.get('reviewed_version') or 'not recorded')}", "",
                 "## Mechanism / relevance", "", p["mechanism"], "", "## Evidence and transfer boundary", "", p["evidence_note"], "",
                 "## Taxonomy dimensions", "", links, "", "## Source and artifact record", "",
                 f"- Metadata provenance: {p['metadata_provenance']}", f"- Evidence pointer: {p.get('evidence_pointer') or 'Manuscript synthesis; individual source locations not yet indexed.'}",
                 f"- Source publication date: {p.get('published') or 'not recorded'}",
                 "- Released code: " + (", ".join(f"[official artifact]({checked_url(u)})" for u in p.get("code_urls", [])) or "not recorded (not a claim of non-availability)"),
                 "", "## BibTeX", "", "```bibtex", p["bibtex"], "```", "", "[Back to all records](../docs/all-papers.md)"]
        out[f"papers/{p['id']}.md"] = "\n".join(lines) + "\n"
        all_lines.append(f"| `{p['id']}` | [{md(p['title'])}](../papers/{p['id']}.md) | {p['role']} |")
    out["docs/all-papers.md"] = "\n".join(all_lines) + "\n"
    bib = lambda ps: "\n\n".join(p["bibtex"].strip() for p in ps) + "\n"
    out["bibliography/references.bib"] = "% Portable publication metadata.\n" + bib(records)
    out["bibliography/manuscript-core.bib"] = "% Frozen 46-study manuscript corpus, cutoff 2026-10-14.\n" + bib(core)
    import re
    out["bibliography/references-scis.bib"] = "% For SCIS scis.bst, which adds Proceedings of itself.\n" + re.sub(r"(?i)(\bbooktitle\s*=\s*\{\s*)(?:Proceedings\s+of\s+)+", r"\1", bib(records))
    out["docs/manuscript-snapshot.md"] = "# Frozen manuscript snapshot\n\nThe snapshot is immutable during weekly updates.\n\n```json\n" + __import__("json").dumps(snapshot, indent=2, ensure_ascii=False) + "\n```\n"
    candidates = read_json(ROOT / "data/inbox.json", [])
    ctext = ["# Candidate queue", "", "Unreviewed search hits are not part of the curated corpus and must not be cited as demonstrated RL evidence.", "",
             "[Search protocol](../docs/search-protocol.md) · [Update status](../data/update_state.json)", ""]
    if not candidates:
        ctext.append("No pending candidates have been recorded. Check the update status before interpreting this as an empty search.")
    for c in candidates:
        ctext += [f"## [{md(c['title'])}]({checked_url(c['url'])})", "",
                  f"- arXiv: `{c['arxiv_id']}` / {c['version'] or 'version not recorded'}",
                  f"- {'Metadata updated' if c.get('metadata_source') else 'Paper updated'}: {md(c['updated'])}",
                  f"- Source: {md(c.get('metadata_source', 'arXiv API'))}", f"- Screening status: {md(c.get('status', 'pending'))}",
                  f"- Query families: {md(', '.join(c.get('queries', [])))}", "",
                  md(c.get("abstract", "")), ""]
    out["updates/candidates.md"] = "\n".join(ctext) + "\n"
    versions = read_json(ROOT / "data/version_observations.json", [])
    vtext = ["# Version observations", "", "New versions do not overwrite reviewed or manuscript versions. Re-read changed experiments before changing a paper card.", ""]
    vtext += [f"- [{md(v['id'])}]({checked_url(v['url'])}): reviewed {md(v['reviewed_version'] or 'unspecified')}, observed {md(v['observed_version'])} ({v['observed_at']})." for v in versions]
    out["updates/versions.md"] = "\n".join(vtext) + "\n"
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for name, content in build().items():
        path = ROOT / name
        if not path.exists() or path.read_text() != content:
            stale.append(name)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
    if args.check and stale:
        raise SystemExit("Generated files are stale: " + ", ".join(stale))
    print(f"{'Checked' if args.check else 'Rendered'} {len(build())} generated views.")


if __name__ == "__main__":
    main()
