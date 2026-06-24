#!/usr/bin/env python3
"""
MAKOTO — 誠 Shorts cover (9:16) — Kanji-Concept Series.

Layout (mirrors long-form thumb style):
- Background: NanoBanana 9:16 source (samurai vertical) cropped/resized to 1080x1920
- Text 1: 誠 — IPAMincho GOLD, lower-left over dark grass/mist zone
- Text 2: MAKOTO — Liberation Serif Bold GOLD, below kanji

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

GOLD = (201, 168, 76)   # #C9A84C

# 誠 kanji lower-left (proportional to long-form: 120px on 720h → 180px on 1920h)
KANJI_TEXT = "誠"
KANJI_SIZE = 180
KANJI_X    = 80
KANJI_Y    = 1480       # lower-left over dark grass zone

# MAKOTO romaji
ROMAJI_TEXT           = "MAKOTO"
ROMAJI_SIZE           = 78
ROMAJI_X              = 80
ROMAJI_LETTER_SPACING = 5


def load_source() -> Image.Image:
    if not SRC.exists():
        raise SystemExit(
            f"Source image not found: {SRC}\n"
            "Drop the NanoBanana 9:16 MAKOTO render here, then re-run."
        )
    img = Image.open(SRC).convert("RGB")
    # Cover-fit: scale to fill 1080x1920, centre-crop
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


def draw_with_shadow(draw, xy, text, font, fill, shadow_r=5):
    x, y = xy
    for dx in range(-shadow_r, shadow_r + 1):
        for dy in range(-shadow_r, shadow_r + 1):
            if dx == 0 and dy == 0:
                continue
            draw.text((x + dx, y + dy), text, font=font, fill=(0, 0, 0))
    draw.text(xy, text, font=font, fill=fill)


def darken_corner(bg: Image.Image) -> Image.Image:
    """Soft radial darken on lower-left so gold text reads cleanly."""
    w, h = bg.size
    cx, cy = 240, 1700           # darkness anchor inside text zone
    radius = 880                 # falloff radius
    ys, xs = np.mgrid[0:h, 0:w]
    dist = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2) / radius
    strength = np.clip(1.0 - dist, 0, 1) ** 1.4
    alpha = (strength * 165).astype(np.uint8)     # peak ~65% black
    veil = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    veil_arr = np.array(veil)
    veil_arr[:, :, 3] = alpha
    veil = Image.fromarray(veil_arr, "RGBA").filter(ImageFilter.GaussianBlur(40))
    bg = bg.convert("RGBA")
    bg.alpha_composite(veil)
    return bg.convert("RGB")


def main() -> None:
    bg = load_source()
    bg = darken_corner(bg)
    draw = ImageDraw.Draw(bg)

    kanji_font  = ImageFont.truetype(KANJI_FONT_PATH,  KANJI_SIZE)
    romaji_font = ImageFont.truetype(ROMAJI_FONT_PATH, ROMAJI_SIZE)

    # 誠 kanji lower-left
    bb = kanji_font.getbbox(KANJI_TEXT)
    kx = KANJI_X - bb[0]
    ky = KANJI_Y - bb[1]
    draw_with_shadow(draw, (kx, ky), KANJI_TEXT, kanji_font, GOLD)

    kanji_bottom = KANJI_Y + (bb[3] - bb[1])

    # MAKOTO romaji below kanji, tracked letters
    rx = ROMAJI_X
    ry = kanji_bottom + 22
    for ch in ROMAJI_TEXT:
        cbb = romaji_font.getbbox(ch)
        w = cbb[2] - cbb[0]
        draw_with_shadow(draw, (rx - cbb[0], ry - cbb[1]),
                         ch, romaji_font, GOLD)
        rx += w + ROMAJI_LETTER_SPACING

    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
