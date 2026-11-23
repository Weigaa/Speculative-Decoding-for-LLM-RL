# Callo

**Callo: Serving Cache-Miss Requests with Speculative Decoding on Invalidated KV under Prefill-Decode Disaggregation**

- Citation key: `ou2026callo`
- Authors: Ou, Jianjun and Lentz, Matthew
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.18459v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Uses repositioned KV invalidated by context edits for target-model drafting while exact re-prefill streams replacement KV, then verifies against exact state, with load-aware admission and early stopping.

## Evidence and transfer boundary

SWE-agent prompt/reply-length replay on two H200 NVL GPUs with disaggregated vLLM, three model families and default fixed-tie greedy verification. Main end-to-end serving gains combine streaming KV transfer and speculation; Callo-Stream isolates transfer. A temperature-0.8 single-request ablation is separate, and 96-GPU results are simulation rather than direct measurements. Numerical output identity across batches is not assumed. No RL training evaluation. Transfer concerns repeated long-context agent rollouts with context edits, spare decode capacity and exact current-policy state available for verification. Reusing KV after a context edit does not establish validity across policy-weight updates, which additionally require policy-version-aware invalidation. Code not recorded.

## Taxonomy dimensions

- Workload Recurrence
- Proposal Source
- Memory and Reuse State
- Placement and Idle Resources
- Scheduling and Mode Selection

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned primary HTML reviewed on 2026-11-23. Dates are source submission dates, not registry-update timestamps. Technical evaluation remains inference-origin. No formal acceptance inferred.
- Evidence pointer: Sections 4.2–4.6, 5.1–5.5 and 6, plus Appendices C and F; Table 3 all-request/miss latency differs from simulation and single-request ablations.
- Source publication date: 2026-11-13
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{ou2026callo,
  author = {Ou, Jianjun and Lentz, Matthew},
  title = {{Callo: Serving Cache-Miss Requests with Speculative Decoding on Invalidated KV under Prefill-Decode Disaggregation}},
  journal = {arXiv preprint arXiv:2611.18459},
  year = {2026},
  eprint = {2611.18459},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
