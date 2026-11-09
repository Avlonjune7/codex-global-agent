# 全局工作约定

- 默认简体中文，先说结果、验证与缺口；持续完成已授权工作，仅在关键歧义时提问。
- 开发、构建、测试优先 WSL Debian，Windows 操作用原生工具；优先复用项目实现、脚本和 CLI，按需用 MCP、浏览器。
- 遵循项目 AGENTS.md、DESIGN.md；技能按任务选用，按需读取，复用已有信息，避免重复检查、安装和流程。
- 先定位再读取：文本用 rg，语法结构用 ast-grep，数据用 jq/yq/sqlite3；Python 临时工具优先 uv/uvx。
- 第三方库文档优先 Context7，不足时查官方文档；遵循专用技能的来源要求。
- 保留用户修改，失败先诊断，按风险验证；Shell 用 ShellCheck，Actions 用 actionlint，网页交互优先 Playwright CLI。
- GitHub 用 gh，提交推送用 git；操作前核实仓库、分支和登录态，不泄露凭据；发布部署遵循授权和项目流程，区分本地与生产结果。
