# Seer

**Seer: Online Context Learning for Fast Synchronous LLM Reinforcement Learning**

- Citation key: `qin2026seer`
- Authors: Ruoyu Qin and Weiran He and Weixiao Huang and Yangkun Zhang and Yikai Zhao and Bo Pang and Xinran Xu and Yingdi Shan and Yongwei Wu and Mingxing Zhang
- Year: 2026
- Bibliographic venue: 20th USENIX Symposium on Operating Systems Design and Implementation
- Source: [paper](https://arxiv.org/abs/2511.14617)
- Evidence setting: **Direct RL rollout / training**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: not recorded

## Mechanism / relevance

Combines context-aware scheduling, divided rollouts, and grouped speculative decoding.

## Evidence and transfer boundary

Direct RL evidence. Scheduling changes the workload presented to the speculative engine.

## Taxonomy dimensions

- Closed-Batch Tail
- Placement and Idle Resources

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified. Primary paper URL added during repository setup; source link does not independently verify every imported field.
- Evidence pointer: Manuscript synthesis; individual source locations not yet indexed.
- Source publication date: not recorded
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@inproceedings{qin2026seer,
  author    = {Ruoyu Qin and Weiran He and Weixiao Huang and Yangkun Zhang and Yikai Zhao and Bo Pang and Xinran Xu and Yingdi Shan and Yongwei Wu and Mingxing Zhang},
  title     = {Seer: Online Context Learning for Fast Synchronous LLM Reinforcement Learning},
  booktitle = {20th USENIX Symposium on Operating Systems Design and Implementation},
  pages     = {883--901},
  year      = {2026}
}
```

[Back to all records](../docs/all-papers.md)
