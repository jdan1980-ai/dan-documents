#!/usr/bin/env python3
"""
MONO NO AWARE thumbnail — Kanji-Concept Series style.
Matches SATORI / MUSHIN template: tategaki kanji LEFT + ROMAJI bottom-left.

Output: mono-no-aware-2h-thumb.jpg (1280x720, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC  = HERE / "mono-no-aware-source.jpg"
OUT  = HERE / "mono-no-aware-2h-thumb.jpg"

CANVAS = (1280, 720)

KANJI_FONT  = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

CREAM  = (245, 234, 210)   # #F5EAD2 — locked StillWave cream
SHADOW = 4

# --- Tategaki block (4 chars: 物の哀れ) ---
KANJI_TEXT  = "物の哀れ"
KANJI_SIZE  = 108           # slightly smaller than 2-char SATORI (130) to fit 4 chars
KANJI_GAP   = 8             # extra spacing between chars
KANJI_X     = 152           # column center from left edge
KANJI_Y_TOP = 72            # start near top

# --- Romaji block ---
ROMAJI_TEXT    = "MONO NO AWARE"
ROMAJI_SIZE    = 58
ROMAJI_X_CTR   = 370        # center pushed right — long 13-char string needs room
ROMAJI_Y       = 618
ROMAJI_SPACING = 4          # extra letter spacing


def shadow_text(draw, xy, text, font, fill, offset=SHADOW):
    x, y = xy
    draw.text((x + offset, y + offset), text, font=font, fill=(0, 0, 0))
    draw.text(xy, text, font=font, fill=fill)


def main():
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")

    bg = Image.open(SRC).convert("RGB")
    if bg.size != CANVAS:
        bg = bg.resize(CANVAS, Image.LANCZOS)

    draw = ImageDraw.Draw(bg)
    kf = ImageFont.truetype(KANJI_FONT,  KANJI_SIZE)
    rf = ImageFont.truetype(ROMAJI_FONT, ROMAJI_SIZE)

    # --- Tategaki: one char per line, vertically stacked ---
    y = KANJI_Y_TOP
    for ch in KANJI_TEXT:
        bb = kf.getbbox(ch)
        w  = bb[2] - bb[0]
        x  = KANJI_X - w // 2 - bb[0]
        shadow_text(draw, (x, y), ch, kf, CREAM)
        y += (bb[3] - bb[1]) + KANJI_GAP

    # --- Romaji: centered on KANJI_X column ---
    advances = []
    for ch in ROMAJI_TEXT:
        bb = rf.getbbox(ch)
        advances.append((ch, bb[2] - bb[0], bb))
    total_w = sum(a[1] for a in advances) + ROMAJI_SPACING * (len(advances) - 1)
    x = ROMAJI_X_CTR - total_w // 2
    for ch, w, bb in advances:
        shadow_text(draw, (x - bb[0], ROMAJI_Y), ch, rf, CREAM)
        x += w + ROMAJI_SPACING

    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
