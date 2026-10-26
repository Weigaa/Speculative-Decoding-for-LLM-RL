# DominoTree

**DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding**

- Citation key: `lin2026dominotree`
- Authors: Saw S. Lin and Jyh-Shing Roger Jang
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2607.08642v4)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v4

## Mechanism / relevance

Makes tree proposals conditional on each candidate path through a Domino recurrent correction and constructs a high-value tree with a best-first or GPU frontier builder. Verification must maintain tree-correct recurrent as well as attention state.

## Evidence and transfer boundary

Both single-stream research-harness and SGLang inference experiments are reported. In the served concurrency sweep, a low-concurrency advantage can reverse at larger batches despite longer acceptance. Transfer therefore requires engine-level profiling and tree-correct recurrent-state handling, rather than translating research-harness speedup to RL. The paper does not evaluate target-policy evolution or RL training.

## Taxonomy dimensions

- Proposal Source
- Verification Semantics
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history, cross-checked against full HTML v4 on 2026-10-26. Curated after the manuscript cutoff; this is not a claim that the first posting was after the cutoff. No accepted venue is inferred.
- Evidence pointer: Sections 3.2–3.4; 4.4 (numerical agreement); 4.5.1–4.5.4 (serving, concurrency and hybrid recurrent verification); Section 6 (implementation scope and load-budget limitations).
- Source publication date: 2026-07-09
- Released code: [official artifact](https://github.com/slin-zhq/Domino-Tree)
- Artifact checks: linked and checked; public repository on 2026-10-26, revision `6f5a2bfec7bb07bfbe98800d741bd6c30b0ceb0d`

## BibTeX

```bibtex
@misc{lin2026dominotree,
  author = {Lin, Saw S. and Jang, Jyh-Shing Roger},
  title = {{DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding}},
  year = {2026},
  eprint = {2607.08642},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2607.08642v4}
}
```

[Back to all records](../docs/all-papers.md)
