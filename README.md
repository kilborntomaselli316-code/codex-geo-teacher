# codex-geo-teacher

面向中国高中地理备课的开源工具包：用可复现的提示词模板 + 课程种子数据，生成教案大纲，并可对接 OpenAI API 或在 [Codex](https://openai.com/codex) 等环境中手工迭代。

> **诚实声明**：本项目为社区开源软件，使用官方 [openai](https://pypi.org/project/openai/) Python SDK。**不是** OpenAI / Codex 官方产品，与 OpenAI 无隶属或背书关系。

[English summary](#english-summary) · [MIT License](LICENSE) · [Contributing](CONTRIBUTING.md)

## 功能

- CLI `geo-lesson outline`：按课题 / 年级 / 课时 / 教材生成教案大纲提示词或模型输出
- `--dry-run`：只打印提示词，不调用 API、不需要密钥
- `data/curriculum_seed.json`：内置「地球的圈层结构」等易错点（莫霍面≈33 km、古登堡面≈2900 km、岩石圈≠地壳等）
- `prompts/` + `AGENTS.md` + `docs/codex-workflow.md`：方便 Codex / 代理协作

## 安装

```bash
git clone https://github.com/kilborntomaselli316-code/codex-geo-teacher.git
cd codex-geo-teacher
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## 快速开始（dry-run）

```bash
geo-lesson outline \
  --topic "地球的圈层结构" \
  --grade 高一 \
  --minutes 45 \
  --curriculum 中图版必修一 \
  --lang zh \
  --dry-run
```

写入文件：

```bash
geo-lesson outline --topic "地球的圈层结构" --dry-run --out /tmp/outline-prompt.md
```

## 调用 OpenAI API（可选）

```bash
export OPENAI_API_KEY="sk-..."   # 使用你自己的密钥，切勿提交到 Git
geo-lesson outline --topic "地球的圈层结构" --out lesson.md
```

默认模型为 `gpt-4o-mini`，可用 `--model` 覆盖。费用与配额以你的 OpenAI 账户为准。

## 开发与测试

```bash
pytest
```

CI：GitHub Actions（见 `.github/workflows/ci.yml`）。

## 仓库结构

```
src/geo_lesson/     # Python 包与 CLI
data/               # 课程种子 JSON
prompts/            # 提示词模板
docs/               # Codex 工作流说明
tests/              # pytest
AGENTS.md           # 给自动化代理的约定
```

## English summary

**codex-geo-teacher** is an MIT-licensed CLI for Chinese high-school geography lesson prep. It builds structured prompts from curriculum seed data (pitfalls, goals) and optionally calls the OpenAI API via the official SDK. Use `--dry-run` to inspect prompts without network access. This project is **not** an official OpenAI product.

## License

[MIT](LICENSE)
