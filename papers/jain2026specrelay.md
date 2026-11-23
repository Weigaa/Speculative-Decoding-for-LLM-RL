# SpecRelay

**SpecRelay: Amortize or Avoid the Round Trip in Edge-Cloud Speculative Decoding**

- Citation key: `jain2026specrelay`
- Authors: Jain, Jai and Ahn, Chihyo and Liu, Yong and Chen, Charles and Hoang, Duc N.M and Jaiswal, Ajay Kumar and Ilhan, Fatih and Kim, Han-Byul and Hannah, Lauren and Dixit, Richa and Cho, Minsik and Lin, Yingyan Celine and Kim, Hyesoon
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.18963v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Pipelines fixed-budget draft trees across edge-cloud round trips, hedges over alternative continuation anchors and rejects stale requests before target execution, with a separate latency-aware local/cloud router.

## Evidence and transfer boundary

Primary setup uses an RTX 4090 Qwen3-1.7B drafter and A100 Qwen3-14B verifier with injected round-trip delay. Main evaluations are greedy; a temperature-0.7 spot check is separate. Baseline is a corrected reproduction of synchronous SpecEdge. Cloud-path throughput ablations differ from full-system gains that include local-model routing at matched aggregate accuracy. Choosing local outputs does not preserve the cloud target distribution. RL transfer is limited to asynchronous draft/verify placement, lineage validation and stale-request rejection, requiring fixed per-trajectory policy identity and measured communication cost. Request staleness here is speculative-prefix mismatch, not actor-policy age. No RL training evaluation or verified project code link.

## Taxonomy dimensions

- Placement and Idle Resources
- Synchronization and Versioning
- Parallel and Load-Aware Drafting
- Scheduling and Mode Selection

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned primary HTML reviewed on 2026-11-23. Dates are source submission dates, not registry-update timestamps. Technical evaluation remains inference-origin. No formal acceptance inferred.
- Evidence pointer: Sections 4–6 and Appendices A, B.8–B.10 and C distinguish cloud scheduling, routing quality and denominators.
- Source publication date: 2026-11-13
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{jain2026specrelay,
  author = {Jain, Jai and Ahn, Chihyo and Liu, Yong and Chen, Charles and Hoang, Duc N.M and Jaiswal, Ajay Kumar and Ilhan, Fatih and Kim, Han-Byul and Hannah, Lauren and Dixit, Richa and Cho, Minsik and Lin, Yingyan Celine and Kim, Hyesoon},
  title = {{SpecRelay: Amortize or Avoid the Round Trip in Edge-Cloud Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.18963},
  year = {2026},
  eprint = {2611.18963},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
