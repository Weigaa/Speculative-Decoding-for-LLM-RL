# EAGLE-3

**EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test**

- Citation key: `li2025eagle3`
- Authors: Yuhui Li and Fangyun Wei and Chao Zhang and Hongyang Zhang
- Year: 2025
- Bibliographic venue: Advances in Neural Information Processing Systems
- Source: [paper](https://arxiv.org/abs/2503.01840)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: not recorded

## Mechanism / relevance

Uses learned target-conditioned proposal state for accelerated inference.

## Evidence and transfer boundary

Serving-origin evidence. An external learned drafter trained for a fixed target is not automatically maintained as an RL policy evolves.

## Taxonomy dimensions

- Proposal Source
- Proposal Maintenance
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified. Primary paper URL added during repository setup; source link does not independently verify every imported field.
- Evidence pointer: Manuscript synthesis; individual source locations not yet indexed.
- Source publication date: not recorded
- Released code: [official artifact](https://github.com/SafeAILab/EAGLE)

## BibTeX

```bibtex
@inproceedings{li2025eagle3,
  author    = {Yuhui Li and Fangyun Wei and Chao Zhang and Hongyang Zhang},
  title     = {EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test},
  booktitle = {Advances in Neural Information Processing Systems},
  year      = {2025}
}
```

[Back to all records](../docs/all-papers.md)
