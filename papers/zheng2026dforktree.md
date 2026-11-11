# DForkTree

**DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees**

- Citation key: `zheng2026dforktree`
- Authors: Zheng, Zhicheng and Zhang, Cheng and Tang, Chenkai
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.12356v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Uses target-generated n-gram statistics to correct branch scores after candidate-tree forks and constructs the selected tree on the GPU.

## Evidence and transfer boundary

Fixed Qwen3.5 targets at batch one on RTX 5090. Greedy and temperature-one sample-and-match verification are evaluated. Offline target-generation corpus and branch scores would need policy-aware refresh in RL. Not direct RL rollout evaluation.

## Taxonomy dimensions

- Workload Recurrence
- Proposal Source
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned full text checked on 2026-11-11. Query-family discovery supplemented by official-source keyword search and citation tracing. Newly screened does not imply newly published.
- Evidence pointer: Sections 3–5.7 and Appendices A, G and I
- Source publication date: 2026-11-09
- Released code: [official artifact](https://github.com/Perseus037/DForkTree)
- Artifact checks: Paper-linked public repository metadata and HEAD checked; code not executed on 2026-11-11, revision `eeed8b698b8822aa2767ec5c191efc4e1b6cdbe3`

## BibTeX

```bibtex
@article{zheng2026dforktree,
  author = {Zheng, Zhicheng and Zhang, Cheng and Tang, Chenkai},
  title = {{DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees}},
  journal = {arXiv preprint arXiv:2611.12356},
  year = {2026},
  eprint = {2611.12356},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
