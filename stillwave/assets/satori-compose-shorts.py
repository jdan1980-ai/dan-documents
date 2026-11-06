#!/usr/bin/env python3
"""
SATORI Shorts cover composite — 9:16 portrait, Kanji-Concept Series template.

Layout (matches MUSHIN Shorts cover):
- Background: NanoBanana 9:16 source (monk on cliff + sunrise, vertical)
- KANJI (悟り) — IPAMincho cream, LARGE, upper-center
- ROMAJI (SATORI) — Liberation Serif Bold cream, below kanji
- BOTTOM Jobs quote — small, cream, two lines (optional, kept simple)

Run after dropping the 9:16 source at:
  satori-sudden-awakening-shorts-source.jpg

Output:
  satori-sudden-awakening-shorts-cover.jpg (1080×1920, JPEG quality 92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC = HERE / "satori-sudden-awakening-shorts-source.jpg"
OUT = HERE / "satori-sudden-awakening-shorts-cover.jpg"

CANVAS = (1080, 1920)

KANJI_FONT = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
QUOTE_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

CREAM = (245, 234, 210)

KANJI_TEXT = "悟り"
KANJI_SIZE = 380
KANJI_Y = 280       # upper third

ROMAJI_TEXT = "SATORI"
ROMAJI_SIZE = 130
ROMAJI_Y = 720      # below kanji
ROMAJI_LETTER_SPACING = 6

QUOTE_LINES = [
    "Before awakening: mountains are mountains.",
    "During awakening: mountains are not mountains.",
    "After awakening: mountains are mountains again.",
    "— Qingyuan",
]
QUOTE_SIZE = 38
QUOTE_Y = 1520      # bottom area, above Shorts UI safe zone (~150px)
QUOTE_LINE_GAP = 14


def load_source() -> Image.Image:
    if not SRC.exists():
        raise SystemExit(
            f"Source image not found: {SRC}\n"
            "Drop the NanoBanana 9:16 SATORI render here, then re-run."
        )
    img = Image.open(SRC).convert("RGB")
    if img.size != CANVAS:
        img = img.resize(CANVAS, Image.LANCZOS)
    return img


def draw_centered(draw, y, text, font, fill, shadow=4):
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]
    x = (CANVAS[0] - w) // 2 - bbox[0]
    draw.text((x + shadow, y + shadow), text, font=font, fill=(0, 0, 0))
    draw.text((x, y), text, font=font, fill=fill)


def draw_centered_spaced(draw, y, text, font, fill, spacing, shadow=4):
    advances = []
    for ch in text:
        bb = font.getbbox(ch)
        advances.append((ch, bb[2] - bb[0], bb))
    total_w = sum(a[1] for a in advances) + spacing * (len(advances) - 1)
    x = (CANVAS[0] - total_w) // 2
    for ch, w, bb in advances:
        draw.text((x - bb[0] + shadow, y + shadow), ch, font=font, fill=(0, 0, 0))
        draw.text((x - bb[0], y), ch, font=font, fill=fill)
        x += w + spacing


def main() -> None:
    bg = load_source()
    draw = ImageDraw.Draw(bg)

    kanji_font = ImageFont.truetype(KANJI_FONT, KANJI_SIZE)
    romaji_font = ImageFont.truetype(ROMAJI_FONT, ROMAJI_SIZE)
    quote_font = ImageFont.truetype(QUOTE_FONT, QUOTE_SIZE)

    draw_centered(draw, KANJI_Y, KANJI_TEXT, kanji_font, CREAM, shadow=6)
    draw_centered_spaced(draw, ROMAJI_Y, ROMAJI_TEXT, romaji_font, CREAM, ROMAJI_LETTER_SPACING)

    y = QUOTE_Y
    for line in QUOTE_LINES:
        draw_centered(draw, y, line, quote_font, CREAM, shadow=4)
        y += QUOTE_SIZE + QUOTE_LINE_GAP

    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
