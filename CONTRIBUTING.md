# 贡献指南

感谢关注 **codex-geo-teacher**。欢迎通过 Issue / PR 改进提示词、种子数据与 CLI。

## 开发环境

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## 贡献类型（优先）

1. 为 `data/curriculum_seed.json` 增加课题与**有依据的**易错点
2. 改进 `prompts/` 模板的可操作性与课标对齐
3. CLI / 测试 / 文档的缺陷修复

## PR 要求

- 本地 `pytest` 通过
- 不提交密钥、`.env`、个人隐私或未授权教材全文扫描件
- 不要在 README 中暗示本项目为 OpenAI 官方工具
- 一个 PR 尽量只做一件事；说明「为什么」而非只罗列文件名

## 行为准则

友善、就事论事。争议请开 Issue 讨论后再改代码。
