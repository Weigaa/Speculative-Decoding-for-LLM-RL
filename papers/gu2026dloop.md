# DLoop

**DLoop: Looped Speculative Decoding**

- Citation key: `gu2026dloop`
- Authors: Geonmo Gu and Byeongho Heo and HeeJae Jun and Yoohoon Kang and Sangmin Lee and Sangdoo Yun and Dongyoon Han
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.07659v2)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v2

## Mechanism / relevance

Runs multiple whole drafting stages before one target verification, continuing while draft confidence exceeds a threshold. Loop-aware training exposes the drafter to its own hidden states at unverified positions.

## Evidence and transfer boundary

Serving/inference across autoregressive, parallel and MTP drafters. The standard target acceptance rule is retained; experiments include greedy and temperature-one sampling. A rollout transfer must tune confidence thresholds against target-verification cost and load, and maintain a compatible drafter after policy refresh. This is not direct RL evaluation. DLoop (2610.07659) is distinct from the separately queued D-Loop (2610.06011).

## Taxonomy dimensions

- Proposal Source
- Verification Semantics
- Scheduling and Mode Selection
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history, cross-checked against full HTML v2 on 2026-10-26. Curated after the manuscript cutoff; this is not a claim that the first posting was after the cutoff. No accepted venue is inferred.
- Evidence pointer: Section 3 (confidence-controlled drafting loop and loop-aware training), Section 4 and Appendix A.1–A.2 (setup and greedy/sampling results).
- Source publication date: 2026-10-06
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: paper-linked public repository checked; README-only placeholder says code is under internal review and will be released; implementation not yet verified on 2026-10-26, revision `577bb1a42bea5c28d14937cb6fe14fd745e7a705`

## BibTeX

```bibtex
@misc{gu2026dloop,
  author = {Gu, Geonmo and Heo, Byeongho and Jun, HeeJae and Kang, Yoohoon and Lee, Sangmin and Yun, Sangdoo and Han, Dongyoon},
  title = {{DLoop: Looped Speculative Decoding}},
  year = {2026},
  eprint = {2610.07659},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2610.07659v2}
}
```

[Back to all records](../docs/all-papers.md)
