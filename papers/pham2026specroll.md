# SpecRoll

**SpecRoll: Fast-Slow Verifier-Feedback Adaptation for Speculative Reinforcement Learning Rollouts**

- Citation key: `pham2026specroll`
- Authors: Nhat Minh Pham and Duy Tung Doan and Thi Duyen Ngo and Vinh Van Nguyen and Khac-Hoai Nam Bui
- Year: 2026
- Bibliographic venue: arXiv preprint arXiv:2608.04962
- Source: [paper](https://arxiv.org/abs/2608.04962v1)
- Evidence setting: **Direct RL rollout / training**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: v1

## Mechanism / relevance

Separates fast verifier-feedback corrections from triggered slower head updates.

## Evidence and transfer boundary

Direct RL evidence. Distinguish trajectory-local correction, parameter updates, and target-verification semantics.

## Taxonomy dimensions

- Proposal Maintenance
- Verification Semantics
- Synchronization and Versioning

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified.
- Evidence pointer: Manuscript synthesis; individual source locations not yet indexed.
- Source publication date: 2026-08-05T15:32:27Z
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## Version review: v2

**SPARK: Learning from Verification in Speculative GRPO Rollouts**

- Authors in this version: Nhat Minh Pham and Duy Tung Doan and Quang Huy Phung and Thi Duyen Ngo and Vinh Van Nguyen and Khac-Hoai Nam Bui
- [Version source](https://arxiv.org/abs/2608.04962v2); revised 2026-10-14T04:53:03Z; checked 2026-10-26.
- Evidence pointer: Official arXiv v1/v2 submission history and full text; v2 Sections 3–4, ablations on correction sharing/reset and Appendix B.4.

The same arXiv study is now titled SPARK and has a revised author list. Its v2 description uses a low-rank logit correction shared among responses to the same prompt, updated after every verification round from verifier probabilities and reset at each rollout. A projection from draft features is retained and trained across rollouts. The v2 method does not update the draft backbone during generation or add target forward passes. Its training results and ablations must be interpreted using the v2 configuration, not substituted for v1 measurements.

Material version change, not a new study. The v2 revision was public on the manuscript cutoff date. The imported SpecRoll title, v1 BibTeX, reviewed_version and 46-study snapshot are retained for traceability. The author should reconcile the manuscript name, fast–slow-head description, Table 6 classification and any numerical claims with the chosen version before submission. No performance numbers have been silently overwritten.

## BibTeX

```bibtex
@article{pham2026specroll,
  author  = {Nhat Minh Pham and Duy Tung Doan and Thi Duyen Ngo and
             Vinh Van Nguyen and Khac-Hoai Nam Bui},
  title   = {{SpecRoll}: Fast-Slow Verifier-Feedback Adaptation for
             Speculative Reinforcement Learning Rollouts},
  journal = {arXiv preprint arXiv:2608.04962},
  year    = {2026},
  doi     = {10.48550/arXiv.2608.04962}
}
```

[Back to all records](../docs/all-papers.md)
