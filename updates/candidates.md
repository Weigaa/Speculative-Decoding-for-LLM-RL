# Candidate queue

Unreviewed search hits are not part of the curated corpus and must not be cited as demonstrated RL evidence.

[Search protocol](../docs/search-protocol.md) · [Update status](../data/update_state.json)

## [MobiInfer: Accelerating On-Device GUI Agents with Workload-Aware Inference](https://arxiv.org/abs/2611.08496)

- arXiv: `2611.08496` / version not recorded
- Metadata updated: 2026-11-09T04:44:00Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-reuse

Mobile GUI agents assist users in executing phone tasks through iterative observe-reason-act loops. However, deploy ing multimodal GUI agents directly on smartphones is challenging due to strict end-to-end latency requirements and significant memory overhead. We observe that GUI-agent work loads exhibit recurring workflows and structured I/O: their prompts contain reusable context, while their outputs follow fixed schemas with phase-dependent predictability. Based on this observation, we present MobiInfer, a workload-aware inference engine for on-device multimodal GUI agents. MobiInfer combines trajectory-aware prefix reuse, phase-indexed vocabulary specialization, and schema-guided speculative decoding to eliminate redundant prefill computation and reduce structured-generation overhead. We implement MobiInfer on top of MNN and evaluate it on AndroidWorld and a real world dataset using three real Android devices. Across the four model-benchmark settings, MobiInfer achieves average speedups of 2.6x in prefill and 2.5x in decoding, reduces end-to-end task latency by 2.4x on average, and cuts total deployment storage by 30%, while limiting task-success degradation to less than one percentage point.

## [Lookahead Prediction-Guided Adaptive Visual Refocusing for Interleaved Multimodal Reasoning](https://arxiv.org/abs/2611.02780v2)

- arXiv: `2611.02780` / v2
- Paper updated: 2026-11-06T16:52:15Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Interleaved multimodal chain-of-thought reasoning improves the visual reasoning capabilities of multimodal large language models by dynamically incorporating visual evidence during reasoning. However, existing methods primarily select evidence from historical context. When the reasoning focus shifts, history-guided evidence may remain focused on prior regions and fail to cover the visual information required by the next step. We refer to this lag between visual evidence and subsequent reasoning demands as Temporal Evidence Myopia. To address this issue, we propose Lookahead Prediction-guided Adaptive Visual Refocusing (LPAVR), a training-free test-time framework. LPAVR transforms Multi-Token Prediction (MTP) from a decoding acceleration mechanism into a lookahead signal for anticipating upcoming reasoning intent. During MTP decoding, the draft head generates multiple future tokens, while the target model verifies them in parallel and retains the longest prefix consistent with its decoding trajectory. This target-verified prefix contains near-future semantics, which LPAVR uses to construct lookahead-guided visual evidence and assess whether history-guided evidence covers the indicated regions. If the coverage is sufficient, the history-guided evidence is retained; otherwise, LPAVR switches to the lookahead-guided evidence. This better aligns the visual context with upcoming reasoning and improves consistency between draft predictions and target-model decoding. Experiments on multiple multimodal reasoning benchmarks show that LPAVR improves both reasoning accuracy and the acceptance rates of MTP speculative tokens, jointly enhancing visual reasoning and speculative decoding efficiency.

## [Generative Search and Recommendation at Shopify](https://arxiv.org/abs/2611.08804v1)

- arXiv: `2611.08804` / v1
- Paper updated: 2026-11-05T23:56:02Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-primary-draft-posttraining, primary-draft-posttraining

Search and recommendation at Shopify require retrieving relevant products from a changing catalog of billions of products under strict latency constraints. We present SID-LLM, which casts both tasks as generating semantic IDs: short sequences of content-derived tokens representing products. We jointly pre-train SID-LLM on catalog and behavioral data, giving search and recommendation a shared representation and training objective. We show that reinforcement learning further improves judged search relevance. Furthermore, distillation from task-specific experts improves recommendation quality over joint supervised fine-tuning without a statistically detected loss in search quality. Finally, for efficient serving, we pair multi-token prediction with a lightweight ranker, improving retrieval quality over our autoregressive baseline while reducing latency. We evaluate SID-LLM both as a standalone retriever and as a component of Shopify's production search and recommendation systems. As a standalone search system, SID-LLM achieves quality comparable to Shopify's existing multi-model search stack while meeting production latency requirements. Integrating SID-LLM into the search and recommendation stacks provides significant gains in both offline evaluations and online A/B tests. Together, these results demonstrate the practical value of semantic-ID generation as a unified approach to product discovery at scale.

## [ChainFlow: Few-Step Latent Flow Matching for Speculative Decoding](https://arxiv.org/abs/2611.08669v1)

- arXiv: `2611.08669` / v1
- Paper updated: 2026-11-05T20:26:25Z
- Source: arXiv API
- Screening status: pending
- Query families: secondary-tail-load

Speculative decoding has become a standard way to accelerate LLM inference: a lightweight drafter proposes tokens that the target verifies in one parallel pass. Existing drafters face trade-offs that limits their speedups: autoregressive drafters generate tokens one at a time, so drafting cost grows with draft length, while diffusion drafters generate tokens in parallel but predict each position independently, ignoring inter-token dependencies. We introduce ChainFlow, a new speculative decoding paradigm and the first flow-matching drafter conditioned on the target's hidden states. ChainFlow treats drafting as a short transport over hidden states, needing one or two flow steps instead of the many denoising steps of generation from noise. A variational autoencoder compresses these states so drafting cost barely grows with target size, lightweight feedback heads restore inter-token dependencies, and tree drafting raises acceptance. On Qwen3.5 models, at matched drafter size and training data, ChainFlow outperforms EAGLE-3 and DFlash in vLLM by 39% and 11%, respectively. These gains further widen as drafters are adapted to new languages sequentially. Our ablations cover drafter design and concurrent serving, and we open-source our code and drafter models.

## [CoRD: Coupled Rollouts Fill the Blind Spot of On-Policy Distillation](https://arxiv.org/abs/2611.07959v1)

- arXiv: `2611.07959` / v1
- Paper updated: 2026-11-05T12:55:51Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-primary-sampling-rl, datacite-secondary-policy-adaptation, primary-sampling-rl, secondary-policy-adaptation

On-policy distillation trains a student on its own rollouts, so states the teacher would reach but the student does not are seldom supervised. We introduce CoRD (coupled-rollout distillation), which keeps the on-policy loss and moves only the distribution of training states toward the teacher, drawing rollouts from a geometric interpolation of student and teacher through the maximal coupling of speculative decoding. The coupling keeps the student's token wherever the two distributions agree and otherwise substitutes a token from the part of the target the student underweights, so interventions are as rare as any exact sampler allows and recede as the student learns. Across six base students from two model families (Qwen3 and Qwen3.5, 0.6B to 4B), CoRD raises average pass@1 over on-policy distillation by 0.9 to 2.0 points and pass@8 by 1.2 to 3.4 points on five public math benchmarks at equal steps and data. On frozen teacher-reached states, a 4B student trained with CoRD reaches in 16 steps a gap closure that on-policy distillation does not reach in 80, and substitution rules intervening at least as often in other directions fall short of CoRD.

## [AiXapply: Fast and Reliable Full-File Code Integration with Specialized Small Models for IDE Workflows](https://arxiv.org/abs/2611.07634v1)

- arXiv: `2611.07634` / v1
- Paper updated: 2026-11-05T08:19:22Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-primary-sampling-rl, primary-sampling-rl

