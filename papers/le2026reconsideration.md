# Parallel Reconsideration

**Give the Drafter a Second Chance to Guess: Parallel Reconsideration for Speculative Decoding**

- Citation key: `le2026reconsideration`
- Authors: Le, Hoang Anh Duy and Dong, Huibing and Khadem, Alireza and Sun, Ziteng and Song, Xiang and Huang, Yizheng and Radpour, Soroush and Shrivastava, Anshumali and He, Ye
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.05724v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Revises uncertain feature-level guesses in parallel and appends refined candidates to the draft tree.

## Evidence and transfer boundary

Serving evaluation compares EAGLE-3.1 at matched budgets across Llama, Qwen and Gemma models. Verification is retained. RL transfer must recalibrate uncertainty after policy changes and measure the additional draft work at changing load.

## Taxonomy dimensions

- Parallel and Load-Aware Drafting
- Proposal Maintenance

## Source and artifact record

- Metadata provenance: Official arXiv metadata and full text checked on 2026-11-08. Discovery used the recorded query families and author-supplied FlexFloor link.
- Evidence pointer: Sections 3–6 and Appendix C–D
- Source publication date: 2026-11-03
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{le2026reconsideration,
  author = {Le, Hoang Anh Duy and Dong, Huibing and Khadem, Alireza and Sun, Ziteng and Song, Xiang and Huang, Yizheng and Radpour, Soroush and Shrivastava, Anshumali and He, Ye},
  title = {{Give the Drafter a Second Chance to Guess: Parallel Reconsideration for Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.05724},
  year = {2026},
  eprint = {2611.05724},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
