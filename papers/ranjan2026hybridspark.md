# Hybrid Spark

**Hybrid Spark: Adaptive Speculative Decoding That Lets the Content Choose the Drafter**

- Citation key: `ranjan2026hybridspark`
- Authors: Ranjan, Ekagra and Venkitesh, Bharat
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.05611v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Selects between neural and n-gram draft chains using calibrated acceptance and a load-dependent verification-slot price.

## Evidence and transfer boundary

vLLM serving with DSpark and an n-gram drafter. Appendix H permits the proposed selector under greedy drafting at positive target temperature, but not under probabilistic drafting at positive temperature. Alternative selectors cover that setting. RL transfer requires a valid selector and refreshed calibration. Distinct from SPARK (2608.04962).

## Taxonomy dimensions

- Workload Recurrence
- Scheduling and Mode Selection
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv metadata and full text checked on 2026-11-08. Discovery used the recorded query families and author-supplied FlexFloor link.
- Evidence pointer: Sections 3–5 and Appendices H–J
- Source publication date: 2026-11-03
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{ranjan2026hybridspark,
  author = {Ranjan, Ekagra and Venkitesh, Bharat},
  title = {{Hybrid Spark: Adaptive Speculative Decoding That Lets the Content Choose the Drafter}},
  journal = {arXiv preprint arXiv:2611.05611},
  year = {2026},
  eprint = {2611.05611},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
