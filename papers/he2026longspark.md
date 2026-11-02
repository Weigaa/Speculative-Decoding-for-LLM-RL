# LongSpark

**LongSpark: Efficient speculative decoding with a fixed-cost parallel drafter**

- Citation key: `he2026longspark`
- Authors: Hao-Yuan He and Peng-Fei Liu and Chen Chen and Si Shen and Quan He and Runzhou Liu and Xinqi Li and Zhenhua Dong and Ming Li
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2609.37029v2)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v2

## Mechanism / relevance

Builds a fixed-size drafter context from a recent target-cache window, boundary features and incrementally updated global summaries. A parallel backbone and lightweight sequential correction propose tokens without maintaining a growing draft KV cache.

## Evidence and transfer boundary

Serving/inference only. Main Qwen3-4B/8B/14B tests use temperature one and a target–drafter-disaggregated configuration that adds a dedicated drafter GPU over the AR baseline. Long-context experiments reach 128K; full-prefix work and the complete target cache still belong to target verification. Fixed cost applies to the additional drafter state/computation at fixed architecture and block width, not to the whole decoder. RL transfer requires summary reconstruction or invalidation when policy weights change, correct state updates after rejection, and equal-resource net rollout measurements.

## Taxonomy dimensions

- Proposal Source
- Memory and Reuse State
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract/submission metadata, full HTML and paper-linked public code repository checked on 2026-11-02. No RL result or accepted venue inferred from serving evaluation.
- Evidence pointer: v2 Sections 2.2–2.4 (context interface, corrected sampling and state maintenance), 3.1–3.3 (hardware/sampling/load), and Appendices C–D.
- Source publication date: 2026-09-29
- Released code: [official artifact](https://github.com/Hao-Yuan-He/LongSpark)
- Artifact checks: paper-linked public repository checked; source files visible; code not executed on 2026-11-02, revision `9ab6526e481bbea67489f3a73ebc782218d56f71`

## BibTeX

```bibtex
@article{he2026longspark,
  author = {He, Hao-Yuan and Liu, Peng-Fei and Chen, Chen and Shen, Si and He, Quan and Liu, Runzhou and Li, Xinqi and Dong, Zhenhua and Li, Ming},
  title = {{LongSpark: Efficient speculative decoding with a fixed-cost parallel drafter}},
  journal = {arXiv preprint arXiv:2609.37029},
  year = {2026},
  eprint = {2609.37029},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
