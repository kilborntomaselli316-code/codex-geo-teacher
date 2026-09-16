"""CLI entry point: geo-lesson."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from geo_lesson import __version__
from geo_lesson.outline import generate_outline

app = typer.Typer(
    name="geo-lesson",
    help="中国高中地理备课助手（OpenAI / Codex 友好工具包）",
    no_args_is_help=True,
)
console = Console()


def _version_callback(value: bool) -> None:
    if value:
        console.print(f"geo-lesson {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-V",
        callback=_version_callback,
        is_eager=True,
        help="Show version and exit.",
    ),
) -> None:
    """codex-geo-teacher CLI."""


@app.command("outline")
def outline_cmd(
    topic: str = typer.Option(..., "--topic", help="课题，如：地球的圈层结构"),
    grade: str = typer.Option("高一", "--grade", help="年级，如：高一"),
    minutes: int = typer.Option(45, "--minutes", help="课时时长（分钟）"),
    curriculum: str = typer.Option(
        "中图版必修一",
        "--curriculum",
        help="教材版本，如：中图版必修一",
    ),
    lang: str = typer.Option("zh", "--lang", help="输出语言代码，默认 zh"),
    model: str = typer.Option(
        "gpt-4o-mini",
        "--model",
        help="OpenAI 模型名（非 dry-run 时使用）",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="只打印将发送给模型的提示词，不调用 API",
    ),
    out: Optional[Path] = typer.Option(
        None,
        "--out",
        help="将结果写入文件；省略则打印到 stdout",
    ),
) -> None:
    """生成一节地理课的教案大纲（或 dry-run 打印提示词）。"""
    try:
        result = generate_outline(
            topic=topic,
            grade=grade,
            minutes=minutes,
            curriculum=curriculum,
            lang=lang,
            model=model,
            dry_run=dry_run,
        )
    except RuntimeError as exc:
        console.print(f"[red]错误：[/red] {exc}")
        raise typer.Exit(code=1) from exc
    except Exception as exc:  # noqa: BLE001 — surface API/IO errors cleanly
        console.print(f"[red]失败：[/red] {exc}")
        raise typer.Exit(code=1) from exc

    if out is not None:
        out.write_text(result, encoding="utf-8")
        console.print(f"[green]已写入[/green] {out}")
    else:
        console.print(result)


if __name__ == "__main__":
    app()
