#!/usr/bin/env python3
"""
ZANSHIN — 残心 | Wisdom intro overlay (transparent PNG, 1920x1080).

Phrase (§6a): 平常心是道 / Heijōshin kore michi / The ordinary, steady mind is the Way.
Channel standard: LEFT side, cream #F5EAD2, Liberation Serif Bold (romaji/gloss)
+ IPA Mincho (kanji). Soft shadow for legibility. Drop on CapCut top track
0:03–0:14, fades 2s.

Output: zanshin-wisdom-overlay.png (RGBA, transparent)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
OUT = HERE / "zanshin-wisdom-overlay.png"

W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SHADOW = (0, 0, 0, 150)

KANJI_FONT = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"

X = 130
KANJI = ("平常心是道", 108, 372)
ROMAJI = ("Heijōshin kore michi", 56, 520)
GLOSS = ("The ordinary, steady mind is the Way", 40, 600)


def track(d, xy, text, font, spacing):
    x, y = xy
    for ch in text:
        d.text((x + 3, y + 3), ch, font=font, fill=SHADOW)
        d.text((x, y), ch, font=font, fill=CREAM)
        x += d.textlength(ch, font=font) + spacing


def main():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    kt, ks, ky = KANJI
    track(d, (X, ky), kt, ImageFont.truetype(KANJI_FONT, ks), 12)
    rt, rs, ry = ROMAJI
    track(d, (X + 4, ry), rt, ImageFont.truetype(SERIF_BOLD, rs), 2)
    gt, gs, gy = GLOSS
    track(d, (X + 4, gy), gt, ImageFont.truetype(SERIF, gs), 2)
    img.save(OUT)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
