# FlexFloor

**Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism**

- Citation key: `wei2026flexfloor`
- Authors: Wei, Jia and Qiu, Ziyi and Xu, Yi and Qian, Xuehai
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.06984v1)
- Evidence setting: **Background / related survey / infrastructure**
- Library role: `background`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Coordinates history-based prompt placement and elastic expert parallelism to release completed ranks while preserving expert availability.

## Evidence and transfer boundary

Supporting RL infrastructure, not token-level speculative decoding. Qwen3-30B-A3B on 16 Ascend devices. Reported 52.74% throughput and 65.40% tokens-per-occupied-rank-time gains compare a Planned configuration with verl under matched accounting. These are distinct from end-to-end training gains and SD-on/off gains.

## Taxonomy dimensions

Outside the core taxonomy.

## Source and artifact record

- Metadata provenance: Official arXiv metadata and full text checked on 2026-11-08. Discovery used the recorded query families and author-supplied FlexFloor link.
- Evidence pointer: Sections 2, 4.2–4.4 and 5.1–5.7
- Source publication date: 2026-11-04
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{wei2026flexfloor,
  author = {Wei, Jia and Qiu, Ziyi and Xu, Yi and Qian, Xuehai},
  title = {{Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism}},
  journal = {arXiv preprint arXiv:2611.06984},
  year = {2026},
  eprint = {2611.06984},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
