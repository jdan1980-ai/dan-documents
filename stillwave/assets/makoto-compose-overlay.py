#!/usr/bin/env python3
"""
MAKOTO opening title card overlay — 1920×1080 RGBA PNG.

不動心 (Fudōshin) — The immovable mind.
Samurai Bushidō concept: the mind that does not waver before death.

Format matches satori-sudden-awakening-overlay.png:
- Transparent background
- Lower-left position over dark grass/mist zone
- Line 1: 不 動 心 (spaced kanji, gold)
- Line 2: Fudōshin (italic romaji, gold)
- Line 3: "The immovable mind." (regular, gold)

Color: gold #C9A84C — matches MAKOTO thumbnail (Bushidō honor theme)

In CapCut: drop on video track → blend mode Screen → opacity 100%
Timing: 0:00–0:03 scene + sound only → fade in 2s → hold → fade out by 0:14

Output: makoto-fudoshin-overlay.png
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
OUT  = HERE / "makoto-fudoshin-overlay.png"

CANVAS = (1920, 1080)
GOLD   = (201, 168, 76)    # #C9A84C — warm gold, matches thumbnail

KANJI_FONT_PATH   = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT_PATH  = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
ENGLISH_FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"

KANJI_SIZE   = 96
ROMAJI_SIZE  = 36
ENGLISH_SIZE = 34

# Bottom-left anchor — over dark grass/mist zone for legibility
LEFT_MARGIN = 80
KANJI_Y     = 852
ROMAJI_Y    = KANJI_Y + KANJI_SIZE + 12
ENGLISH_Y   = ROMAJI_Y + ROMAJI_SIZE + 8

# Extra spacing between kanji characters (横書き with air)
KANJI_LETTER_GAP = 18


def draw_spaced(draw, x, y, text, font, fill):
    """Draw text with extra letter spacing."""
    cx = x
    for ch in text:
        bb = font.getbbox(ch)
        draw.text((cx - bb[0], y - bb[1]), ch, font=font, fill=fill)
        cx += (bb[2] - bb[0]) + KANJI_LETTER_GAP


def main():
    img  = Image.new("RGBA", CANVAS, (255, 255, 255, 0))   # fully transparent
    draw = ImageDraw.Draw(img)

    kanji_font   = ImageFont.truetype(KANJI_FONT_PATH,   KANJI_SIZE)
    romaji_font  = ImageFont.truetype(ROMAJI_FONT_PATH,  ROMAJI_SIZE)
    english_font = ImageFont.truetype(ENGLISH_FONT_PATH, ENGLISH_SIZE)

    # Line 1 — 不 動 心 (spaced)
    draw_spaced(draw, LEFT_MARGIN, KANJI_Y, "不動心", kanji_font, GOLD)

    # Line 2 — Fudōshin (italic romaji)
    draw.text((LEFT_MARGIN, ROMAJI_Y), "Fudōshin", font=romaji_font, fill=GOLD)

    # Line 3 — English meaning
    draw.text((LEFT_MARGIN, ENGLISH_Y), "The immovable mind.", font=english_font, fill=GOLD)

    img.save(OUT, "PNG")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
