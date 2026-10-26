# ReAnchor

**ReAnchor: Reusing Rejected Verifier States for Diffusion Drafting**

- Citation key: `lee2026reanchor`
- Authors: Sanghyun Lee and Wonjin Nam and Seungho Jang and Jaeho Lee and Jiho Park and Jaewoon Lee and Seungryong Kim
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.26531v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Reuses verifier hidden states beyond the first rejection as shifted anchors for parallel blocks from a pretrained diffusion drafter. Positive overlaps attach those blocks to a baseline proposal and merge shared prefixes for a new target verification.

## Evidence and transfer boundary

Serving/inference with pretrained DFlash drafters and four autoregressive targets, evaluated at temperature zero across eight benchmarks. Rejected-suffix states are speculative proposal hints, not committed KV state or accepted output. Transfer requires correct-prefix target re-verification and bounded extra state/verification width. Nonzero-temperature RL sampling and end-to-end RL gains have not been demonstrated.

## Taxonomy dimensions

- Proposal Source
- Memory and Reuse State
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history, cross-checked against full HTML v1 on 2026-10-26. Curated after the manuscript cutoff; this is not a claim that the first posting was after the cutoff. No accepted venue is inferred.
- Evidence pointer: Sections 3.1–3.3 (shifted anchors and trie construction), 4.1–4.3 (setup and ablations), and the appendix on earliest positive-overlap selection.
- Source publication date: 2026-10-19
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: paper-linked repository not retrievable through public GitHub API; release not verified on 2026-10-26

## BibTeX

```bibtex
@misc{lee2026reanchor,
  author = {Lee, Sanghyun and Nam, Wonjin and Jang, Seungho and Lee, Jaeho and Park, Jiho and Lee, Jaewoon and Kim, Seungryong},
  title = {{ReAnchor: Reusing Rejected Verifier States for Diffusion Drafting}},
  year = {2026},
  eprint = {2610.26531},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2610.26531v1}
}
```

[Back to all records](../docs/all-papers.md)
