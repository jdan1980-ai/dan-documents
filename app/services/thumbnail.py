"""Thumbnail analysis: contrast, brightness, hot regions, file weight."""
from __future__ import annotations

import io
from typing import Any

from PIL import Image, ImageStat


YT_RECOMMENDED_MAX_BYTES = 2 * 1024 * 1024  # 2 MB


def analyze_thumbnail(file_bytes: bytes) -> dict[str, Any]:
    """Analyze an uploaded thumbnail image.

    Returns: dimensions, aspect ratio, brightness, contrast, dominant colors,
    file size, readability hints, and an overall score.
    """
    issues: list[str] = []
    tips: list[str] = []
    score = 50

    try:
        img = Image.open(io.BytesIO(file_bytes))
    except Exception as e:
        return {"error": f"Не могу прочитать файл: {e}", "score": 0}

    width, height = img.size
    aspect = width / max(height, 1)
    file_size = len(file_bytes)

    factors: dict[str, Any] = {
        "width": width,
        "height": height,
        "aspect_ratio": round(aspect, 2),
        "file_size_kb": round(file_size / 1024, 1),
        "format": img.format or "unknown",
    }

    if abs(aspect - 16 / 9) < 0.05:
        score += 10
        factors["aspect_ok"] = True
    elif abs(aspect - 9 / 16) < 0.05:
        factors["aspect_ok"] = True
        tips.append("9:16 — для Shorts ок, но для обычных видео стандарт 16:9")
    else:
        score -= 10
        factors["aspect_ok"] = False
        issues.append(f"Соотношение {aspect:.2f}:1 — стандарт YouTube 16:9 (1.78)")

    if width < 1280:
        score -= 10
        issues.append(f"Ширина {width}px меньше рекомендованных 1280px")
    elif width >= 1920:
        score += 5

    if file_size > YT_RECOMMENDED_MAX_BYTES:
        score -= 10
        issues.append(f"Файл {factors['file_size_kb']} KB > 2 MB — YouTube не примет")
    elif file_size < 50 * 1024:
        tips.append(f"Файл {factors['file_size_kb']} KB — очень лёгкий, проверь качество")

    rgb = img.convert("RGB")
    stat = ImageStat.Stat(rgb)
    brightness = sum(stat.mean) / 3
    factors["brightness"] = round(brightness, 1)

    if brightness < 60:
        tips.append(f"Тумбнейл тёмный (яркость {brightness:.0f}) — текст на нём виднее, но в ленте может теряться")
    elif brightness > 200:
        tips.append(f"Тумбнейл очень светлый ({brightness:.0f}) — может выглядеть выцветшим")

    contrast = sum(stat.stddev) / 3
    factors["contrast"] = round(contrast, 1)
    if contrast > 60:
        score += 10
    elif contrast < 35:
        score -= 10
        issues.append(f"Низкий контраст ({contrast:.0f}) — тумбнейл будет «плоским» в ленте")

    small = rgb.resize((320, int(320 / aspect)))
    small_stat = ImageStat.Stat(small)
    small_contrast = sum(small_stat.stddev) / 3
    factors["contrast_at_320px"] = round(small_contrast, 1)
    if small_contrast < 30:
        score -= 5
        issues.append("После уменьшения до 320px контраст просел — текст потеряет читаемость в ленте")

    sample_size = 100
    quantized = rgb.resize((sample_size, sample_size)).quantize(colors=5)
    palette = quantized.getpalette() or []
    color_counts = sorted(quantized.getcolors() or [], reverse=True)
    total_pixels = sample_size * sample_size
    dominant = []
    for count, idx in color_counts[:5]:
        if idx * 3 + 2 < len(palette):
            r, g, b = palette[idx * 3], palette[idx * 3 + 1], palette[idx * 3 + 2]
            dominant.append({"hex": f"#{r:02X}{g:02X}{b:02X}", "rgb": [r, g, b], "share": round(count / total_pixels, 2)})
    factors["dominant_colors"] = dominant

    score = max(0, min(100, score))
    factors["issues"] = issues
    factors["tips"] = tips
    return {"score": score, "factors": factors}
