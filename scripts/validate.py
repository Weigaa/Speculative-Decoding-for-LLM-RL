"""Validate corpus counts, identities, records, and internal Markdown links."""
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote
from library import ROOT, read_json, identities, checked_url, parse_bibtex


def validate():
    papers = read_json(ROOT / "data/papers.json")
    snapshot = read_json(ROOT / "data/manuscript_snapshot.json")
    dims = {d["id"] for b in read_json(ROOT / "data/taxonomy.json") for d in b["dimensions"]}
    ids, identity_index = set(), {}
    required = {"id", "name", "title", "authors", "year", "venue", "url", "role", "evidence", "dimensions", "mechanism", "evidence_note", "metadata_provenance", "bibtex", "manuscript_cited"}
    for p in papers:
        assert required <= p.keys(), f"Missing fields: {p.get('id')}"
        assert re.fullmatch(r"[A-Za-z0-9_-]+", p["id"]), "Unsafe record id"
        assert p["id"] not in ids, f"Duplicate key {p['id']}"
        ids.add(p["id"])
        checked_url(p["url"])
        assert p["evidence"] in {"direct_rl", "serving_transfer", "contextual", "supporting"}
        assert set(p["dimensions"]) <= dims
        if p["role"] in {"core", "post_cutoff"}:
            assert p["dimensions"] and p["evidence"] in {"direct_rl", "serving_transfer"}
        else:
            assert not p["dimensions"], f"Non-core study appears in taxonomy: {p['id']}"
        bib = parse_bibtex(p["bibtex"])
        assert len(bib) == 1 and bib[0]["id"] == p["id"]
        for key in identities(p):
            assert key not in identity_index, f"Duplicate study {p['id']} / {identity_index.get(key)}"
            identity_index[key] = p["id"]
    assert set(snapshot["bibliography_ids"]) <= ids
    assert len(snapshot["bibliography_ids"]) == 111
    assert len(snapshot["cited_ids"]) == 107
    assert len(set(snapshot["core_ids"])) == 46
    core = [p for p in papers if p["id"] in snapshot["core_ids"]]
    counts = Counter(p["evidence"] for p in core)
    assert counts == {"direct_rl": 21, "serving_transfer": 25}, counts
    assert {p["id"] for p in papers if p["manuscript_cited"]} == set(snapshot["cited_ids"])
    assert {p["id"] for p in papers if p["role"] == "core"} == set(snapshot["core_ids"])
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        content = path.read_text()
        assert "/Users/" not in content and "gho_" not in content, f"Private material in {path}"
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            dest = (path.parent / unquote(target.split("#", 1)[0])).resolve()
            assert dest.is_relative_to(ROOT), f"Escaping link {path}: {target}"
            assert dest.exists(), f"Broken link {path.relative_to(ROOT)}: {target}"
    print(f"Validated {len(papers)} records, 46 frozen core studies, and all internal Markdown links.")


if __name__ == "__main__":
    validate()
