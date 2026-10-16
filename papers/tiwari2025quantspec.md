# QuantSpec

**QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache**

- Citation key: `tiwari2025quantspec`
- Authors: Rishabh Tiwari and Haocheng Xi and Aditya Tomar and Coleman Richard Charles Hooper and Sehoon Kim and Maxwell Horton and Mahyar Najibi and Michael W. Mahoney and Kurt Keutzer and Amir Gholami
- Year: 2025
- Bibliographic venue: Proceedings of the 42nd International Conference on Machine Learning
- Source: [paper](https://arxiv.org/abs/2502.10424)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: not recorded

## Mechanism / relevance

Uses hierarchical quantized KV state in a target-derived speculative path.

## Evidence and transfer boundary

Serving-origin evidence. RL transfer requires accounting for cache refresh, memory residency, and evolving target weights.

## Taxonomy dimensions

- Proposal Source
- Memory and Reuse State

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified. Primary paper URL added during repository setup; source link does not independently verify every imported field.
- Evidence pointer: Manuscript synthesis; individual source locations not yet indexed.
- Source publication date: not recorded
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@inproceedings{tiwari2025quantspec,
  author    = {Rishabh Tiwari and Haocheng Xi and Aditya Tomar and Coleman Richard Charles Hooper and Sehoon Kim and Maxwell Horton and Mahyar Najibi and Michael W. Mahoney and Kurt Keutzer and Amir Gholami},
  title     = {{QuantSpec}: Self-Speculative Decoding with Hierarchical Quantized {KV} Cache},
  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
  volume    = {267},
  pages     = {59668--59686},
  year      = {2025}
}
```

[Back to all records](../docs/all-papers.md)
