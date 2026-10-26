# DCOCO

**Contextual Correction of Parallel Drafts for Speculative Decoding**

- Citation key: `eisenstadt2026dcoco`
- Authors: Roy Eisenstadt and Harel Lidar and Tal Gonen and Omer Luxembourg and Itamar Zimerman and Lior Wolf and Eli David and Ilan Naiman
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.12570v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Retains multiple draft-token candidates per position and scores compatibility between adjacent positions in parallel, recovering intra-block dependence without a serial correction chain.

## Evidence and transfer boundary

Serving experiments retrain comparator drafters on the same corpus/backbone and test greedy and stochastic decoding, including 4–32 concurrent requests. The relevant transfer is the cost of draft correction as rollout concurrency changes. Target-policy refresh, correction-model maintenance and any closed-batch activation rule remain to be evaluated in RL. Higher acceptance alone is not treated as a throughput guarantee.

## Taxonomy dimensions

- Proposal Source
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history, cross-checked against full HTML v1 on 2026-10-26. Curated after the manuscript cutoff; this is not a claim that the first posting was after the cutoff. No accepted venue is inferred.
- Evidence pointer: Method section on parallel contextual candidate scoring; experimental setup and serving results; Appendix F (higher concurrency) and G (stochastic verification with deterministic proposals).
- Source publication date: 2026-10-08
- Released code: [official artifact](https://github.com/two-delta/DCOCO)
- Artifact checks: linked and checked; public repository on 2026-10-26, revision `7a39cf1ec2d273894082463b41ef95d823b4fc7a`

## BibTeX

```bibtex
@misc{eisenstadt2026dcoco,
  author = {Eisenstadt, Roy and Lidar, Harel and Gonen, Tal and Luxembourg, Omer and Zimerman, Itamar and Wolf, Lior and David, Eli and Naiman, Ilan},
  title = {{Contextual Correction of Parallel Drafts for Speculative Decoding}},
  year = {2026},
  eprint = {2610.12570},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2610.12570v1}
}
```

[Back to all records](../docs/all-papers.md)
