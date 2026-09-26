#!/usr/bin/env python3
"""
SATORI opening title card overlay — 1920×1080 RGBA PNG.

Format matches healing-hour-963hz-tenchi-ichinyo-overlay.png:
- Transparent background
- Lower-left position
- Line 1: kanji large, gold
- Line 2: romaji italic, gold smaller
- Line 3: English meaning, gold regular

In CapCut: drop on video track → blend mode Screen → opacity 100%
Timing: 0:00–0:03 no text; 0:03–0:05 fade in; 0:05–0:13 hold; 0:13–0:16 fade out

Output: satori-sudden-awakening-overlay.png
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
OUT = HERE / "satori-sudden-awakening-overlay.png"

CANVAS = (1920, 1080)
GOLD = (201, 168, 76)        # #C9A84C — warm gold, matches 963Hz overlay

KANJI_FONT_PATH  = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
ENGLISH_FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"

KANJI_SIZE   = 96
ROMAJI_SIZE  = 36
ENGLISH_SIZE = 36

# Bottom-left anchor — over the dark rock area for max legibility
LEFT_MARGIN = 80
KANJI_Y     = 852
ROMAJI_Y    = KANJI_Y + KANJI_SIZE + 12
ENGLISH_Y   = ROMAJI_Y + ROMAJI_SIZE + 8

# Kanji spacing (横書き with air between characters)
KANJI_LETTER_GAP = 14


def draw_spaced(draw, x, y, text, font, fill):
    """Draw text with extra letter spacing."""
    cx = x
    for ch in text:
        bb = font.getbbox(ch)
        draw.text((cx - bb[0], y - bb[1]), ch, font=font, fill=fill)
        cx += (bb[2] - bb[0]) + KANJI_LETTER_GAP


def main():
    img = Image.new("RGBA", CANVAS, (255, 255, 255, 0))   # fully transparent
    draw = ImageDraw.Draw(img)

    kanji_font   = ImageFont.truetype(KANJI_FONT_PATH,  KANJI_SIZE)
    romaji_font  = ImageFont.truetype(ROMAJI_FONT_PATH, ROMAJI_SIZE)
    english_font = ImageFont.truetype(ENGLISH_FONT_PATH, ENGLISH_SIZE)

    # Line 1 — 見 性 成 仏 (spaced kanji)
    draw_spaced(draw, LEFT_MARGIN, KANJI_Y, "見性成仏", kanji_font, GOLD)

    # Line 2 — Kenshō Jōbutsu (italic romaji)
    draw.text((LEFT_MARGIN, ROMAJI_Y), "Kenshō Jōbutsu", font=romaji_font, fill=GOLD)

    # Line 3 — English meaning
    draw.text((LEFT_MARGIN, ENGLISH_Y), "See your nature. Become Buddha.", font=english_font, fill=GOLD)

    img.save(OUT, "PNG")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
