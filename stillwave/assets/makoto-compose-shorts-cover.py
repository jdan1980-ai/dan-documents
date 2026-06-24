#!/usr/bin/env python3
"""
MAKOTO — 誠 Shorts cover (9:16) — Kanji-Concept Series.

Layout (per Kanji-Concept spec — upper-centre over sun):
- Background: NanoBanana 9:16 source (samurai vertical) cropped to 1080×1920
- Text 1: 誠 — IPAMincho DEEP BLACK sumi-ink, large, upper-centre over the sun
- Text 2: MAKOTO — Liberation Serif Bold CREAM #F5EAD2, centred below kanji

Black kanji reads on the bright sun; cream romaji reads on the warm sky.
Soft white halo around the text gives lift without losing the ink look.

Output: makoto-the-last-samurai-shorts-cover.jpg (1080×1920, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np

HERE = Path(__file__).parent
SRC  = HERE / "makoto-the-last-samurai-shorts-source.jpg"
OUT  = HERE / "makoto-the-last-samurai-shorts-cover.jpg"

CANVAS = (1080, 1920)

KANJI_FONT_PATH  = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

SUMI_BLACK = (12, 10, 8)        # near-black sumi ink
CREAM      = (245, 234, 210)    # #F5EAD2

# 誠 kanji upper-centre over the sun zone
KANJI_TEXT = "誠"
KANJI_SIZE = 460                # big — owns the upper third
KANJI_Y_CENTER = 560            # vertical centre of kanji block

# MAKOTO romaji below kanji
ROMAJI_TEXT           = "MAKOTO"
ROMAJI_SIZE           = 132
ROMAJI_LETTER_SPACING = 14


def load_source() -> Image.Image:
    if not SRC.exists():
        raise SystemExit(
            f"Source image not found: {SRC}\n"
            "Drop the NanoBanana 9:16 MAKOTO render here, then re-run."
        )
    img = Image.open(SRC).convert("RGB")
    sw, sh = img.size
    target_ratio = CANVAS[0] / CANVAS[1]
    src_ratio    = sw / sh
    if src_ratio > target_ratio:
        new_h = CANVAS[1]
        new_w = int(sw * new_h / sh)
    else:
        new_w = CANVAS[0]
        new_h = int(sh * new_w / sw)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - CANVAS[0]) // 2
    top  = (new_h - CANVAS[1]) // 2
    return img.crop((left, top, left + CANVAS[0], top + CANVAS[1]))


def draw_with_halo(base: Image.Image, xy, text, font, fill,
                   halo_color=(255, 255, 255), halo_radius=14, halo_alpha=180):
    """Soft white halo under the glyph for lift over the bright sun."""
    w, h = base.size
    halo_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(halo_layer)
    d.text(xy, text, font=font, fill=(*halo_color, halo_alpha))
    halo_layer = halo_layer.filter(ImageFilter.GaussianBlur(halo_radius))
    base.alpha_composite(halo_layer)

    fill_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(fill_layer).text(xy, text, font=font, fill=(*fill, 255))
    base.alpha_composite(fill_layer)


def main() -> None:
    bg = load_source().convert("RGBA")

    kanji_font  = ImageFont.truetype(KANJI_FONT_PATH,  KANJI_SIZE)
    romaji_font = ImageFont.truetype(ROMAJI_FONT_PATH, ROMAJI_SIZE)

    # 誠 — centred horizontally, vertical centre at KANJI_Y_CENTER
    bb = kanji_font.getbbox(KANJI_TEXT)
    kw = bb[2] - bb[0]
    kh = bb[3] - bb[1]
    kx = (CANVAS[0] - kw) // 2 - bb[0]
    ky = KANJI_Y_CENTER - kh // 2 - bb[1]
    draw_with_halo(bg, (kx, ky), KANJI_TEXT, kanji_font, SUMI_BLACK,
                   halo_color=(255, 255, 255), halo_radius=18, halo_alpha=200)

    kanji_bottom = KANJI_Y_CENTER + kh // 2

    # MAKOTO — centred, tracked letters, below kanji
    advances = []
    for ch in ROMAJI_TEXT:
        cbb = romaji_font.getbbox(ch)
        advances.append((ch, cbb[2] - cbb[0], cbb))
    total_w = sum(w for _, w, _ in advances) + ROMAJI_LETTER_SPACING * (len(advances) - 1)
    rx = (CANVAS[0] - total_w) // 2
    ry = kanji_bottom + 70

    for ch, w, cbb in advances:
        draw_with_halo(bg, (rx - cbb[0], ry - cbb[1]), ch, romaji_font, CREAM,
                       halo_color=(0, 0, 0), halo_radius=8, halo_alpha=160)
        rx += w + ROMAJI_LETTER_SPACING

    bg.convert("RGB").save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
