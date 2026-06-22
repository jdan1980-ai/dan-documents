#!/usr/bin/env python3
"""
StillWave channel watermark overlay — 1920×1080 RGBA PNG.

Bottom-right corner — covers NanoBanana diamond watermark position.
In CapCut: drop on video track → blend mode Normal → opacity 70–80%

Output: stillwave-watermark.png
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
OUT  = HERE / "stillwave-watermark.png"

CANVAS = (1920, 1080)

BOLD_FONT   = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
ITALIC_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"

CREAM = (245, 234, 210)   # #F5EAD2 — locked StillWave text color

BRAND_SIZE  = 42          # "StillWave"
HANDLE_SIZE = 24          # "@stillwavezen"

RIGHT_MARGIN  = 60
BOTTOM_MARGIN = 48        # from bottom edge


def draw_with_shadow(draw, xy, text, font, fill, alpha=255, shadow_r=2):
    x, y = xy
    shadow_color = (0, 0, 0, 160)
    for dx in range(-shadow_r, shadow_r + 1):
        for dy in range(-shadow_r, shadow_r + 1):
            if dx == 0 and dy == 0:
                continue
            draw.text((x + dx, y + dy), text, font=font, fill=shadow_color)
    draw.text(xy, text, font=font, fill=(*fill, alpha))


def main():
    img  = Image.new("RGBA", CANVAS, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    brand_font  = ImageFont.truetype(BOLD_FONT,   BRAND_SIZE)
    handle_font = ImageFont.truetype(ITALIC_FONT, HANDLE_SIZE)

    brand_text  = "StillWave"
    handle_text = "@stillwavezen"

    # Measure widths (right-aligned)
    bbb = brand_font.getbbox(brand_text)
    hbb = handle_font.getbbox(handle_text)

    brand_w  = bbb[2] - bbb[0]
    handle_w = hbb[2] - hbb[0]
    brand_h  = bbb[3] - bbb[1]
    handle_h = hbb[3] - hbb[1]

    gap = 8  # pixels between brand and handle lines

    block_h = brand_h + gap + handle_h

    # Anchor: bottom-right
    bx = CANVAS[0] - RIGHT_MARGIN - brand_w - bbb[0]
    by = CANVAS[1] - BOTTOM_MARGIN - block_h - bbb[1]

    hx = CANVAS[0] - RIGHT_MARGIN - handle_w - hbb[0]
    hy = by + bbb[1] + brand_h + gap - hbb[1]

    draw_with_shadow(draw, (bx, by), brand_text,  brand_font,  CREAM, alpha=230)
    draw_with_shadow(draw, (hx, hy), handle_text, handle_font, CREAM, alpha=180)

    img.save(OUT, "PNG")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
