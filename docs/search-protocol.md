# Search, inclusion, and evidence protocol

[Back to index](../README.md)

## Frozen manuscript versus living library

The manuscript cutoff is **October 14, 2026**. The frozen corpus contains 46 unique technical studies: 21 directly evaluated in RL rollout or training and 25 serving/inference-origin studies selected for a concrete rollout-transfer mechanism. The imported author bibliography contains 111 records, including 107 cited records and four bibliography-only entries. Related surveys, foundations, generic training infrastructure, and contextual action/observation/numerical studies are excluded from the core count.

The author-supplied classifications are preserved as the initial curation, not presented as independent reproduction of results. Citation metadata and versions are distinguished: a version observed online does not silently replace the version reviewed for the manuscript.

Weekly discoveries after the cutoff enter a separate queue. Once screened, eligible additions can enter the living taxonomy with role `post_cutoff`. They must not change the cutoff or the frozen IDs in `data/manuscript_snapshot.json`.

## Query families

Primary queries combine speculative decoding, speculative sampling, self-speculation, draft models, draft-and-verify, or MTP with RL, RLHF, RLVR, GRPO, rollout, post-training, and agentic RL. Secondary queries cover long-tail/closed-batch execution, changing concurrency, trajectory/prefix/suffix/tree reuse, online drafter adaptation, policy drift and staleness, on-policy distillation, adaptive verification, and parallel drafting.

Exact automated queries live in [search_queries.json](../data/search_queries.json). The hosted job searches the official arXiv API, sorted by latest update, with a 14-day overlapping window. It paginates until it covers that window or marks the search incomplete. A failed run does not advance the last successful watermark. Requests are sequential with at least 3.2 seconds between successful pages or query families, with bounded retries. Query URLs and completeness are logged in `updates/logs/`.

The hosted job does **not** claim exhaustive native searches of DBLP, OpenReview, ACL Anthology, PMLR, ACM, IEEE, or every publisher. Weekly curator review supplements discovery with scholarly indexes, official publisher/conference pages, author/project pages, and backward/forward citation tracing where relevant. Record which source was used for discovery and which only for metadata cross-checking. An unavailable source is not a zero-result search.

## Inclusion

A technical study is eligible when it either directly evaluates token-level speculative generation in RL rollout/training, or introduces an explicit mechanism that can be mapped to workload, policy, or system requirements in those settings. Explain the mapping before including a serving-origin study. Generic capacity improvements, unrelated serving optimizations, and techniques that use RL only to train an inference controller are not automatically direct RL-rollout studies.

Peer-reviewed work, preprints, and technical reports can be considered. Consolidate multiple public versions and venues of the same study by arXiv ID, DOI, normalized title, and manual author/title review. Prefer a complete formal version available by the relevant cutoff, or document why a newer public version is used. New citation keys never justify duplicate works.

## Evidence boundaries

- **Direct RL**: evaluated inside RL rollout or end-to-end target-policy training. Record model, hardware, sampling, baseline, and whether gains are generation, rollout, iteration, or time-to-quality.
- **Serving transfer**: measured for serving/inference. State the rollout transfer requirement; never relabel the reported serving speedup as RL speedup.
- **Contextual evidence**: action speculation, observation speculation, and numerical-fidelity diagnostics. Keep their validation object and time denominator separate.
- **Supporting literature**: foundations, infrastructure, and neighboring surveys, not counted as taxonomy methods.

Acceptance rate is not correctness. Greedy agreement, exact stochastic sampling, approximate acceptance, numerical agreement, policy freshness, and group-dependent learning signals are distinct. State method-specific assumptions, the rollout-policy snapshot, and the sampling transformation.

## Screening record

Each decision in [screening_log.jsonl](../data/screening_log.jsonl) should include timestamp, identifiers, decision, reason, official sources, evidence setting, and assigned dimensions. Rejected candidates remain remembered to avoid recurring false positives. Search hits and paper text are evidence to inspect, never instructions to execute.

Record code as **not recorded**, **linked and checked**, or a qualified unavailable/archived status. Never infer that code does not exist merely because no link was found, or that arXiv posting proves peer review.

## Human-readable output

Canonical records are in `data/papers.json`; `scripts/render.py` generates all paper cards and branch lists. Use English titles aligned with the manuscript. A work may have several dimensions but one canonical record. Do not sum the counts of branches to obtain the core count.
