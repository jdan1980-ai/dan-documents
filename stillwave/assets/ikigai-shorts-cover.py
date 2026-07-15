#!/usr/bin/env python3
"""
IKIGAI — Shorts cover (9:16, 1080x1920).
Series style (matches GAMAN cover): tategaki kanji in dark sumi ink over the
glowing shoji screen (left) + cream ROMAJI over the dark floor (bottom-left).

Source: ikigai-shorts-source.jpg (NanoBanana 9:16 — monk + sunrise + shoji)
Output: ikigai-shorts-cover.jpg (1080x1920, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC  = HERE / "ikigai-shorts-source.jpg"
OUT  = HERE / "ikigai-shorts-cover.jpg"

W, H = 1080, 1920
CREAM = (245, 234, 210)          # #F5EAD2 — locked StillWave cream
INK   = (30, 24, 18)             # sumi ink — kanji over the lit shoji paper

KANJI_FONT  = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

# --- Tategaki 生き甲斐 — over the glowing shoji screen, left ---
KANJI_TEXT  = "生き甲斐"
KANJI_SIZE  = 108
KANJI_GAP   = 18
KANJI_X     = 100                # column center from left edge
KANJI_Y_TOP = 470

# --- IKIGAI — cream, over the dark floor, bottom-left ---
ROMAJI_TEXT    = "IKIGAI"
ROMAJI_SIZE    = 118
ROMAJI_X       = 64
ROMAJI_Y       = 1690
ROMAJI_SPACING = 12


def main():
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")

    bg = Image.open(SRC).convert("RGB")
    sw, sh = bg.size
    target = W / H
    if sw / sh > target:
        nw = int(sh * target)
        bg = bg.crop(((sw - nw) // 2, 0, (sw + nw) // 2, sh))
    else:
        nh = int(sw / target)
        bg = bg.crop((0, (sh - nh) // 2, sw, (sh + nh) // 2))
    bg = bg.resize((W, H), Image.LANCZOS)

    d = ImageDraw.Draw(bg)
    kf = ImageFont.truetype(KANJI_FONT,  KANJI_SIZE)
    rf = ImageFont.truetype(ROMAJI_FONT, ROMAJI_SIZE)

    y = KANJI_Y_TOP
    for ch in KANJI_TEXT:
        bb = kf.getbbox(ch)
        w  = bb[2] - bb[0]
        d.text((KANJI_X - w // 2 - bb[0], y), ch, font=kf, fill=INK)
        y += (bb[3] - bb[1]) + KANJI_GAP

    x = ROMAJI_X
    for ch in ROMAJI_TEXT:
        bb = rf.getbbox(ch)
        d.text((x - bb[0], ROMAJI_Y), ch, font=rf, fill=CREAM)
        x += (bb[2] - bb[0]) + ROMAJI_SPACING

    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
