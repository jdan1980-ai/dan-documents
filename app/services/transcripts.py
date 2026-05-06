"""Fetch video transcripts (free, no API quota)."""
from __future__ import annotations

from collections import Counter
from typing import Any

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

from ..db import cache_get, cache_set


_STOPWORDS_RU = {
    "и", "в", "не", "на", "что", "я", "с", "по", "это", "как", "а", "но",
    "так", "же", "то", "за", "из", "для", "у", "о", "от", "до", "ли",
    "да", "вот", "если", "бы", "был", "была", "было", "есть", "будет",
    "уже", "ещё", "его", "её", "их", "мы", "вы", "они", "он", "она",
    "оно", "мой", "твой", "наш", "ваш", "этот", "тот", "там", "тут",
    "где", "когда", "почему", "зачем", "потом", "сейчас", "только",
}
_STOPWORDS_EN = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "of", "to", "in", "for", "on", "with", "as", "by", "at", "from",
    "and", "or", "but", "if", "so", "than", "that", "this", "these",
    "those", "it", "its", "we", "you", "he", "she", "they", "i",
    "my", "your", "our", "their", "his", "her", "what", "when", "why",
    "how", "where", "do", "does", "did", "have", "has", "had", "will",
    "would", "could", "should", "can", "just", "all", "any", "some",
    "no", "not", "yes", "yeah", "okay", "ok", "like", "really",
}
_STOPWORDS = _STOPWORDS_RU | _STOPWORDS_EN


def get_transcript(video_id: str, languages: list[str] | None = None) -> dict[str, Any] | None:
    languages = languages or ["ru", "en"]
    cache_key = f"transcript:{video_id}:{','.join(languages)}"
    cached = cache_get(cache_key)
    if cached is not None:
        return cached or None

    try:
        items = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    except (NoTranscriptFound, TranscriptsDisabled, VideoUnavailable):
        cache_set(cache_key, "")
        return None
    except Exception:
        return None

    text = " ".join(i["text"] for i in items if i.get("text"))
    result = {
        "video_id": video_id,
        "text": text,
        "segments": items,
        "duration_s": sum(int(i.get("duration", 0)) for i in items),
    }
    cache_set(cache_key, result)
    return result


def top_keywords(text: str, top_n: int = 25) -> list[tuple[str, int]]:
    if not text:
        return []
    words = [
        w.strip(".,!?;:()[]\"'`«»").lower()
        for w in text.split()
    ]
    words = [w for w in words if len(w) >= 4 and w not in _STOPWORDS and w.isalpha()]
    counts = Counter(words)
    return counts.most_common(top_n)
