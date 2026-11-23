# Version observations

New versions do not overwrite reviewed or manuscript versions. Re-read changed experiments before changing a paper card.

- [he2026s3r](https://arxiv.org/abs/2610.13202v2): reviewed v1, observed v2 (2026-11-03T16:41:33Z).
- [he2026valuspec](https://arxiv.org/abs/2610.31338v2): reviewed v1, observed v2 (2026-11-05T15:09:32Z).
- [malvankar2026tabletune](https://arxiv.org/abs/2610.38968v2): reviewed v1, observed v2 (2026-11-02T17:44:59Z).
- [nie2026unilaspec](https://arxiv.org/abs/2611.01617v2): reviewed v1, observed v2 (2026-11-06T09:31:14Z).
- [pham2026specroll](https://arxiv.org/abs/2608.04962v2): reviewed v1, observed v2 (2026-10-14T04:53:03Z).
- [song2026forespark](https://arxiv.org/abs/2611.13442v2): reviewed v1, observed v2 (2026-11-13T01:33:53Z).
- [song2026specmem](https://arxiv.org/abs/2610.31840v2): reviewed v1, observed v2 (2026-11-13T16:46:22Z).
- [wang2026draftcotraining](https://arxiv.org/abs/2609.07108v3): reviewed v1, observed v3 (2026-11-04T03:48:05Z).
- [xia2026acceptanceaware](https://arxiv.org/abs/2609.24150v2): reviewed v1, observed v2 (2026-11-10T07:58:07Z).
- [xu2026tailsieve](https://arxiv.org/abs/2608.22788v3): reviewed v2, observed v3 (2026-11-06T09:28:32Z).
- [zheng2026dforktree](https://arxiv.org/abs/2611.12356v2): reviewed v1, observed v2 (2026-11-12T06:04:02Z).

Curator review of `he2026s3r` (2026-11-08): The reviewed v2 retains sparse drafting, dense verification and response-group semantics. Reviewed its setup and KV scheduling discussion. Historical values retained. See the [paper card](../papers/he2026s3r.md).

Curator review of `he2026valuspec` (2026-11-08): Reviewed v2 calibration split, candidate-source separation, and greedy-only evaluation. No stochastic or direct RL evidence inferred. See the [paper card](../papers/he2026valuspec.md).

Curator review of `malvankar2026tabletune` (2026-11-08): Reviewed v2 serving-runner, graph-switching, profiling and cache-preemption limitations. Historical measurements retained. See the [paper card](../papers/malvankar2026tabletune.md).

Curator review of `nie2026unilaspec` (2026-11-11): Reviewed expanded runtime controls and hardware evaluation. Full-text primary comparisons are greedy, with additional stochastic checks in appendices. Existing mechanism description remains applicable. Original v1 numerical counts remain historical and are not replaced silently. See the [paper card](../papers/nie2026unilaspec.md).

Curator review of `pham2026specroll` (2026-10-26): SpecRoll v1 was renamed and substantially revised as SPARK v2 under the same arXiv ID. Method and authors changed. Keep one canonical study and retain v1 snapshot/BibTeX; manuscript reconciliation is recommended. The revision predates or coincides with the cutoff, not a new post-cutoff study. See the [paper card](../papers/pham2026specroll.md).

Curator review of `song2026forespark` (2026-11-16): Reviewed official v2 metadata and full text, revised November 13. Author list and headline serving results unchanged. Clarifies pre-draft estimation, concave-envelope global sorting, packed variable-length drafting and post-draft verification allocation. Expanded discussion and ablations cover other drafters. Main evaluations are greedy serving unless noted; standard stochastic verification is described separately. No direct RL rollout evaluation added. The manuscript retains its concise joint-budget mechanism summary. Official implementation is newly linked and checked. Original v1 source and BibTeX remain unchanged. See the [paper card](../papers/song2026forespark.md).

Curator review of `song2026specmem` (2026-11-23): Reviewed SpecMem v2 methods, Tables 1–4, wall-clock timing and limitations against v1. The checked core lifecycle mechanism, headline MAT and external-loop speedup settings remain consistent. Canonicalized greedy-call MAT remains a proxy separate from wire-token acceptance, and the wall-clock loop is not an engine-integrated RL evaluation. No material change requiring replacement of historical v1 measurements was identified in these checked sections. Original v1 metadata, BibTeX and source selection retained. See the [paper card](../papers/song2026specmem.md).

Curator review of `wang2026draftcotraining` (2026-11-08): Reviewed v3 CP branch attention, TapChannel, and expanded direct RL evaluations up to 122B. Existing mechanism summary remains applicable; no old numerical claim overwritten. See the [paper card](../papers/wang2026draftcotraining.md).

Curator review of `xia2026acceptanceaware` (2026-11-11): Reviewed weighted window-start objectives, tree acceptance objectives and optional GRPO for the drafter. This remains fixed-target drafter training, not target-policy RL rollout evidence. See the [paper card](../papers/xia2026acceptanceaware.md).

Curator review of `xu2026tailsieve` (2026-11-11): Reviewed refreshed full-response generation and group selection, plus Appendix G matched-decoder routing controls. Headline 1.67x routing and 2.59x combined gains remain versus uniform routing without speculation; matched-decoder routing gains are separate. No historical headline value replaced. See the [paper card](../papers/xu2026tailsieve.md).

Curator review of `zheng2026dforktree` (2026-11-16): Reviewed v2 full text and official metadata. Author list adds Tianxiang Zhao. Fork-aware PMI scoring, GPU exact tree construction, batch-one RTX 5090 setup and headline gains remain. V2 expands the branch-coverage/tree-shape/calibration analyses and output-agreement confidence intervals. Stochastic sample-and-match evaluation remains separate from greedy verification. Original v1 authors, BibTeX, source selection and measurements retained; v2 metadata and BibTeX are recorded explicitly here for future citation reconciliation. See the [paper card](../papers/zheng2026dforktree.md).
