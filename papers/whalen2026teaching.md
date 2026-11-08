# Teaching Diffusion to Speculate Left-to-Right

**Teaching Diffusion to Speculate Left-to-Right**

- Citation key: `whalen2026teaching`
- Authors: Whalen, Lexington and Ito, Yuki and Sakamoto, Ryo
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2606.11552v3)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v3

## Mechanism / relevance

Trains parallel drafters using position weighting, first-error focal loss and a surrogate for accepted-prefix length.

## Evidence and transfer boundary

Reviewed v3, updated November 4; first public June 10. Fixed instruction-tuned targets with no target RL. Transfer is an acceptance-oriented drafter-maintenance objective, whose update cost and effectiveness must be evaluated under evolving rollout policies.

## Taxonomy dimensions

- Proposal Maintenance
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and full text checked on 2026-11-08. Discovery used the recorded query families and author-supplied FlexFloor link.
- Evidence pointer: Sections 3–5.6
- Source publication date: 2026-06-10
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{whalen2026teaching,
  author = {Whalen, Lexington and Ito, Yuki and Sakamoto, Ryo},
  title = {{Teaching Diffusion to Speculate Left-to-Right}},
  journal = {arXiv preprint arXiv:2606.11552},
  year = {2026},
  eprint = {2606.11552},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
