# BunshinRL

**BunshinRL: Whole-Workspace Forking for Agentic Reinforcement Learning Rollouts**

- Citation key: `huang2026bunshinrl`
- Authors: Huang, Yutong and Srivatsa, Vikranth and Asch, Alex and Zhang, Yiying
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.10453v2)
- Evidence setting: **Contextual evidence**
- Library role: `contextual`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v2

## Mechanism / relevance

Forks live agent workspaces with copy-on-write sharing, caches repeated tool prefixes, and executes predicted historical tool calls during model reasoning with signature checks and rollback.

## Evidence and transfer boundary

Contextual tool/action speculation inside agentic RL, not token-level draft-and-verify decoding. Qwen3-VL-8B with synchronous GRPO on OSWorld and a WebArena shopping subset. Section 5.2 compares memory under replayed trajectories against CRIU and AgentENV. Section 5.3 separately compares Base, speculative-tool-only Spec and combined Full under live training, distinguishing prefix-cache and speculation gains. Reported rollout-epoch latency includes tool/environment effects and must not be relabeled as token-decoding or whole-training speedup. Adoption requires matching tool signatures and validating dependencies; failed branches discard private state and roll back. This can complement token-level speculation but no combined gain is established.

## Taxonomy dimensions

Outside the core taxonomy.

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned full text reviewed on 2026-11-16. Discovery used the recorded query families supplemented by official-source keyword search and citation tracing. Publication dates are not inferred from registry timestamps.
- Evidence pointer: Sections 3.1–3.3, 4 and 5.1–5.3; replay-based memory comparison differs from live GRPO tool-latency ablations.
- Source publication date: 2026-11-07
- Released code: [official artifact](https://github.com/WukLab/ForkRL)
- Artifact checks: checked public repository and selected branch HEAD; code not executed on 2026-11-16, revision `f1a682576d142c231c0c0feb62bbda9a9834d6d6`

## BibTeX

```bibtex
@article{huang2026bunshinrl,
  author = {Huang, Yutong and Srivatsa, Vikranth and Asch, Alex and Zhang, Yiying},
  title = {{BunshinRL: Whole-Workspace Forking for Agentic Reinforcement Learning Rollouts}},
  journal = {arXiv preprint arXiv:2611.10453},
  year = {2026},
  eprint = {2611.10453},
  archivePrefix = {arXiv},
  note = {Reviewed version v2}
}
```

[Back to all records](../docs/all-papers.md)
