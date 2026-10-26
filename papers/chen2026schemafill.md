# SchemaFill

**SchemaFill: Efficient LLM Tool Calling via Slot-Parallel Speculative Decoding**

- Citation key: `chen2026schemafill`
- Authors: Zhi-Kai Chen and Song-Yan Li and De-Chuan Zhan and Han-Jia Ye
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.07086v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Uses public tool schemas to draft argument slots and multiple tool calls in parallel, then assembles structural text and slot candidates for target verification under their actual autoregressive prefixes.

## Evidence and transfer boundary

Tool-call token generation on Glaive/BFCL serving benchmarks, not end-to-end agentic RL. Main experiments are greedy; Appendix B defines the stochastic correction rule and Appendix C.5 reports temperature-one results. This is token-level proposal acceleration, not execution or acceptance of unverified tool actions. Transfer requires preserving the current rollout policy and validation of the additional structured-drafting overhead within the agent loop.

## Taxonomy dimensions

- Proposal Source
- Verification Semantics
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history, cross-checked against full HTML v1 on 2026-10-26. Curated after the manuscript cutoff; this is not a claim that the first posting was after the cutoff. No accepted venue is inferred.
- Evidence pointer: Sections 3.1–3.3 and 4; Appendix B (greedy and stochastic consistency) and C.5 (temperature-one evaluation).
- Source publication date: 2026-10-05
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: paper-linked repository not retrievable through public GitHub API; release not verified on 2026-10-26

## BibTeX

```bibtex
@misc{chen2026schemafill,
  author = {Chen, Zhi-Kai and Li, Song-Yan and Zhan, De-Chuan and Ye, Han-Jia},
  title = {{SchemaFill: Efficient LLM Tool Calling via Slot-Parallel Speculative Decoding}},
  year = {2026},
  eprint = {2610.07086},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2610.07086v1}
}
```

[Back to all records](../docs/all-papers.md)
