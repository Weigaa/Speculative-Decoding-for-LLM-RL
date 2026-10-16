# SPEC-RL (Liu et al.)

**SPEC-RL: Accelerating On-Policy Reinforcement Learning with Speculative Rollouts**

- Citation key: `liu2025specrl`
- Authors: Bingshuai Liu and Ante Wang and Zijun Min and Liang Yao and Haibo Zhang and Yang Liu and Xu Han and Peng Li and Anxiang Zeng and Jinsong Su
- Year: 2025
- Bibliographic venue: arXiv preprint arXiv:2509.23232
- Source: [paper](https://arxiv.org/abs/2509.23232)
- Evidence setting: **Direct RL rollout / training**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: v3

## Mechanism / relevance

Reuses previous-rollout trajectories as proposals and verifies them under the current policy.

## Evidence and transfer boundary

Direct RL evidence. Exact and lenient acceptance settings must be distinguished. This is a different paper from SpecRL by Jin et al.

## Taxonomy dimensions

- Workload Recurrence
- Proposal Source
- Verification Semantics
- Memory and Reuse State

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified.
- Evidence pointer: Manuscript synthesis; individual source locations not yet indexed.
- Source publication date: 2025-09-27T10:32:34Z
- Released code: not recorded (not a claim of non-availability)

## BibTeX

```bibtex
@article{liu2025specrl,
  author  = {Bingshuai Liu and Ante Wang and Zijun Min and Liang Yao and
             Haibo Zhang and Yang Liu and Xu Han and Peng Li and
             Anxiang Zeng and Jinsong Su},
  title   = {{SPEC-RL}: Accelerating On-Policy Reinforcement Learning with
             Speculative Rollouts},
  journal = {arXiv preprint arXiv:2509.23232},
  year    = {2025},
  doi     = {10.48550/arXiv.2509.23232}
}
```

[Back to all records](../docs/all-papers.md)
