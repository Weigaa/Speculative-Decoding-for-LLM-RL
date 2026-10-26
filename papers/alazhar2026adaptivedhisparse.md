# Adaptive DHiSparse

**Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy**

- Citation key: `alazhar2026adaptivedhisparse`
- Authors: Naji Alazhar and Wassel Alazhar
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.13708v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Makes hierarchical sparse KV residency depend on load, protects the required working set, retains optional history when memory is free, and fetches missing rows from host storage. Shared retrieval, a window-bounded draft ring and reusable verification staging support speculative blocks.

## Evidence and transfer boundary

Long-context serving of GLM-5.3 and DeepSeek-V4.1-Flash with DSpark/DFlash2, including offered-load steps and latency-bounded throughput comparisons. The baseline is the same sparse target computation, not a claim of dense-policy equivalence. Transfer requires rollout-engine support for hierarchical retrieval, cache invalidation at policy refresh and the same acceptance rule. No RL training evaluation is reported.

## Taxonomy dimensions

- Scheduling and Mode Selection
- Memory and Reuse State
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history, cross-checked against full HTML v1 on 2026-10-26. Curated after the manuscript cutoff; this is not a claim that the first posting was after the cutoff. No accepted venue is inferred.
- Evidence pointer: Sections 3.1–3.5 (KV hierarchy and speculative-state lifetime), 4.1 (matched configuration) and 4.2–4.3 (load/latency/residency measurements).
- Source publication date: 2026-10-09
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@misc{alazhar2026adaptivedhisparse,
  author = {Alazhar, Naji and Alazhar, Wassel},
  title = {{Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy}},
  year = {2026},
  eprint = {2610.13708},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2610.13708v1}
}
```

[Back to all records](../docs/all-papers.md)
