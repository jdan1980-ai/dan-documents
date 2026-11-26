#!/usr/bin/env python3
"""
IKIGAI — 生き甲斐 | long-form thumbnail compose (1280x720).

Layout (user's design, brand-corrected):
  - Tategaki kanji 生き甲斐 — LEFT column over the dark indigo sky, cream #F5EAD2
  - IKIGAI romaji — lower-left over the dark hillside, Liberation Serif Bold, cream
  - No outline, no glow, no shadow, no duration tag (channel lock)

Source: ikigai-2h-source.jpg (NanoBanana 16:9 — monk on engawa above sea of clouds)
Output: ikigai-2h-thumb.jpg (1280x720, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC  = HERE / "ikigai-2h-source.jpg"
OUT  = HERE / "ikigai-2h-thumb.jpg"

W, H = 1280, 720
CREAM = (245, 234, 210)          # #F5EAD2 — locked StillWave cream

KANJI_FONT  = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

# --- Tategaki 生き甲斐 (4 chars, vertical, left edge over dark sky) ---
KANJI_TEXT  = "生き甲斐"
KANJI_SIZE  = 104
KANJI_GAP   = 10
KANJI_X     = 96                  # column center from left edge
KANJI_Y_TOP = 42

# --- IKIGAI (lower-left, over dark hillside) ---
ROMAJI_TEXT    = "IKIGAI"
ROMAJI_SIZE    = 108
ROMAJI_X       = 52
ROMAJI_Y       = 560
ROMAJI_SPACING = 10


def main():
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")

    bg = Image.open(SRC).convert("RGB")
    # center-crop to 16:9 then resize
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

    # tategaki — one char per line, centered on KANJI_X
    y = KANJI_Y_TOP
    for ch in KANJI_TEXT:
        bb = kf.getbbox(ch)
        w  = bb[2] - bb[0]
        d.text((KANJI_X - w // 2 - bb[0], y), ch, font=kf, fill=CREAM)
        y += (bb[3] - bb[1]) + KANJI_GAP

    # romaji — tracked left-to-right
    x = ROMAJI_X
    for ch in ROMAJI_TEXT:
        bb = rf.getbbox(ch)
        d.text((x - bb[0], ROMAJI_Y), ch, font=rf, fill=CREAM)
        x += (bb[2] - bb[0]) + ROMAJI_SPACING

    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
