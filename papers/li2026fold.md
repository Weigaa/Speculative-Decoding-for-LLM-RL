# FOLD

**FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding**

- Citation key: `li2026fold`
- Authors: Shuxuan Li and Jialiang Kang and Yanghao Zhou and Ziye Zhu and Xiao Yang
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.20392v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Extends a pretrained short-context drafter without retraining by preserving local positional order and presenting distant entries as position-free far memory. Separate attention normalization controls the contribution of distant memory.

## Evidence and transfer boundary

Long-context serving/inference experiments, not RL rollout. Transfer targets long rollout prefixes whose draft attention/state is the bottleneck. The memory transformation belongs to the drafter; current-policy target verification must remain intact. The reported greedy output-agreement checks do not establish stochastic RL-update equivalence or behavior after target-policy drift.

## Taxonomy dimensions

- Proposal Source
- Memory and Reuse State

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history, cross-checked against full HTML v1 on 2026-10-26. Curated after the manuscript cutoff; this is not a claim that the first posting was after the cutoff. No accepted venue is inferred.
- Evidence pointer: Sections 3.1–3.3 and 4; Appendix B.2–B.5 (evaluation data, length dispatch, storage-matched controls and output agreement).
- Source publication date: 2026-10-14
- Released code: [official artifact](https://github.com/NuyoahNasuS/FOLD)
- Artifact checks: linked and checked; public repository on 2026-10-26, revision `22beb43a7704beeabd6e5a242404aa2f44982a79`

## BibTeX

```bibtex
@misc{li2026fold,
  author = {Li, Shuxuan and Kang, Jialiang and Zhou, Yanghao and Zhu, Ziye and Yang, Xiao},
  title = {{FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding}},
  year = {2026},
  eprint = {2610.20392},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2610.20392v1}
}
```

[Back to all records](../docs/all-papers.md)
