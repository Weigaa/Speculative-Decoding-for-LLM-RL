# PolyGraph

**PolyGraph: Plan-Buffered CUDA Graphs for Adaptive Speculative Decoding**

- Citation key: `yang2026polygraph`
- Authors: Junchao Yang
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.23861v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Captures one maximum-grid CUDA Graph and updates a fixed-address GPU plan buffer containing active batch and draft dimensions. Custom Triton kernels guard inactive tiles instead of executing maximum-shape padding.

## Evidence and transfer boundary

Mechanism-level prototype on one H800 with Qwen2.5-3B-shaped custom kernels and synthetic request/draft traces. It uses no trained model weights, draft model, production scheduler, tokenization, networking or paged KV implementation. Compared with warmed shape-specific graphs, the study measures similar step latency with fewer graphs and less pre-serving graph-build time; comparisons with MaxPad isolate padding waste. These are not end-to-end inference or RL speedups. Transfer is a runtime mechanism for changing rollout batch/draft widths, conditional on plan-aware kernels, fixed allocation/layout/pointers and integration with real target verification. Opaque libraries and model/topology refresh may still require graph boundaries or recapture.

## Taxonomy dimensions

- Scheduling and Mode Selection
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract, v1 HTML and Atom id-list metadata checked on 2026-11-09. Both abstract history and Atom response report first publication 2026-08-14 despite the identifier month prefix; the supplied source date is retained explicitly rather than inferred from the ID. Newly curated from the prior queue, not newly published this week. No separate paper code repository recorded.
- Evidence pointer: Sections 3.1–3.3 and 4.1–4.4; Section 4.1 explicitly states no trained weights, and 4.4 distinguishes prototype measurements from production serving.
- Source publication date: 2026-08-14
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{yang2026polygraph,
  author = {Yang, Junchao},
  title = {{PolyGraph}: Plan-Buffered {CUDA} Graphs for Adaptive Speculative Decoding},
  journal = {arXiv preprint arXiv:2610.23861},
  year = {2026},
  eprint = {2610.23861},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
