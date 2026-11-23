# G-MTP

**Efficient and Robust Drafting with Multi-Token Prediction**

- Citation key: `galgani2026gmtp`
- Authors: Galgani, Filippo and Ji, Ziwei and Homburger, Omri and Jawahar, Ganesh and Ramanovich, Michelle and Korotkov, Ivan and Martins, Luciano and Evci, Utku and Yvinec, Edouard and Consul, Pooja and Kumar, Vivek and Schuster, Tal
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.25813v1)
- Evidence setting: **Serving / inference — RL transfer potential**
- Library role: `post_cutoff`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Uses one recurrent four-layer draft head conditioned on target activations, direct cross-attention to target KV without a separate draft cache, and clustered vocabulary projection, with joint or two-stage distillation after target fine-tuning.

## Evidence and transfer boundary

Gemma 4 inference on H100 GPUs and two mobile devices. Server generation throughput and mobile greedy decoding are distinct evaluations. Domain adaptation uses teacher-forced LoRA supervised fine-tuning and total-variation distillation on SciQA and GSM8K, not target-policy RL. Joint adaptation detaches drafter gradients from backbone activations and KV. The 1.83x figure concerns fewer target forward passes after adaptation, not measured training wall-clock acceleration. Shared-head prediction is autoregressive rather than a one-pass parallel block. RL transfer concerns head alignment after policy refresh and shared-KV memory cost, requiring stochastic sampling validation, cache consistency and exposed adaptation costs. The initial drafter pretraining recipe is outside the report scope.

## Taxonomy dimensions

- Proposal Source
- Proposal Maintenance
- Memory and Reuse State

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned primary HTML reviewed on 2026-11-23. Dates are source submission dates, not registry-update timestamps. Technical evaluation remains inference-origin. No formal acceptance inferred.
- Evidence pointer: Sections 3–5, Tables 1–4, and Appendices A.1–A.3, especially teacher forcing and stop-gradient in A.3.2.
- Source publication date: 2026-11-19
- Released code: [official artifact](https://github.com/google-research/gemma4-mtp-drafter-domain-adaptation)
- Artifact checks: Paper-linked public repository and HEAD checked; code not executed on 2026-11-23, revision `3ca321f2a356bd29d99c5d5fcea4018960f8b691`

## BibTeX

```bibtex
@article{galgani2026gmtp,
  author = {Galgani, Filippo and Ji, Ziwei and Homburger, Omri and Jawahar, Ganesh and Ramanovich, Michelle and Korotkov, Ivan and Martins, Luciano and Evci, Utku and Yvinec, Edouard and Consul, Pooja and Kumar, Vivek and Schuster, Tal},
  title = {{Efficient and Robust Drafting with Multi-Token Prediction}},
  journal = {arXiv preprint arXiv:2611.25813},
  year = {2026},
  eprint = {2611.25813},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
