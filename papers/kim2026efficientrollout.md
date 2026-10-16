# EfficientRollout

**EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts**

- Citation key: `kim2026efficientrollout`
- Authors: Minseo Kim and Minjae Lee and Seunghyuk Oh and Kevin Galim and Donghoon Kim and Coleman Hooper and Harman Singh and Amir Gholami and Hyung Il Koo and Wonjun Kang
- Year: 2026
- Bibliographic venue: arXiv preprint arXiv:2606.18967
- Source: [paper](https://arxiv.org/abs/2606.18967)
- Evidence setting: **Direct RL rollout / training**
- Library role: `core`
- Cited in the manuscript PDF: yes
- Reviewed arXiv version: v2

## Mechanism / relevance

Derives a quantized self-drafter from the rollout policy and controls speculation using the current execution regime.

## Evidence and transfer boundary

Direct RL evidence. The September 30 v2 reports latency reductions up to 24.2% for rollout generation and 15.6% for the full training step. These are latency reductions, not multiplicative speedups.

## Taxonomy dimensions

- Closed-Batch Tail
- Proposal Source
- Proposal Maintenance
- Scheduling and Mode Selection

## Source and artifact record

- Metadata provenance: Author-supplied BibTeX; arXiv versions cross-checked against saved official API metadata where available. Full field-level publication metadata has not been independently reverified.
- Evidence pointer: Manuscript synthesis; individual source locations not yet indexed.
- Source publication date: 2026-06-17T11:51:06Z
- Released code: [official artifact](https://github.com/furiosa-ai/EfficientRollout)
- Artifact checks: public_repository_checked on 2026-10-16, revision `3191d383523797f1adc0136d4907f5c97026519f`

## BibTeX

```bibtex
@article{kim2026efficientrollout,
  author  = {Minseo Kim and Minjae Lee and Seunghyuk Oh and Kevin Galim and
             Donghoon Kim and Coleman Hooper and Harman Singh and
             Amir Gholami and Hyung Il Koo and Wonjun Kang},
  title   = {{EfficientRollout}: System-Aware Self-Speculative Decoding for
             {RL} Rollouts},
  journal = {arXiv preprint arXiv:2606.18967},
  year    = {2026},
  doi     = {10.48550/arXiv.2606.18967}
}
```

[Back to all records](../docs/all-papers.md)
