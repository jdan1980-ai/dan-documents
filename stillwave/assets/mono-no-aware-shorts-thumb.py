#!/usr/bin/env python3
"""
MONO NO AWARE — Shorts thumbnail (9:16 cover).
Matches Kanji-Concept Series style: tategaki kanji LEFT + ROMAJI bottom-left.

Source image: Scene 4 NanoBanana 9:16 still (petals on koi pond).
Drop the generated image at mono-no-aware-shorts-source.jpg, then run.

Output: mono-no-aware-shorts-thumb.jpg (1080x1920, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC  = HERE / "mono-no-aware-shorts-source.jpg"
OUT  = HERE / "mono-no-aware-shorts-thumb.jpg"

CANVAS = (1080, 1920)

KANJI_FONT  = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

CREAM  = (245, 234, 210)   # #F5EAD2 — locked StillWave cream
SHADOW = 4

# --- Tategaki block (4 chars: 物の哀れ) ---
KANJI_TEXT  = "物の哀れ"
KANJI_SIZE  = 120
KANJI_GAP   = 10
KANJI_X     = 150           # column center from left edge
KANJI_Y_TOP = 120           # start near top

# --- Romaji block ---
ROMAJI_TEXT    = "MONO NO AWARE"
ROMAJI_SIZE    = 55
ROMAJI_X_CTR   = 370        # center of romaji string
ROMAJI_Y       = 1780       # near bottom
ROMAJI_SPACING = 4


def shadow_text(draw, xy, text, font, fill, offset=SHADOW):
    x, y = xy
    draw.text((x + offset, y + offset), text, font=font, fill=(0, 0, 0))
    draw.text(xy, text, font=font, fill=fill)


def main():
    if not SRC.exists():
        raise SystemExit(
            f"Source not found: {SRC}\n"
            "Generate Scene 4 (petals on koi pond) in NanoBanana 9:16,\n"
            "save it as mono-no-aware-shorts-source.jpg, then re-run."
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
