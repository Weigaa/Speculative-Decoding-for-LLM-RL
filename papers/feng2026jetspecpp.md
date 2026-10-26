# JetSpec++

**JetSpec++: Foresight Parallel Drafting with Self Refinements**

- Citation key: `feng2026jetspecpp`
- Authors: Zhaoxiang Feng and Lanxiang Hu and Haoran Yuan and Yu-Yang Qian and Jihui Yang and Peng Zhao and Yibo Zhu and Tajana Rosing and Hao Zhang
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.19792v2)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v2

## Mechanism / relevance

Combines within-block Jacobi refinement with inter-block foresight. An adapter predicts future verifier states and likely acceptance outcomes so that a drafter on another GPU can prepare candidates while the target verifies the preceding block.

## Evidence and transfer boundary

Serving/inference evidence only. Acceptance is evaluated at temperatures 0 and 1, while the main throughput comparison uses single-request greedy decoding. The pipelined configuration uses a separate drafter GPU, so its latency ratio is not an equal-GPU-cost RL throughput gain. Transfer requires affordable spare placement, current-policy feature compatibility, and an unchanged target acceptance/correction rule; policy refresh and closed-batch RL training were not evaluated.

## Taxonomy dimensions

- Proposal Source
- Verification Semantics
- Placement and Idle Resources
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history, cross-checked against full HTML v2 on 2026-10-26. Curated after the manuscript cutoff; this is not a claim that the first posting was after the cutoff. No accepted venue is inferred.
- Evidence pointer: Sections 4.1–4.3 and 5.1–5.6; Appendix E (hardware/serving protocol and correctness checks) and F.3 (lossless verification).
- Source publication date: 2026-10-14
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: paper-linked public JetSpec repository checked; README and implementation identify the prior JetSpec (2606.18394); JetSpec++-specific release not verified on 2026-10-26, revision `2c7b3fae75690dfe9a188a37d7fdfd43ee0e032f`

## BibTeX

```bibtex
@misc{feng2026jetspecpp,
  author = {Feng, Zhaoxiang and Hu, Lanxiang and Yuan, Haoran and Qian, Yu-Yang and Yang, Jihui and Zhao, Peng and Zhu, Yibo and Rosing, Tajana and Zhang, Hao},
  title = {{JetSpec++: Foresight Parallel Drafting with Self Refinements}},
  year = {2026},
  eprint = {2610.19792},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2610.19792v2}
}
```

[Back to all records](../docs/all-papers.md)