Large language models increasingly assist developers by proposing small code edits, yet reliably integrating a partial update snippet into an existing file while preserving unrelated content remains poorly supported by current code-generation workflows. We formalize the Code Integration (Apply) task as follows: given an original file and an update snippet, the system must produce the complete merged file while preserving all content outside the requested edit. We construct a high-quality multi-language dataset from real commits via a structured pipeline that converts code changes into update snippets paired with full-file ground truth and enforces consistency through verification and filtering. We then train a specialized 4B model, aiXapply, using supervised fine-tuning and reinforcement learning (GRPO). The supervised variant achieves 94.4% accuracy under our language-aware comparison, surpassing a strong large-model (Deepseek-V3.2) baseline (91.6%). Speculative decoding enables aiXapply-RL to reach $\sim$2700 tokens/s on a single A100 in a decoding subset; on the full benchmark, it achieves roughly 75$\times$ lower latency than the API-served Deepseek-V3.2 baseline. We further conduct an industrial deployment of aiXapply-RL in the aiXcoder IDE plugin as a dedicated Apply service, reducing mean Apply latency from 50 seconds to 1.89 seconds by offloading full-file generation from the upstream large model. Under time-based capacity planning, replacing one of five upstream serving instances would save 20% of upstream machine cost before the additional shared A100 service cost. Overall, our results demonstrate that treating code integration as a standalone task enables small models to achieve high accuracy, practical efficiency, and concrete industrial benefits in real-world IDE workflows where latency, cost and privacy are critical.

## [ROCm InferaSim: Cut LLM Serving Trial Costs and Deploy the Best Configuration](https://arxiv.org/abs/2611.04032v1)

- arXiv: `2611.04032` / v1
- Paper updated: 2026-11-02T22:23:40Z
- Source: arXiv API
- Screening status: pending
- Query families: secondary-tail-load

Serving an LLM efficiently depends on the engine, how the model is split across GPUs, precision, scheduler settings, speculative decoding, KV-cache management, and prefill-decode disaggregation. The best configuration depends on the model, hardware, workload, and objective. Operators usually find it by trial and error. Exhaustively measuring the candidates in our study would take about 25,000 GPU-hours. ROCm InferaSim predicts serving performance from a few short measurements. Choices such as batch size, prompt length, and GPU count change the amount of work per GPU without changing the kernels. ROCm InferaSim benchmarks each distinct set of kernels once, on at most one node. We call this measurement an anchor. Analytical laws carry that anchor to other deployments that run the same kernels. For multi-node deployments, ROCm InferaSim reduces the configuration to a single-node equivalent, measures it, and scales the result analytically. A simulator replays multi-turn traffic, and a tuning agent searches configurations using the predictions. On AMD Instinct MI355X GPUs with vLLM, SGLang, and ATOM, 11 anchors took 9.1 GPU-hours, against 204 GPU-hours to measure the 226 fixed-length configurations they cover. On 172 configurations, time per output token has 8.1% median error. On a multi-turn coding workload, throughput is within 8%. For 159 disaggregated deployments, none used as an anchor, throughput is within 5.5%. A five-candidate short list contains a deployment within 12% of the best feasible pairing of model and latency target.

## [HERALD: High-Throughput Block Diffusion LLM Inference via CPU-GPU Cooperative KV Cache Retrieval](https://arxiv.org/abs/2606.21633v3)

- arXiv: `2606.21633` / v3
- Paper updated: 2026-11-01T16:58:02Z
- Source: arXiv API
- Screening status: pending
- Query families: secondary-reuse

Block diffusion LLMs (block dLLMs) improve decode throughput by generating tokens in parallel, and are emerging as a next-generation alternative to autoregressive LLMs. At long contexts, however, the KV cache remains a major throughput bottleneck in both memory bandwidth and capacity. For autoregressive LLMs, dynamic sparse attention is often combined with KV offloading to alleviate both bottlenecks, keeping the full KV cache in CPU DRAM and fetching only a critical subset to the GPU. However, KV subset selection and retrieval over bandwidth-limited PCIe incur substantial offloading overheads that often stall the GPU. We present HERALD, the first dynamic sparse attention method for block dLLMs that supports KV offloading. HERALD exploits a property of block dLLMs: a critical KV subset selected once per block is reused across all of its denoising steps, so the next block's selection can be hidden behind the current block's denoising. HERALD realizes this with a two-stage selection algorithm co-designed with its execution system. While the GPU denoises the current block, the CPU speculatively searches the full KV cache for the next block with a single query merged from the current block's B queries, cutting the selection compute by Bx; the GPU then refines the candidates into the final top-K subset with the next block's real queries. At K=1024, HERALD achieves near-lossless accuracy relative to Dense on LongBench and reasoning tasks across four block dLLMs, and improves decode throughput by up to 3.70x over Dense GPU-only inference, 2.59x over MAGE, a state-of-the-art block-dLLM sparse attention method, and 8.38x over MAGE-Offload, its direct KV-offloading extension.

## [ReFrame: Silence-Aware Compute Reclamation for Full-Duplex Speech Models](https://arxiv.org/abs/2611.01835v1)

- arXiv: `2611.01835` / v1
- Paper updated: 2026-11-01T12:10:55Z
- Source: arXiv API
- Screening status: pending
- Query families: secondary-reuse

Full-duplex speech models execute dense model inference for every audio frame throughout a live interaction. This uniform framewise schedule creates sustained GPU load across dialogue states whose computation has strong, reusable temporal structure. ReFrame formulates full-duplex inference as a silence-aware computation problem. Mutual Silence Speculation (MSS) operates when both participants are silent: it evaluates multi-frame Temporal continuations, verifies text and hidden-state stability, and applies batched Mimi audio-token correction. Listening Frame Folding (LFF) operates while the user speaks and the agent listens: it processes already-arrived user frames through parallel Temporal execution and frame-batched audio-token generation while accepting only the verified prefix. Frame-Budget Reinvestment (FBR) assigns the released frame intervals to resumable external retrieval and language-model workers, then injects timely references through Moshi's conditioning interface. We instantiate ReFrame on five full-duplex models spanning Moshi-family, phase-structured, and flattened autoregressive generation. Across the complete 1,225-conversation FDBench, ReFrame reduces measured GPU execution time by 18.80-31.01% and retains 96.92-100% non-PAD text agreement on five different models. On HaluEval tests, FBR increases the number of correct generated spoken answers from 86 to 205 under the same auxiliary-service budget. ReFrame turns recurring dialogue structure into lower inference cost and higher end-to-end service capability.

## [UBTree: Parallel Tree Drafting via Unigram and Bigram Models for Speculative Decoding](https://arxiv.org/abs/2609.39972)

- arXiv: `2609.39972` / version not recorded
- Metadata updated: 2026-10-30T13:28:30Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Speculative decoding accelerates language model inference by verifying multiple draft tokens in a single target-model pass. Recent parallel drafters have achieved breakthrough performance in frontier production models, but their effectiveness deteriorates as the entropy of target distributions increases due to insufficient draft diversity. To overcome this bottleneck without sacrificing parallelism, we introduce UBTree, a parallel drafter that couples a Unigram proposer with a Bigram selector to construct drafting Trees. The unigram proposer is trained with the standard cross-entropy objective to generate candidate tokens independently for each position, while a lightweight bigram selector predicts transition scores between adjacent candidate pairs. Unlike the proposer, the selector is trained with a renormalized KL objective on high-temperature data. This tree-native training broadens the supervision beyond the greedy path, encouraging plausible alternative branches that improve the chance of accepting additional tokens during tree verification. Across seven standardized benchmarks with Qwen3-4B and Qwen3-8B, UBTree achieves an average speedup of $5.84$--$6.94\times$ over autoregressive decoding and outperforms DARTree in all 28 comparisons. Production-scale evaluation further demonstrates UBTree's advantage over frontier baselines such as DSpark.

