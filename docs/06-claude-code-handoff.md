# 给本地 Claude Code 的实施说明

本仓库是研究输入，目标是提升已部署 Hermes 的体验；本地工程继续由你开发。不要把上游最新 main 等同于本机版本，也不要批量运行本仓库引用项目的安装器。

## 第一次任务可直接使用的指令

> 阅读本仓库 README 和 docs/02-hermes-baseline.md、docs/04-roadmap.md、docs/05-evaluation.md。先实施 T00：只读核实本机 Hermes 版本、安装方式、入口渠道、主模型、启用的工具/技能/记忆/上下文能力。只读取必要的非秘密配置键，不输出 .env、token、OAuth 凭据或私聊内容。将脱敏结果写入本地 compatibility-report，逐项映射本仓库建议在当前版本是否支持。然后在独立分支与隔离 Hermes profile/数据目录中实施 T01–T03，复用原生机制，逐项改变并建立基线。交付实际产物、检查结果、局限和回滚。不要自动升级生产 Hermes，不覆盖现有技能、记忆或配置，不新增对本地生产服务的自动连接。

以上是用户未来主动交给本地 Claude Code 时的实施范围；本研究室没有执行这些动作。

## 兼容报告必须回答

- 安装来源、版本/commit；本地补丁和工作目录是否干净。
- 主要使用 CLI/TUI、桌面还是 Gateway；本地模型还是 API，token usage 是否可获取。
- 本地是否有 background_review 预算/路由、MemoryProvider、ContextEngine、技能写审批、MCP 工具筛选。
- 各能力对应真实文件、函数或配置项；没有的标缺口，不凭本仓库接口名称硬造兼容层。
- 现有记忆与技能备份/恢复方式；隔离环境如何确保不会写入生产 HOME/profile。
- 上游语义与本地版本的差异；是否只需配置/技能即可解决，确需代码的理由。

## 实施约束

策略 JSON、run record 和 candidate 模板均为研究室自己的格式，不是 Hermes 可直接读取的配置。skill 草案使用标准目录格式，安装前需检查该版本 Hermes 作者规范、工具名称、触发描述与冲突。

不把 Claude 的 `PreToolUse`/`PostToolUse`、`${CLAUDE_PLUGIN_ROOT}`、`.claude/settings.json`、`/compact` 原样塞给 Hermes；Hermes 本次文档使用 `/compress`。以本地命令帮助和代码为准。

新增观察代码先评估原生 usage/日志是否足够。任何 hook 若 best-effort 或异常路径不触发，不能承担唯一持久化/安全门禁。对外部副作用用真实状态与回执验证。

每个 PR 只解决一个可识别问题，说明触发场景、之前/之后行为、测试证据和回滚。优先 targeted regression，再跑该仓库要求的检查；不得用 mocked 格式检查宣称真实 Hermes A/B 通过。

## 回传给研究室的材料

兼容报告、脱敏实验报告、固定版本、场景级指标、最严重失败的最小复现、成本分解、采用/否决原因。私有轨迹留本地，只提交经审阅的脱敏摘要。研究室据此更新方案而非远程接管本地开发。
