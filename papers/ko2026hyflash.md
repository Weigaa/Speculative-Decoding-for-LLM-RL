# HyFlash

**HyFlash: A Prefix-Memory Prior for On-Device Speculative Decoding**

- Citation key: `ko2026hyflash`
- Authors: Ko, Jongwoo and Cameron, Pashmina
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.07263v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Combines recent-context attention with fixed-size recurrent memory of target features in a shallow parallel drafter.

## Evidence and transfer boundary

Fixed-target inference on Qwen3-4B and Phi-4-reasoning, with greedy and stochastic sampling. The bounded memory applies to the drafter, not the target KV cache. RL transfer requires memory reconstruction after policy refresh and profiling draft cost under rollout concurrency.

## Taxonomy dimensions

- Memory and Reuse State
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and full text checked on 2026-11-08. Discovery used the recorded query families and author-supplied FlexFloor link.
- Evidence pointer: Sections 3–4 and Appendix C–D
- Source publication date: 2026-11-05
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{ko2026hyflash,
  author = {Ko, Jongwoo and Cameron, Pashmina},
  title = {{HyFlash: A Prefix-Memory Prior for On-Device Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.07263},
  year = {2026},
  eprint = {2611.07263},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