Curator note: Needs full-text assessment of high-entropy tree drafting, verification assumptions and a concrete RL workload/maintenance mapping beyond generic drafter accuracy. Registry dates are not posting dates.

## [Verification-Aware Training for Speculative Decoding](https://arxiv.org/abs/2608.30135v2)

- arXiv: `2608.30135` / v2
- Paper updated: 2026-10-28T08:06:17Z
- Source: arXiv API
- Screening status: pending
- Query families: secondary-tail-load

Speculative decoding accelerates large language model inference by using a draft model to generate candidate tokens, which are verified by the target model in a single forward pass. Verification proceeds sequentially and discards every position from the first rejection onward, yet existing draft training relies on token-level imitation of the target with a fixed per-position weighting that reflects neither property. We introduce Verification-Aware Training (VAT), a plug-in framework that simulates verification at every training step and turns the resulting accept and reject patterns into supervision. VAT consists of two components: (i) a verification head, a lightweight jointly trained binary classifier that supervises the draft model on whether each position survives sequential verification; (ii) verification-adaptive weighting, which replaces the fixed weighting schedule by keeping full weight up to each sample's first rejection point and re-anchoring the decay to start there. VAT modifies only the training objective, so it can be layered on top of existing methods without changing the draft architecture, the target model, or the inference procedure. Applied to EAGLE-3 and DFlash on Qwen3-4B, Qwen3-8B, and LLaMA-3.1-8B, VAT improves average acceptance length by up to 11.4% and wall-clock speedup by up to 8.7%, with consistent gains across math, code, and chat benchmarks. Code will be available at https://github.com/naver-ai/vat

Curator note: Needs full-text cost and transfer review of verification-aware drafter training. A fixed-verifier training objective is not direct target-policy RL evidence.

## [Multi-Token Prediction Done Right](https://arxiv.org/abs/2610.38331v1)

- arXiv: `2610.38331` / v1
- Paper updated: 2026-10-28T06:31:05Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Multi-Token Prediction (MTP) is now a common ingredient in language-model pre-training, as it improves downstream performance and enables faster inference through speculative decoding. We identify a flaw in standard MTP training, in which a residual component of the MTP gradient interferes with both next-token and multi-token learning, increasingly so with scale. Specifically, the MTP cross-entropy gradient can be decomposed exactly into a KL self-distillation term that pulls each MTP head toward the model's own next-token prediction (NTP) distribution and improves speculative decoding, and a residual that has a low signal-to-noise ratio and buries the useful KL signal. We introduce the KL gradient-recovery trick: when two distributions share a linear output head, the gradient of their KL divergence can be recovered exactly by combining their cross-entropy gradients through straight-through gradient routing. Unlike minimizing the KL directly, this trick requires no vocabulary-sized logit matrices and is compatible with standard fused cross-entropy kernels. This enables Soft Multi-Token Prediction (Soft-MTP), a one-line code change to MTP that removes the noisy residual and backpropagates only the KL self-distillation signal by reusing the existing NTP and MTP cross-entropy computations. Soft-MTP supports both DeepSeek- and Meta-style MTP, adds no parameters, and incurs no measurable overhead. From 167M to 1.2B parameters, Soft-MTP improves over standard MTP with lower NTP perplexity, faster speculative decoding and higher zero-shot accuracy at every scale, lower MTP perplexity from 689M onward, and stronger math and code reasoning after fine-tuning at 1.2B. Soft-MTP also matches, if not exceeds, direct KL divergence minimization on most metrics. Soft-MTP is, in effect, a free lunch for MTP optimization. Our code can be found at https://github.com/JaydenTeoh/Soft-MTP.

Curator note: Official abstract and full HTML retrieved; detailed eligibility review is unfinished. Primarily MTP pretraining/gradient routing; distinguish background on training coupling from a demonstrated RL-rollout mechanism.

## [Bastion: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting](https://arxiv.org/abs/2605.29727v4)

- arXiv: `2605.29727` / v4
- Paper updated: 2026-10-28T05:42:31Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Block-diffusion drafters have recently emerged as a powerful alternative for speculative decoding by predicting multiple future-token distributions in a single parallel step. However, since these parallel predictions are sampled from position-wise marginals rather than fully conditioned sequences, committing to a single greedy path often fails to capture the target model's preferred trajectory. To address this, we propose BASTION, a budget-aware speculative decoding framework with tree-based diffusion drafting. Unlike existing methods that rely on static tree topologies, BASTION dynamically constructs query-dependent trees by balancing draft quality against hardware constraints. Our framework integrates three synergistic components: (1) an acceptance surrogate that estimates expected accepted length via path confidence, (2) an online latency estimator that calibrates a hardware-aware roofline model, and (3) an adaptive best-first expansion that grows the tree until marginal gains no longer justify incremental verification costs. BASTION is training-free, preserves the target model's distribution, and requires no per-setting tuning. Across diverse benchmarks and GPU architectures, BASTION achieves up to a $6.61\times$ speedup over standard autoregressive decoding, outperforming state-of-the-art block-diffusion baselines by 39%.

Curator note: Needs primary full-text review of the hardware-aware tree-budget estimator and actual serving-versus-RL evaluation. Not a new study merely because v4 is newly observed.

## [Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI](https://arxiv.org/abs/2610.38095v1)

- arXiv: `2610.38095` / v1
- Paper updated: 2026-10-28T00:28:08Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-primary-sampling-rl, datacite-secondary-policy-adaptation, primary-sampling-rl, secondary-policy-adaptation

We introduce Nemotron 3.5 Super and Nemotron 3.5 Lightning, open and efficient Mixture-of-Experts Hybrid Mamba-Transformer models designed for reasoning, long-context understanding, and agentic workloads. Super is a 120B-parameter, 12B-active multimodal model, while Lightning is a smaller 30B-parameter, 3B-active text model; both designed for efficient deployment. Both models combine large-scale distillation, long-context training, and native speculative decoding, while Super further incorporates Indic continued pretraining and agentic software-engineering mid-training. We develop a comprehensive post-training pipeline spanning supervised fine-tuning and reinforcement learning (RLVR and RLHF), complemented in Super by specialized teacher training and multi- teacher on-policy distillation (MOPD). This transforms Super from a text-only base model into a multimodal agent capable of reasoning over text, images, video, and interactive tool environments. We further explore test-time scaling through parallel agent execution and self-verification. Across training and deployment, we jointly optimize capability and efficiency. Indic continued pretraining improves Indian-language benchmarks by up to 9.82 percentage points, while agentic mid-training strengthens software-engineering capabilities and robustness across agent harnesses. The post-trained Super model achieves 51.78% on SWE-bench Pro, surpassing Nemotron 3 Ultra despite using approximately 4.6x fewer active parameters. Post-training MTP boosting improves speculative- decoding acceptance length by up to 21.8% under probabilistic draft sampling, while NVFP4 quantization achieves 99.62% median accuracy recovery relative to BF16. Inference optimizations enable up to 4,856 output tokens/s/GPU on GB200 while sustaining at least 50 tokens/s/user.

Curator note: Foundation-model report with RL and post-training MTP boosting. Locate whether SD is actually evaluated during target-policy RL, after RL, or only at deployment before assigning direct evidence.

## [XPress: Parallel Refinement for Diffusion Drafters in Speculative Decoding](https://arxiv.org/abs/2608.02438v2)

