# Spexis

**Spexis: Speculative Lookahead Scheduling for LLM Inference**

- Citation key: `jung2026spexis`
- Authors: Hyungyu Jung and Jaehyeok Yu and Hoonseo Choi and Sungkyun Kim and Jinho Lee and Jiwon Seo
- Year: 2026
- Bibliographic venue: arXiv preprint arXiv:2609.34370
- Source: [paper](https://arxiv.org/abs/2609.34370)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: v1

## Mechanism / relevance

Lookahead scheduling using expected acceptance and memory pressure.

## Evidence and transfer boundary

Serving / inference evaluation, not direct RL training evidence. Claims remain tied to the source evaluation setting. For transfer, verify stochastic sampling semantics, evolving-policy compatibility, and net runtime cost.

## Taxonomy dimensions

- Placement and Idle Resources
- Scheduling and Mode Selection

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified.
- Evidence pointer: Sections 3–5
- Source publication date: 2026-09-28T05:46:02Z
- Released code: [official artifact](https://github.com/mlsys-seo/spexis)
- Artifact checks: public_repository_checked on 2026-10-16, revision `038c3b9f666dd96989f7c66d5b7cb1236a5a4664`

## BibTeX

```bibtex
@article{jung2026spexis,
  author  = {Hyungyu Jung and Jaehyeok Yu and Hoonseo Choi and Sungkyun Kim and Jinho Lee and Jiwon Seo},
  title   = {Spexis: Speculative Lookahead Scheduling for {LLM} Inference},
  journal = {arXiv preprint arXiv:2609.34370},
  year    = {2026},
  doi     = {10.48550/arXiv.2609.34370}
}
```

[Back to all records](../docs/all-papers.md)
