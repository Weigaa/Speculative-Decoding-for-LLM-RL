# Maintaining the literature library

The owner has authorized weekly discovery, curation, and repository updates. Follow the [search protocol](docs/search-protocol.md). No extra approval is required for routine bibliographic corrections or screened additions within this scope.

## Weekly curator checklist

1. Pull the latest `main` with a fast-forward-only update. Preserve unrelated changes.
2. Inspect `data/update_state.json`, the candidate queue, and version observations. If the last hosted search failed, retry discovery or document a primary-source fallback; do not claim there were no updates.
3. Deduplicate by arXiv ID without version suffix, DOI, normalized title, and author/title review against **all** library records, not only the 46 core records.
4. Read the relevant primary text and original evaluation setting. Cross-check formal venue metadata and released project artifacts when appropriate. Do not infer direct RL training evidence from an inference paper that trains its drafter with RL.
5. Assign eligible studies to the manuscript's three branches and existing second-level dimensions. Add new dimensions only if the existing definitions cannot express the mechanism, and explain the change. Keep contextual and related-survey records outside the core count.
6. Add a full record to `data/papers.json`. For later technical additions use `role: post_cutoff` and `manuscript_cited: false`. Keep every field present in the existing records, provide a stable HTTPS paper URL and valid BibTeX, and explain the evidence and RL transfer boundary. Do not change frozen IDs or cutoff dates.
7. Append decisions to `data/screening_log.jsonl`; remove processed hits from `data/inbox.json`. For exclusions, include normalized `identities` so the same work does not reappear every week. If a paper is eligible but classification needs evidence, keep it pending with a clear reason.
8. For new versions, retain the original reviewed version. Record material changes and source dates before updating current notes. Never rewrite historical performance numbers without noting the source version and configuration.
9. Run the commands below, inspect the diff, and commit/push only this library's intended changes. Include a brief dated update note under `updates/` when curated findings change.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/render.py
python3 scripts/validate.py
python3 scripts/render.py --check
```

## Data contract

Use `data/papers.json` as the source of truth, not generated Markdown. The required record fields are validated by `scripts/validate.py`. Preserve `bibtex` and citation key when correcting a version of the same work. `bibliography/references.bib` restores the normal publication title for portability; `references-scis.bib` removes the prefix that SCIS adds itself.

The initial bibliography was imported, so metadata corrections are welcome. Distinguish an imported claim from a publisher-verified correction in `metadata_provenance`. Do not invent a DOI, accepted venue, date, speedup, or repository.

## Weekly hosted discovery

The workflow `.github/workflows/weekly-update.yml` runs every Monday at 00:17 UTC (08:17 Asia/Shanghai) and on manual dispatch. It uses the automatically supplied GitHub token with repository-contents permission; no personal token or paid API key is required. It queries arXiv and the official DataCite arXiv DOI registry, then updates pending candidates, observed versions, and exact-query logs only. DataCite metadata-update dates are not paper-version dates. The semantic curator pass is a separate scheduled Codex task.

If GitHub disables a public repository's schedule after inactivity, re-enable it in Actions. Scheduler latency and source outages are visible through workflow status and search logs. Failure must never be reported as a successful empty search.

## Publication and rights

Publish metadata, original synthesis, source links, and verified artifact links. Do not upload third-party PDFs, the private manuscript source, publisher templates, local attachment paths, credentials, private project data, or draft funding placeholders. The companion paper is in preparation; do not claim journal acceptance.
