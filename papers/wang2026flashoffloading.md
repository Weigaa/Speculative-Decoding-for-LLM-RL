# FlashOffloading

**FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving**

- Citation key: `wang2026flashoffloading`
- Authors: Wang, Xuan and Wu, Zhuanhao and Fang, Tingzhu and Li, Xushi and Zhang, Sicheng and Yang, Zhenyu and Liu, Feng and Fan, Zhaohui and Xie, Qiang and Zou, Huayi and Liu, Yuncong and Song, Zeyu and Zhu, Ke and Zeng, Yanjia and Gao, Jingchun and Shi, Yan and Luo, Kui and Li, Gezi and Feng, Liangjun and Li, Cheng
- Year: 2026
- Bibliographic venue: arXiv preprint
- Source: [paper](https://arxiv.org/abs/2611.07542v1)
- Evidence setting: **Background / related survey / infrastructure**
- Library role: `background`
- Cited in the manuscript PDF: no (screened library addition)
- Reviewed arXiv version: v1

## Mechanism / relevance

Overlaps host KV transfers with computation using rolling prefill and hot decode caches.

## Evidence and transfer boundary

Supporting inference infrastructure. GLM-5.2 on Ascend910C with MTP3 enabled in all decode arms. Offload gains are not isolated gains from speculative decoding. Useful for discussing the memory and transfer costs of long-context rollouts.

## Taxonomy dimensions

Outside the core taxonomy.

## Source and artifact record

- Metadata provenance: Official arXiv metadata and full text checked on 2026-11-08. Discovery used the recorded query families and author-supplied FlexFloor link.
- Evidence pointer: Sections 3–6
- Source publication date: 2026-11-05
- Released code: not recorded (not a claim of non-availability)
- Artifact checks: not independently checked in this library

## BibTeX

```bibtex
@article{wang2026flashoffloading,
  author = {Wang, Xuan and Wu, Zhuanhao and Fang, Tingzhu and Li, Xushi and Zhang, Sicheng and Yang, Zhenyu and Liu, Feng and Fan, Zhaohui and Xie, Qiang and Zou, Huayi and Liu, Yuncong and Song, Zeyu and Zhu, Ke and Zeng, Yanjia and Gao, Jingchun and Shi, Yan and Luo, Kui and Li, Gezi and Feng, Liangjun and Li, Cheng},
  title = {{FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving}},
  journal = {arXiv preprint arXiv:2611.07542},
  year = {2026},
  eprint = {2611.07542},
  archivePrefix = {arXiv}
}
```

[Back to all records](../docs/all-papers.md)
