"""Онбординг как конечный автомат. Чистые функции, чтобы легко тестировать."""

import re
from dataclasses import dataclass, field

TEXT_STEPS = ["name", "baseline", "drink", "triggers", "tried", "motivation"]
HEAVY_WEEKLY_DRINKS = 35  # примерно 5 порций в день


@dataclass
class Result:
    updates: dict = field(default_factory=dict)
    next_step: str | None = None  # None = остаёмся на шаге (ошибка ввода)
    error_key: str | None = None


def handle_text(step: str, text: str) -> Result:
    text = text.strip()
    if step == "name":
        return Result({"name": text[:40]}, "goal")
    if step == "baseline":
        m = re.search(r"\d+(?:[.,]\d+)?", text)
        if not m:
            return Result(error_key="q_baseline_bad")
        value = int(round(float(m.group().replace(",", "."))))
        if value > 500:
            return Result(error_key="q_baseline_bad")
        return Result({"baseline_per_week": value}, "drink")
    if step == "drink":
        return Result({"drink": text[:80]}, "triggers")
    if step == "triggers":
        return Result({"triggers": text[:300]}, "tried")
    if step == "tried":
        return Result({"tried": text[:500]}, "motivation")
    if step == "motivation":
        return Result({"motivation": text[:500]}, "done")
    return Result(error_key="q_baseline_bad")


def is_heavy(baseline_per_week: int | None) -> bool:
    return baseline_per_week is not None and baseline_per_week >= HEAVY_WEEKLY_DRINKS


QUESTION_KEY = {
    "name": "q_name",
    "goal": "q_goal",
    "baseline": "q_baseline",
    "drink": "q_drink",
    "triggers": "q_triggers",
    "tried": "q_tried",
    "motivation": "q_motivation",
}
