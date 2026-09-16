"""Tests for dry-run outline generation and CLI."""

from __future__ import annotations

from typer.testing import CliRunner

from geo_lesson.cli import app
from geo_lesson.outline import build_outline_prompt, generate_outline

runner = CliRunner()


def test_build_outline_prompt_contains_topic_and_pitfalls() -> None:
    prompt = build_outline_prompt(
        topic="地球的圈层结构",
        grade="高一",
        minutes=45,
        curriculum="中图版必修一",
        lang="zh",
    )
    assert "地球的圈层结构" in prompt
    assert "高一" in prompt
    assert "45" in prompt
    assert "莫霍" in prompt or "33" in prompt
    assert "2900" in prompt
    assert "岩石圈" in prompt


def test_generate_outline_dry_run_no_api() -> None:
    text = generate_outline(topic="地球的圈层结构", dry_run=True)
    assert "教案大纲" in text or "课标" in text
    assert "地球的圈层结构" in text


def test_cli_outline_dry_run() -> None:
    result = runner.invoke(
        app,
        [
            "outline",
            "--topic",
            "地球的圈层结构",
            "--grade",
            "高一",
            "--minutes",
            "45",
            "--curriculum",
            "中图版必修一",
            "--lang",
            "zh",
            "--dry-run",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "地球的圈层结构" in result.output
    assert "2900" in result.output or "古登堡" in result.output


def test_cli_outline_dry_run_to_file(tmp_path) -> None:  # type: ignore[no-untyped-def]
    out = tmp_path / "prompt.md"
    result = runner.invoke(
        app,
        [
            "outline",
            "--topic",
            "地球的圈层结构",
            "--dry-run",
            "--out",
            str(out),
        ],
    )
    assert result.exit_code == 0, result.output
    assert out.is_file()
    content = out.read_text(encoding="utf-8")
    assert "地球的圈层结构" in content
