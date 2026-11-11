---
name: playwright-cli
description: Automate browser interactions, test web pages and work with Playwright tests.
allowed-tools: Bash(playwright-cli:*) Bash(npx playwright:*) Bash(npx --no-install playwright:*)
---

# Playwright CLI

复用现有预览与浏览器会话，验证当前改动；同一流程不切换多个浏览器工具重复执行。需要用户已有登录态时按 browser-skill 的授权流程操作，不提取凭据或关闭用户会话。

- 先依据当前页面与快照定位元素，再执行操作；导航或页面变化后刷新观察，不猜元素引用。
- 局部改动检查影响区域；布局与响应式改动覆盖目标设备，关键操作从真实入口验证到可观察结果。
- 批量截取必要状态并实际查看；DOM 快照不替代视觉验收。等待可观察状态，不用固定长延时。
- 复用相关测试，只在缺少必要回归覆盖时补测试；录屏、追踪、Mock、测试生成按实际诊断需求使用。
- 不例行重装或升级；命令失败先看当前帮助与环境。只清理本任务创建且不再需要的会话。

已知命令直接使用，不预读整个手册；不熟悉的参数先用 `playwright-cli <command> --help`。需示例时在 [命令目录](references/command-catalog.md) 搜索相应命令；复杂能力再读该目录链接的专项参考。
