# Candidate queue

Unreviewed search hits are not part of the curated corpus and must not be cited as demonstrated RL evidence.

[Search protocol](../docs/search-protocol.md) · [Update status](../data/update_state.json)

## [Long-Context Drafting Does Not Require Long-Context Drafters](https://arxiv.org/abs/2610.20865)

- arXiv: `2610.20865` / version not recorded
- Metadata updated: 2026-10-16T02:38:35Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Speculative decoding pairs a cheap drafter with parallel verification against the target. At ultra-long context it stops paying, because a drafter that attends over the full prefix inherits the target's context-dependent cost, so the speedup it was meant to provide first erodes and then reverses. The standard response is to build a long-context drafter, by training or fine-tuning one, or by using a multi-token-prediction head shipped inside the target checkpoint. We argue this is unnecessary, because the drafters in use are target-conditioned, reading hidden states the target computed over the entire prefix, so distant context already reaches them without their own attention, and verification corrects what they miss. We therefore freeze released short-context drafters and run them far past their training length under two inference-time mechanisms, one bounding the attention cache they see, which fixes their cost, and one re-basing their rotary position indices into the trained range. No weight is touched and the only tunable saturates early, so one vLLM-side configuration spans 4k to two million tokens, costing at most 0.16x of speedup at short length. We prove when a common index shift leaves the drafter's computation exactly unchanged, and decompose acceptance into two measurable gaps with sharp bounds. Whatever speedup a frozen drafter delivers at short context, it retains out to two million tokens, across three target-drafter pairs and five corpora. The claim concerns the flatness rather than the multiple, and removing either mechanism eliminates it. The gain is conditional on the speculative cost per emitted token staying below the matched target-only cost.

## [On-Policy Residual Learning for Diffusion Language Models](https://arxiv.org/abs/2610.20687)

- arXiv: `2610.20687` / version not recorded
- Metadata updated: 2026-10-16T02:34:37Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Residual context is key to unlocking the speed-quality Pareto frontier of diffusion language models (DLMs) by carrying forward predictive distributions across denoising steps. Yet turning this seemingly simple mechanism into an effective learning paradigm is far from simple: there is no clear recipe for how residual context should be learned. We introduce ORL, a framework for on-policy residual learning in DLMs. Algorithmically, we identify that residual learning is inherently on-policy. ORL learns from model-induced residual trajectories on the fly and introduces an entropy-contraction objective that sharpens predictions as the model revisits its own predictions. System-wise, exact residual supervision requires capturing, retaining, and reprocessing many trajectory-dependent states. ORL co-designs the algorithm with asynchronous residual capture and transport, specialized block-diffusion attention, and packed compute-balanced training, making it practical at scale. On a 4B DLM converted from Qwen3-4B, ORL improves tokens per forward (TPF) by up to 6.2x and, with our dlmrt engine, end-to-end throughput by approximately 6.9x at comparable or better quality. In single-request serving on one H100, this mode achieves a stronger speed-quality Pareto frontier than autoregressive models with EAGLE3 and DFlash speculative decoding under both strict and relaxed verification, running 1.74x faster than DFlash at matched accuracy. ORL also transfers to existing DLMs: on LLaDA-2.1-mini, 36 H100-hours and 4.2M self-generated tokens, about 10x less data than prior LLaDA recipes, yield up to 1.5x higher TPF and up to 3x higher throughput at comparable quality, and on DiffusionGemma, ORL raises TPF by 1.1-1.2x. With dlmrt and NVFP4 quantization, ORL models decode a single request at up to 5,046 tokens/s on one B200, 7,708 on eight B200s, and 2,788 on a consumer RTX 5090, with comparable quality.

## [Fish Audio Drama 3 Technical Report](https://arxiv.org/abs/2610.18010)

- arXiv: `2610.18010` / version not recorded
- Metadata updated: 2026-10-15T03:22:58Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-primary-draft-posttraining

