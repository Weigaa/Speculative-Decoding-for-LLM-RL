# Packed-SS

**One Call Ahead: Packed Self-Speculative Decoding with Diffusion Drafting**

- Citation key: `chen2026packedss`
- Authors: Yuxiao Chen and Changxiao Cai
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.33379v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Packs verification of a deferred draft and preparation of the next draft into one shared AR/diffusion-model call. Retained candidates keep their original proposal distributions while verification uses the current committed prefix.

## Evidence and transfer boundary

Serving/inference on shared-weight AR/diffusion models, not RL training. Section 3.2 and Appendix B.2 provide a stochastic construction that stores proposal distributions and performs exact rejection correction; the pathwise call-count result has separate greedy monotonicity assumptions. Experiments include greedy and temperature-one cases. Transfer requires a compatible shared-mode architecture, correct attention/cache masks and a documented fixed rollout-policy snapshot. A reduction in model calls alone does not establish lower GPU cost, rollout makespan or time-to-quality under policy updates.

## Taxonomy dimensions

- Proposal Source
- Verification Semantics
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract/submission metadata, full HTML and paper-linked public code repository checked on 2026-11-02. No RL result or accepted venue inferred from serving evaluation.
- Evidence pointer: Sections 3.1–3.2, 4.1–4.2 and 5; Appendix B.1 versus B.2 distinguishes greedy call-count assumptions from exact stochastic sampling; Appendices D–F give packing and timing details.
- Source publication date: 2026-10-24
- Released code: [official artifact](https://github.com/cyx78/One-Call-Ahead-Packed-Self-Speculative-Decoding-with-Diffusion-Drafting)
- Artifact checks: paper-linked public repository checked; source files visible; code not executed on 2026-11-02, revision `02343e3d69d5412c184de7de4cf3d47f99d3e02e`

## BibTeX

```bibtex
@article{chen2026packedss,
  author = {Chen, Yuxiao and Cai, Changxiao},
  title = {{One Call Ahead: Packed Self-Speculative Decoding with Diffusion Drafting}},
  journal = {arXiv preprint arXiv:2610.33379},
  year = {2026},
  eprint = {2610.33379},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
