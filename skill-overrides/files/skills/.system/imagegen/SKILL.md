---
name: imagegen
description: "用户要求生成或编辑位图（照片、插画、素材、设计稿）时使用；常规页面实现、现有 SVG 或代码绘图不触发。"
---

# Image generation

- 普通生成、编辑及透明背景请求直接使用内置 image_gen，不需要 API key；按当前工具参数调用。先查看待编辑的本地图片，明确各参考图角色，保留用户要求不变的内容。
- 提示词只补必要的主体、构图、风格、精确文字和约束。缺少关键输入才询问；多素材用各自提示词，不默认转 CLI。
- 透明输出请求真实透明背景并保留 alpha。查看结果再做有针对性的迭代；不要覆盖用户现有素材，除非已要求替换。
- 预览图直接展示；项目使用的最终图保存到项目内，不能只引用默认生成目录。遵循用户指定输出路径；内置工具没有承诺的保存参数时先生成再复制实际返回的文件。
- CLI/API 仅在用户明确选择或确认时使用。内置失败不自动转收费 API；需要本地 OPENAI_API_KEY，不要求在聊天发送密钥，不修改随附执行脚本。
- 需要复杂提示词与素材示例时读 [prompting.md](references/prompting.md) 或 [sample-prompts.md](references/sample-prompts.md) 的相关部分。
- 用户选择 CLI 后先读 [详细模式与参数边界](references/mode-guide.md) 的 CLI 章节，再按需读 [CLI 用法](references/cli.md)。保留模型选择与切换授权要求，不猜参数。