We introduce Fish Audio Drama 3, an open-source speech generation model that turns text into directed performances, built on a 35B-parameter mixture-of-experts backbone that activates 3B parameters per token. It clones voices from multiple references, follows natural-language direction, revises a take when the next turn gives a note, voices multi-character scenes, edits existing speech by infilling, and synthesizes long-form and streaming audio. Multi-turn revision, scene dubbing, editing by infilling, and streaming text input are new in Drama 3, all in one model. Drama 3 pairs the hybrid linear-attention backbone with a new codebook multi-token-prediction audio decoder that predicts the acoustic codebooks of each frame in dedicated layers that attend over the entire sequence. The model is trained with a three-stage pre-training recipe, instruction fine-tuning, and large-batch reinforcement learning whose only reward is a single learned model of human preference. Its inference engine decodes a single stream at 271 frames per second on one H200, against 177 for Fish Audio S2, although Drama 3 has more than seven times as many parameters. The model weights are available on GitHub (https://github.com/fishaudio/fish-speech) and Hugging Face (https://huggingface.co/fishaudio/drama-3), and inference is available through SGLang-Omni (https://github.com/sgl-project/sglang-omni). We highly encourage readers to visit https://fish.audio to direct their own performances.

## [ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models](https://arxiv.org/abs/2610.20503)

- arXiv: `2610.20503` / version not recorded
- Metadata updated: 2026-10-15T03:02:43Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-reuse

Speculative decoding accelerates autoregressive generation by drafting multiple tokens per step, yet feature-based drafters rely on target hidden features whose contextual emphasis may not align with the needs of subsequent draft positions. Hybrid linear attention (HLA) models maintain compact recurrent states that accumulate historical associations, offering an efficient source of complementary context for speculative drafting. We introduce ReaDy, the first speculative decoding method, to the best of our knowledge, to leverage HLA recurrent states for position-specific context retrieval during drafting. ReaDy equips each draft position with a learned query to retrieve supplementary context directly from the target's committed recurrent states. A lightweight state reader integrates this context into draft representations through residual updates, while low-rank state reads and fused operators keep additional computation and I/O overhead low. Building on DSpark's parallel backbone and sequential prediction head, ReaDy employs a lightweight two-stage adaptation strategy, with reader capacity, state sources, and residual placement examined through ablation studies. Across seven benchmarks spanning mathematics, code generation, and dialogue, ReaDy achieves an average $3.16\times$ decoding speedup over autoregressive decoding with Qwen3.8-27B on a single NVIDIA B200 GPU. It outperforms DSpark on every benchmark, improving throughput by 7.97% and acceptance length by 8.50% on average. Our code is available at https://github.com/StartLuxLabs/ReaDy.

## [JetSpec++: Foresight Parallel Drafting with Self Refinements](https://arxiv.org/abs/2610.19792)

- arXiv: `2610.19792` / version not recorded
- Metadata updated: 2026-10-15T02:46:25Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Speculative decoding's effectiveness is governed by two quantities: the acceptance rate of drafted tokens and the cost of producing them. We show the two objectives can be co-optimized with algorithm-system co-design, and present JetSpec++, which retains a strong learned draft model while hiding its cost almost entirely. JetSpec++ combines three components: intra-block self refinement, which trains the draft model to iteratively correct its own parallel predictions within a block of tokens; inter-block foresight drafting, which begins the next block before the current one is verified; and pipelined drafting and verification, which overlaps the two stages so drafting's marginal wall-clock cost approaches zero. In comparison with state-of-the-art speculative decoding methods, JetSpec++ attains a wall-clock speedup of up to $7.45\times$ over autoregressive (AR) decoding and $1.54\times$ over DSpark, with up to 1,361 tokens per second for a single request on GB200, and an average acceptance length of 8.94 across seven benchmarks, while preserving the target model's output distribution. Our code and models are available at https://github.com/hao-ai-lab/JetSpec.

## [Contextual Correction of Parallel Drafts for Speculative Decoding](https://arxiv.org/abs/2610.12570)

- arXiv: `2610.12570` / version not recorded
- Metadata updated: 2026-10-14T08:55:16Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Speculative decoding accelerates large language model inference by using a lightweight drafter to propose multiple tokens that are subsequently verified in parallel by the target model. Recent diffusion-based drafters make this paradigm particularly attractive: deep attention-based neural backbones provide strong predictions, while drafting multiple future positions in parallel avoids the sequential cost of autoregressive generation. This parallelism, however, comes at a cost. Tokens within a draft block are predicted without access to the realized identities of preceding draft tokens, removing intra-block dependencies that would naturally be available under autoregressive generation. We introduce DCOCO (DFlash Contextual Corrector), a lightweight mechanism that restores these dependencies while preserving parallel drafting. Rather than committing to each position's top prediction, DCOCO retains multiple candidate tokens and evaluates their contextual compatibility across adjacent draft positions in parallel, enabling contextually informed token selection at low additional cost. Across four verifier backbones and ten benchmarks, DCOCO achieves the highest average throughput in every evaluated configuration, spanning greedy and stochastic decoding with and without extended reasoning, with speedups of up to 6.6x over vanilla decoding. Its advantage persists under concurrent serving: DCOCO outperforms the strongest competing method by 6-23% across 4-32 concurrent requests, while other sequential correctors fall below uncorrected DFlash at these loads. These results demonstrate that recovering intra-block dependencies through parallel contextual scoring delivers consistent acceleration across decoding regimes and serving loads.

## [LUMOS: Tracing Parametric Knowledge from Training Data to Behavioral Outputs in LLMs](https://arxiv.org/abs/2610.02902)

- arXiv: `2610.02902` / version not recorded
- Metadata updated: 2026-10-14T08:51:33Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-reuse

Current analyses of LLMs' parametric knowledge are largely output-centric, drawing conclusions about what a model knows without verifying what it was actually trained on. This leaves fundamental questions, such as whether a correct response reflects genuine generalization or rote memorization, grounded in speculation rather than evidence. To resolve these ambiguities, we introduce LUMOS, a diagnostic framework that traces knowledge along the causal chain from training-data exposure to behavioral output, leveraging OLMo 2 with its fully transparent training corpus. By grounding analysis in verified exposure, we reveal that models internally encode rare facts with high separability (84%) yet fail to express them behaviorally (54%), though this retrieval gap narrows with scale. Furthermore, when models are asked to self-reflect on their own answers, they perform reliably on trained content (83%) but drop to random-baseline levels (49%) on unseen content. This collapse persists even under chain-of-thought prompting, which inflates confidence signals rather than improving calibration. Collectively, these findings demonstrate that incorporating the training-data axis into LLM evaluation transforms speculative diagnoses into verifiable claims, and we advocate that this axis should be a standard component of knowledge assessment in LLMs.

## [Draft in Parallel, Condition Through Depth: Adjacent Causal Injection for Speculative Decoding](https://arxiv.org/abs/2609.36173)

- arXiv: `2609.36173` / version not recorded
- Metadata updated: 2026-10-14T08:49:45Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Parallel speculative drafting generates multiple candidates in one backbone pass, but independent token selection can produce inconsistent continuations that shorten the accepted prefix. Existing methods mostly leave conditional decoding to a lightweight module after the backbone, which limits the flow of predecessor information to successors. Our analysis of DFlash shows that early positions already form recoverable predictions in shallow layers, and that accurate adjacent predecessors help successors more when they enter earlier. We therefore propose DSpine, a drafter with causal conditioning injection throughout the backbone: at every layer, gated adjacent injection writes each predecessor's predicted feature into its successor, so the causal conditioning chain unfolds over network depth while all positions update in parallel. A unified transfer space built from the target model's output embeddings unifies layer-wise injection with predecessor-conditioned decoding, and layer-wise output-embedding supervision promotes the formation of predicted features in shallow layers. Fused kernels and a transition cache execute both efficiently in parallel within SGLang. Across seven math, code, and chat benchmarks, DSpine achieves the longest acceptance length at both temperatures on Qwen3-4B and Qwen3-8B. At temperature zero on Qwen3-8B, it raises the seven-benchmark mean from DFlash's 3.77 to 4.82 (+27.8%); in SGLang serving tests, it delivers 23.3% higher throughput than DFlash on average. Project page: https://dspine-project.github.io

## [Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2606.15007)

- arXiv: `2606.15007` / version not recorded
- Metadata updated: 2026-10-14T08:37:09Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-primary-draft-posttraining

We introduce Nemotron 3 Ultra, a 550 billion total and 55 billion active parameter Mixture-of-Experts Hybrid Mamba-Attention language model. We pre-trained Nemotron 3 Ultra on 20 trillion text tokens, then extended the context length to 1M tokens, and post-trained using Supervised Fine Tuning (SFT), Reinforcement Learning (RL), and Multi-teacher On-Policy Distillation (MOPD). Nemotron 3 Ultra is our most capable model yet, employing multiple key technologies - LatentMoE, Multi Token Prediction (MTP), NVFP4 pre-training, multi-environment RLVR, MOPD, and reasoning budget control. Nemotron 3 Ultra achieves up to ~6x higher inference throughput as compared to state-of-the-art publicly available LLMs while attaining on-par accuracy. The state-of-the-art accuracy, high inference throughput, and 1M token context length make Nemotron 3 Ultra ideal for long-running autonomous agentic tasks. We open-source the base, post-trained, and quantized checkpoints, along with the training data and recipe on HuggingFace.

## [Personalized LLM Recommendation with Semantic IDs: Autoregressive Beam Search vs. Multi-Token Prediction](https://arxiv.org/abs/2610.15864)

- arXiv: `2610.15864` / version not recorded
- Metadata updated: 2026-10-14T06:54:06Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-primary-draft-posttraining

Large-scale personalization is shifting from embedding-table retrieval to LLM-based recommenders that generate the Semantic ID (SID) of the item to recommend, where each SID is a short sequence of discrete hierarchical content codes. A single instruction-tuned model can then unify retrieval, content understanding, and language, and recommend brand-new titles from their content alone using SID; then, how should the model generate the SID? Traditionally, models rely on a single language modeling head that generates tokens autoregressively, typically using constrained beam search. In contrast, an emerging body of work explores multi-token prediction (MTP), where dedicated heads predict all tokens in parallel, substantially reducing the decoding latency associated with beam search. We report an industry-scale, apples-to-apples comparison of these two generation paradigms: single-head autoregressive decoding vs. MTP. We introduce a new auxiliary ranking loss, defined over the joint SID score, to train the MTP objective. We evaluate the SID training objectives on both quality and training/inference cost, inside a multi-task LLM that jointly does personalized retrieval, content question-answering (QA), and instruction following over a large streaming-media catalog. Our experiments show single-head beam search consistently beats MTP on most product-critical metrics: ranking and content QA, and trains at roughly 2.6x lower dollar cost on Qwen3-8B scale; MTP wins only on raw inference throughput. Around this finding, we detail an efficient training and inference stack and report end-to-end gains over the previous non-SID baseline equipped with an auxiliary ranking head: +77% item cold-start ranking, +22% content-QA accuracy, +2.8x faster training, with language metric regression traced to SID vocabulary expansion. We address the language regression by reinforcement learning post training.

## [An Edge-First Multimodal Asset Management Studio and Retrieval Engine for Heterogeneous AI-Generated Media](https://arxiv.org/abs/2610.14046)

- arXiv: `2610.14046` / version not recorded
- Metadata updated: 2026-10-14T06:07:40Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-reuse

AI-generated image collections combine visual content with heterogeneous provenance such as prompts, model parameters, and workflow graphs. Managing these collections locally requires coordinated metadata extraction, responsive browsing, and retrieval without mandatory remote inference. We present Berry AI Studio, an edge-first asset management system built with Vue, Tauri, Rust, SQLite, and ONNX Runtime. Berry integrates format-specific metadata parsing with raw-payload retention, generation-aware cancellation of queued thumbnail work, a persistent multi-tier thumbnail manifest, cursor pagination, and local image-text retrieval. We evaluate these mechanisms in five independent repetitions on a pinned source revision. With 50,000 catalog records, the median warm first-page database call was 285.3 ms; at offset 40,000, keyset pagination reduced median raw-query latency from 57.9 to 0.46 ms. A controlled browser harness recorded a 0.3 ms median-of-run P95 update time during virtualized scrolling, while cancellation prevented all 1,200 stale speculative decodes in the tested trace. A versioned 10-case corpus produced 53/53 exact metadata-field matches, and controlled retrieval and grouping tests exercised the authentic storage and clustering paths. The implementation, benchmark scripts, raw logs, and checksummed result packages are publicly available.

## [Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy](https://arxiv.org/abs/2610.13708)

- arXiv: `2610.13708` / version not recorded
- Metadata updated: 2026-10-12T02:40:02Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-reuse, datacite-secondary-tail-load

Long-context serving runs out of KV memory before the hardware reaches its useful throughput. HiSparse stores history in host memory and fetches only the selected entries, but it uses one cache budget at every load and does not handle draft-model speculative decoding such as DSpark and DFlash2. We present Adaptive DHiSparse, which supports speculative decoding over hierarchical sparse KV and adapts residency to load. It protects the required working set, retains additional history while GPU memory is spare, and recovers the rest through exact fused retrieval. DSpark and DFlash2 keep their proposal and acceptance rules: queries share missing-row retrieval, draft KV uses a window-bounded ring, and verification staging is reused across layer groups. At 100K context and concurrency 128, GLM-5.3 with DFlash2 delivers 793 output tokens/s per decode GPU, 1.45$\times$ HiSparse and 1.27$\times$ non-speculative adaptive serving. Held to the same latency bounds as HiSparse, it sustains up to 4$\times$ the concurrency and 2.3 to 3.7$\times$ the output, depending on the per-token bound. On DeepSeek-V4.1-Flash at 500K context and concurrency 512, Adaptive DHiSparse with DSpark delivers 1.85$\times$ the output of resident serving with DSpark. In a load step, optional residency reduces host fetches from 14.2% to 1.4% of selected rows at low load and releases memory under pressure.

## [Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models](https://arxiv.org/abs/2609.00355)

- arXiv: `2609.00355` / version not recorded
- Metadata updated: 2026-10-07T03:24:39Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Speculative decoding accelerates generation without changing its output, but on vision-language models (VLMs) a self-reinforcing cycle holds it back. Because an autoregressive drafter pays a sequential pass for each drafted token, it must stay small and can ill afford to attend to the image at each pass. Prior work therefore compresses or hides the image, leaving the drafter weakest on the text the image determines. We present GLANCE, a one-pass block drafter that breaks this cycle on an unmodified VLM target. Its block-diffusion head drafts a whole block in one forward pass over the target's already fused vision-language states, reading the multimodal context once, however deep the draft. The target verifies a wide candidate tree in one pass and commits exactly its greedy output. In one production engine at a fixed round budget, GLANCE decodes up to 3.05 times faster than autoregressive decoding and outpaces the production EAGLE3-VL head on average and by about 11% on grounded tasks. An entropy law explains when drafting pays, predicting the longest accepted blocks on grounded tasks, where the target's next-token entropy is lowest. Our code is available at https://github.com/js-lee-AI/GLANCE.

## [DLoop: Looped Speculative Decoding](https://arxiv.org/abs/2610.07659)

- arXiv: `2610.07659` / version not recorded
- Metadata updated: 2026-10-07T02:43:08Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Speculative decoding accelerates autoregressive generation in large language models. In each drafting stage, a lightweight draft model proposes tokens that the target model subsequently verifies. With increasingly capable draft models, we find that the target model frequently accepts all tokens produced in a drafting stage. A verification nevertheless follows each drafting stage, resulting in unnecessary target-model forward passes even when drafting could have continued. Adaptive draft length methods decide during decoding how many draft tokens precede a verification, but they raise the speedup only for autoregressive draft models. For a parallel draft model, drafting further requires target-model hidden states for draft tokens that have not been verified. We propose DLoop, a looped form of speculative decoding that adaptively performs multiple drafting stages before verification. DLoop continues drafting while the draft model remains confident and verifies all accumulated draft tokens together. Loop-aware training keeps the draft model reliable in the additional drafting stages by exposing it to its own hidden states for unverified draft tokens. By spending additional draft-model forward passes, DLoop reduces the number of target-model forward passes required for verification. Across diverse speculative decoding methods including EAGLE-3, DFlash, Domino, DSpark, and multi-token prediction modules, DLoop improves the wall-clock speedup by 5 to 41 percent while preserving lossless decoding. Code will be available at https://github.com/naver-ai/DLoop.

## [Recovering Off-Policy Supervision for Speculative Decoding](https://arxiv.org/abs/2609.38795)

- arXiv: `2609.38795` / version not recorded
- Metadata updated: 2026-10-06T06:04:23Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-primary-sampling-rl

Block drafters for speculative decoding are commonly trained on corpora written by external models, where a single off-policy token invalidates supervision for all subsequent slots in a block. Existing approaches discard these divergent slots, resulting in severe supervision loss. To resolve this problem while preserving the training corpus, we propose a rollout-based training framework that recovers full supervision through two complementary components. The first component, Anchor-Label Relabelling (ALR), replaces corpus labels with distributions from greedy target rollouts, restoring valid supervision across all predicted slots. The second component, In-Rollout Anchors (IRA), places draft blocks directly inside these rollouts to expose the drafter to target-generated context, reusing precomputed rollout features at no additional target cost. Across fixed vision-language and text corpora, our framework increases greedy accepted length by up to 36.5% over DFlash and consistently outperforms erasing baselines. Notably, a single epoch of our method surpasses the best erase schedules. After three epochs, it matches the acceptance length of training on target-regenerated responses. These results show that our framework provides an effective and compute-efficient approach for training speculative drafters on fixed corpora without modifying the original text. Code is available at https://github.com/js-lee-AI/ALR-IRA.

## [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting](https://arxiv.org/abs/2606.18394)

- arXiv: `2606.18394` / version not recorded
- Metadata updated: 2026-10-06T05:53:26Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Speculative decoding (SD) accelerates autoregressive Large Language Models (LLMs) by drafting multiple tokens and verifying them in parallel, but it faces a scaling limitation: increasing the draft budget improves speed only when acceptance remains high and drafting overhead stays low. This ceiling has been difficult to break because prior head-based SD methods face a causality-efficiency dilemma. Autoregressive drafters produce path-conditioned candidates that are effective for tree speculative decoding with higher acceptance length, but their drafting cost grows with tree depth. Bidirectional block-diffusion drafters generate all positions in one pass, but their branch-agnostic marginals can form individually plausible yet mutually inconsistent trees, wasting budget and reducing acceptance. We propose JetSpec, a head-based SD framework that combines one-forward drafting efficiency with branch-wise causal conditioning. JetSpec trains a causal parallel draft head over fused hidden states from the frozen target model, producing candidate trees whose scores align with the target model's autoregressive factorization. This enables JetSpec to convert larger draft budgets into longer accepted prefixes and higher end-to-end speedup. Across math, coding, and chat benchmarks on dense and MoE Qwen3 models, JetSpec consistently outperforms bidirectional-head and tree-based SD baselines. On H100 GPUs, JetSpec achieves up to 9.64x speedup on MATH-500 and 4.58x on open-ended conversational workloads, with further latency gains demonstrated through vLLM integration under realistic serving loads. Our code and models are available at https://github.com/hao-ai-lab/JetSpec.

## [D-Loop: Looped Diffusion Drafting for Speculative Decoding](https://arxiv.org/abs/2610.06011)

- arXiv: `2610.06011` / version not recorded
- Metadata updated: 2026-10-06T05:14:16Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Block diffusion accelerates speculative decoding by drafting multiple tokens in one forward pass. However, each position predicts a marginal distribution without observing earlier proposed tokens, limiting draft quality and acceptance length. We identify a concrete failure, the \emph{repetition trap}, in which neighboring positions produce redundant copies of the same token. We explain this tendency theoretically and empirically examine its association with shorter accepted drafts. Recent methods refine marginal predictions with an additional causal head or a separately trained drafter, increasing parameter storage and introducing separate training objectives. We instead propose D-Loop, which introduces \emph{intra-block causal conditioning} within the original diffusion drafter without additional model components. Inspired by semi-autoregressive generation and parameter sharing, D-Loop reuses the same backbone across looped passes. The first pass proposes a block, and the second conditions on a selected prefix to regenerate the suffix in parallel. A complementary prefix--suffix objective trains the shared drafter for both anchor-only prefix prediction and prefix-conditioned suffix prediction. Across eight math, code, and chat benchmarks, D-Loop can beat DFlash and DSpark on Qwen3-4B and Qwen3-8B with obvious gains.

## [From Positionwise Confidence to Prefix Scheduling: Verifier Skipping in Speculative Decoding](https://arxiv.org/abs/2608.14787)

- arXiv: `2608.14787` / version not recorded
- Metadata updated: 2026-10-05T02:49:55Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-tail-load

Speculative decoding is a leading technique to reduce the cost of autoregressive generation by using a small drafter to propose several tokens, which are then verified in parallel by a larger target model. Speculative diffusion decoding (SDD) further removes sequential drafting by generating every position in a draft block in parallel with a discrete diffusion model. However, SDD still invokes the target on every block, leaving verification as a potential bottleneck. This paper recognizes that this creates a new control handle: whether to invoke the verifier at all. Thus, we study verifier skipping, a lossy policy that commits a selected draft prefix directly, and ask which confidence signal should schedule it. Interestingly, our study finds that better token predictors need not yield better schedulers: skips require contiguous high-confidence prefixes, while short skips can induce additional drafting rounds. To study this mismatch, we compare raw confidence with learned marginal and conditional survival scores under the same policy, using Strict SDD, lenience, and top-$k$ acceptance as baselines. On HumanEval with DiffuCoder-7B-Instruct and Qwen3-32B, all three confidence signals save $9.6\%$ to $13.5\%$ of verifier calls at the same observed pass@1 as Strict SDD. Surprisingly, raw confidence saves the most; marginal survival has higher positionwise AUROC than raw confidence at most positions, yet neither learned signal dominates online. Our analysis shows that verifier skipping is a useful new lossy axis and, surprisingly, its key challenge is prefix scheduling rather than token prediction alone.

## [EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures](https://arxiv.org/abs/2610.03394)

- arXiv: `2610.03394` / version not recorded
- Metadata updated: 2026-10-05T02:33:13Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-tail-load

Emerging multi-agent LLMs demand privacy-preserving edge deployment, yet current inference systems struggle with these collaborative workflows. Specifically, the memory-bound decode phase causes severe bus contention on unified memory architectures (UMA), paralyzing naive CPU-GPU co-execution. Furthermore, speculative decoding in multi-agent workloads faces extreme variance in drafting difficulty, alternating between complex reasoning and predictable structured generation. Compounded by frequent tool-induced stalls, this highly fragmented execution severely underutilizes hardware and defeats traditional static batching.  We present EdgeAgent, a cross-layer inference system explicitly co-designed for edge UMA and multi-agent workloads. At the micro-architectural level, it bypasses rigid graph-compiler constraints to enable zero-copy UMA-aware tensor parallelism, utilizing asymmetric memory layouts to fully saturate both CPU and GPU compute units. At the scheduling level, it dynamically allocates draft budgets based on real-time sequence predictability to bound bandwidth waste. Concurrently, an asynchronous suspend-and-yield mechanism actively evicts stalled agents, ensuring continuous hardware saturation during unpredictable tool invocations.  Extensive evaluations on an Apple M4 SoC demonstrate that the UMA-aware execution alone contributes a 1.29x speedup over batched speculative decoding. Adding the agent-aware scheduling lifts the full EdgeAgent system to a 1.77x speedup under extreme tool-use latencies.

## [DRelay: Global Draft Context for Prefix-Aware Parallel Speculative Decoding Repair](https://arxiv.org/abs/2610.01439)

- arXiv: `2610.01439` / version not recorded
- Metadata updated: 2026-10-02T03:06:01Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Parallel drafting reduces the drafting overhead of speculative decoding for large language models (LLMs), but its gains remain limited by the accepted prefix length. Even when the correct token is present in the candidate pool, a single early selection error prevents subsequent predictions from being used. We propose DRelay, which uses global information from the entire draft block to perform prefix-aware selective repair of candidate selections before target-model verification. DRelay bases its decisions on candidate correlations and the selected path: a global reader extracts predictive information across positions for each candidate. While a causal selector combines candidate-level information extracted by the global read with the tokens selected at preceding positions to determine whether the native choice at the current position is consistent with the global evidence and the selected prefix. It then decides whether to retain or replace the token, thereby repairing early errors and extending the accepted prefix. We further jointly train the draft backbone and the selector, combining candidate-support learning with a repair objective, while weighting the repair loss according to each block position's potential contribution to the consecutive accepted prefix. Across eight diverse benchmarks on an H800 GPU, DRelay consistently improves both average acceptance length and end-to-end decoding performance over DFlash, Domino, and DSpark. Under SGLang serving, DRelay improves average end-to-end speedup over DFlash, Domino, and DSpark by 14.7%-16.8%, 8.7%-9.3%, and 8.1%-9.3%, respectively.

