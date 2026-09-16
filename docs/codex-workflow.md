# Codex / OpenAI 工作流建议

本仓库是**独立开源备课工具**，使用 [OpenAI Python SDK](https://github.com/openai/openai-python) 调用你自己的 API Key。  
**不是** OpenAI 或 Codex 的官方产品，也不构成任何形式的背书。

## 推荐流程

1. **先 dry-run**  
   ```bash
   geo-lesson outline --topic "地球的圈层结构" --dry-run
   ```  
   检查提示词是否含正确易错点与课标约束。

2. **在 Codex / ChatGPT / API 中迭代**  
   - 把 dry-run 输出粘贴到 Codex，或去掉 `--dry-run` 并设置 `OPENAI_API_KEY`。  
   - 用 `prompts/` 下模板做易错点卡、小测卷等变体。

3. **人工审校**  
   深度、物态、专名以现行课标与所用教材为准；模型输出必须由教师把关后再进课堂。

4. **贡献回种子库**  
   新主题的易错点请写入 `data/curriculum_seed.json` 并附测试。

## 与 AGENTS.md 的关系

自动化代理（含 Codex）应优先阅读仓库根目录 `AGENTS.md`，遵守「先 dry-run、不提交密钥、不虚假宣传」规则。
