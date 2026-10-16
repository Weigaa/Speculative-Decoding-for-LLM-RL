# DAS

**Beat the Long Tail: Distribution-Aware Speculative Decoding for RL Training**

- Citation key: `shao2026das`
- Authors: Zelei Shao and Vikranth Srivatsa and Sanjana Srivastava and Qingyang Wu and Alpay Ariyak and Xiaoxia Wu and Ameen Patel and Jue Wang and Percy Liang and Tri Dao and Ce Zhang and Yiying Zhang and Ben Athiwaratkun and Chenfeng Xu and Junxiong Wang
- Year: 2026
- Bibliographic venue: Proceedings of Machine Learning and Systems
- Source: [paper](https://arxiv.org/abs/2511.13841)
- Evidence setting: **Direct RL rollout / training**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: not recorded

## Mechanism / relevance

Uses historical nonparametric proposals and length-aware speculative budgeting for long-tail rollouts.

## Evidence and transfer boundary

Direct RL evidence. Keep the original training configuration and quality comparison attached to numerical gains.

## Taxonomy dimensions

- Closed-Batch Tail
- Workload Recurrence
- Scheduling and Mode Selection
- Memory and Reuse State

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified. Primary paper URL added during repository setup; source link does not independently verify every imported field.
- Evidence pointer: Manuscript synthesis; individual source locations not yet indexed.
- Source publication date: not recorded
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@inproceedings{shao2026das,
  author    = {Zelei Shao and Vikranth Srivatsa and Sanjana Srivastava and
               Qingyang Wu and Alpay Ariyak and Xiaoxia Wu and Ameen Patel and
               Jue Wang and Percy Liang and Tri Dao and Ce Zhang and
               Yiying Zhang and Ben Athiwaratkun and Chenfeng Xu and
               Junxiong Wang},
  title     = {Beat the Long Tail: Distribution-Aware Speculative Decoding for
               {RL} Training},
  booktitle = {Proceedings of Machine Learning and Systems},
  volume    = {8},
  year      = {2026},
}
```

[Back to all records](../docs/all-papers.md)
