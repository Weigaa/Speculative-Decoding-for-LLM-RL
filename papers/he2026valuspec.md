# ValuSpec

**ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding**

- Citation key: `he2026valuspec`
- Authors: Liang He and SiYuan Ma and Qishi Zhan and Yongqi Fan and Mingyu Cao and Qizhen Lan and Zhaolu Kang and Xilu Wang
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.31338v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Filters low-value branches of an already supplied candidate tree before target verification. A threshold is calibrated from separate target greedy trajectories, with retrieval-tree and EAGLE-3 tree suppliers evaluated independently.

## Evidence and transfer boundary

Serving/inference only. Evaluation uses greedy decoding, a non-overlapping calibration/evaluation split, main batch size one and extra batch-size-four/eight tests. Output identity is a greedy guarantee; it is not a general stochastic RL guarantee. Transfer to recurrent rollout trees requires current-policy verification and recalibration under policy/reward-workload change. Calibration and verification savings must be amortized rather than reported as demonstrated RL speedup.

## Taxonomy dimensions

- Workload Recurrence
- Verification Semantics
- Scheduling and Mode Selection

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history, cross-checked against full HTML v1 on 2026-10-26. Curated after the manuscript cutoff; this is not a claim that the first posting was after the cutoff. No accepted venue is inferred.
- Evidence pointer: Section 3 (valuation/filtering and greedy fallback), Section 4 (recurring-workload/calibration protocol) and Section 5 (retrieval and EAGLE-3 results).
- Source publication date: 2026-10-22
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@misc{he2026valuspec,
  author = {He, Liang and Ma, SiYuan and Zhan, Qishi and Fan, Yongqi and Cao, Mingyu and Lan, Qizhen and Kang, Zhaolu and Wang, Xilu},
  title = {{ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding}},
  year = {2026},
  eprint = {2610.31338},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2610.31338v1}
}
```

[Back to all records](../docs/all-papers.md)
