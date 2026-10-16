# EDR

**Training Parallel Speculative Draft Models by Directly Minimizing Expected Decoding Rounds**

- Citation key: `zhao2026edr`
- Authors: Yunxiao Zhao and Changxiao Cai
- Year: 2026
- Bibliographic venue: arXiv preprint arXiv:2610.10411
- Source: [paper](https://arxiv.org/abs/2610.10411)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: v1

## Mechanism / relevance

Optimize decoding rounds across speculative blocks.

## Evidence and transfer boundary

Serving / inference evaluation, not direct RL training evidence. Claims remain tied to the source evaluation setting. For transfer, verify stochastic sampling semantics, evolving-policy compatibility, and net runtime cost.

## Taxonomy dimensions

- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified.
- Evidence pointer: Sections 3–5
- Source publication date: 2026-10-07T16:56:29Z
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{zhao2026edr,
  author  = {Yunxiao Zhao and Changxiao Cai},
  title   = {Training Parallel Speculative Draft Models by Directly Minimizing Expected Decoding Rounds},
  journal = {arXiv preprint arXiv:2610.10411},
  year    = {2026},
  doi     = {10.48550/arXiv.2610.10411}
}
```

[Back to all records](../docs/all-papers.md)
