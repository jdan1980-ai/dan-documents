#!/usr/bin/env python3
"""
WABI SABI — 侘寂 | long-form thumbnail compose (1280x720).

Layout (user brief 2026-07-17):
  - Tategaki kanji 侘寂 — LEFT column top-down, gold matched to the bowl's cracks
  - WABI SABI — lower-left, same gold, Liberation Serif Bold
  - No outline, no shadow, no tags (channel lock)

Source: wabi-sabi-2h-source.jpg (kintsugi bowl on black, bowl right-of-center)
Output: wabi-sabi-2h-thumb.jpg (1280x720, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC  = HERE / "wabi-sabi-2h-source.jpg"
OUT  = HERE / "wabi-sabi-2h-thumb.jpg"

W, H = 1280, 720
GOLD = (228, 186, 92)            # warm gold matched to the kintsugi cracks

KANJI_FONT  = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

# --- Tategaki 侘寂 (2 chars, vertical, upper-left over black) ---
KANJI_TEXT  = "侘寂"
KANJI_SIZE  = 168
KANJI_GAP   = 26
KANJI_X     = 138                # column center from left edge
KANJI_Y_TOP = 64

# --- WABI SABI (lower-left over black) ---
ROMAJI_TEXT    = "WABI SABI"
ROMAJI_SIZE    = 92
ROMAJI_X       = 56
ROMAJI_Y       = 590
ROMAJI_SPACING = 8
SPACE_ADVANCE  = 34


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
        d.text((KANJI_X - w // 2 - bb[0], y), ch, font=kf, fill=GOLD)
        y += (bb[3] - bb[1]) + KANJI_GAP

    x = ROMAJI_X
    for ch in ROMAJI_TEXT:
        if ch == " ":
            x += SPACE_ADVANCE
            continue
        bb = rf.getbbox(ch)
        d.text((x - bb[0], ROMAJI_Y), ch, font=rf, fill=GOLD)
        x += (bb[2] - bb[0]) + ROMAJI_SPACING

    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