- arXiv: `2608.02438` / v2
- Paper updated: 2026-10-26T00:18:30Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Block-diffusion drafters like dFlash generate an entire block of draft tokens in a single forward pass, drastically reducing the overhead of multiple-token drafting in speculative decoding. The crucial final step of the single-pass discrete denoising process involves using the logit distribution at each position to sample conditionally independent tokens. The resulting draft is thus a set of per-position marginals, rather than a joint distribution: no draft token is guaranteed to depend on its predecessors. Such independently sampled marginals tend to produce sequences with tokens that are individually likely, but jointly improbable under the target model's distribution, which verifies each token conditionally. This can cause early rejection and limits acceptance length. To address this, we propose xPress as a means to restore the missing causality in diffusion drafters. xPress is a lightweight causal refiner that reconciles the whole diffusion block at once through parallel refinement, restoring and propagating causal dependencies across the draft without a token-by-token loop. On Qwen3-8B, across seven math, code, and chat benchmarks, xPress raises acceptance length by about 30% on average (up to +56%) and its end-to-end decoding throughput by about 1.3 on average (up to 1.7) compared to the original dFlash diffusion drafter.

Curator note: Needs full-text assessment of parallel causal-refinement cost and a concrete rollout transfer beyond a generic increase in draft capacity.

## [OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching](https://arxiv.org/abs/2608.08097v2)

- arXiv: `2608.08097` / v2
- Paper updated: 2026-10-25T10:57:32Z
- Source: arXiv API
- Screening status: pending
- Query families: secondary-tail-load

Large language model (LLM) inference serving is increasingly constrained by memory rather than compute. As long-context and long-form reasoning workloads become more prevalent, the key-value (KV) cache dominates both memory footprint and memory traffic at the token generation (i.e., decode) stage. HBM capacity has therefore become a critical bottleneck, constraining inference batch size and throughput. This paper introduces OasisKV, a memory-centric LLM inference system that alleviates HBM limitations by offloading the KV-cache to alternative memory tiers. Exploiting the sparsity of decode-time attention and leveraging speculative decoding to predict important tokens, OasisKV selectively prefetches and stages only the most relevant KV entries in HBM for efficient LLM inference computation. To support growing LLM context and the larger batches enabled by sparse HBM residency, OasisKV employs tiered KV management across decode, prefill, and remote-memory nodes, relaxing decode-host memory capacity limits under disaggregated serving. An asynchronous prefetch pipeline hides off-GPU transfer latency while bounding per-step traffic to fit the available bandwidth. We implement OasisKV on vLLM. With only 2,048 KV tokens resident in HBM, OasisKV maintains average accuracy within a negligible 0.61 points of full attention on LongBench v2 for long-context understanding and across AIME24-25 and GPQA-Diamond for long-form reasoning. This sparsity translates into a 1.86x throughput gain over vLLM on AIME24. Synthetic long-context workloads further show up to 2.2x higher throughput in multi-GPU serving. Under prefill-decode disaggregation, OasisKV achieves 2.29x vLLM's throughput while supporting 2.42x as many concurrent requests under the same host-memory budget.

Curator note: Must distinguish draft-assisted KV prefetch from altered sparse target computation. Review numerical/quality approximation and full-cache verification assumptions before inclusion.

## [BitMTP: When Multi-Token Prediction Meets Low-Bit Large Language Models](https://arxiv.org/abs/2610.28500)

- arXiv: `2610.28500` / version not recorded
- Metadata updated: 2026-10-21T03:07:29Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

For efficient deployment of large language models (LLMs), methods of ultra-low-bit backbones reduce weight storage, memory traffic, and linear-layer execution cost, while multi-token prediction (MTP) methods reduce sequential decoding steps by predicting multiple future tokens in parallel. Although complementary, the direct combination of these methods cannot accelerate decoding at comparable quality: masked drafting lacks intermediate token input supplied in next-token training, while wider computation and causal key-value (KV) updates can offset the savings from fewer steps. To address these challenges, we propose BitMTP, an algorithm-system co-design framework for efficient MTP on ultra-low-bit LLM backbones. A joint next-token prediction and MTP objective equips a single model with both autoregressive (AR) generation and block-causal drafting. Confidence-only decoding, speculative-only decoding, and hybrid decoding provide different quality-throughput operating points without using separate draft and verifier models. Accepted-prefix alignment keeps the committed prefix, materialized causal KV boundary, and CUDA Graph replay state consistent for continued generation. BitMTP uses this contract to select width-specialized low-bit execution and reuse captured graphs over shared KV storage. On NVIDIA H20, BitMTP with hybrid decoding achieves five-task mean speedups of 2.2x on BitNet b1.58-2B and 2.1-2.4x on 1.7B-4B Bonsai models at comparable task quality. On RTX 3090 and Jetson Orin, it further achieves up to 2.0x in five-task mean throughput and 3.3x on MBPP+, respectively. These results demonstrate that BitMTP accelerates ultra-low-bit LLM generation across backbones, model sizes, and GPU types. The source code is released at https://github.com/PolyU-VCLab/BitMTP

Curator note: Needs full-text verification of the low-bit/MTP target verification rule, policy-coupled maintenance cost and inference baseline.

## [Large Flow Language Models](https://arxiv.org/abs/2610.28559v1)

- arXiv: `2610.28559` / v1
- Paper updated: 2026-10-20T17:20:29Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Continuous flow language models offer a path to parallel generation with tools for control and acceleration unavailable to discrete diffusion, yet effective techniques for building them at the billion-parameter scale remain less established. We present Lafa (Large flow language model), a fast, high-performing flow language model scaled to 8B parameters in a data-efficient manner. Lafa is a blockwise flow model with causal attention on the prefix and bidirectional, asynchronous flow within each block. This design enables efficient training by adapting pretrained autoregressive (AR) models and fast inference via prefix caching and blockwise parallel decoding. We train Lafa at 0.5B, 7B, and 8B scales with fewer than 30B tokens, more efficient than previous diffusion models, and evaluate it on instruction following, reasoning, and coding, where the learned flow matches or surpasses the quality of AR and can be distilled into flow maps for one- and few-step generation. Notably, flow training preserves or even improves pretrained AR capabilities via a multi-token prediction effect, which we leverage in a self-speculative decoding scheme that verifies flow-based drafts autoregressively within a single model. This yields 2.54x the throughput of an AR model at comparable quality, outperforming multi-token prediction and discrete diffusion methods. Our findings show that continuous flows can serve as a scalable foundation for language modeling.

Curator note: Confirm an explicit rollout-transfer mechanism and AR target-verification semantics; a new flow language-model architecture alone is insufficient.

## [Performance-Driven Policy Optimization for Speculative Decoding with Adaptive Windowing](https://arxiv.org/abs/2605.14978v3)

- arXiv: `2605.14978` / v3
- Paper updated: 2026-10-20T13:08:31Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-primary-draft-posttraining, datacite-primary-sampling-rl, primary-draft-posttraining, primary-sampling-rl

Speculative decoding accelerates LLM inference by having a lightweight draft model propose speculative windows of candidate tokens for parallel verification by a larger target model. In practice, speculative efficiency is often bottlenecked by hard-to-draft positions, where an early mismatch truncates the accepted prefix and invalidates the rest of the speculative window. Most learning-based drafters are still optimized with token-level supervised objectives, even though speculative utility is inherently window-level and prefix-sensitive. We propose PPOW (Performance-Driven Policy Optimization with Adaptive Windowing), a reinforcement learning framework that shifts drafter optimization from token-level imitation to window-level optimization. PPOW combines a Cost-Aware Speedup Reward, a Distribution-Based Proximity Reward, and Adaptive Divergence-Aware Windowing, which prioritizes informative windows with high confidence-weighted draft-target divergence. PPOW achieves average acceptance lengths of 6.29-6.52 and speedups of 3.39-4.36$\times$ across multiple model families and benchmarks under a unified decoding protocol. These results show that performance-driven window-level optimization is a practical approach to improving speculative decoding efficiency.

