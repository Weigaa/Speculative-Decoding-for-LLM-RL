# D3D

**D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding**

- Citation key: `chen2026d3d`
- Authors: Chen, Baoyou and Mei, Ruiqiao and Lin, Guancong and Song, Tao and Yuan, Weihao and Liu, Qun and Zhu, Siyu
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.06425v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Uses a standalone diffusion drafter to prepare successor blocks for possible verification outcomes concurrently with target verification.

## Evidence and transfer boundary

Greedy Transformers inference with two H800 GPUs for asynchronous methods versus one for synchronous DFlash/DSpark/EAGLE baselines. The study does not establish throughput-per-GPU superiority over alternative uses of two GPUs. Transfer to RL requires resource-matched evaluation, miss/rollback handling and current-policy draft adaptation.

## Taxonomy dimensions

- Proposal Source
- Placement and Idle Resources
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned full text checked on 2026-11-11. Query-family discovery supplemented by official-source keyword search and citation tracing. Newly screened does not imply newly published.
- Evidence pointer: Sections 3.2–4.1 and Limitations
- Source publication date: 2026-11-04
- Released code: [official artifact](https://github.com/fudan-generative-vision/D3D)
- Artifact checks: Paper-linked public repository metadata and HEAD checked; code not executed on 2026-11-11, revision `cd7762436217fb51d7e7a310b310b72766bb816f`

## BibTeX

```bibtex
@article{chen2026d3d,
  author = {Chen, Baoyou and Mei, Ruiqiao and Lin, Guancong and Song, Tao and Yuan, Weihao and Liu, Qun and Zhu, Siyu},
  title = {{D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.06425},
  year = {2026},
  eprint = {2611.06425},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
