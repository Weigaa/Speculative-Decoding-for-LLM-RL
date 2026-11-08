# RECAP

**RECAP: Context-Aware Prediction Recycling with Request-Local and Persistent Memories for Multimodal Speculative Decoding**

- Citation key: `zhu2026recap`
- Authors: Zhu, Hengjie and Wu, Dayan and Liu, Xinze and Fu, Peng and Lin, Zheng and Wang, Weiping
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.05894v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Combines request-local contextual prediction memories with persistent token-level memory to build verified candidate trees.

## Evidence and transfer boundary

Qwen2.5-VL-7B and LLaVA-1.6-7B greedy inference at batch one. Request-local context avoids mixing image-conditioned predictions. RL transfer requires policy-version-aware memory and stochastic verification.

## Taxonomy dimensions

- Workload Recurrence
- Memory and Reuse State
- Proposal Source

## Source and artifact record

- Metadata provenance: Official arXiv metadata and full text checked on 2026-11-08. Discovery used the recorded query families and author-supplied FlexFloor link.
- Evidence pointer: Sections 3–5 and Appendices A, D, G
- Source publication date: 2026-11-04
- Released code: [official artifact](https://github.com/Senmo996/RECAP-official-code)
- Artifact checks: paper-linked public repository and default-branch commit checked; code not executed on 2026-11-08, revision `e46894933ed2f42f1703f677ef0314d6c0ee471d`

## BibTeX

```bibtex
@article{zhu2026recap,
  author = {Zhu, Hengjie and Wu, Dayan and Liu, Xinze and Fu, Peng and Lin, Zheng and Wang, Weiping},
  title = {{RECAP: Context-Aware Prediction Recycling with Request-Local and Persistent Memories for Multimodal Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.05894},
  year = {2026},
  eprint = {2611.05894},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
