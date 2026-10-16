# H-Spec

**H-Spec: Parallel Speculative Decoding Without a Drafter-Side KV Cache**

- Citation key: `jiang2026hspec`
- Authors: Weifan Jiang and Krishna Teja Chitty-Venkata and Megan Flynn and Reed Meyerson and Zhenting Qi and Tianyu Wu and Eldar Kurtic and Minlan Yu and Alexandre Marques
- Year: 2026
- Bibliographic venue: arXiv preprint arXiv:2609.24197
- Source: [paper](https://arxiv.org/abs/2609.24197)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: v1

## Mechanism / relevance

Target KV reuse without a separate drafter KV cache.

## Evidence and transfer boundary

Serving / inference evaluation, not direct RL training evidence. Claims remain tied to the source evaluation setting. For transfer, verify stochastic sampling semantics, evolving-policy compatibility, and net runtime cost.

## Taxonomy dimensions

- Memory and Reuse State
- Proposal Source

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified.
- Evidence pointer: Sections 3–4
- Source publication date: 2026-09-21T07:11:29Z
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{jiang2026hspec,
  author  = {Weifan Jiang and Krishna Teja Chitty-Venkata and Megan Flynn and Reed Meyerson and Zhenting Qi and Tianyu Wu and Eldar Kurtic and Minlan Yu and Alexandre Marques},
  title   = {{H-Spec}: Parallel Speculative Decoding Without a Drafter-Side {KV} Cache},
  journal = {arXiv preprint arXiv:2609.24197},
  year    = {2026},
  doi     = {10.48550/arXiv.2609.24197}
}
```

[Back to all records](../docs/all-papers.md)
