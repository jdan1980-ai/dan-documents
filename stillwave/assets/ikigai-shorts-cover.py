#!/usr/bin/env python3
"""
IKIGAI — Shorts cover (9:16, 1080x1920).
Layout v2 (giant-sun source): kanji 生き甲斐 in dark sumi ink brushed ACROSS the
sun disc (the visual hero — Kanji-Concept series trick) + cream IKIGAI over the
dark wooden deck, bottom-left.

Source: ikigai-shorts-source.jpg (NanoBanana 9:16 — monk, giant sun, tea steam)
Output: ikigai-shorts-cover.jpg (1080x1920, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC  = HERE / "ikigai-shorts-source.jpg"
OUT  = HERE / "ikigai-shorts-cover.jpg"

W, H = 1080, 1920
CREAM = (245, 234, 210)          # #F5EAD2 — locked StillWave cream
INK   = (30, 24, 18)             # sumi ink — kanji over the bright sun disc

KANJI_FONT  = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

# --- 生き甲斐 — horizontal row across the sun disc ---
KANJI_TEXT   = "生き甲斐"
KANJI_SIZE   = 118
KANJI_GAP    = 22
KANJI_X_CTR  = 620               # sun disc center-ish
KANJI_Y      = 380

# --- IKIGAI — cream, bottom-left over the dark deck ---
ROMAJI_TEXT    = "IKIGAI"
ROMAJI_SIZE    = 112
ROMAJI_X       = 56
ROMAJI_Y       = 1740
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

    # kanji — horizontal, centered on KANJI_X_CTR
    widths = []
    for ch in KANJI_TEXT:
        bb = kf.getbbox(ch)
        widths.append((ch, bb[2] - bb[0], bb))
    total = sum(w for _, w, _ in widths) + KANJI_GAP * (len(widths) - 1)
    x = KANJI_X_CTR - total // 2
    for ch, w, bb in widths:
        d.text((x - bb[0], KANJI_Y), ch, font=kf, fill=INK)
        x += w + KANJI_GAP

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
