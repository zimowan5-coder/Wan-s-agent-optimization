# 原创技能草案

三个草案参考本次 Agent Skills 格式与 Hermes house authoring section order。仅两个必需元数据字段，描述不超过60字符。正文用 Hermes 工具能力表述，不依赖 Claude hooks 或虚构命令。

这些是 proposed 研究产物，未安装、未通过真实 Hermes 场景评测。先在隔离环境试验单个技能；不全量写入 `~/.hermes/skills`。本地当前版本可能另有规范，安装前复核。

- evidence-delivery：复杂任务交付前核对产物与完成声明。
- task-continuity：长任务在压缩、换会话或恢复前保存最小交接。
- scoped-learning：把纠错转为有范围和来源的学习候选。
