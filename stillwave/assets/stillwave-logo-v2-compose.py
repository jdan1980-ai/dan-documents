#!/usr/bin/env python3
"""
StillWave logo v2 — gold ensō + wave on dark slate circle.
Matches #5 from the candidate sheet: gold brushstroke ring, wave inside, "StillWave" below.

Outputs:
  stillwave-logo-v2.png          — 512×512 RGBA (transparent bg) for upload
  stillwave-logo-v2-circle.png   — 512×512 RGBA (dark slate circle bg)
"""

import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).parent

GOLD   = (201, 168, 76)     # #C9A84C
GOLD_L = (230, 200, 110)    # lighter highlight
SLATE  = (48, 50, 58)       # dark slate circle background
WHITE  = (255, 255, 255)
CREAM  = (245, 234, 210)

SIZE   = 512
CX, CY = SIZE // 2, SIZE // 2


def draw_enso(draw: ImageDraw.ImageDraw, cx, cy, r, thickness=22):
    """Gold ensō — thick arc ~330°, brush-stroke style via layered ellipses."""
    box = [cx - r, cy - r, cx + r, cy + r]
    # Draw thick arc (270° sweep, gap at bottom-right — classic ensō gap)
    for t in range(-thickness // 2, thickness // 2 + 1):
        offset = t
        b = [cx - r + offset, cy - r + offset, cx + r - offset, cy + r - offset]
        draw.arc(b, start=50, end=370, fill=GOLD, width=3)
    # Thicker main stroke
    for w in range(3, 8):
        draw.arc(box, start=50, end=370, fill=GOLD, width=thickness - w)

    # Bold main ring
    draw.arc(box, start=50, end=370, fill=GOLD, width=thickness)

    # Tapered ends — small filled circles at start/end of arc
    angle_start = math.radians(50)
    angle_end   = math.radians(370)
    for angle in (angle_start, angle_end):
        ex = cx + r * math.cos(angle)
        ey = cy + r * math.sin(angle)
        er = thickness // 2 - 1
        draw.ellipse([ex - er, ey - er, ex + er, ey + er], fill=GOLD)


def draw_wave(draw: ImageDraw.ImageDraw, cx, cy, scale=1.0):
    """Simple two-crest wave inside the ensō."""
    wave_y   = cy + int(30 * scale)
    wave_w   = int(90 * scale)
    wave_h   = int(18 * scale)
    lw       = max(3, int(5 * scale))

    # Three arcs forming a ~~~  wave
    for i, (sx, ex, flip) in enumerate([
        (cx - wave_w, cx - wave_w // 3, False),
        (cx - wave_w // 3, cx + wave_w // 3, True),
        (cx + wave_w // 3, cx + wave_w, False),
    ]):
        mid = (sx + ex) // 2
        if flip:
            box = [sx, wave_y, ex, wave_y + wave_h * 2]
            draw.arc(box, start=180, end=360, fill=GOLD_L, width=lw)
        else:
            box = [sx, wave_y - wave_h, ex, wave_y + wave_h]
            draw.arc(box, start=0, end=180, fill=GOLD_L, width=lw)


def make_logo(with_circle_bg: bool) -> Image.Image:
    img  = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if with_circle_bg:
        # Dark slate circle
        pad = 8
        draw.ellipse([pad, pad, SIZE - pad, SIZE - pad], fill=(*SLATE, 255))

    # Ensō ring
    enso_r = 155
    draw_enso(draw, CX, CY - 20, enso_r, thickness=26)

    # Wave inside ensō
    draw_wave(draw, CX, CY - 20, scale=1.0)

    # "StillWave" text — serif bold, bottom of circle
    try:
        font_bold   = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf", 52)
    except OSError:
        font_bold = ImageFont.load_default()

    text = "StillWave"
    bb   = font_bold.getbbox(text)
    tw   = bb[2] - bb[0]
    tx   = CX - tw // 2 - bb[0]
    ty   = CY + enso_r + 10

    # Shadow
    draw.text((tx + 2, ty + 2), text, font=font_bold, fill=(0, 0, 0, 180))
    draw.text((tx, ty),         text, font=font_bold, fill=(*GOLD, 255))

    return img


def main():
    # Version with circle background (for preview / watermark)
    logo_circle = make_logo(with_circle_bg=True)
    out_circle  = HERE / "stillwave-logo-v2-circle.png"
    logo_circle.save(out_circle, "PNG")
    print(f"Wrote {out_circle} ({out_circle.stat().st_size // 1024} KB)")

    # Version transparent bg (for YouTube upload)
    logo_trans  = make_logo(with_circle_bg=False)
    out_trans   = HERE / "stillwave-logo-v2.png"
    logo_trans.save(out_trans, "PNG")
    print(f"Wrote {out_trans} ({out_trans.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
