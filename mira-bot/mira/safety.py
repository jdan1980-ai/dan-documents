"""Детерминированная проверка безопасности ДО обращения к модели.

Модель тоже получает инструкции по безопасности, но в критических случаях
ответ не должен зависеть от LLM. ВАЖНО: перед платным запуском проверь и
локализуй номера телефонов под страны своих пользователей."""

import re

CRISIS_PATTERNS = [
    r"kill myself", r"suicid", r"end my life", r"want to die", r"don'?t want to live",
    r"hurt myself", r"self[- ]harm",
    r"покончить с собой", r"суицид", r"хочу умереть", r"не хочу жить",
    r"убить себя", r"причинить себе вред", r"наложить на себя руки",
]

WITHDRAWAL_PATTERNS = [
    r"seizure", r"convuls", r"hallucinat", r"delirium", r"\bdt'?s\b", r"tremors",
    r"судорог", r"галлюцинац", r"белая горячка", r"белой горячк", r"тремор",
    r"руки трясутся", r"трясутся руки", r"трясет все тело",
]

_crisis = re.compile("|".join(CRISIS_PATTERNS))
_withdrawal = re.compile("|".join(WITHDRAWAL_PATTERNS))


def _norm(text: str) -> str:
    return text.lower().replace("ё", "е")


def check(text: str) -> str | None:
    """Возвращает 'crisis', 'withdrawal' или None."""
    t = _norm(text)
    if _crisis.search(t):
        return "crisis"
    if _withdrawal.search(t):
        return "withdrawal"
    return None
