# Session-local recency and restraint

**Text Speeding Itself Up: Recency and Restraint in Session-Local Drafting**

- Citation key: `vandenbosch2026sessiondraft`
- Authors: van den Bosch, Antal
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.19455v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Copies continuations from the most recent matching prompt/output n-gram and can abstain below a match-length floor, comparing this cheap rule against recency-weighted session memory and confidence gating.

## Evidence and transfer boundary

Mistral-7B-v0.1 float16 greedy inference on an Apple M1 Max Mac Studio with CPU drafters. Experiments compare speed, whole-system energy and token agreement on general, medical and legal text. Most-recent lookup captures the speed benefit; the richer memory adds no measurable improvement at 30–40 times drafting cost. Long-output gains shrink with a repetition penalty. Approximately 94% token-identical generations and near-tie divergence do not establish stochastic equivalence. No sampling, batched GPU serving or target-policy RL evaluation. Rollout transfer concerns inexpensive recent-history proposals and selective activation, with history scope, sampling, length and resource costs to test. This is a distinct session-local ablation study citing the earlier offline-trained Olifant work, not a new key for that same paper.

## Taxonomy dimensions

- Workload Recurrence
- Proposal Source
- Memory and Reuse State
- Scheduling and Mode Selection

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned primary HTML reviewed on 2026-11-23. Dates are source submission dates, not registry-update timestamps. Technical evaluation remains inference-origin. No formal acceptance inferred. Author byline and prior verified author record support the name van den Bosch, Antal; the arXiv meta tag splits the surname particle incorrectly. Distinct title, arXiv ID and session-local comparison were checked against the earlier Olifant record.
- Evidence pointer: Sections 2–6 and Limitations; Section 2.3 rebuilds session memory each call, and Section 6/Appendix A separate agreement from speed.
- Source publication date: 2026-11-14
- Released code: [official artifact](https://github.com/antalvdb/olifant-speculative)
- Artifact checks: Paper-linked public repository and HEAD checked; code not executed on 2026-11-23, revision `6d7d17fe37bbfca6e4f0c1e2ca6f8f4c0d853ab8`

## BibTeX

```bibtex
@article{vandenbosch2026sessiondraft,
  author = {van den Bosch, Antal},
  title = {{Text Speeding Itself Up: Recency and Restraint in Session-Local Drafting}},
  journal = {arXiv preprint arXiv:2611.19455},
  year = {2026},
  eprint = {2611.19455},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