Curator note: RL optimizes the draft/acceptance window for inference; do not classify this as direct RL rollout evidence. Review adaptive-window cost and policy-transfer requirements.

## [PACT-VLA: Speculative Action-Chunk Verification with Pre-Commit Observations](https://arxiv.org/abs/2610.28019v1)

- arXiv: `2610.28019` / v1
- Paper updated: 2026-10-20T11:08:41Z
- Source: arXiv API
- Screening status: pending
- Query families: secondary-policy-adaptation

Vision-language-action (VLA) policies are commonly deployed with asynchronous inference in real-world settings, where the next action chunk is generated while the robot is still executing the previous one. By the time the new chunk is committed, the robot and scene have changed, so the chunk is conditioned on a stale observation and task success drops sharply as this inference delay grows. Generating multiple candidate chunks could let newer observations inform the final choice, but existing multi-candidate methods either rank candidates with the stale inference-start observation or repeatedly switch between candidates during execution, which can make the executed action sequence discontinuous. Our key insight is that inference delay can be used as decision time. While candidate generation is still underway, candidate selection can reuse the VLA itself to choose the complete action chunk that best fits a later observation. We propose PACT-VLA, a training-free framework that generates candidates from the inference-start observation and selects one using this pre-commit observation. Its scoring function, FlowRes, measures the residual between each candidate's implied flow direction and the velocity predicted by the frozen policy under the pre-commit observation, requiring no separate verifier. A pipelined implementation overlaps observation processing with candidate generation and batches scoring, so selection adds no control-step delay on the evaluated hardware. At a four-step delay, PACT-VLA improves average success by 15.0 percentage points over RTC on Kinetix and by 5.2 points over single-candidate asynchronous execution with GR00T N1.7 on LIBERO, and it further improves existing delay-robust methods. On three real-robot tasks, it raises average success from 60% to 82% over naive asynchronous execution with the same frozen $π_{0.5}$ checkpoint.

## [Factorization-Guided Training and Inference for Diffusion-Drafted Speculative Decoding](https://arxiv.org/abs/2610.23935)

- arXiv: `2610.23935` / version not recorded
- Metadata updated: 2026-10-20T04:03:43Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-tail-load

Speculative decoding accelerates large language model inference through parallel verification of tokens proposed by a drafter. Diffusion drafters further parallelize proposal generation, but greater proposal capacity or higher mean accepted tokens (MAT) need not yield higher throughput. Because verification accepts only a consecutive prefix, early rejections can render later correct predictions ineffective, limiting MAT gains, while even higher MAT may not improve throughput if per-round latency increases. We introduce DScout, which uses two complementary factorizations to guide diffusion drafter training and inference for higher throughput. For training, DScout factorizes position-wise loss into inclusion, weighting, and prediction loss. This guides the design and combination of mixed-horizon training, intra-block unmasking, and acceptance-weighted loss to align supervision with prefix acceptance and improve MAT. For inference, DScout factorizes throughput as the ratio of MAT to per-round latency, guiding target-conditioning depth, drafter depth, and inference block size selection to identify a high-throughput configuration for each workload. Across six benchmarks, DScout achieves $3.84\times$ and $4.14\times$ mean speedups over autoregressive decoding on Qwen3-4B and Qwen3-8B, respectively, improving mean speedup over the state-of-the-art baseline by 9.1% and 7.1%. Across models and concurrency settings, our inference configuration policy provides up to 9.75% additional mean speedup over DScout's fixed configuration.

Curator note: Official abstract verified, but arXiv HTML was unavailable (404). Full-text review of DScout scheduling and concurrency evidence is still required.

## [DStill: Trajectory Consistency Distillation for Accelerated One-Step Drafting in Block Diffusion Speculative Decoding](https://arxiv.org/abs/2610.27379v1)

- arXiv: `2610.27379` / v1
- Paper updated: 2026-10-19T23:05:16Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Block-diffusion speculative decoding accelerates large language model inference by drafting multiple tokens in parallel. However, one-step drafting in discrete diffusion is limited by token factorization error: each token is predicted from the same masked block, without conditioning on the tokens selected at other positions in that step. This can produce inconsistent drafts and reduce acceptance length. Iterative refinement mitigates this limitation by conditioning later predictions on previously committed tokens, though additional passes increase drafting cost. To address this trade-off between draft fidelity and inference latency, we introduce DStill, a two-stage framework that distills a target-conditioned drafter's own multi-step refinement into one-step drafting. We first train the drafter to complete partially revealed blocks, then use its refinement trajectories to train a student to predict the final completion in one pass. Using a curriculum that gradually transitions from partial to fully masked inputs, we successfully transfer the multi-step refinement capabilities into one step. Across reasoning, math, code benchmarks on three model families DStill improves acceptance length by up to 28% and speedup by up to 25% over one-step DFlash, achieving up to 6.45x speedup over auto-regressive decoding.

Curator note: Needs full-text assessment of whether one-step distillation supplies a distinct, costed rollout-transfer mechanism beyond generic drafter accuracy.

## [HyCo: Hybrid Drafting for Cost-Efficient Mobile-Cloud Speculative Decoding](https://arxiv.org/abs/2610.21436v2)

- arXiv: `2610.21436` / v2
- Paper updated: 2026-10-19T22:39:59Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Device-cloud speculative decoding reduces server computation, but growing a deep draft tree with a small language model (SLM) requires repeated passes on a mobile neural processing unit (NPU). We present HyCo, which runs the server model's native multi-token prediction (MTP) head on the device to build a deep chain and uses one SLM pass to add alternative branches. The server returns the hidden state, input embedding, and key-value entries needed by the head instead of executing its sequential steps. Quantization, a restricted vocabulary, and a 1K-token window fit both drafters to the NPU. An ε-threshold rule additionally relaxes exact preservation of the verifier's sampling distribution. In single-client runs with a Galaxy S26 Ultra over LTE/5G, HyCo reduces server GPU time per output token relative to server-side MTP self-speculation by 38.6% on Spec-Bench and 29.2% on 32K-token summarization. With the same acceptance rule, three runs of each system on Spec-Bench show 9.0 percentage points more saving and 1.9x delivery speed than an SLM-only drafter. HyCo differs from Cloud+MTP by +0.2 judge-score points (paired 95% CI: -0.9 to +1.3); exploratory translation favors SpecEdge-ε. Without relaxation, HyCo exact saves 27.7% and 11.9% on the two datasets.

Curator note: Needs full-text cost/placement and acceptance-rule review. Mobile-cloud savings cannot directly establish distributed RL rollout benefit.

## [Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening in Realtime Voice Agents](https://arxiv.org/abs/2610.26233v1)

- arXiv: `2610.26233` / v1
- Paper updated: 2026-10-19T11:59:57Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-reuse, secondary-reuse

Tool-using voice agents often leave users waiting after speech ends, even when actionable information arrives earlier in the request. Speculative approaches begin work during speech, but chunk-bounded or interrupt-on-update generation can truncate a tool call before its arguments are complete. This couples computation time to speech updates, limiting useful work completed in advance. We introduce Heartbeat Thinking, which handles updated input through new Thinker invocations while allowing ongoing invocations and dispatched tools to finish. Periodic invocations read the latest partial transcript and a shared record of completed reasoning and tool results. These results help resolve missing arguments and initiate dependent calls, allowing preparation to progress across speech updates. Across SpeechFCEval, FDBench v3, and AudioCRAG, Heartbeat improves aggregate speculative tool coverage or retrieval reuse over a SHANKS-style windowed baseline, with benchmark-dependent effects on final task quality. On FDBench v3, it increases tool coverage by 16 percentage points and reduces mean final-response latency by 36.4\%. The results show that heartbeat thinking paradigm preserving ongoing computation during speech can turn listening time into reusable preparation for faster and more capable voice-agent responses.

