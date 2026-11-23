# FACT

**FACT: Fixed-Budget Allocation and Cross-Step Training for Speculative Decoding**

- Citation key: `fares2026fact`
- Authors: Fares, Hadi and Hassan, Mayssa Hajj and Salman, Ali and Mohanna, Ammar
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.23463v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Combines step-weighted backpropagation through predicted-feature drafts with confidence-based candidate allocation under matched per-depth tree budgets, measuring how training and execution costs affect accepted progress.

## Evidence and transfer boundary

Fixed Llama-3-8B-Instruct, one H100, bfloat16 and greedy decoding. Main timings use 50 prompts per benchmark, 256 nodes and a 128-token cap, including prefill but excluding model loading. Training comparisons jointly vary gradient flow and weighting, not either independently, and match optimizer steps rather than compute. Reported acceptance gains are not latency gains; host-thread settings can erase speedups without changing acceptance. The framework combines established ideas and does not claim each component as novel. No target-policy RL evaluation. Rollout transfer concerns cost-aware tree budgeting and drafter maintenance under refreshed targets, with stochastic verification and net training cost still to test. Numerical greedy disagreement is reported separately.

## Taxonomy dimensions

- Proposal Maintenance
- Scheduling and Mode Selection
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned primary HTML reviewed on 2026-11-23. Dates are source submission dates, not registry-update timestamps. Technical evaluation remains inference-origin. No formal acceptance inferred.
- Evidence pointer: Sections 3.1–3.4, 4.1–4.4 and 5; Appendices A–E distinguish proxy supervision, greedy verification, training attribution and numerical agreement.
- Source publication date: 2026-11-17
- Released code: [official artifact](https://github.com/mrfares11/specdec)
- Artifact checks: Paper-linked public repository and HEAD checked; code not executed on 2026-11-23, revision `537f6c9c7877d9b80cc18c15a873d2af9c1bdfbb`

## BibTeX

```bibtex
@article{fares2026fact,
  author = {Fares, Hadi and Hassan, Mayssa Hajj and Salman, Ali and Mohanna, Ammar},
  title = {{FACT: Fixed-Budget Allocation and Cross-Step Training for Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.23463},
  year = {2026},
  eprint = {2611.23463},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
