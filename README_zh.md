# LLM强化学习投机解码文献库

[English index](README.md)

本仓库配套综述 *Speculative Decoding for LLM Reinforcement Learning: A Survey of Algorithms, Systems, and Training Semantics*，按论文中的分类整理。

| 一级分支 | 二级维度 |
|---|---|
| Workload-Aware Speculation | Closed-Batch Tail、Workload Recurrence |
| Policy-Aware Speculation | Proposal Source、Proposal Maintenance、Verification Semantics |
| System Co-Design | Scheduling and Mode Selection、Placement and Idle Resources、Memory and Reuse State、Synchronization and Versioning、Parallel and Load-Aware Drafting |

原稿检索截止2026年10月14日，核心46篇，其中直接RL证据21篇、serving迁移研究25篇。最新PDF引用107篇，工作BibTeX共有111条，其余4条以“仅存在于工作文献库”标记。所有记录均有独立文献页和可复制BibTeX。跨分支引用同一研究不重复计数。

相关综述、基础背景、action/observation speculation及数值精度诊断分开存放，不计入46篇技术核心。

## 每周更新

- GitHub Actions每周一北京时间08:17检索arXiv及其DataCite DOI元数据、去重、记录版本变化，并提交候选队列及检索日志。无需个人电脑开机，也不需要付费API密钥。
- 配套的Codex每周复核核查主来源、纳入条件、证据类型和分类，合格后更新正式文献页。此复核依赖配置的本地主机可用。
- 新发现不会直接改写原稿截止日期或核心数量。截止后新增研究单独标识。
- 检索失败会显示失败/不完整，不会伪装成“没有新文献”。候选命中不代表已经纳入。

仓库提供论文官方链接，不重新分发第三方PDF。当前书目信息来自作者工作文献库，导入不意味着每个作者/会议/页码字段均已独立核验。

## 在论文中引用仓库

```latex
\footnote{The companion literature repository is available at
\url{https://github.com/Weigaa/Speculative-Decoding-for-LLM-RL}.}
```

建议放在摘要之外，例如引言贡献段或Literature Search and Selection节。仅在每周流程与分类符合实际时描述为定期维护；不要将关键词候选队列称作已经筛选的正式文献。
