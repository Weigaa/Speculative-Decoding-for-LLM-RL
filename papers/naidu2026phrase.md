# Phrase-level drafting

**Phrase-Level Speculative Decoding on a Frozen Target**

- Citation key: `naidu2026phrase`
- Authors: Naidu, Madhusudhana
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.12464v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Predicts entries of a separate phrase vocabulary from frozen target features, expands each phrase into target tokens, and verifies candidate paths.

## Evidence and transfer boundary

Greedy frozen-target inference at batch one on small prompt sets. Output agreement is qualified by floating-point tie-breaking. Online adaptation is not established, and the larger EAGLE-3 tree remains faster. Transfer concerns candidate units and head cost, requiring stochastic verification and policy-aware head/vocabulary maintenance.

## Taxonomy dimensions

- Proposal Source
- Verification Semantics

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned full text checked on 2026-11-11. Query-family discovery supplemented by official-source keyword search and citation tracing. Newly screened does not imply newly published.
- Evidence pointer: Sections 2–5
- Source publication date: 2026-11-09
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{naidu2026phrase,
  author = {Naidu, Madhusudhana},
  title = {{Phrase-Level Speculative Decoding on a Frozen Target}},
  journal = {arXiv preprint arXiv:2611.12464},
  year = {2026},
  eprint = {2611.12464},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
