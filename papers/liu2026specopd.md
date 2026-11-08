# SpecOPD

**SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding**

- Citation key: `liu2026specopd`
- Authors: Liu, Tianyu and Zhang, Jun and Huang, Wenjie and Shen, Yuhao and Xu, Tianqi and Hao, Xinyue and Gu, Hongyaoxing and Liu, Xuyang and Zhang, Baolin and Zhu, Yating and Ge, Shuang and Dai, Jun and Chen, Lei and Li, Yue and Wan, Mingchen
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.02846v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Packs independent drafter-generated branches at reference anchors for parallel target supervision, preserving branch-specific sparse or recurrent state.

## Evidence and transfer boundary

Drafter distillation with frozen targets. Measures acceptance, supervision throughput and separate serving throughput. RL transfer requires refreshed teacher features and accounting for training/transport costs. It does not evaluate target-policy RL rollout acceleration.

## Taxonomy dimensions

- Proposal Maintenance
- Synchronization and Versioning
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and full text checked on 2026-11-08. Discovery used the recorded query families and author-supplied FlexFloor link.
- Evidence pointer: Method sections and Appendix A.3, A.8, D
- Source publication date: 2026-11-02
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{liu2026specopd,
  author = {Liu, Tianyu and Zhang, Jun and Huang, Wenjie and Shen, Yuhao and Xu, Tianqi and Hao, Xinyue and Gu, Hongyaoxing and Liu, Xuyang and Zhang, Baolin and Zhu, Yating and Ge, Shuang and Dai, Jun and Chen, Lei and Li, Yue and Wan, Mingchen},
  title = {{SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.02846},
  year = {2026},
  eprint = {2611.02846},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
