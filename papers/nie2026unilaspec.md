# Uni-LaSpec

**Seeing What Matters, Verifying What Pays: Load-Adaptive Speculative Decoding for Vision-Language Models**

- Citation key: `nie2026unilaspec`
- Authors: Nie, Hong and Gao, Zhangchi and Liang, Yuqian and Yu, Jun and Wang, Bo and Sun, Jianqing and Liu, Shengping
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.01617v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Selects visual context from verifier attention and switches between tree and truncated-chain verification according to current load.

## Evidence and transfer boundary

Frozen VLM inference across six models, concurrency 1–64 and multiple GPUs, with greedy and temperature-one settings. RL transfer requires current-policy visual state and recalibration under evolving rollout load.

## Taxonomy dimensions

- Scheduling and Mode Selection
- Memory and Reuse State
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and full text checked on 2026-11-08. Discovery used the recorded query families and author-supplied FlexFloor link.
- Evidence pointer: Sections III–IV and evaluation appendices
- Source publication date: 2026-11-01
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{nie2026unilaspec,
  author = {Nie, Hong and Gao, Zhangchi and Liang, Yuqian and Yu, Jun and Wang, Bo and Sun, Jianqing and Liu, Shengping},
  title = {{Seeing What Matters, Verifying What Pays: Load-Adaptive Speculative Decoding for Vision-Language Models}},
  journal = {arXiv preprint arXiv:2611.01617},
  year = {2026},
  eprint = {2611.01617},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
