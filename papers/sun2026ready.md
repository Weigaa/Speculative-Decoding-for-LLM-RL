# ReaDy

**ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models**

- Citation key: `sun2026ready`
- Authors: Bohan Sun and Zunhai Su and Xialie Zhuang and Jianjin Li and Ngai Wong and Chuan-Wei Kuo
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.20503v2)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v2

## Mechanism / relevance

Reads committed hybrid-linear-attention recurrent states using learned position-conditioned queries and low-rank projections, then injects the retrieved context into a DSpark-style drafter through residual fusion.

## Evidence and transfer boundary

Fixed-target inference on Qwen3.8-27B, one B200 GPU, greedy decoding and concurrency one. The reader is trained against the target recurrent state and does not demonstrate policy-refresh robustness. Transfer to recurrent/hybrid rollout targets requires consistent committed states, rollback handling, and reader maintenance after policy updates. Greedy agreement here is not experimental evidence of stochastic RL sampling equivalence.

## Taxonomy dimensions

- Proposal Source
- Memory and Reuse State

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history, cross-checked against full HTML v2 on 2026-10-26. Curated after the manuscript cutoff; this is not a claim that the first posting was after the cutoff. No accepted venue is inferred.
- Evidence pointer: Sections 3.1–3.2 and 4.1–4.4; Appendix D.2 and the greedy serving/diagnostic protocol.
- Source publication date: 2026-10-14
- Released code: [official artifact](https://github.com/StartLuxLabs/ReaDy)
- Artifact checks: linked and checked; public repository on 2026-10-26, revision `8ac61b51d529fad980566cfde7a3c41415ba93a5`

## BibTeX

```bibtex
@misc{sun2026ready,
  author = {Sun, Bohan and Su, Zunhai and Zhuang, Xialie and Li, Jianjin and Wong, Ngai and Kuo, Chuan-Wei},
  title = {{ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models}},
  year = {2026},
  eprint = {2610.20503},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2610.20503v2}
}
```

[Back to all records](../docs/all-papers.md)
