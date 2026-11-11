# ChainFlow

**ChainFlow: Few-Step Latent Flow Matching for Speculative Decoding**

- Citation key: `aktas2026chainflow`
- Authors: Aktas, Selim and Erdem, Yusuf Erdem and Zeer, Ahmed and Kesgin, Himmet Toprak and Yuce, Muzaffer Kaan and Amasyali, Mehmet Fatih
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.08669v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Predicts target-conditioned latent states in one or two flow steps, then uses token-feedback heads and tree emission for candidate generation.

## Evidence and transfer boundary

Greedy vLLM inference on fixed Qwen3.5 targets, plus sequential language adaptation and concurrent serving. The fixed draft/tree configurations and load cutoff do not establish adaptive RL rollout performance. Transfer concerns low-cost parallel proposals and adaptation, with policy refresh and stochastic verification still to evaluate.

## Taxonomy dimensions

- Proposal Source
- Proposal Maintenance
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned full text checked on 2026-11-11. Query-family discovery supplemented by official-source keyword search and citation tracing. Newly screened does not imply newly published.
- Evidence pointer: Sections 3–4 and Limitations
- Source publication date: 2026-11-05
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{aktas2026chainflow,
  author = {Aktas, Selim and Erdem, Yusuf Erdem and Zeer, Ahmed and Kesgin, Himmet Toprak and Yuce, Muzaffer Kaan and Amasyali, Mehmet Fatih},
  title = {{ChainFlow: Few-Step Latent Flow Matching for Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.08669},
  year = {2026},
  eprint = {2611.08669},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
