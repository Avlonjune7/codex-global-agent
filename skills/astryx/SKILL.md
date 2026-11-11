---
name: astryx
description: "用于已选用 Astryx 或依赖 @astryxdesign 的项目，查询组件、主题、模板并实现 UI；不自动迁移其他项目。"
---

# Astryx

基于 [官方 Skill](https://github.com/meta/astryx/blob/main/plugins/astryx/skills/astryx/SKILL.md) 的个人适配版。遵循个人及项目设计规范，WSL Debian 为默认开发环境。

## 查询与实现

- 已知组件先用 `astryx component Button --props`；多个组件一次查，如 `astryx component Button Badge --props`。需要示例再去掉 `--props`，需求不明确才 `astryx search '<需求>'`；主题等规则用 `astryx docs <topic>`。
- 项目中的 CLI 自动优先项目版本。已读文档且版本未变时复用，不重复列目录、查版本或读取整个包源码。
- 新页面先 `astryx build "<需求>"` 选模板，再 `astryx template <name> <path>`；缺少的区块按需查询。沿用主题、排版与间距，仅按业务、响应式、可访问性需要调整；局部修改复用当前页面。
- 组件和设计变量优先，保留必要的语义 HTML 与自定义 CSS。Oil UI Pro 按需完善布局和体验，不重做 Astryx 视觉体系。

## 接入与验证

- 只给已选定 Astryx 的项目安装依赖；CLI 与 core 使用匹配版本，加入所选主题及 peer dependencies。`astryx init` 后审查修改，不覆盖原有工程规则。
- 找不到命令先检查现有安装和 PATH；确认缺失再安装 `@astryxdesign/cli`。普通开发任务不例行升级或重装环境。
- 按项目要求完成检查和生产构建，按改动范围查看实际画面与交互。复用预览和已通过的验证，不重复无关全站检查；未验证部分如实说明。
