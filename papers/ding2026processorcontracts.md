# Processor-contract diagnostics

**Testing Processor Contracts in Speculative Decoding Engines**

- Citation key: `ding2026processorcontracts`
- Authors: Ding, Tianyu and Tong, Yaocheng and Yang, Muzhi and Yang, Lei and Jiang, Fei
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.04042v1)
- Evidence setting: **Contextual evidence**
- Library role: `contextual`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Checks whether logits processors see the correct verified prefix and rolled-back state at every speculative position.

## Evidence and transfer boundary

Contextual implementation-correctness evidence from selected Transformers/llama-cpp-python releases, tiny-model enumeration and trained-checkpoint output-event checks. No trainer–engine integration or measured RL effect. Directed selection does not outperform random selection in cause recovery. Not a new acceleration mechanism or a core taxonomy study.

## Taxonomy dimensions

Outside the core taxonomy.

## Source and artifact record

- Metadata provenance: Official arXiv metadata and versioned full text checked on 2026-11-11. Query-family discovery supplemented by official-source keyword search and citation tracing. Newly screened does not imply newly published.
- Evidence pointer: Sections 3–6 and Appendix J
- Source publication date: 2026-11-02
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{ding2026processorcontracts,
  author = {Ding, Tianyu and Tong, Yaocheng and Yang, Muzhi and Yang, Lei and Jiang, Fei},
  title = {{Testing Processor Contracts in Speculative Decoding Engines}},
  journal = {arXiv preprint arXiv:2611.04042},
  year = {2026},
  eprint = {2611.04042},
  archivePrefix = {arXiv},
  note = {Reviewed version v1}
}
```

[Back to all records](../docs/all-papers.md)
