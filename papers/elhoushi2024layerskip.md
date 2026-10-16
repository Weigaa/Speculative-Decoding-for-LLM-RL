# LayerSkip

**LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding**

- Citation key: `elhoushi2024layerskip`
- Authors: Mostafa Elhoushi and Akshat Shrivastava and Diana Liskovich and Basil Hosmer and Bram Wasti and Liangzhen Lai and Anas Mahmoud and Bilge Acun and Saurabh Agarwal and Ahmed Roman and Ahmed Aly and Beidi Chen and Carole-Jean Wu
- Year: 2024
- Bibliographic venue: Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics
- Source: [paper](https://doi.org/10.18653/v1/2024.acl-long.681)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: not recorded

## Mechanism / relevance

Uses early transformer layers as a self-speculative draft path and later computation for verification.

## Evidence and transfer boundary

Serving-origin evidence. State the actual greedy or stochastic configuration and its verification rule before asserting exactness for RL.

## Taxonomy dimensions

- Proposal Source
- Proposal Maintenance
- Verification Semantics

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified.
- Evidence pointer: Manuscript synthesis; individual source locations not yet indexed.
- Source publication date: not recorded
- Released code: not recorded (not a claim of non-availability)

## BibTeX

```bibtex
@inproceedings{elhoushi2024layerskip,
  author    = {Mostafa Elhoushi and Akshat Shrivastava and Diana Liskovich and Basil Hosmer and Bram Wasti and Liangzhen Lai and Anas Mahmoud and Bilge Acun and Saurabh Agarwal and Ahmed Roman and Ahmed Aly and Beidi Chen and Carole-Jean Wu},
  title     = {LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding},
  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
  pages     = {12622--12642},
  year      = {2024},
  doi       = {10.18653/v1/2024.acl-long.681}
}
```

[Back to all records](../docs/all-papers.md)
