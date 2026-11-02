# FlashNext-RL

**FlashNext-RL: A System Optimization Study for Long-Horizon Agentic RL of Qwen3.8-Flash-Next**

- Citation key: `yao2026flashnextrl`
- Authors: Zhewei Yao and Yuxiong He
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2610.28998v1)
- Evidence setting: **Direct RL rollout / training**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Integrates a frozen native MTP head with long-context SWE RL rollouts, choosing tensor/expert parallel topology and KV-aware admission jointly. Layerwise weight transfer and bounded receive buffers coordinate refreshed target weights with rollout memory.

## Evidence and transfer boundary

Direct RL system-integration evidence, not a new speculative algorithm or an isolated SD speedup. The live BF16 Qwen3.8-Flash-Next run uses prime-rl, vLLM, one eight-B200 training node and three eight-B200 inference nodes, MTP3 proposals and 672 concurrent sessions. Section 2 separates replayed engine measurements from live telemetry; Section 5 reports steps 5–15. The MTP head is frozen while parts of the target are updated, leaving longer-run acceptance drift open. The paper does not isolate SD-on versus SD-off gains or independently establish exact stochastic rollout/group equivalence. Training-kernel and checkpoint gains must not be attributed to MTP.

## Taxonomy dimensions

- Proposal Source
- Proposal Maintenance
- Scheduling and Mode Selection
- Memory and Reuse State
- Synchronization and Versioning
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract-page citation metadata and submission history cross-checked with full HTML v1 on 2026-11-02. Public preprint; no formal acceptance inferred. Added to the living library after the October 14 snapshot.
- Evidence pointer: Sections 1 and 2.1–2.3 (MTP configuration, topology replay and live telemetry); 4.3 (policy-weight refresh); 5 and Table 16 (live SWE RL run).
- Source publication date: 2026-10-20
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: paper-linked underlying framework checked; a FlashNext-RL-specific implementation/revision was not verified, so this is not recorded as released study code on 2026-11-02, revision `4e94a8616558d99f9a39d6a1facbadbfe6233e86`

## BibTeX

```bibtex
@article{yao2026flashnextrl,
  author = {Yao, Zhewei and He, Yuxiong},
  title = {{FlashNext-RL: A System Optimization Study for Long-Horizon Agentic RL of Qwen3.8-Flash-Next}},
  journal = {arXiv preprint arXiv:2610.28998},
  year = {2026},
  eprint = {2610.28998},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
