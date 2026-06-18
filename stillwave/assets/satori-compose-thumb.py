#!/usr/bin/env python3
"""
SATORI thumbnail composite — Kanji-Concept Series v4 template.

Layout (matches MUSHIN final v4):
- Background: NanoBanana 16:9 source image (monk on cliff + golden sunrise)
- Text 1: 悟り — IPAMincho cream, vertical tategaki, LEFT side over dark mountain mass
- Text 2: SATORI — Liberation Serif Bold cream, below kanji, same column

Run after dropping the source image at:
  satori-sudden-awakening-source.jpg

Output:
  satori-sudden-awakening-thumb.jpg (1280×720, JPEG quality 92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC = HERE / "satori-sudden-awakening-source.jpg"
OUT = HERE / "satori-sudden-awakening-thumb.jpg"

CANVAS = (1280, 720)

KANJI_FONT = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

CREAM = (245, 234, 210)         # #F5EAD2 — locked StillWave text color
SHADOW = (0, 0, 0, 180)         # dark drop for legibility on mid-tones

# Tategaki kanji block — vertical, left side (over dark mountain area)
KANJI_TEXT = "悟り"
KANJI_SIZE = 95
KANJI_LINE_GAP = 8
KANJI_X = 120                   # horizontal center of the tategaki column
KANJI_Y_TOP = 130               # top of the first character

# Romaji block — bottom-left under the kanji
ROMAJI_TEXT = "SATORI"
ROMAJI_SIZE = 62
ROMAJI_X_CENTER = 120
ROMAJI_Y = 540
ROMAJI_LETTER_SPACING = 3


def load_source() -> Image.Image:
    if not SRC.exists():
        raise SystemExit(
            f"Source image not found: {SRC}\n"
            "Drop the NanoBanana 16:9 SATORI render here, then re-run."
        )
    img = Image.open(SRC).convert("RGB")
    if img.size != CANVAS:
        img = img.resize(CANVAS, Image.LANCZOS)
    return img


def draw_shadow_text(draw: ImageDraw.ImageDraw, xy, text, font, fill, shadow_offset=3):
    x, y = xy
    # Soft shadow for cream-on-mid-tone legibility
    draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=(0, 0, 0))
    draw.text(xy, text, font=font, fill=fill)


def main() -> None:
    bg = load_source()
    draw = ImageDraw.Draw(bg)

    kanji_font = ImageFont.truetype(KANJI_FONT, KANJI_SIZE)
    romaji_font = ImageFont.truetype(ROMAJI_FONT, ROMAJI_SIZE)

    # --- Tategaki kanji ---
    y = KANJI_Y_TOP
    for ch in KANJI_TEXT:
        bbox = kanji_font.getbbox(ch)
        w = bbox[2] - bbox[0]
        x = KANJI_X - w // 2 - bbox[0]
        draw_shadow_text(draw, (x, y), ch, kanji_font, CREAM)
        y += (bbox[3] - bbox[1]) + KANJI_LINE_GAP

    # --- Romaji ---
    advances = []
    for ch in ROMAJI_TEXT:
        bb = romaji_font.getbbox(ch)
        advances.append((ch, bb[2] - bb[0], bb))
    total_w = sum(a[1] for a in advances) + ROMAJI_LETTER_SPACING * (len(advances) - 1)
    x = ROMAJI_X_CENTER - total_w // 2
    for ch, w, bb in advances:
        draw_shadow_text(draw, (x - bb[0], ROMAJI_Y), ch, romaji_font, CREAM)
        x += w + ROMAJI_LETTER_SPACING

    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
