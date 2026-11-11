---
name: astryx
description: "在用户选用 Astryx、项目已依赖 @astryxdesign，或新 React 项目按设计规范选定 Astryx 后，查询组件、主题、模板并实现 UI；不用于给已有非 Astryx 项目自动换库。"
---

# Astryx

基于 [官方 Skill](https://github.com/meta/astryx/blob/main/plugins/astryx/skills/astryx/SKILL.md) 的个人适配版。

遵循个人 DESIGN.md 和项目约束：Astryx 提供已选用项目的视觉基准；Oil UI Pro 仅按需完善业务布局、体验和截图验收。已有非 Astryx 项目不因一般 UI 请求安装本库。开发、构建和 CLI 默认在 WSL Debian 执行。

Astryx, a design system and UI library, is available on this computer.
Use it for UI, components and themes in projects that have selected Astryx.
Its docs, components, templates, and themes are all reachable through `astryx`. Start with `astryx search '<what you need>'`.
Then read `astryx component <Name>` or `astryx docs <topic>`, not the package's files.
In a project, the project's version of Astryx answers automatically.
To build UI, work in a project folder (create one if there is none). Add `@astryxdesign/core` and `@astryxdesign/cli` to a new project or one without `@astryxdesign/core`; to a project that already has `@astryxdesign/core`, add `@astryxdesign/cli` at the same version. Run `astryx init` there and follow the agent docs it writes.
WORKFLOW — start new Astryx pages from a suitable template; local edits reuse the existing page:
1. `astryx build "<idea>"` — names the template to scaffold from and the parts it lacks.
2. `astryx template <name> <path>` — scaffold it; preserve its frame, gap and padding unless business requirements, responsiveness or accessibility require a change; replace the content.
3. `astryx template <Block>` for parts it lacks; `astryx component <Name>` to read props before using one.
Before delivery, prefer Astryx components and tokens; retain necessary semantic HTML and custom CSS without expanding a local edit. Follow the project’s required checks and production build, and inspect the actual desktop/mobile rendering as appropriate. Do not skip engineering checks because a design skill suggests doing so.
If `astryx` is not found, run `npm i -g @astryxdesign/cli` first.

