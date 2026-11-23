# SpecMem

**SPECMEM: Accelerating Agentic Tool Calling via Live Memory Management**

- Citation key: `song2026specmem`
- Authors: Zihe Song and Wenting Zhao and Ye Liu and Yuanjie Zhu and Ke Xu and Shanghao Li and Philip S. Yu
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.31840v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Keeps retrieved tool-call drafts live through online write-back of verified calls and bounded per-user stores with eviction. A separate schema-level gate defers tool effects until verification where needed.

## Evidence and transfer boundary

Serving/agent-inference evidence only. Main recurrence streams use synthetic per-user sessions; canonicalized-call longest-common-prefix scores against greedy target outputs are proxies, distinct from wire-token acceptance. Section 4.3 times an external speculative loop with a ToolSpec reimplementation, not an engine-integrated RL rollout path. BFCL/Seal-Tools and live tau-squared-bench checks do not establish RL training gains. Transfer requires verified current-policy token sampling, context/version-aware invalidation, bounded state and measured lookup/write-back costs. Tool-side execution gating is contextual evidence and is not counted as a separate token-level method.

## Taxonomy dimensions

- Workload Recurrence
- Proposal Source
- Memory and Reuse State

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history cross-checked with full HTML v1 on 2026-11-02. Public preprint; no formal acceptance inferred. Added to the living library after the October 14 snapshot.
- Evidence pointer: Sections 3.1–3.4, 4.1–4.3 and 5.4; Limitations: simulated repetition, metric/integration scope and side-effect-gate scope.
- Source publication date: 2026-10-22
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## Version review: v2

**SpecMem: Accelerating Agentic Tool Calling via Live Memory Management**

- Authors in this version: Zihe Song and Wenting Zhao and Ye Liu and Yuanjie Zhu and Ke Xu and Shanghao Li and Philip S. Yu
- [Version source](https://arxiv.org/html/2610.31840v2); revised 2026-11-13; checked 2026-11-23.
- Evidence pointer: Sections 3–5, Tables 1–4 and Limitations

Reviewed SpecMem v2 methods, Tables 1–4, wall-clock timing and limitations against v1. The checked core lifecycle mechanism, headline MAT and external-loop speedup settings remain consistent. Canonicalized greedy-call MAT remains a proxy separate from wire-token acceptance, and the wall-clock loop is not an engine-integrated RL evaluation. No material change requiring replacement of historical v1 measurements was identified in these checked sections. Original v1 metadata, BibTeX and source selection retained.

No historical snapshot, manuscript edition or original reviewed-version field changed.

## BibTeX

```bibtex
@article{song2026specmem,
  author = {Song, Zihe and Zhao, Wenting and Liu, Ye and Zhu, Yuanjie and Xu, Ke and Li, Shanghao and Yu, Philip S.},
  title = {{SPECMEM: Accelerating Agentic Tool Calling via Live Memory Management}},
  journal = {arXiv preprint arXiv:2610.31840},
  year = {2026},
  eprint = {2610.31840},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
