#!/usr/bin/env python3
"""
GAMAN — Shorts thumbnail (9:16 cover).
Matches Kanji-Concept Series style: tategaki kanji LEFT + ROMAJI bottom-left.

Source image: gaman-shorts-frame2.jpg (Scene 2 NanoBanana 9:16 — monk + scroll).
Output: gaman-shorts-cover.jpg (1080x1920, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC  = HERE / "gaman-shorts-frame2.jpg"
OUT  = HERE / "gaman-shorts-cover.jpg"

CANVAS = (1080, 1920)

KANJI_FONT  = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

CREAM  = (245, 234, 210)   # #F5EAD2 — locked StillWave cream
SHADOW = 4

# --- Tategaki block (2 chars: 我慢) ---
KANJI_TEXT  = "我慢"
KANJI_SIZE  = 190
KANJI_GAP   = 26
KANJI_X     = 165           # column center from left edge
KANJI_Y_TOP = 150

# --- Romaji block ---
ROMAJI_TEXT    = "GAMAN"
ROMAJI_SIZE    = 72
ROMAJI_X_CTR   = 300        # center of romaji string
ROMAJI_Y       = 1760       # near bottom
ROMAJI_SPACING = 6


def shadow_text(draw, xy, text, font, fill, offset=SHADOW):
    x, y = xy
    draw.text((x + offset, y + offset), text, font=font, fill=(0, 0, 0))
    draw.text(xy, text, font=font, fill=fill)


def main():
    if not SRC.exists():
        raise SystemExit(
            f"Source not found: {SRC}\n"
            "Generate Scene 2 (monk + scroll, §3b prompt) in NanoBanana 9:16,\n"
            "save it as gaman-shorts-frame2.jpg, then re-run."
        )

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

    # --- Romaji: centered on ROMAJI_X_CTR ---
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
