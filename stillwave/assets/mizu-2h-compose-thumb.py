#!/usr/bin/env python3
"""
MIZU — 水 | long-form thumbnail compose (1280x720).

Kanji-Concept layout: 水 LARGE upper-center + MIZU romaji below, white with a
soft shadow, over a soft radial darkening so the text pops on the bright morning
koi-pond image. Lower-right kept clear for the logo.

Source: mizu-2h-source.jpg (koi pond, bamboo spout, morning light)
Output: mizu-2h-thumb.jpg (1280x720, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).parent
SRC = HERE / "mizu-2h-source.jpg"
OUT = HERE / "mizu-2h-thumb.jpg"

W, H = 1280, 720
WHITE = (250, 250, 248)
SHADOW = (0, 0, 0, 160)

KANJI_FONT = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

KANJI = "水"
KANJI_SIZE = 330
KANJI_Y = 48

ROMAJI = "MIZU"
ROMAJI_SIZE = 132
ROMAJI_Y = 402
ROMAJI_SPACING = 12


def fit_cover(img):
    sw, sh = img.size
    target = W / H
    if sw / sh > target:
        nw = int(sh * target)
        img = img.crop(((sw - nw) // 2, 0, (sw + nw) // 2, sh))
    else:
        nh = int(sw / target)
        img = img.crop((0, (sh - nh) // 2, sw, (sh + nh) // 2))
    return img.resize((W, H), Image.LANCZOS)


def darken_behind(bg):
    """Soft radial darkening centered on the upper-center text zone."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    cx, cy = W // 2, 300
    rx, ry = 560, 340
    d.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=(0, 0, 0, 135))
    layer = layer.filter(ImageFilter.GaussianBlur(70))
    return Image.alpha_composite(bg.convert("RGBA"), layer).convert("RGB")


def draw_center(d, y, text, font, spacing):
    total = d.textlength(text, font=font) + spacing * (len(text) - 1)
    x = (W - total) / 2
    for ch in text:
        d.text((x + 4, y + 4), ch, font=font, fill=SHADOW)
        d.text((x, y), ch, font=font, fill=WHITE)
        x += d.textlength(ch, font=font) + spacing


def main():
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")

    bg = fit_cover(Image.open(SRC).convert("RGB"))
    bg = darken_behind(bg)

    d = ImageDraw.Draw(bg)
    draw_center(d, KANJI_Y, KANJI, ImageFont.truetype(KANJI_FONT, KANJI_SIZE), 0)
    draw_center(d, ROMAJI_Y, ROMAJI, ImageFont.truetype(ROMAJI_FONT, ROMAJI_SIZE), ROMAJI_SPACING)

    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
