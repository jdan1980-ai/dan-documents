#!/usr/bin/env python3
"""
MIZU — 水 | Wisdom intro overlay (transparent PNG, 1920x1080).

Phrase (§6a): 上善若水 / Jōzen wa mizu no gotoshi / The highest good is like water.
Channel standard: LEFT side, cream #F5EAD2, Liberation Serif Bold (romaji/gloss)
+ IPA Mincho (kanji). No box, no glow. Drop on CapCut top track 0:03–0:14, fades 2s.

Output: mizu-wisdom-overlay.png (RGBA, transparent)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
OUT = HERE / "mizu-wisdom-overlay.png"

W, H = 1920, 1080
GOLD = (228, 196, 108, 255)          # #E4C46C — kintsugi / channel gold
SHADOW = (0, 0, 0, 130)              # soft shadow for legibility over bright morning bg

KANJI_FONT = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"

X = 120                       # left column start
KANJI = ("上善若水", 150, 548)        # lowered from 360
ROMAJI = ("Jōzen wa mizu no gotoshi", 60, 742)
GLOSS = ("The highest good is like water", 44, 828)


def track(d, xy, text, font, spacing=2):
    x, y = xy
    for ch in text:
        d.text((x + 3, y + 3), ch, font=font, fill=SHADOW)
        d.text((x, y), ch, font=font, fill=GOLD)
        x += d.textlength(ch, font=font) + spacing


def main():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    kt, ks, ky = KANJI
    track(d, (X, ky), kt, ImageFont.truetype(KANJI_FONT, ks), spacing=10)

    rt, rs, ry = ROMAJI
    track(d, (X + 4, ry), rt, ImageFont.truetype(SERIF_BOLD, rs), spacing=2)

    gt, gs, gy = GLOSS
    track(d, (X + 4, gy), gt, ImageFont.truetype(SERIF, gs), spacing=2)

    img.save(OUT)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
