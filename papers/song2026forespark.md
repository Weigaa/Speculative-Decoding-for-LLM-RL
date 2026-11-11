# ForeSpark

**ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative Decoding**

- Citation key: `song2026forespark`
- Authors: Song, Jaeyong and Wang, Daniel and Patel, Pratyush and Kong, Jonny and Shah, Preyas and Kanaujia, Shobhit
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.13442v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Predicts acceptance before drafting and jointly allocates per-request draft lengths and a batch-wide verification budget.

## Evidence and transfer boundary

Fixed-target vLLM serving with standard speculative sampling. Pre-draft selection uses context, followed by post-draft verification allocation. RL transfer requires recalibration after policy refresh and profiling changing rollout concurrency. Reported serving throughput and SLO capacity are not RL training gains.

## Taxonomy dimensions

- Scheduling and Mode Selection
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned full text checked on 2026-11-11. Query-family discovery supplemented by official-source keyword search and citation tracing. Newly screened does not imply newly published.
- Evidence pointer: Sections 4–6
- Source publication date: 2026-11-10
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{song2026forespark,
  author = {Song, Jaeyong and Wang, Daniel and Patel, Pratyush and Kong, Jonny and Shah, Preyas and Kanaujia, Shobhit},
  title = {{ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.13442},
  year = {2026},
  eprint = {2611.13442},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
