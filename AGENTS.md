# 全局工作约定

- 默认简体中文，简述结果、验证与缺口；持续完成已授权工作，仅关键歧义时提问。小改直接做，复杂任务简要规划。
- 开发、构建、测试优先 WSL Debian，系统操作用原生工具；复用现有环境、登录态和 CLI，按需用 MCP/浏览器。
- 遵循项目 AGENTS.md；UI 按项目规范与个人 Design 执行：优先读 `~/.codex/design/DESIGN.md`，缺失再取 https://github.com/Avlonjune7/Design/blob/main/DESIGN.md 。按任务读规范与技能，不例行联网查更新。
- 先定位再读取，独立只读查询批量执行并限制输出；用 rg、ast-grep、jq/yq/sqlite3，Python 临时工具优先 uv/uvx。需查库文档时优先专用 CLI 或 Context7，不足再查官方文档，来源充分即停止扩搜。
- 当前任务已核实的信息与验证结果复用；相关变化、失败或疑点出现时再查。不例行盘点工具、重读全文或生成过程文档。
- 保留用户修改，按影响与风险完成必要验证及项目要求；改 Shell 用 ShellCheck，改 Actions 用 actionlint，网页交互优先 Playwright CLI。失败先诊断，相关改动后重验。
- GitHub 用 gh，提交推送用 git；操作前核实仓库、分支和登录态，保护凭据；部署遵循授权与项目流程，区分本地和生产结果。
