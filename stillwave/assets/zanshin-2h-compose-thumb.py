#!/usr/bin/env python3
"""
ZANSHIN — 残心 | long-form thumbnail compose (1280x720).

Layout (WABI SABI / IKIGAI style): 残心 upper-left, ZANSHIN lower-left,
warm gold #E4C46C (matches the tiger mural's gold + the sepia hall), soft
darkening behind both corners. Lower-right kept clear for the logo.

Source: zanshin-2h-source.jpg (tiger-and-pine mural + samurai in seiza)
Output: zanshin-2h-thumb.jpg (1280x720, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).parent
SRC = HERE / "zanshin-2h-source.jpg"
OUT = HERE / "zanshin-2h-thumb.jpg"

W, H = 1280, 720
GOLD = (228, 196, 108)               # #E4C46C
SHADOW = (0, 0, 0, 180)

KANJI_FONT = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

KANJI = "残心"
KANJI_SIZE = 228
KANJI_X = 58
KANJI_Y = 44

ROMAJI = "ZANSHIN"
ROMAJI_SIZE = 104
ROMAJI_X = 60
ROMAJI_Y = 566
ROMAJI_SPACING = 10


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
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.ellipse((-300, 20, 520, 470), fill=(0, 0, 0, 135))       # upper-left (残心)
    d.ellipse((-340, 470, 620, 900), fill=(0, 0, 0, 150))      # lower-left (ZANSHIN, over bright windows)
    layer = layer.filter(ImageFilter.GaussianBlur(78))
    return Image.alpha_composite(bg.convert("RGBA"), layer).convert("RGB")


def draw_left(d, x, y, text, font, spacing):
    for ch in text:
        d.text((x + 4, y + 4), ch, font=font, fill=SHADOW)
        d.text((x, y), ch, font=font, fill=GOLD)
        x += d.textlength(ch, font=font) + spacing


def main():
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")
    bg = darken(fit_cover(Image.open(SRC).convert("RGB")))
    d = ImageDraw.Draw(bg)
    draw_left(d, KANJI_X, KANJI_Y, KANJI, ImageFont.truetype(KANJI_FONT, KANJI_SIZE), 0)
    draw_left(d, ROMAJI_X, ROMAJI_Y, ROMAJI, ImageFont.truetype(ROMAJI_FONT, ROMAJI_SIZE), ROMAJI_SPACING)
    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
