# TraceSpec

**TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents**

- Citation key: `zhao2026tracespec`
- Authors: Zhao, Jihao and Zu, Shuaishuai and Li, Pengfei and Qin, Biao and Fang, Guanghuan and Feng, Ben and Yang, Baochuan
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.41177v2)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v2

## Mechanism / relevance

Combines agent trajectory replay and dynamic execution with state-conditioned allocation of a fixed drafter-supervision budget.

## Evidence and transfer boundary

Frozen Qwen3 targets at temperatures zero and one. Adaptive training gains are measured on fixed-prefix replay, while separate dynamic agent experiments distinguish episode latency from decoding. Repository tasks include real file reads but simulated edit/test feedback. Transfer concerns context/phase-aware drafter supervision and comparable agent-rollout measurement, not demonstrated target-RL training acceleration.

## Taxonomy dimensions

- Proposal Maintenance
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned full text checked on 2026-11-11. Query-family discovery supplemented by official-source keyword search and citation tracing. Newly screened does not imply newly published.
- Evidence pointer: Sections 3–4 and Appendices A–E
- Source publication date: 2026-10-30
- Released code: [official artifact](https://github.com/Robot2050/TraceSpec)
- Artifact checks: Paper-linked public repository metadata and HEAD checked; code not executed on 2026-11-11, revision `1acb4be52e028b2a1aed550b187c227dc8b87cbe`

## BibTeX

```bibtex
@article{zhao2026tracespec,
  author = {Zhao, Jihao and Zu, Shuaishuai and Li, Pengfei and Qin, Biao and Fang, Guanghuan and Feng, Ben and Yang, Baochuan},
  title = {{TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents}},
  journal = {arXiv preprint arXiv:2610.41177},
  year = {2026},
  eprint = {2610.41177},
  archivePrefix = {arXiv},
  note = {Reviewed version v2}
}
```

[Back to all records](../docs/all-papers.md)
