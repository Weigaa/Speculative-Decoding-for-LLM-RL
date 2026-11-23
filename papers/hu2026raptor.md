# Raptor

**Raptor: Rejection-aware Adaptive Tree based on Speculative Decoding**

- Citation key: `hu2026raptor`
- Authors: Hu, Qishu and Wang, Haozhao and Hong, Zicong and Zhan, Yufeng and Xia, Yuanqing
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.25436v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Uses accepted progress, uncovered target probability at the rejection frontier and wasted deep nodes to adjust tree depth, width and node budget with smoothing, bounded updates and expansion recovery.

## Evidence and transfer boundary

Greedy multimodal inference on LLaVA-1.6-Vicuna-7B and Qwen2.5-VL-7B with Medusa, EAGLE and ViSpec, two RTX 3090 GPUs and seven benchmark subsets. Timing includes prefill, drafting, verification, cache/controller work and visual processing inside generation. Reported throughput is a mean of per-example rates. Controller coefficients are calibrated on separate examples, not learned target/drafter weights. Appendix A.1 notes terminal-block handling that can retain tokens after EOS, despite clipped pseudocode, so stopping and token accounting need reconciliation before reuse. No stochastic RL or training evidence. Transfer concerns feedback-guided candidate budgets as rollout content and policy alignment change, requiring current-policy probabilities, stochastic verification and concurrency-aware net latency evaluation. Code not recorded.

## Taxonomy dimensions

- Scheduling and Mode Selection
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned primary HTML reviewed on 2026-11-23. Dates are source submission dates, not registry-update timestamps. Technical evaluation remains inference-origin. No formal acceptance inferred.
- Evidence pointer: Sections 3–4 and Appendices A.1–A.4 and B.1–B.5, especially implementation stopping convention and timing scope.
- Source publication date: 2026-11-19
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{hu2026raptor,
  author = {Hu, Qishu and Wang, Haozhao and Hong, Zicong and Zhan, Yufeng and Xia, Yuanqing},
  title = {{Raptor: Rejection-aware Adaptive Tree based on Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.25436},
  year = {2026},
  eprint = {2611.25436},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
