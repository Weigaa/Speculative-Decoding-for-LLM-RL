# SpecPilot

**SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding**

- Citation key: `li2026specpilot`
- Authors: Li, Kunjun and Chai, Wenhao and Liang, Yihao and Hu, Yuezhou and Xu, Shuyao and Pan, Yi and Zheng, William X. and Ramchandran, Kannan and Keutzer, Kurt and Jiao, Jiantao
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.02501v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Uses a measured cost model and automated optimization to improve hybrid-target tree verification, batching and verification execution.

## Evidence and transfer boundary

Greedy SGLang serving on H100 and RTX PRO 6000. Token forcing checks stock-output agreement. Autonomous coding agents are the optimization tool, not evidence of agentic RL training. RL transfer needs per-load profiling, stochastic validation and compatibility after model updates.

## Taxonomy dimensions

- Parallel and Load-Aware Drafting
- Scheduling and Mode Selection

## Source and artifact record

- Metadata provenance: Official arXiv metadata and full text checked on 2026-11-08. Discovery used the recorded query families and author-supplied FlexFloor link.
- Evidence pointer: Sections 3–5
- Source publication date: 2026-11-02
- Released code: [official artifact](https://github.com/StargazerX0/SpecPilot)
- Artifact checks: paper-linked public repository and default-branch commit checked; code not executed on 2026-11-08, revision `78c42af4297bdd0b58020a491802817241a37331`

## BibTeX

```bibtex
@article{li2026specpilot,
  author = {Li, Kunjun and Chai, Wenhao and Liang, Yihao and Hu, Yuezhou and Xu, Shuyao and Pan, Yi and Zheng, William X. and Ramchandran, Kannan and Keutzer, Kurt and Jiao, Jiantao},
  title = {{SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.02501},
  year = {2026},
  eprint = {2611.02501},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
