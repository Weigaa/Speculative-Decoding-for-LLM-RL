# Windowed-MTP

**Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context**

- Citation key: `valliappan2026windowedmtp`
- Authors: Alagappan Valliappan
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2607.21535v2)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v2

## Mechanism / relevance

Restricts the built-in MTP draft head to an attention sink and recent-token window while retaining full-context target verification. A compact ring buffer reclaims the unused draft KV pool.

## Evidence and transfer boundary

Inference evaluation of recurrent-hybrid Qwen and Nemotron targets in SGLang, principally at approximately one-million-token context on B200, with TP2 and H100 replications. Main comparisons distinguish native MTP, dense decoding, acceptance-free per-step savings and acceptance-dependent TPOT. Greedy and temperature-one configurations are reported. The compact draft pool does not remove the target full-context KV requirement. Continuous-arrival results can be prefill-limited. Transfer to RL concerns reducing draft-side attention traffic and memory at long context, with model-compatible MTP, valid target verification, ring-buffer state management and refresh after actor updates. No direct RL rollout/training evaluation is claimed.

## Taxonomy dimensions

- Proposal Source
- Memory and Reuse State
- Parallel and Load-Aware Drafting

## Source and artifact record

- Metadata provenance: Official arXiv abstract, v2 HTML and official Atom id-list response checked on 2026-11-09. First public July 23, revised October 30. Paper-linked reproduction repository metadata and HEAD checked; upstream SGLang PR merge status checked through GitHub API. Newly curated from the existing pending queue, not newly published this week.
- Evidence pointer: Sections 3–4 and 6–7; Appendices A, E and F distinguish per-step cost, physical pool reclamation, stochastic sampling, backend controls and continuous-arrival limits.
- Source publication date: 2026-07-23
- Released code: [official artifact](https://github.com/avalliappan-nvidia/windowed-mtp-b200), [official artifact](https://github.com/sgl-project/sglang/pull/32673)
- Artifact checks: Paper-linked reproduction repository metadata and default-branch HEAD checked; code not executed on 2026-11-09, revision `335cb4736d69f29e6924c468b7efa188bf4cfff7`; Upstream PR confirmed merged on 2026-09-22; this establishes windowed draft-attention integration, not every reproduction component or an RL result on 2026-11-09

## BibTeX

```bibtex
@article{valliappan2026windowedmtp,
  author = {Valliappan, Alagappan},
  title = {{Windowed-MTP}: Removing the Full-Context Draft-{KV} Tax at Million-Token Context},
  journal = {arXiv preprint arXiv:2607.21535},
  year = {2026},
  eprint = {2607.21535},
  archivePrefix = {arXiv},
  note = {Reviewed version v2, October 30, 2026}
}
```

[Back to all records](../docs/all-papers.md)
