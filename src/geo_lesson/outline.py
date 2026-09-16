"""Build lesson-outline prompts and optionally call OpenAI."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from geo_lesson.curriculum import find_topic, format_pitfalls, load_curriculum

_PROMPTS_DIRS = (
    Path(__file__).resolve().parent.parent.parent / "prompts",
    Path(__file__).resolve().parent / "prompts",
)


def prompts_dir() -> Path:
    for base in _PROMPTS_DIRS:
        if base.is_dir():
            return base
    raise FileNotFoundError("prompts/ directory not found")


def load_prompt_template(name: str = "outline_zh.md") -> str:
    path = prompts_dir() / name
    if not path.is_file():
        raise FileNotFoundError(f"Prompt template not found: {path}")
    return path.read_text(encoding="utf-8")


def build_outline_prompt(
    *,
    topic: str,
    grade: str = "高一",
    minutes: int = 45,
    curriculum: str = "中图版必修一",
    lang: str = "zh",
) -> str:
    """Assemble the full user prompt for a lesson outline."""
    seed = load_curriculum()
    topic_data = find_topic(topic)
    pitfalls = format_pitfalls(topic_data) if topic_data else "（种子库中暂无该主题，请据课标自行把关）"
    goals = ""
    if topic_data:
        goals = "\n".join(f"- {g}" for g in topic_data.get("learning_goals", []))
    else:
        goals = "（请根据课标与教材自行拟定）"

    template = load_prompt_template("outline_zh.md" if lang.startswith("zh") else "outline_zh.md")
    return template.format(
        topic=topic,
        grade=grade,
        minutes=minutes,
        curriculum=curriculum or seed.get("curriculum", "中图版必修一"),
        learning_goals=goals,
        pitfalls=pitfalls,
        topic_id=topic_data.get("id", "unknown") if topic_data else "unknown",
    )


def generate_outline(
    *,
    topic: str,
    grade: str = "高一",
    minutes: int = 45,
    curriculum: str = "中图版必修一",
    lang: str = "zh",
    model: str = "gpt-4o-mini",
    dry_run: bool = False,
) -> str:
    """Return prompt (dry-run) or model completion text."""
    prompt = build_outline_prompt(
        topic=topic,
        grade=grade,
        minutes=minutes,
        curriculum=curriculum,
        lang=lang,
    )
    if dry_run:
        return prompt

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Export it or use --dry-run to print the prompt only."
        )

    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "你是一位熟悉中国高中地理课程标准的备课助手。"
                    "输出结构清晰、可直接用于课堂的教案大纲。"
                    "不编造与教材/课标明显冲突的数值；不确定处请标明。"
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
    )
    choice = response.choices[0].message.content
    return choice or ""
