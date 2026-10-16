# Post-training MTP heads

**Match the Distribution, Not the Compute: Post-Training Multi-Token Prediction Heads**

- Citation key: `badarayani2026posttrainingmtp`
- Authors: Prachi Badarayani and Aidan Jay and Chenghui Zhou and Dayquan Julienne and Yuan Gao and Tianwei Chen and George Zerveas and Ishmam Zabir and Xiren Zhou and Chris Quirk and Xia Song
- Year: 2026
- Bibliographic venue: arXiv preprint arXiv:2610.00888
- Source: [paper](https://arxiv.org/abs/2610.00888)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: v1

## Mechanism / relevance

Frozen-target head training, adaptive depth and relaxed verification.

## Evidence and transfer boundary

Serving / inference evaluation, not direct RL training evidence. Claims remain tied to the source evaluation setting. For transfer, verify stochastic sampling semantics, evolving-policy compatibility, and net runtime cost.

## Taxonomy dimensions

- Proposal Source

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified.
- Evidence pointer: Sections 3–5
- Source publication date: not recorded
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{badarayani2026posttrainingmtp,
  author  = {Prachi Badarayani and Aidan Jay and Chenghui Zhou and Dayquan Julienne and Yuan Gao and Tianwei Chen and George Zerveas and Ishmam Zabir and Xiren Zhou and Chris Quirk and Xia Song},
  title   = {Match the Distribution, Not the Compute: Post-Training Multi-Token Prediction Heads},
  journal = {arXiv preprint arXiv:2610.00888},
  year    = {2026},
  doi     = {10.48550/arXiv.2610.00888}
}
```

[Back to all records](../docs/all-papers.md)
