# Hermes 能力对照与兼容边界

分析基于 2026-10-12 的固定上游提交，本地能力标记为“待核实”。先做版本映射，再把每项标成：已有可用、已有需调优、版本不具备、确有缺口。

| 体验目标 | 上游已具备的能力 | 优化切入点 | 证据 |
|---|---|---|---|
| 跨会话记住偏好 | MEMORY.md / USER.md、memory 工具、会话开始冻结快照 | 验证真实写入，保留来源、作用域与更正记录；不要靠口头“记住了” | MEMORY |
| 查回旧任务 | SQLite + FTS5 session_search | 建立带精确术语与语义改写的失败场景；先搜索历史再扩张常驻记忆 | MEMORY / ARCH |
| 学到可复用方法 | skill_manage、按需 skills、后台 review | 原生学习已有；补候选审核、失败样本和回归，不建第二套自动写入循环 | SKILLS / MEMORY |
| 长会话不丢关键约束 | 原生压缩、ContextEngine 扩展接口 | 任务交接文件与关键约束保留测试；先调默认引擎，后考虑插件 | CONTEXT |
| 控制后台开销 | auxiliary.background_review 路由、开关与累计输入预算 | 单独统计 review 成本与纠错捕获；异模型冷缓存可能抵消便宜单价 | MEMORY |
| 增加外部记忆 | MemoryProvider 接口、catalog 插件 | 只选择一个外部 provider；内置存储是否同时启用要明确 | PROVIDER |
| 精简 MCP | 原生 per-server 工具筛选、timeout、connect_timeout | 每类任务的最小工具集合，记录 schema 与输出 token 占用 | MCP |
| 失败与恢复 | session 持久化、retry 工具代码、审批与恢复相关模块 | 本地核实取消/恢复语义；外部写入未知结果不自动重放 | ARCH / RETRY |
| 用户控制 | 原生命令审批、隔离、记忆/技能 write_approval | 复用既有确认界面；已授权常规工作不额外重复询问 | SECURITY / MEMORY |
| 项目说明 | .hermes.md、AGENTS.md、CLAUDE.md 等 | 选择一种主项目上下文，保持短且指向资料；不假定全部文件叠加 | FILES |

## 已核实的接口，不是拟造 API

- `agent/memory_provider.py`：MemoryProvider 生命周期、`prefetch`、`sync_turn`、`on_session_switch`、`on_pre_compress`、`on_memory_write` 等；外部 provider 同时只激活一个。插件身份、线程上下文和版本能力声明也需要兼容，不应只实现几个同名函数。
- `agent/context_engine.py`：`should_compress`、`compress`、`select_context`、`on_turn_complete` 等。`select_context` 返回请求用上下文，不得当成持久化会话记录；`on_turn_complete` 为 best-effort，异常退出可能不触发，不能用作唯一审计或事务提交点。
- `agent/session_persistence.py` 是持久化阅读入口，不保证每个外部工具恰好执行一次。恢复后的副作用正确性必须单独测试。

## 会影响真实体验的语义

内置记忆在会话开始作为冻结快照加载，以保护前缀缓存。会话中写入会立刻落盘，但系统提示快照不会同步刷新；工具结果可以显示当前状态。不能为了“立即记住”每轮重写系统提示。

内置记忆满时返回错误，不自动压缩。扩大限额会增加常驻输入；先合并稳定事实、把任务细节移到会话或任务文件，并验证写入结果。

Gateway 重启不一定是新会话。适合在任务完成或自然换题时交接并 `/new`；未完成任务或待审批写入期间不强制重置。每次实际切换都要验证任务、权限和身份隔离。

本次文档的项目上下文选择有优先级，主类型是 first-match，而非无条件把所有 AGENTS/CLAUDE/HERMES 文档拼接。SOUL 单独加载。不要往多个文件放同一份长规则。

同模型后台 review 继承主模型 reasoning effort，单独指定 review effort 不会降低它。改频率、累计预算，或者比较异模型 review 才是本次版本里的有效实验路径。

## 证据索引

- **MEMORY**：[MEMORY](https://github.com/NousResearch/hermes-agent/blob/54b07ec7f16ec077b86847095f84adf1924eca92/website/docs/user-guide/features/memory.md)
- **SKILLS**：[SKILLS](https://github.com/NousResearch/hermes-agent/blob/54b07ec7f16ec077b86847095f84adf1924eca92/website/docs/user-guide/features/skills.md)
- **ARCH**：[ARCH](https://github.com/NousResearch/hermes-agent/blob/54b07ec7f16ec077b86847095f84adf1924eca92/website/docs/developer-guide/architecture.md)
- **CONTEXT**：[CONTEXT](https://github.com/NousResearch/hermes-agent/blob/54b07ec7f16ec077b86847095f84adf1924eca92/agent/context_engine.py)
- **PROVIDER**：[PROVIDER](https://github.com/NousResearch/hermes-agent/blob/54b07ec7f16ec077b86847095f84adf1924eca92/agent/memory_provider.py)
- **MCP**：[MCP](https://github.com/NousResearch/hermes-agent/blob/54b07ec7f16ec077b86847095f84adf1924eca92/website/docs/user-guide/features/mcp.md)
- **RETRY**：[RETRY](https://github.com/NousResearch/hermes-agent/blob/54b07ec7f16ec077b86847095f84adf1924eca92/agent/retry_utils.py)
- **SECURITY**：[SECURITY](https://github.com/NousResearch/hermes-agent/blob/54b07ec7f16ec077b86847095f84adf1924eca92/website/docs/user-guide/security.md)
- **FILES**：[FILES](https://github.com/NousResearch/hermes-agent/blob/54b07ec7f16ec077b86847095f84adf1924eca92/website/docs/user-guide/features/context-files.md)

本仓库未提供自动改写 `~/.hermes` 的脚本；所有扩展路径都需本地 Claude Code 对当前版本复核。