Curator note: Action/tool execution during realtime voice input is a different validation object. Review only as possible contextual evidence, outside technical-core counts.

## [ECHO: Efficient Causal Self-Recursion Beyond Auxiliary Multi-Token Prediction](https://arxiv.org/abs/2610.24766v1)

- arXiv: `2610.24766` / v1
- Paper updated: 2026-10-17T16:18:15Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Existing Multi-token prediction (MTP) methods are auxiliary by design: the multi-horizon loss mostly trains modules attached to the backbone, and each added horizon costs another module and another pass. We propose Efficient Causal Self-Recursion (ECHO), which removes both costs. The backbone's own final layer predicts every horizon, so the supervision lands on the parameters that generate the next token, and Dynamic Depth Sampling (DDS) keeps deeper horizons affordable by drawing the training depth with probabilities that decay along depth. Future prediction thus becomes part of the autoregressive objective rather than a task attached to it, and the gains follow on both sides of it. In pretraining, added depth converts into downstream accuracy where auxiliary modules saturate, concentrating on reasoning and code at half the MTP training overhead of training every depth. At inference, the pretrained model is its own drafter: it drafts beyond the depth it was trained for, and keeps its draft-target alignment on the open-ended, high-entropy generation where post-hoc drafters lose theirs. The advantage survives a doubled token budget, a repeated pretraining run, and supervised finetuning.

Curator note: Needs full text to verify self-recursive MTP proposal construction, verification, and maintenance under target-policy updates.

## [FlashMap: Flow Map Speculative Decoding](https://arxiv.org/abs/2610.24365v1)

- arXiv: `2610.24365` / v1
- Paper updated: 2026-10-17T01:32:44Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Speculative decoding accelerates large language model (LLM) inference by using a lightweight drafter to propose a block of tokens that the target model verifies in one parallel pass. Autoregressive drafters generate this block one token at a time, whereas block diffusion drafters such as DFlash generate it in one pass, making drafting faster. However, these diffusion drafters predict each token independently, ignoring dependencies between tokens in the block. We introduce FlashMap, a continuous flow drafter that conditions a flow map language model on the target model's hidden states and generates the whole block in one forward pass while capturing inter-token dependencies. On Qwen3-8B, FlashMap is faster than a matched DFlash baseline on every benchmark, with 7% higher average speedup and up to 6.1x lossless acceleration.

Curator note: Needs full text on flow-map proposal generation, AR target verification and a concrete rollout cost/state transfer.

## [Trajectory-Triggered Sparse Collaborative Decoding](https://arxiv.org/abs/2610.23613v1)

- arXiv: `2610.23613` / v1
- Paper updated: 2026-10-16T15:24:05Z
- Source: arXiv API
- Screening status: pending
- Query families: secondary-tail-load

Dense assistance methods such as speculative decoding repeatedly verify draft tokens with a target model, keeping target computation coupled to generation. We study sparse collaborative decoding, where a draft model generates most tokens and a target model is invoked only for short corrective segments. The key problem is deciding when to call the target. We show that local uncertainty is a weak trigger: entropy, negative log-likelihood, logit margin, top-$k$ mass, and velocity features give near-chance failure prediction, with AUC 0.50-0.53. In contrast, aggregate trajectory-shape features over the draft confidence path reach AUC 0.86 using a lightweight logistic predictor trained only from draft correctness labels. This induces a trigger-timing tradeoff: early calls have more leverage but weaker evidence, while later calls have stronger evidence but less ability to redirect the trajectory. Used online, learned sparse collaborative decoding improves over the best open-loop schedule by +5.3 to +20.0 accuracy points across five GSM8K draft-target pairs. On MATH-500, it gains 7.0-13.5 points when early prediction and target competence align, but loses when either is weak. On StrategyQA, it improves over open-loop by 5.0-8.3 points, showing transfer beyond arithmetics.

Curator note: Review whether sparse target interventions preserve any stated target sampling policy. Quality comparisons from collaborative decoding must not be presented as exact token verification.

## [Long-Context Drafting Does Not Require Long-Context Drafters](https://arxiv.org/abs/2610.20865v1)

- arXiv: `2610.20865` / v1
- Paper updated: 2026-10-14T19:54:59Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Speculative decoding pairs a cheap drafter with parallel verification against the target. At ultra-long context it stops paying, because a drafter that attends over the full prefix inherits the target's context-dependent cost, so the speedup it was meant to provide first erodes and then reverses. The standard response is to build a long-context drafter, by training or fine-tuning one, or by using a multi-token-prediction head shipped inside the target checkpoint. We argue this is unnecessary, because the drafters in use are target-conditioned, reading hidden states the target computed over the entire prefix, so distant context already reaches them without their own attention, and verification corrects what they miss. We therefore freeze released short-context drafters and run them far past their training length under two inference-time mechanisms, one bounding the attention cache they see, which fixes their cost, and one re-basing their rotary position indices into the trained range. No weight is touched and the only tunable saturates early, so one vLLM-side configuration spans 4k to two million tokens, costing at most 0.16x of speedup at short length. We prove when a common index shift leaves the drafter's computation exactly unchanged, and decompose acceptance into two measurable gaps with sharp bounds. Whatever speedup a frozen drafter delivers at short context, it retains out to two million tokens, across three target-drafter pairs and five corpora. The claim concerns the flatness rather than the multiple, and removing either mechanism eliminates it. The gain is conditional on the speculative cost per emitted token staying below the matched target-only cost.

Curator note: Official metadata verified; arXiv HTML unavailable (404). Review full text for draft-only long-context state compression and verification semantics.

## [TreeGraft: Adaptive Multi-Drafter Grafting for Tree-Based Speculative Decoding](https://arxiv.org/abs/2608.26112v3)

- arXiv: `2608.26112` / v3
- Paper updated: 2026-10-14T12:28:01Z
- Source: arXiv API
- Screening status: pending
- Query families: secondary-tail-load

Speculative decoding accelerates large language model inference through a draft-then-verify paradigm. Building on this, tree-structured methods improve inference by organizing proposals into multiple candidate paths, increasing the accepted length. However, existing tree-structured methods use a single drafter for all drafting steps, creating a dilemma: a smaller drafter is fast but yields lower-quality trees, whereas a larger drafter improves tree quality but suffers from high latency. To address this, we propose TreeGraft, a multi-drafter framework in which drafters of different costs jointly construct a shared draft tree. TreeGraft uses the stronger drafter to rescore candidates by updating scores assigned by the weaker drafter, reselect grafting positions, and recover promising paths left unexplored. It also integrates stronger drafter expansions non-destructively, preserving existing branches that may still be accepted by the target model. Together, these designs improve the quality of the shared draft tree. To control the drafting cost, TreeGraft introduces a lightweight scheduler distilled from an offline value system to decide when to call the stronger drafter. Across 10 model pairs and 6 benchmarks, TreeGraft outperforms the better of the two fixed single-drafter endpoint strategies by 15.1% on average, reaching a maximum gain of 26.6%. Our code is available at https://github.com/fjm9933/TreeGraft.

Curator note: Review the full multi-drafter tree construction and placement/load cost, and deduplicate any renamed versions by arXiv ID.

## [Draft in Parallel, Condition Through Depth: Adjacent Causal Injection for Speculative Decoding](https://arxiv.org/abs/2609.36173)

