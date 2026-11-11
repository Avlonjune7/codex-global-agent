# 全局工作约定

- 默认简体中文，先说结果、验证与缺口；持续完成已授权工作，仅关键歧义时提问。
- 开发、构建、测试优先 WSL Debian，系统操作用原生工具；复用现有环境、登录态和 CLI，按需用 MCP/浏览器。
- 遵循项目 AGENTS.md；UI 按 https://github.com/Avlonjune7/Design/blob/main/DESIGN.md 与项目设计规范执行。小改直接做，复杂任务先规划；规范与技能按需读取。
- 先定位再读取：rg、ast-grep、jq/yq/sqlite3；Python 临时工具优先 uv/uvx。库文档优先 Context7 或专用 CLI，再查官方文档。
- 保留用户修改，失败先诊断，按风险完成必要验证；Shell 用 ShellCheck，Actions 用 actionlint，网页交互优先 Playwright CLI。
- GitHub 用 gh，提交推送用 git；核实仓库、分支和登录态，保护凭据；部署遵循授权与项目流程，区分本地和生产结果。
