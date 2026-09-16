# AGENTS.md — 给 Codex / 自动化代理的说明

## 项目目标

帮助中国高中地理教师用可复现的提示词与课程种子数据准备教案大纲。CLI：`geo-lesson`。

## 必做

- 改代码前先跑：`pip install -e ".[dev]" && pytest`
- 涉及 API 的功能必须保留 `--dry-run`（不调用网络、不需要 Key）
- 新增课题时同步更新 `data/curriculum_seed.json` 与测试
- 提交信息用英文祈使句；不要提交 `.env`、密钥、真实学生数据

## 禁止

- 声称本项目为 OpenAI / Codex「官方」工具或合作产品
- 在文档中粘贴真实 API Key 或把 Key 写进代码
- 编造与中学教材明显冲突的深度/物态「事实」而不加核对提示

## 常用命令

```bash
geo-lesson outline --topic "地球的圈层结构" --grade 高一 --minutes 45 --curriculum 中图版必修一 --lang zh --dry-run
pytest
```

## 包布局

- `src/geo_lesson/` — CLI 与逻辑
- `data/curriculum_seed.json` — 课题与易错点种子
- `prompts/` — 提示词模板
- `tests/` — pytest