- arXiv: `2609.36173` / version not recorded
- Metadata updated: 2026-10-14T08:49:45Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Parallel speculative drafting generates multiple candidates in one backbone pass, but independent token selection can produce inconsistent continuations that shorten the accepted prefix. Existing methods mostly leave conditional decoding to a lightweight module after the backbone, which limits the flow of predecessor information to successors. Our analysis of DFlash shows that early positions already form recoverable predictions in shallow layers, and that accurate adjacent predecessors help successors more when they enter earlier. We therefore propose DSpine, a drafter with causal conditioning injection throughout the backbone: at every layer, gated adjacent injection writes each predecessor's predicted feature into its successor, so the causal conditioning chain unfolds over network depth while all positions update in parallel. A unified transfer space built from the target model's output embeddings unifies layer-wise injection with predecessor-conditioned decoding, and layer-wise output-embedding supervision promotes the formation of predicted features in shallow layers. Fused kernels and a transition cache execute both efficiently in parallel within SGLang. Across seven math, code, and chat benchmarks, DSpine achieves the longest acceptance length at both temperatures on Qwen3-4B and Qwen3-8B. At temperature zero on Qwen3-8B, it raises the seven-benchmark mean from DFlash's 3.77 to 4.82 (+27.8%); in SGLang serving tests, it delivers 23.3% higher throughput than DFlash on average. Project page: https://dspine-project.github.io

Curator note: Needs full-text review of causal-injection overhead and an explicit RL-transfer argument beyond improving draft capacity.

## [Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2606.15007)

- arXiv: `2606.15007` / version not recorded
- Metadata updated: 2026-10-14T08:37:09Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-primary-draft-posttraining

We introduce Nemotron 3 Ultra, a 550 billion total and 55 billion active parameter Mixture-of-Experts Hybrid Mamba-Attention language model. We pre-trained Nemotron 3 Ultra on 20 trillion text tokens, then extended the context length to 1M tokens, and post-trained using Supervised Fine Tuning (SFT), Reinforcement Learning (RL), and Multi-teacher On-Policy Distillation (MOPD). Nemotron 3 Ultra is our most capable model yet, employing multiple key technologies - LatentMoE, Multi Token Prediction (MTP), NVFP4 pre-training, multi-environment RLVR, MOPD, and reasoning budget control. Nemotron 3 Ultra achieves up to ~6x higher inference throughput as compared to state-of-the-art publicly available LLMs while attaining on-par accuracy. The state-of-the-art accuracy, high inference throughput, and 1M token context length make Nemotron 3 Ultra ideal for long-running autonomous agentic tasks. We open-source the base, post-trained, and quantized checkpoints, along with the training data and recipe on HuggingFace.

Curator note: A foundation-model report with agentic reasoning/MTP is not automatically a speculative-rollout study. Locate explicit draft/verify and rollout evidence before assigning a role.

## [Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models](https://arxiv.org/abs/2609.00355v3)

- arXiv: `2609.00355` / v3
- Paper updated: 2026-10-06T14:49:05Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Speculative decoding accelerates generation without changing its output, but on vision-language models (VLMs) a self-reinforcing cycle holds it back. Because an autoregressive drafter pays a sequential pass for each drafted token, it must stay small and can ill afford to attend to the image at each pass. Prior work therefore compresses or hides the image, leaving the drafter weakest on the text the image determines. We present GLANCE, a one-pass block drafter that breaks this cycle on an unmodified VLM target. Its block-diffusion head drafts a whole block in one forward pass over the target's already fused vision-language states, reading the multimodal context once, however deep the draft. The target verifies a wide candidate tree in one pass and commits exactly its greedy output. In one production engine at a fixed round budget, GLANCE decodes up to 3.05 times faster than autoregressive decoding and outpaces the production EAGLE3-VL head on average and by about 11% on grounded tasks. An entropy law explains when drafting pays, predicting the longest accepted blocks on grounded tasks, where the target's next-token entropy is lowest. Our code is available at https://github.com/js-lee-AI/GLANCE.

Curator note: Vision-language inference is not automatically transferable to the text-rollout corpus. Needs an explicit mechanism and scope argument before inclusion.

## [Learning What to Imitate: Entropy-Aware Distribution Mixing](https://arxiv.org/abs/2610.06671v1)

- arXiv: `2610.06671` / v1
- Paper updated: 2026-10-05T16:44:02Z
- Source: arXiv API
- Screening status: pending
- Query families: secondary-tail-load

Small language models are often post-trained as students on reasoning traces from stronger teacher models to efficiently learn new skills. However, token-level imitation on traces that lie far outside the student's expected distribution often produces \textit{confident conflicts}, whereby the student is required to imitate a continuation that it deems unlikely (i.e., low-probability) despite being confident in a different continuation (i.e., in a low-entropy state). To mitigate the degradation in generalisation and catastrophic forgetting caused by these conflicts, we propose \textbf{Entropy-Aware Mixing}: a dynamic per-token interpolation of the student and teacher distributions, gated by the student's predictive entropy. We implement both convex and geometric interpolations for both offline trace generation (via speculative decoding, then SFT) and on-policy forward-KL distillation. Our results show that entropy-aware mixing stabilises distillation, improving in-distribution and out-of-distribution math reasoning while better preserving general capabilities than fixed-teacher supervision. Nonetheless, the optimal entropy schedule depends on the training source, with offline-generated traces favouring concave schedules (greater overall teacher influence) and on-policy training favouring linear or convex schedules (teacher concentrated in high-entropy states).

Curator note: Needs full-text scope review to distinguish distribution-mixing distillation from an actual rollout-compatible proposal or verification mechanism.

## [D-Loop: Looped Diffusion Drafting for Speculative Decoding](https://arxiv.org/abs/2610.06011v1)

- arXiv: `2610.06011` / v1
- Paper updated: 2026-10-05T09:08:24Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Block diffusion accelerates speculative decoding by drafting multiple tokens in one forward pass. However, each position predicts a marginal distribution without observing earlier proposed tokens, limiting draft quality and acceptance length. We identify a concrete failure, the \emph{repetition trap}, in which neighboring positions produce redundant copies of the same token. We explain this tendency theoretically and empirically examine its association with shorter accepted drafts. Recent methods refine marginal predictions with an additional causal head or a separately trained drafter, increasing parameter storage and introducing separate training objectives. We instead propose D-Loop, which introduces \emph{intra-block causal conditioning} within the original diffusion drafter without additional model components. Inspired by semi-autoregressive generation and parameter sharing, D-Loop reuses the same backbone across looped passes. The first pass proposes a block, and the second conditions on a selected prefix to regenerate the suffix in parallel. A complementary prefix--suffix objective trains the shared drafter for both anchor-only prefix prediction and prefix-conditioned suffix prediction. Across eight math, code, and chat benchmarks, D-Loop can beat DFlash and DSpark on Qwen3-4B and Qwen3-8B with obvious gains.

Curator note: Full text retrieved; finish cost/verification and rollout-transfer review. This is D-Loop, a different study from DLoop (2610.07659), not an acronym-based duplicate.

## [From Positionwise Confidence to Prefix Scheduling: Verifier Skipping in Speculative Decoding](https://arxiv.org/abs/2608.14787)

- arXiv: `2608.14787` / version not recorded
- Metadata updated: 2026-10-05T02:49:55Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-tail-load

