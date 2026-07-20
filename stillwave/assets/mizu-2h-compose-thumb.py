#!/usr/bin/env python3
"""
MIZU — 水 | long-form thumbnail compose (1280x720).

Layout (same as WABI SABI / IKIGAI):
  - 水 kanji — UPPER-LEFT corner
  - MIZU romaji — LOWER-LEFT corner
  - soft darkening behind BOTH corners so text pops on the bright koi-pond image
  - lower-right kept clear for the logo

Source: mizu-2h-source.jpg (koi pond, bamboo spout, morning light)
Output: mizu-2h-thumb.jpg (1280x720, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).parent
SRC = HERE / "mizu-2h-source.jpg"
OUT = HERE / "mizu-2h-thumb.jpg"

W, H = 1280, 720
CREAM = (247, 241, 228)
SHADOW = (0, 0, 0, 170)

KANJI_FONT = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

KANJI = "水"
KANJI_SIZE = 260
KANJI_X = 60
KANJI_Y = 40

ROMAJI = "MIZU"
ROMAJI_SIZE = 118
ROMAJI_X = 60
ROMAJI_Y = 556
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


def darken(bg):
    """Soft darkening behind the upper-left and lower-left text corners."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # upper-left (behind 水)
    d.ellipse((-260, -220, 470, 430), fill=(0, 0, 0, 140))
    # lower-left (behind MIZU)
    d.ellipse((-320, 470, 620, 940), fill=(0, 0, 0, 140))
    layer = layer.filter(ImageFilter.GaussianBlur(75))
    return Image.alpha_composite(bg.convert("RGBA"), layer).convert("RGB")


def draw_left(d, x, y, text, font, spacing):
    for ch in text:
        d.text((x + 4, y + 4), ch, font=font, fill=SHADOW)
        d.text((x, y), ch, font=font, fill=CREAM)
        x += d.textlength(ch, font=font) + spacing


def main():
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")

    bg = fit_cover(Image.open(SRC).convert("RGB"))
    bg = darken(bg)

    d = ImageDraw.Draw(bg)
    draw_left(d, KANJI_X, KANJI_Y, KANJI, ImageFont.truetype(KANJI_FONT, KANJI_SIZE), 0)
    draw_left(d, ROMAJI_X, ROMAJI_Y, ROMAJI, ImageFont.truetype(ROMAJI_FONT, ROMAJI_SIZE), ROMAJI_SPACING)

    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
