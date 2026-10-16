# Speculative Decoding for LLM Reinforcement Learning

A companion literature library for **Speculative Decoding for LLM Reinforcement Learning: A Survey of Algorithms, Systems, and Training Semantics**.

Browse the same three branches used in the manuscript: **Workload-Aware Speculation**, **Policy-Aware Speculation**, and **System Co-Design**. Each paper has a canonical card with its source, citation, evidence setting, mechanism, and transfer boundary. [中文说明](README_zh.md).

The repository records bibliographic links and original synthesis notes, not hosted copies of third-party PDFs. Background references, related surveys, and contextual studies are kept separate from the technical taxonomy.

## Library status

- Manuscript literature cutoff: **2026-10-14**.
- Frozen core: **46** unique studies, including **21** with direct RL evidence and **25** serving-origin transfer studies.
- Imported bibliography: **111** records, of which **107** appear in the manuscript PDF.
- Screened additions after the cutoff: **0**. These do not alter the manuscript snapshot.

## Browse by the manuscript taxonomy

A study may appear under several dimensions. Every study has one canonical record and is counted once.

### [Workload-Aware Speculation](taxonomy/workload-aware/README.md)

- [Closed-Batch Tail](taxonomy/workload-aware/closed-batch-tail.md) — 8 studies
- [Workload Recurrence](taxonomy/workload-aware/workload-recurrence.md) — 9 studies

### [Policy-Aware Speculation](taxonomy/policy-aware/README.md)

- [Proposal Source](taxonomy/policy-aware/proposal-source.md) — 21 studies
- [Proposal Maintenance](taxonomy/policy-aware/proposal-maintenance.md) — 17 studies
- [Verification Semantics](taxonomy/policy-aware/verification-semantics.md) — 9 studies

### [System Co-Design](taxonomy/system-co-design/README.md)

- [Scheduling and Mode Selection](taxonomy/system-co-design/scheduling-mode-selection.md) — 11 studies
- [Placement and Idle Resources](taxonomy/system-co-design/placement-idle-resources.md) — 5 studies
- [Memory and Reuse State](taxonomy/system-co-design/memory-reuse-state.md) — 11 studies
- [Synchronization and Versioning](taxonomy/system-co-design/synchronization-versioning.md) — 9 studies
- [Parallel and Load-Aware Drafting](taxonomy/system-co-design/parallel-load-aware-drafting.md) — 7 studies

## Other reading lists

- [Related surveys](supporting/related-surveys.md)
- [Background, foundational methods, and infrastructure](supporting/background.md)
- [Contextual evidence on actions, observations, and numerical fidelity](supporting/contextual-evidence.md)
- [All records](docs/all-papers.md)
- [New candidates awaiting screening](updates/candidates.md)
- [Version observations](updates/versions.md)
- [Manuscript snapshot](docs/manuscript-snapshot.md)
- [Search and inclusion protocol](docs/search-protocol.md)
- [Maintenance instructions](CONTRIBUTING.md)

## Weekly updates

GitHub Actions checks arXiv and its DataCite DOI registry every Monday at **08:17 Asia/Shanghai** (00:17 UTC). It deduplicates discoveries, records version changes, and commits the candidate queue and search log. You can also run it from the Actions tab. The workflow uses no paid API or secret.

A separate weekly curator review is configured in the maintainer's Codex chat. Primary-source screening is required before a candidate enters the curated taxonomy. The hosted discovery job works independently of the maintainer's computer; the curator run requires its configured host to be available.

A successful empty search is reported as such. Failed or truncated searches are recorded as incomplete and do not advance the last-success timestamp. Scheduled GitHub runs can be delayed, and GitHub may disable schedules in inactive public repositories.

## Bibliography and citation

- [All imported and curated references](bibliography/references.bib)
- [The frozen 46-study core](bibliography/manuscript-core.bib)
- [SCIS-compatible BibTeX](bibliography/references-scis.bib)

BibTeX metadata was imported from the author's working bibliography. Field-level checks are recorded per paper; import does not imply that every author/venue field has been independently reverified. arXiv posting is not a peer-review certificate.

The companion manuscript is **Speculative Decoding for LLM Reinforcement Learning: A Survey of Algorithms, Systems, and Training Semantics**. Its journal submission is in preparation. No acceptance, DOI, or publication date is claimed. Use [CITATION.cff](CITATION.cff) to cite this repository.

## Rights

Paper PDFs are linked from their original sources and are not redistributed here. Third-party articles and artifacts retain their original licenses. Repository scripts and original editorial notes are covered by the [MIT license](LICENSE).
