# D3Tree

**D3Tree: Learning to Prune Block-Diffusion Draft Trees for Efficient Verification**

- Citation key: `nie2026d3tree`
- Authors: Nie, Hong and Gao, Zhangchi and Yu, Jun and Wang, Bo and Sun, Jianqing and Liu, Shengping
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.11371v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Learns conditional node survival and prunes ancestor-closed draft trees under a load-dependent batch-wide verification budget.

## Evidence and transfer boundary

Six frozen VLM targets across text and multimodal serving workloads. Verification is greedy, with stochastic tree pruning explicitly left for future work. Transfer to RL requires stochastic verification, current-policy survival calibration and cost-aware tree/recurrent-state execution.

## Taxonomy dimensions

- Scheduling and Mode Selection
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned full text checked on 2026-11-11. Query-family discovery supplemented by official-source keyword search and citation tracing. Newly screened does not imply newly published.
- Evidence pointer: Sections III–IV and Conclusion
- Source publication date: 2026-11-08
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{nie2026d3tree,
  author = {Nie, Hong and Gao, Zhangchi and Yu, Jun and Wang, Bo and Sun, Jianqing and Liu, Shengping},
  title = {{D3Tree: Learning to Prune Block-Diffusion Draft Trees for Efficient Verification}},
  journal = {arXiv preprint arXiv:2611.11371},
  year = {2026},
  eprint = {2611.11371},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
