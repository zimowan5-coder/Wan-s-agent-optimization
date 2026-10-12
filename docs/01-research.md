# 项目研究与取舍

## 研究方法和范围

从截图中的 Superpowers、Matt Pocock Skills、ECC、Hermes 出发，扩展检索 GitHub 的记忆、上下文工程、Hermes 优化主题，再沿官方文档和相关项目补齐评测、工具协议、可靠执行、模型路由、观测和浏览器能力。检索词与筛选理由存于 `research/discovery.json`。共读取 21 个仓库名称对应的元数据与固定提交 README，ECC 的旧名称重定向后去重为 20 个项目，并对重点来源读取代码/文档。

这是有明确范围的第一轮研究，不是全量市场覆盖或所有仓库的代码安全审计。stars 只用于发现候选，不作为效果证据。README 的能力和成绩属于项目方陈述；代码接口核对也不等于运行验证。推荐为本研究室的设计判断。

## 精华如何进入 Hermes

| 项目与固定证据 | 采用定位 | 取其精华 | 不直接搬运的部分 |
|---|---|---|---|
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent/blob/54b07ec7f16ec077b86847095f84adf1924eca92/README.md) | 原生能力基线 | 原生记忆、技能、FTS5 会话搜索、压缩、MCP、插件优先复用 | 不重写 agent loop；最新 main 不代表本地版本 |
| [obra/superpowers](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/README.md) | 重点方法参考 | 调试先定位根因；交付前验证；复杂开发先写计划 | 不把所有请求变成设计访谈、TDD 或多代理任务；主要服务本地开发 |
| [mattpocock/skills](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/README.md) | 重点方法参考 | 需求变成可验收任务；交接文档引用已有产物；回复简明 | 不照搬密集提问风格；用户已明确的约束不再询问 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC/blob/b92f181b3b748d1abbc2afd94af6aa7d8c8fca29/README.md) | 重点方法参考 | 项目作用域的纠错经验、按阶段压缩、评测循环、宿主兼容检查 | Claude hooks 和变量不能直接在 Hermes 执行；不全量安装 |
| [agentskills/agentskills](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/README.md) | 格式依据 | 技能只暴露元数据，触发后加载正文，支持文件按需读取 | 通用规范上限不等于 Hermes 作者规范；格式兼容不代表工具兼容 |
| [anthropics/skills](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/README.md) | 选择性样例 | 以任务为中心的技能、说明与资源分离 | 文档类技能存在独立许可证；逐项核对，不批量复制 |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/README.md) | 设计参考 | 将系统提示、记忆、工具描述和结果一起计入上下文预算 | 只借鉴与当前失败样本相关的方法；不预装整套目录 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph/blob/10f1fabb3b2f2d550b8133fba1217391c27694c4/README.md) | 可靠性参考 | 持久执行、检查点、人类介入；学习恢复语义 | 不迁移 Hermes 到 LangGraph；恢复不能等同于重复执行外部写入 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python/blob/125efa029b4bfd84238bd2c4fd69c3406f802663/README.md) | 架构参考 | session、handoff、tracing 的明确边界 | 不替换 Hermes 主运行时，不默认开启多代理 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0/blob/d26ba5e4518cef7fff3c66d4f715b21adf9feabe/README.md) | 条件候选 | 语义召回与独立记忆层；Hermes 已有 catalog 集成路径 | 仅原生召回不足时比较；托管平台成绩不能算 OSS 或 Hermes 收益 |
| [plastic-labs/honcho](https://github.com/plastic-labs/honcho/blob/3922af856d78ec41133916deec4d821fa9c5a92e/README.md) | 条件候选 | 变化中的用户与项目建模；已有 Hermes 集成 | 不是所有用户都需要后台推断；考虑延迟、模型成本和 AGPL 服务边界 |
| [letta-ai/letta](https://github.com/letta-ai/letta/blob/5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a/README.md) | 历史与边界参考 | 有状态代理与持久记忆思路 | 当前 README 指向 letta-code；不推荐旧 V1 服务为新依赖，未深审新运行时 |
| [langfuse/langfuse](https://github.com/langfuse/langfuse/blob/5d866bbe7a65522d209124348e53f9efd73dcc7c/README.md) | 条件候选 | 调用轨迹、成本、数据集与评测反馈关联 | 先本地 JSONL；出现检索与跨实验需求后再接，区分 MIT 核心和企业目录 |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo/blob/129cdb7ca768de316f0cb86cebc60b0db457b132/README.md) | 评测参考/候选 | 声明式场景、模型对照与对抗输入测试 | 全链路需 Hermes 适配器，单个提示词评测不能代表工具任务成功 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm/blob/f516668f96f9891510640b62a0216adb229bbcb9/README.md) | 条件候选 | 成本跟踪、路由、有限重试与降级 | 先用 Hermes 原生 provider；新增网关多一层故障点，企业功能另有许可 |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk/blob/c9356a2a8fb805ac2202e44c05371cf005edc923/README.md) | 协议依据 | MCP 客户端/服务端的标准生命周期 | Hermes 已支持 MCP，不重复写协议层，重点控制工具暴露与超时 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use/blob/c75e8476e26d18b7617643bc2ae082fae8eae431/README.md) | 专项候选 | 浏览器任务执行能力与专门场景评测 | 只用于实际浏览器失败场景；Hermes 已有浏览器能力，避免双栈 |
| [All-Hands-AI/OpenHands](https://github.com/OpenHands/OpenHands/blob/02e02ae0c92ebb033afcf2fb399bd3683df82ca8/README.md) | 开发边界参考 | 开发执行环境与沙箱的分离 | 当前仓库已重定向 OpenHands/OpenHands；不取代本地 Claude Code |
| [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution/blob/0a929e3aa20e15cf04dc7c28492a7d41a5139125/README.md) | 后期优先候选 | 官方 DSPy/GEPA 技能优化，独立训练/验证/holdout | README 只有技能阶段已实现；测试门禁在代码中需显式 --run-tests |
| [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes/blob/65c31d6a240a443750e35cafabf6f55aedda5aa2/README.md) | 同类方案参考 | Hermes 之上的工作流与证据边界、编码交接 | 未审计安装器或运行插件；不宣称兼容或收益，借鉴轻量组件即可 |

## 三个容易误判的地方

1. ECC 与 `everything-claude-code` 在本次请求中落到相同提交、相同规范 URL，应算一个来源。Claude Code 的 hooks、目录和插值变量要转换为 Hermes 实际接口。
2. Hermes Self-Evolution 的 README 描述完整愿景，但工具描述、系统提示、代码与连续进化阶段仍是 Planned。技能入口代码的 `run_tests` 默认为 false，必须显式启用测试；“项目有 guardrails”不代表每次调用默认执行所有门禁。
3. Mem0 本次 README 明确区分托管平台专有优化与开源 SDK。任何第三方 benchmark、成本倍率、宣传性“提升”都不能直接写成本地 Hermes 的效果。

## 许可证与复用方式

本仓库以原创分析、链接和原创模板为主，不复制第三方技能全文或安装器。`sources.json` 的 license 来自 GitHub 元数据，可能缺失或粗略，不能替代文件级核实。

- Agent Skills：代码 Apache-2.0，文档 CC-BY-4.0。
- Anthropic Skills：混合许可，文档技能有特殊条款，逐目录核对。
- Honcho：元数据 AGPL-3.0；服务/API 使用与复制修改服务源码需分别评估。
- Langfuse、LiteLLM：已读根 LICENSE，开源核心 MIT，指定企业目录使用单独条款。
- Hermes Self-Evolution：README 声称 MIT，本次根 LICENSE 路径返回 404、GitHub license 为空；只作方法参考，代码复用前查明许可。

## 首选组合

第一阶段只用 Hermes 原生记忆、会话搜索、压缩、技能和工具选择，辅以本仓库的轻量任务/交接/证据约定。第二阶段按真实失败数据调预算与学习治理。第三阶段按需选择一个外部能力，不同时叠加 Mem0、Honcho、Letta，也不同时导入多个工作流总包。

证据：[技能优化入口代码](https://github.com/NousResearch/hermes-agent-self-evolution/blob/0a929e3aa20e15cf04dc7c28492a7d41a5139125/evolution/skills/evolve_skill.py)；[Agent Skills 格式规范](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/specification.mdx)；[Langfuse 许可](https://github.com/langfuse/langfuse/blob/5d866bbe7a65522d209124348e53f9efd73dcc7c/LICENSE)；[LiteLLM 许可](https://github.com/BerriAI/litellm/blob/f516668f96f9891510640b62a0216adb229bbcb9/LICENSE)。
