#!/usr/bin/env python3
"""
MAKOTO — 誠 thumbnail composite — Kanji-Concept Series.

Layout:
- Background: NanoBanana 16:9 source (samurai in susuki grass + sunrise)
- Text 1: 誠 — IPAMincho GOLD, large, upper-center over the sunrise sky
- Text 2: MAKOTO — Liberation Serif Bold GOLD, centered below kanji

Gold (#C9A84C) chosen over cream/black: the bright sunrise background
kills black sumi-ink; gold reads over the warm sky and echoes Bushidō honor.
Multi-pass dark shadow for legibility over the bright sun zone.

Run after source image is at:
  makoto-the-last-samurai-source.jpg

Output:
  makoto-the-last-samurai-thumb.jpg (1280×720, JPEG quality 92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC  = HERE / "makoto-the-last-samurai-source.jpg"
OUT  = HERE / "makoto-the-last-samurai-thumb.jpg"

CANVAS = (1280, 720)

KANJI_FONT_PATH  = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

GOLD = (201, 168, 76)   # #C9A84C — warm gold, Bushidō honor

# Single large kanji 誠 — lower-left over dark grass/mist zone
KANJI_TEXT = "誠"
KANJI_SIZE = 120
KANJI_X = 80       # left margin
KANJI_Y = 480      # lower zone over dark grass

# MAKOTO romaji — left-aligned below kanji
ROMAJI_TEXT = "MAKOTO"
ROMAJI_SIZE = 52
ROMAJI_X = 80
ROMAJI_LETTER_SPACING = 4


def load_source() -> Image.Image:
    if not SRC.exists():
        raise SystemExit(
            f"Source image not found: {SRC}\n"
            "Drop the NanoBanana 16:9 MAKOTO render here, then re-run."
        )
    img = Image.open(SRC).convert("RGB")
    if img.size != CANVAS:
        img = img.resize(CANVAS, Image.LANCZOS)
    return img


def draw_with_shadow(draw: ImageDraw.ImageDraw, xy, text, font, fill, shadow_r=4):
    """Multi-pass dark halo for legibility over bright backgrounds."""
    x, y = xy
    for dx in range(-shadow_r, shadow_r + 1):
        for dy in range(-shadow_r, shadow_r + 1):
            if dx == 0 and dy == 0:
                continue
            draw.text((x + dx, y + dy), text, font=font, fill=(0, 0, 0))
    draw.text(xy, text, font=font, fill=fill)


def main() -> None:
    bg = load_source()
    draw = ImageDraw.Draw(bg)

    kanji_font  = ImageFont.truetype(KANJI_FONT_PATH,  KANJI_SIZE)
    romaji_font = ImageFont.truetype(ROMAJI_FONT_PATH, ROMAJI_SIZE)

    # --- 誠 kanji lower-left ---
    bb = kanji_font.getbbox(KANJI_TEXT)
    kx = KANJI_X - bb[0]
    ky = KANJI_Y - bb[1]
    draw_with_shadow(draw, (kx, ky), KANJI_TEXT, kanji_font, GOLD)

    kanji_bottom = KANJI_Y + (bb[3] - bb[1])

    # --- MAKOTO romaji left-aligned below kanji ---
    advances = []
    for ch in ROMAJI_TEXT:
        cbb = romaji_font.getbbox(ch)
        advances.append((ch, cbb[2] - cbb[0], cbb))
    rx = ROMAJI_X
    ry = kanji_bottom + 14

    for ch, w, cbb in advances:
        draw_with_shadow(draw, (rx - cbb[0], ry - cbb[1]), ch, romaji_font, GOLD)
        rx += w + ROMAJI_LETTER_SPACING

    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
