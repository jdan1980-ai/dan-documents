#!/usr/bin/env python3
"""
MUGA — 無我 | long-form thumbnail compose (1280x720).

Kanji-Concept locked format (upper-center kanji + low-center romaji,
per stillwave/CLAUDE.md — NOT the KAMI series' left-column tategaki):
  - 無我 — large, deep black sumi-ink brush style (YujiBoku), horizontal,
    upper-center, brushed directly onto the glowing enso
  - MUGA — cream #F5EAD2, Liberation Serif Bold, centred low on the
    foreground water/rock, with a soft blurred scrim for contrast
  - No outline/glow/shadow beyond the scrim, no duration tag

Source: muga-2h-source.jpg (NanoBanana 16:9 — monk + dissolving enso over lake)
Output: muga-2h-thumb.jpg (1280x720, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).parent
SRC = HERE / "muga-2h-source.jpg"
OUT = HERE / "muga-2h-thumb.jpg"

W, H = 1280, 720
CREAM = (245, 234, 210, 255)
SUMI = (18, 16, 14, 255)

KANJI_FONT = str(HERE / "fonts" / "YujiBoku-Regular.ttf")
ROMAJI_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

KANJI_TEXT = "無我"
KANJI_SIZE = 190
KANJI_Y = 46

ROMAJI_TEXT = "MUGA"
ROMAJI_SIZE = 68
ROMAJI_Y = 588
ROMAJI_SPACING = 14


def load_source() -> Image.Image:
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")
    img = Image.open(SRC).convert("RGB")
    sw, sh = img.size
    target = W / H
    if sw / sh > target:
        nw = int(sh * target)
        img = img.crop(((sw - nw) // 2, 0, (sw + nw) // 2, sh))
    else:
        nh = int(sw / target)
        img = img.crop((0, (sh - nh) // 2, sw, (sh + nh) // 2))
    return img.resize((W, H), Image.LANCZOS)


def main() -> None:
    bg = load_source().convert("RGBA")

    # --- 無我 — horizontal, centered upper, deep sumi-ink ---
    kf = ImageFont.truetype(KANJI_FONT, KANJI_SIZE)
    kanji_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    kd = ImageDraw.Draw(kanji_layer)
    bb = kf.getbbox(KANJI_TEXT)
    kw = bb[2] - bb[0]
    kx = (W - kw) // 2 - bb[0]
    kd.text((kx, KANJI_Y), KANJI_TEXT, font=kf, fill=SUMI)
    bg.alpha_composite(kanji_layer)

    # --- soft scrim behind MUGA so cream reads over the water/rock ---
    scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(scrim).rounded_rectangle(
        (W // 2 - 260, ROMAJI_Y - 30, W // 2 + 260, ROMAJI_Y + ROMAJI_SIZE + 20),
        radius=90, fill=(8, 6, 4, 140),
    )
    bg.alpha_composite(scrim.filter(ImageFilter.GaussianBlur(60)))

    # --- MUGA — cream, tracked, centered low ---
    rf = ImageFont.truetype(ROMAJI_FONT, ROMAJI_SIZE)
    advances = []
    for ch in ROMAJI_TEXT:
        b = rf.getbbox(ch)
        advances.append((ch, b[2] - b[0], b))
    total_w = sum(a[1] for a in advances) + ROMAJI_SPACING * (len(advances) - 1)
    d = ImageDraw.Draw(bg)
    x = (W - total_w) // 2
    for ch, w, b in advances:
        d.text((x - b[0], ROMAJI_Y), ch, font=rf, fill=CREAM)
        x += w + ROMAJI_SPACING

    bg.convert("RGB").save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
