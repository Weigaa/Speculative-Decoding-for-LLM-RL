# TableTune

**TableTune: Measured, Self-Correcting Draft-Length Tables for Dynamic Speculative Decoding**

- Citation key: `malvankar2026tabletune`
- Authors: Abhishek Malvankar and Paul Castro and Nick Mitchell and Lionel Villard
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.38968v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Profiles decode-step time by active batch and draft length on the actual serving path, then selects a throughput-oriented length table. A runtime controller updates acceptance estimates and rebuilds the table with exploration and hysteresis.

## Evidence and transfer boundary

Serving-transfer evidence, not RL rollout evaluation. H100/T4/A10G and llm-d studies compare tuned tables with fixed or other adaptive speculative configurations; they do not isolate an SD-over-autoregressive gain attributable to the tuner. Main code prompts use temperature one; n-gram/chat cases are greedy. Transfer requires profiling the rollout engine at its actual context lengths and resource sharing, plus accounting for policy refresh and controller cost. CUDA-graph switching, a real speculation-off path and profile errors matter; the controller repairs acceptance drift, not an inaccurate step-time model.

## Taxonomy dimensions

- Scheduling and Mode Selection
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract/submission metadata and full HTML v1 reviewed on 2026-11-02. Preprint status only; no acceptance inferred.
- Evidence pointer: Sections 4–6, especially 6.1 (sampling and baselines), 6.6 (graph/switch/off behavior), 6.7 (profiling errors) and 7 (scope/limitations).
- Source publication date: 2026-10-28
- Released code: [official artifact](https://github.com/asm582/tabletune)
- Artifact checks: linked and checked; matching implementation files and README visible in public repository on 2026-11-02, revision `38170878d901cb06f696a122a0b4140a3d365f02`

## BibTeX

```bibtex
@article{malvankar2026tabletune,
  author = {Malvankar, Abhishek and Castro, Paul and Mitchell, Nick and Villard, Lionel},
  title = {{TableTune: Measured, Self-Correcting Draft-Length Tables for Dynamic Speculative Decoding}},
  journal = {arXiv preprint arXiv:2610.38968},
  year = {2026},
  eprint = {2610.38968},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
