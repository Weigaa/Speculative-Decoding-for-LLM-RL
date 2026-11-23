# SpecSearch

**SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding**

- Citation key: `yildirim2026specsearch`
- Authors: Yildirim, Selin and Zeyrek, Ali and Chen, Deming
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.22296v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Uses a hardware cost model and calibration to choose autoregressive versus speculative execution, draft length and precision, including a batch-dependent length map and a learned selector for static configurations on unseen GPUs.

## Evidence and transfer boundary

Inference evaluation uses Qwen3-4B and one DFlash drafter on RTX 5090, H100, L40 and MI300X. Default speculative baseline has fixed draft length 15. Full calibration can select dynamic lengths, whereas the learned Jev selector currently chooses static configurations only. Throughput gains are configuration-specific serving results, not RL rollout gains. Abstract and conclusion report different aggregate AR-relative averages, so no single reconciled headline number is asserted here. RL transfer concerns changing rollout concurrency and memory budgets, with recalibration after policy/model changes. Changing target or KV precision also changes the numerical verifier configuration and should not be silently treated as an identical sampling baseline. Code not recorded.

## Taxonomy dimensions

- Scheduling and Mode Selection
- Memory and Reuse State
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned primary HTML reviewed on 2026-11-23. Dates are source submission dates, not registry-update timestamps. Technical evaluation remains inference-origin. No formal acceptance inferred.
- Evidence pointer: Sections IV–VII and Appendices A–B, including static-selector limitation in VII and calibration/held-out-GPU controls.
- Source publication date: 2026-11-17
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{yildirim2026specsearch,
  author = {Yildirim, Selin and Zeyrek, Ali and Chen, Deming},
  title = {{SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.22296},
  year = {2026},
  eprint = {2611.22296},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
