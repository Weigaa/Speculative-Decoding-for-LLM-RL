# MDraft

**Multi-Draft On-Policy Distillation for Diffusion Drafters**

- Citation key: `molodyk2026mdraft`
- Authors: Petr Molodyk and Yuchen Zhu and Jaemoo Choi and Molei Tao and Yongxin Chen
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.37778v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Samples multiple parallel draft blocks for each training context and blends the verifier conditionals across sampled prefixes into reverse-KL targets. Detached survival weights use verification feedback; the drafter architecture and inference procedure remain unchanged.

## Evidence and transfer boundary

Fixed-verifier drafter-training/inference evidence, not target-policy RL. DFlash drafters for Qwen3-4B/8B are evaluated on math, code and chat at temperatures 0, 0.6 and 1. The paper reports acceptance length including the bonus token and explicitly does not report wall-clock speedup. Each training context uses one draft forward and K verifier evaluations, which can be batched but are not free. Transfer to evolving RL policies requires current-policy target refresh, amortized verifier/training cost and an unchanged correct acceptance rule. On-policy refers to drafter-generated states, not RL policy optimization.

## Taxonomy dimensions

- Proposal Maintenance
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract/submission metadata and full HTML v1 reviewed on 2026-11-02. Preprint status only; no acceptance inferred.
- Evidence pointer: Sections 3.1–3.3 (target blending, K verifier evaluations and survival weights), 4.1–4.4 (fixed-teacher setup and acceptance-only evaluation) and Appendix 11 (parallel drafting and verification).
- Source publication date: 2026-10-27
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{molodyk2026mdraft,
  author = {Molodyk, Petr and Zhu, Yuchen and Choi, Jaemoo and Tao, Molei and Chen, Yongxin},
  title = {{Multi-Draft On-Policy Distillation for Diffusion Drafters}},
  journal = {arXiv preprint arXiv:2610.37778},
  year = {2026},
  eprint = {2610.37778},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
