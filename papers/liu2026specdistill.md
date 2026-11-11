# SPEC-Distill

**SPEC-Distill: Towards Efficient Speculative Distillation for Reinforcement Learning with Verifiable Rewards**

- Citation key: `liu2026specdistill`
- Authors: Bingshuai Liu and Zijun Min and Ante Wang and Jiajun Cao and Haibo Zhang and Liang Yao and Shuman Liu and Anxiang Zeng and Jinsong Su
- Year: 2026
- Bibliographic venue: EMNLP 2026
- Source: [paper](https://aclanthology.org/2026.emnlp-main.814/)
- Evidence setting: **Direct RL rollout / training**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: EMNLP 2026 published version

## Mechanism / relevance

Uses offline teacher trajectories as early RL speculative prefixes, then switches to refreshed student-rollout history without online teacher scoring.

## Evidence and transfer boundary

Direct GRPO training of Qwen3 students on verifiable reasoning tasks. Section 3.3 explicitly calls the rollout semi-on-policy, omits residual resampling at rejection and does not claim an unbiased update. Lenience and teacher/student source switching trade distribution fidelity for guidance and reuse. Published in October, newly identified by this supplementary screen, not a new November paper. Rollout-token/time savings versus Luffy do not establish a pure lossless-SD or total-training-cost gain including offline teacher generation.

## Taxonomy dimensions

- Workload Recurrence
- Proposal Source
- Proposal Maintenance
- Verification Semantics

## Source and artifact record

- Metadata provenance: Official ACL Anthology metadata/BibTeX and published PDF checked on 2026-11-11. Formal proceedings preferred. Distinct from SPEC-RL by title, author set, DOI and mechanism.
- Evidence pointer: Published pages 18948–18951, Sections 3.1–4 and Algorithm 1
- Source publication date: 2026-10
- Released code: [official artifact](https://github.com/XMUDeepLIT/SPEC-Distill)
- Artifact checks: Paper-linked public repository metadata and HEAD checked; code not executed on 2026-11-11, revision `c385d8c2ae07f9b38d45f6defd2ab2e8020056d6`

## BibTeX

```bibtex
@inproceedings{liu2026specdistill,
  author = {Bingshuai Liu and Zijun Min and Ante Wang and Jiajun Cao and Haibo Zhang and Liang Yao and Shuman Liu and Anxiang Zeng and Jinsong Su},
  title = {{SPEC-Distill: Towards Efficient Speculative Distillation for Reinforcement Learning with Verifiable Rewards}},
  booktitle = {Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing},
  publisher = {Association for Computational Linguistics},
  address = {Budapest},
  pages = {18946--18959},
  year = {2026},
  doi = {10.18653/2026.emnlp-main.814}
}
```

[Back to all records](../docs/all-papers.md)
