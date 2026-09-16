"""Load and query curriculum seed data."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

# Prefer package-adjacent data/, then repo-root data/ for editable installs.
_CANDIDATE_DATA_DIRS = (
    Path(__file__).resolve().parent.parent.parent / "data",
    Path(__file__).resolve().parent / "data",
)


def curriculum_data_path() -> Path:
    """Return path to curriculum_seed.json."""
    for base in _CANDIDATE_DATA_DIRS:
        path = base / "curriculum_seed.json"
        if path.is_file():
            return path
    raise FileNotFoundError(
        "curriculum_seed.json not found. Expected under repo data/ directory."
    )


@lru_cache(maxsize=1)
def load_curriculum() -> dict[str, Any]:
    """Load curriculum seed JSON once."""
    path = curriculum_data_path()
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def find_topic(topic: str) -> dict[str, Any] | None:
    """Find a topic by id or Chinese name (substring match on name)."""
    data = load_curriculum()
    needle = topic.strip()
    for item in data.get("topics", []):
        if item.get("id") == needle or item.get("name") == needle:
            return item
    for item in data.get("topics", []):
        name = item.get("name", "")
        if needle in name or name in needle:
            return item
    return None


def format_pitfalls(topic_data: dict[str, Any]) -> str:
    """Render pitfalls as bullet text for prompt injection."""
    lines: list[str] = []
    for p in topic_data.get("pitfalls", []):
        lines.append(
            f"- 易错：{p.get('wrong', '')}\n"
            f"  纠正：{p.get('correct', '')}\n"
            f"  提示：{p.get('note', '')}"
        )
    return "\n".join(lines) if lines else "（暂无内置易错点）"
