# FactorSpec

**FactorSpec: Serving Exact Relational Constraints as Speculative Drafts**

- Citation key: `su2026factorspec`
- Authors: Su, Jianchang and Xiang, Dawei and Zhang, Wei
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.02297v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Compiles finite-domain schema relations into feasible token masks and deterministic draft runs, with per-request verification widths and CPU/GPU overlap.

## Evidence and transfer boundary

SGLang/vLLM structured serving. Exactness is relative to the specified masked decoder, not the unconstrained model or global conditioning on a valid record. RL transfer requires matching rollout log probabilities and exploration to that constrained policy.

## Taxonomy dimensions

- Proposal Source
- Verification Semantics
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and full text checked on 2026-11-08. Discovery used the recorded query families and author-supplied FlexFloor link.
- Evidence pointer: Sections 3–6 and appendices on sampling and engine integration
- Source publication date: 2026-11-01
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{su2026factorspec,
  author = {Su, Jianchang and Xiang, Dawei and Zhang, Wei},
  title = {{FactorSpec: Serving Exact Relational Constraints as Speculative Drafts}},
  journal = {arXiv preprint arXiv:2611.02297},
  year = {2026},
  eprint = {2611.02297},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
