# Olifant speculative drafting

**Towards Green Text Generation: Memory-Based Speculative Decoding**

- Citation key: `vandenbosch2026olifant`
- Authors: van den Bosch, Antal
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.16714v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Uses an offline-trained information-gain-ordered memory trie to propose next tokens from four-token contexts on CPU, with cached-verifier rejection fast paths and separate latency/energy budget analysis.

## Evidence and transfer boundary

Mistral-7B-v0.1 greedy inference on an Apple M1 Max Mac Studio with 32 GB shared RAM, 300 short general/medical/legal prompts, and cached versus uncached verification compared separately. Memory-based classification generalizes via partial feature matches and is not merely a lookup of verbatim prior rollouts. Cached greedy token agreement is qualified by float16 shape-dependent numerical divergence. Energy-optimal and latency-optimal draft lengths differ. No stochastic sampling, batched server-GPU or RL target-training evaluation. RL transfer requires current-policy/domain matching, CPU-memory accounting, stochastic verification and evaluation at rollout concurrency. The uncached baseline does not represent optimized production rollout decoding.

## Taxonomy dimensions

- Proposal Source
- Workload Recurrence
- Placement and Idle Resources
- Memory and Reuse State
- Scheduling and Mode Selection

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned full text reviewed on 2026-11-16. Discovery used the recorded query families supplemented by official-source keyword search and citation tracing. Publication dates are not inferred from registry timestamps. arXiv reports INLG 2026 proceedings pp. 472–482 and the official INLG accepted-paper list confirms the title. The formal Anthology record/version was not retrieved, so the fully reviewed arXiv version remains the selected source; no formal DOI is invented. Name particles normalized to van den Bosch, Antal using the paper byline and author-provided citation rather than the arXiv citation meta tag.
- Evidence pointer: Sections 2.1–2.4, 3–5.6 and Appendix A; Section 5.6 explicitly leaves sampling and batching for future work.
- Source publication date: 2026-11-12
- Released code: [official artifact](https://github.com/antalvdb/olifant-speculative)
- Artifact checks: checked public repository and selected branch HEAD; code not executed on 2026-11-16, revision `6d7d17fe37bbfca6e4f0c1e2ca6f8f4c0d853ab8`

## BibTeX

```bibtex
@article{vandenbosch2026olifant,
  author = {van den Bosch, Antal},
  title = {{Towards Green Text Generation: Memory-Based Speculative Decoding}},
  journal = {arXiv preprint arXiv:2611.16714},
  year = {2026},
  eprint = {2611.16714},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
