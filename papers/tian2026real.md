# REAL Loss

**REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding**

- Citation key: `tian2026real`
- Authors: Tian, Yu
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.14399v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Uses accepted-path importance weights and conditional marginalization to optimize expected speculative acceptance length rather than a product of marginal acceptance surrogates.

## Evidence and transfer boundary

Frozen Qwen3.6-35B-A3B target and Domino drafter. Controlled loss-level reimplementations share architecture, data and auxiliary cross-entropy. Probabilistic vLLM serving uses temperature 1, top-k 20 and top-p 0.95, five seeds and three repetitions per seed across nine subsets. Appendix G reports batch-80 serving throughput, distinct from acceptance length. The alternative greedy-serving protocol uses greedy proposals while the target still samples; it is not ordinary target-greedy equivalence. Recorded training times do not isolate incremental loss overhead. No target-policy RL rollout/training evaluation. RL transfer requires adapting supervision to refreshed targets and measuring maintenance cost and net training savings.

## Taxonomy dimensions

- Proposal Maintenance
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned full text reviewed on 2026-11-16. Discovery used the recorded query families supplemented by official-source keyword search and citation tracing. Publication dates are not inferred from registry timestamps.
- Evidence pointer: Sections 2–4 and Appendices D–G; Appendix G Table 10 distinguishes serving throughput from AL; Appendix E states timing controls.
- Source publication date: 2026-11-10
- Released code: [official artifact](https://github.com/King-ty/speculators/tree/real-loss)
- Artifact checks: checked public repository and selected branch HEAD; code not executed on 2026-11-16, revision `3dff4579c5f93f692108df8b5178c9e9200b8536`

## BibTeX

```bibtex
@article{tian2026real,
  author = {Tian, Yu},
  title = {{REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.14399},
  year = {2026},
  eprint = {2611.14399},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
