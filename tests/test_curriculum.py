"""Tests for curriculum seed loading."""

from __future__ import annotations

from geo_lesson.curriculum import find_topic, format_pitfalls, load_curriculum


def test_load_curriculum_has_earth_spheres() -> None:
    data = load_curriculum()
    assert data.get("curriculum") == "中图版必修一"
    topics = data.get("topics") or []
    assert any(t.get("id") == "earth-spheres" for t in topics)


def test_find_topic_by_name() -> None:
    topic = find_topic("地球的圈层结构")
    assert topic is not None
    assert topic["id"] == "earth-spheres"
    ids = {p["id"] for p in topic["pitfalls"]}
    assert "moho-depth" in ids
    assert "gutenberg-depth" in ids
    assert "lithosphere-vs-crust" in ids


def test_pitfalls_mention_key_depths() -> None:
    topic = find_topic("earth-spheres")
    assert topic is not None
    text = format_pitfalls(topic)
    assert "33" in text
    assert "2900" in text
    assert "岩石圈" in text
