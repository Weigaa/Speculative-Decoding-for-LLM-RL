# November 2 literature edition

[Updated 64-study manifest](../data/manuscript_editions/2026-11-02.csv) · [Version selections](../data/manuscript_editions/2026-11-02.json) · [Updated core BibTeX](../bibliography/manuscript-2026-11-02-core.bib)

This separate pre-submission literature edition records **64 unique technical studies: 23 with direct RL rollout evaluation/integration and 41 serving-transfer studies**. Direct integration does not imply that a paper isolates a causal SD speedup against an SD-off control. This is not a claim of journal submission or acceptance. The original `manuscript_snapshot.json` and frozen 46-study bibliography remain unchanged.

Two previously pending serving-origin studies were screened from primary full text and added:

- [LongSpark](../papers/he2026longspark.md), reviewed v2: fixed-size recent context and incremental target-derived summaries bound additional drafter state. Target verification still processes the full context. Its separate drafter GPU is included in the evidence boundary; no RL result is inferred.
- [Packed-SS](../papers/chen2026packedss.md), reviewed v1: a shared AR/diffusion model packs deferred verification with next-draft preparation. The stochastic rule stores each candidate's proposal distribution. The greedy call-count result has separate monotonicity assumptions; neither result establishes RL policy-refresh behavior or training speedup.

The manifest selects SPARK v2 under the existing `pham2026specroll` key. This is the same study as SpecRoll v1, with a changed title, author list and mechanism description. The canonical historical record and its reviewed v1 are retained with an additive version note rather than silently replacing the snapshot.

Seven non-core bibliography records received field-level metadata corrections, with their former fields retained in `metadata_corrections`: EAGLE and EAGLE-2 use their formal ICML/EMNLP records and full author names, ZeRO's author spelling is corrected to Olatunji Ruwase, AgentBench/ToolLLM/WebArena use their ICLR 2024 metadata, WebArena's omitted author is restored, and the CSUR serving survey has verified volume/issue/pages. Keys were preserved, so these are not additional studies.

Primary checks: [EAGLE/PMLR](https://proceedings.mlr.press/v235/li24bt.html), [EAGLE-2/ACL Anthology](https://aclanthology.org/2024.emnlp-main.422/), [ZeRO/Microsoft Research](https://www.microsoft.com/en-us/research/publication/zero-memory-optimizations-toward-training-trillion-parameter-models/), [AgentBench publication comment](https://arxiv.org/abs/2308.03688), [ToolLLM camera-ready](https://openreview.net/attachment?id=dHng2O0Jjr&name=pdf), [WebArena camera-ready](https://arxiv.org/pdf/2307.13854), and [CSUR metadata/Crossref](https://api.crossref.org/works/10.1145/3754448).

The day's configured arXiv and DataCite searches are documented in the [weekly review](2026-11-02-curation.md). This edition is a screened selection, not a claim that every pending hit has been fully evaluated or every listed database has been searched exhaustively. Unrecorded historical version metadata is explicitly marked as such in the manifest. No private manuscript, PDF, funding information or third-party full text is published here.
