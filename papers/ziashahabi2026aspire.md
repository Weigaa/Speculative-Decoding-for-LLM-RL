# ASPIRE

**ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference**

- Citation key: `ziashahabi2026aspire`
- Authors: Amir Ziashahabi and Hossein Entezari Zarch and Lei Gao and Murali Annavaram and Salman Avestimehr
- Year: 2026
- Bibliographic venue: arXiv preprint arXiv:2609.17943
- Source: [paper](https://arxiv.org/abs/2609.17943)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: v1

## Mechanism / relevance

Mixed draft/verify batches and request-specific verification timing.

## Evidence and transfer boundary

Serving / inference evaluation, not direct RL training evidence. Claims remain tied to the source evaluation setting. For transfer, verify stochastic sampling semantics, evolving-policy compatibility, and net runtime cost.

## Taxonomy dimensions

- Scheduling and Mode Selection
- Proposal Source

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified.
- Evidence pointer: Sections 3–4
- Source publication date: 2026-09-16T00:04:13Z
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{ziashahabi2026aspire,
  author  = {Amir Ziashahabi and Hossein Entezari Zarch and Lei Gao and Murali Annavaram and Salman Avestimehr},
  title   = {{ASPIRE}: Asynchronous Batched Self-Speculative Decoding for Long-Context {LLM} Inference},
  journal = {arXiv preprint arXiv:2609.17943},
  year    = {2026},
  doi     = {10.48550/arXiv.2609.17943}
}
```

[Back to all records](../docs/all-papers.md)