Speculative decoding is a leading technique to reduce the cost of autoregressive generation by using a small drafter to propose several tokens, which are then verified in parallel by a larger target model. Speculative diffusion decoding (SDD) further removes sequential drafting by generating every position in a draft block in parallel with a discrete diffusion model. However, SDD still invokes the target on every block, leaving verification as a potential bottleneck. This paper recognizes that this creates a new control handle: whether to invoke the verifier at all. Thus, we study verifier skipping, a lossy policy that commits a selected draft prefix directly, and ask which confidence signal should schedule it. Interestingly, our study finds that better token predictors need not yield better schedulers: skips require contiguous high-confidence prefixes, while short skips can induce additional drafting rounds. To study this mismatch, we compare raw confidence with learned marginal and conditional survival scores under the same policy, using Strict SDD, lenience, and top-$k$ acceptance as baselines. On HumanEval with DiffuCoder-7B-Instruct and Qwen3-32B, all three confidence signals save $9.6\%$ to $13.5\%$ of verifier calls at the same observed pass@1 as Strict SDD. Surprisingly, raw confidence saves the most; marginal survival has higher positionwise AUROC than raw confidence at most positions, yet neither learned signal dominates online. Our analysis shows that verifier skipping is a useful new lossy axis and, surprisingly, its key challenge is prefix scheduling rather than token prediction alone.

Curator note: Verify whether skipping changes acceptance semantics or only scheduling. Any approximate output policy must be labeled before inclusion.

## [Recovering Off-Policy Supervision for Speculative Decoding](https://arxiv.org/abs/2609.38795v2)

- arXiv: `2609.38795` / v2
- Paper updated: 2026-10-04T17:01:44Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-primary-sampling-rl, primary-sampling-rl, secondary-tail-load

Block drafters for speculative decoding are commonly trained on corpora written by external models, where a single off-policy token invalidates supervision for all subsequent slots in a block. Existing approaches discard these divergent slots, resulting in severe supervision loss. To resolve this problem while preserving the training corpus, we propose a rollout-based training framework that recovers full supervision through two complementary components. The first component, Anchor-Label Relabelling (ALR), replaces corpus labels with distributions from greedy target rollouts, restoring valid supervision across all predicted slots. The second component, In-Rollout Anchors (IRA), places draft blocks directly inside these rollouts to expose the drafter to target-generated context, reusing precomputed rollout features at no additional target cost. Across fixed vision-language and text corpora, our framework increases greedy accepted length by up to 36.5% over DFlash and consistently outperforms erasing baselines. Notably, a single epoch of our method surpasses the best erase schedules. After three epochs, it matches the acceptance length of training on target-regenerated responses. These results show that our framework provides an effective and compute-efficient approach for training speculative drafters on fixed corpora without modifying the original text. Code is available at https://github.com/js-lee-AI/ALR-IRA.

Curator note: Official abstract verified; HTML unavailable (404). Full-text evidence for off-policy drafter supervision/relabeling is still required; not direct target-policy RL evidence.

## [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting](https://arxiv.org/abs/2606.18394v5)

- arXiv: `2606.18394` / v5
- Paper updated: 2026-10-03T07:00:16Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-verification-parallel, secondary-verification-parallel

Speculative decoding (SD) accelerates autoregressive Large Language Models (LLMs) by drafting multiple tokens and verifying them in parallel, but it faces a scaling limitation: increasing the draft budget improves speed only when acceptance remains high and drafting overhead stays low. This ceiling has been difficult to break because prior head-based SD methods face a causality-efficiency dilemma. Autoregressive drafters produce path-conditioned candidates that are effective for tree speculative decoding with higher acceptance length, but their drafting cost grows with tree depth. Bidirectional block-diffusion drafters generate all positions in one pass, but their branch-agnostic marginals can form individually plausible yet mutually inconsistent trees, wasting budget and reducing acceptance. We propose JetSpec, a head-based SD framework that combines one-forward drafting efficiency with branch-wise causal conditioning. JetSpec trains a causal parallel draft head over fused hidden states from the frozen target model, producing candidate trees whose scores align with the target model's autoregressive factorization. This enables JetSpec to convert larger draft budgets into longer accepted prefixes and higher end-to-end speedup. Across math, coding, and chat benchmarks on dense and MoE Qwen3 models, JetSpec consistently outperforms bidirectional-head and tree-based SD baselines. On H100 GPUs, JetSpec achieves up to 9.64x speedup on MATH-500 and 4.58x on open-ended conversational workloads, with further latency gains demonstrated through vLLM integration under realistic serving loads. Our code and models are available at https://github.com/hao-ai-lab/JetSpec.

Curator note: Identified through the JetSpec++ prior-work path. Consolidate lineage and read the primary JetSpec method/evaluation before adding a separate record.

## [EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures](https://arxiv.org/abs/2610.03394v1)

- arXiv: `2610.03394` / v1
- Paper updated: 2026-10-02T14:43:42Z
- Source: arXiv API
- Screening status: pending
- Query families: datacite-secondary-tail-load, secondary-tail-load

Emerging multi-agent LLMs demand privacy-preserving edge deployment, yet current inference systems struggle with these collaborative workflows. Specifically, the memory-bound decode phase causes severe bus contention on unified memory architectures (UMA), paralyzing naive CPU-GPU co-execution. Furthermore, speculative decoding in multi-agent workloads faces extreme variance in drafting difficulty, alternating between complex reasoning and predictable structured generation. Compounded by frequent tool-induced stalls, this highly fragmented execution severely underutilizes hardware and defeats traditional static batching. We present EdgeAgent, a cross-layer inference system explicitly co-designed for edge UMA and multi-agent workloads. At the micro-architectural level, it bypasses rigid graph-compiler constraints to enable zero-copy UMA-aware tensor parallelism, utilizing asymmetric memory layouts to fully saturate both CPU and GPU compute units. At the scheduling level, it dynamically allocates draft budgets based on real-time sequence predictability to bound bandwidth waste. Concurrently, an asynchronous suspend-and-yield mechanism actively evicts stalled agents, ensuring continuous hardware saturation during unpredictable tool invocations. Extensive evaluations on an Apple M4 SoC demonstrate that the UMA-aware execution alone contributes a 1.29x speedup over batched speculative decoding. Adding the agent-aware scheduling lifts the full EdgeAgent system to a 1.77x speedup under extreme tool-use latencies.

Curator note: Full HTML retrieved; reconcile author/venue metadata and verification assumptions before inclusion. UMA tool-aware inference results do not establish RL training gains.

## [DRelay: Global Draft Context for Prefix-Aware Parallel Speculative Decoding Repair](https://arxiv.org/abs/2610.01439)

- arXiv: `2610.01439` / version not recorded
- Metadata updated: 2026-10-02T03:06:01Z
- Source: DataCite arXiv DOI registry
- Screening status: pending
- Query families: datacite-secondary-verification-parallel

Parallel drafting reduces the drafting overhead of speculative decoding for large language models (LLMs), but its gains remain limited by the accepted prefix length. Even when the correct token is present in the candidate pool, a single early selection error prevents subsequent predictions from being used. We propose DRelay, which uses global information from the entire draft block to perform prefix-aware selective repair of candidate selections before target-model verification. DRelay bases its decisions on candidate correlations and the selected path: a global reader extracts predictive information across positions for each candidate. While a causal selector combines candidate-level information extracted by the global read with the tokens selected at preceding positions to determine whether the native choice at the current position is consistent with the global evidence and the selected prefix. It then decides whether to retain or replace the token, thereby repairing early errors and extending the accepted prefix. We further jointly train the draft backbone and the selector, combining candidate-support learning with a repair objective, while weighting the repair loss according to each block position's potential contribution to the consecutive accepted prefix. Across eight diverse benchmarks on an H800 GPU, DRelay consistently improves both average acceptance length and end-to-end decoding performance over DFlash, Domino, and DSpark. Under SGLang serving, DRelay improves average end-to-end speedup over DFlash, Domino, and DSpark by 14.7%-16.8%, 8.7%-9.3%, and 8.1%-9.3%, respectively.

Curator note: Full HTML retrieved; complete concurrency/correction-cost and rollout-transfer review before promoting this parallel-draft repair method.

