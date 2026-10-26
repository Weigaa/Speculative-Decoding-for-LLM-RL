# RIFT

**RIFT: KV Cache Compression for Draft Models with Complementary Compressibility Training**

- Citation key: `tsur2026rift`
- Authors: Dor Tsur and Maor Ashkenazi and Maximilian Golub and Peter Hicks and Yaniv Galron and Talor Abramovich and Yoav Miron and Tiyasa Mitra and Bita Darvish Rouhani and Ran Zilberstein
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.31098v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Combines prefill-selected and recent KV entries for draft-side compression, refreshes their selection as generation progresses, and uses an adaptive refresh controller to limit rescoring. Optional sparse-mask training makes the drafter more compressible.

## Evidence and transfer boundary

Serving/inference of external and KV-based self-drafters on long-input/long-output SPEED-Bench settings, including greedy and stochastic acceptance measurements. Compression is on the draft cache; an unchanged target and correct rejection sampling preserve the target distribution. Decode staleness here means stale within-sequence KV selection, not actor-policy version drift. RL transfer requires policy-aware cache invalidation, refresh-cost accounting and maintenance of any trained drafter.

## Taxonomy dimensions

- Proposal Source
- Verification Semantics
- Memory and Reuse State

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history, cross-checked against full HTML v1 on 2026-10-26. Curated after the manuscript cutoff; this is not a claim that the first posting was after the cutoff. No accepted venue is inferred.
- Evidence pointer: Sections 2–4 (scope, decode staleness, static/dynamic/adaptive refresh), Section 5 and Appendices D–J (settings, latency/quality and compressibility training).
- Source publication date: 2026-10-22
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@misc{tsur2026rift,
  author = {Tsur, Dor and Ashkenazi, Maor and Golub, Maximilian and Hicks, Peter and Galron, Yaniv and Abramovich, Talor and Miron, Yoav and Mitra, Tiyasa and Rouhani, Bita Darvish and Zilberstein, Ran},
  title = {{RIFT: KV Cache Compression for Draft Models with Complementary Compressibility Training}},
  year = {2026},
  eprint = {2610.31098},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2610.31098v1}
}
```

[Back to all records](../docs/all-papers.md)
