# 全局工作约定

- 默认简体中文，先说结果、验证与缺口；持续完成已授权工作，仅在关键歧义时提问。
- Windows 本机开发、构建、测试优先 WSL Debian，系统操作用原生工具；复用现有环境、登录态、脚本与 CLI，按需用 MCP/浏览器。下列工具在可用且适用时优先，缺失时用现成替代，不为工具偏好重建环境。
- 遵循项目 AGENTS.md、DESIGN.md；小任务直接实施，复杂任务先规划；规范和技能按任务读取，已读且未变化的内容不重复加载。
- UI 遵循 https://github.com/Avlonjune7/Design/blob/main/DESIGN.md；小组件/表单/微调直接复用现有设计并局部验证；新 React 项目适用时优先 Astryx，已选用项目沿用其组件、主题和模板，Oil UI Pro 按需完善布局与体验；旧项目不自动换库。
- 先定位再读取：文本用 rg，语法结构用 ast-grep，数据用 jq/yq/sqlite3；Python 临时工具优先 uv/uvx。
- Astryx 项目优先用项目版本 CLI 查询组件与模板；其他第三方库文档优先 Context7，不足时查官方文档；遵循专用技能的来源要求。
- 保留用户修改，失败先诊断，按风险验证；Shell 用 ShellCheck，Actions 用 actionlint，网页交互优先 Playwright CLI；设计技能不得省略项目要求的测试与生产构建。
- GitHub 用 gh，提交推送用 git；操作前核实仓库、分支和登录态，不泄露凭据；发布部署遵循授权和项目流程，区分本地与生产结果。
