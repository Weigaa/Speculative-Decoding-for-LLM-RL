# NgramRL

**NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware N-gram Speculative Decoding**

- Citation key: `pandey2026ngramrl`
- Authors: Nilesh Prasad Pandey and Jangseon Park and Jason Kong and Onat Gungor and Tajana Rosing
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.32881v1)
- Evidence setting: **Direct RL rollout / training**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Builds bounded per-prompt n-gram draft caches from recent RL rollouts. A fan-out prefetcher prepares candidates for likely acceptance-length/continuation outcomes during target verification, with ordinary lookup on a miss.

## Evidence and transfer boundary

Direct GRPO rollout evidence using verl/vLLM: Qwen3-8B and DeepSeek-LLM-7B, GSM8K/Spider/CodeContests, two A100-80GB GPUs, 64 prompts and five responses per prompt over 15 epochs. The paper states exact speculative-sampling correction under the current rollout policy; the training sampling temperature is not specified in the inspected setup. Tokens per target forward are not tokens/s. Its 1.38x Spider result compares prefetching with synchronous NgramRL on a separately profiled Qwen3-8B, batch-64, k=16 RTX PRO 6000 rig; it is not an end-to-end RL training speedup over autoregressive decoding.

## Taxonomy dimensions

- Workload Recurrence
- Proposal Source
- Proposal Maintenance
- Verification Semantics
- Memory and Reuse State
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history cross-checked with full HTML v1 on 2026-11-02. Public preprint; no formal acceptance inferred. Added to the living library after the October 14 snapshot.
- Evidence pointer: Sections 3.2–3.5; 4.1.1–4.1.5, Table 1, and Figure 7. Separate GRPO acceptance measurements from the dedicated hardware profiling rig.
- Source publication date: 2026-10-23
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{pandey2026ngramrl,
  author = {Pandey, Nilesh Prasad and Park, Jangseon and Kong, Jason and Gungor, Onat and Rosing, Tajana},
  title = {{NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware N-gram Speculative Decoding}},
  journal = {arXiv preprint arXiv:2610.32881},
  year = {2026},
  eprint = {2610.32881},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
