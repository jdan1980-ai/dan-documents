#!/usr/bin/env python3
"""
Generate transparent PNG overlay for series-brand text on YouTube thumbnails.

Locked StillWave overlay style:
  - Font: Bebas Neue Regular (vendored at stillwave/assets/fonts/BebasNeue-Regular.ttf)
  - Color: pure white #FFFFFF
  - Letter spacing: 0.4 × font size (wide tracking)
  - Position: top-center, baseline at ~12% from top of frame
  - No glow, no shadow, no stroke, no effects (per stillwave/CLAUDE.md design rules)

Frame: 1280×720 (YouTube thumbnail). Output: transparent PNG to drop on top
of the NanoBanana 16:9 image in Photopea / Canva / any image editor.

Usage:
  python3 gen_series_overlay.py "POWER HOUR"
  python3 gen_series_overlay.py "HEALING HOUR" --size standard
  python3 gen_series_overlay.py "DEEP NIGHT" --size all

Naming convention:
  <slug>-<size>.png            transparent overlay
  <slug>-<size>-preview.png    same overlay on dark-navy bg (for sanity-checking)
  <slug>-overlay.png           alias for <slug>-standard.png (default pick)

Size cap: if the rendered text exceeds 95% of frame width at the requested
font size, the size is auto-reduced. This protects HEALING HOUR (12 chars)
from overflowing at the same font size that worked for POWER HOUR (10 chars).
"""

import argparse
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_PATH = Path(__file__).parent / "assets" / "fonts" / "BebasNeue-Regular.ttf"
OUT_DIR = Path(__file__).parent / "assets"

FRAME_W, FRAME_H = 1280, 720
LETTER_SPACING_RATIO = 0.25
TOP_PADDING_FRACTION = 0.12
MAX_WIDTH_PCT = 95  # auto-reduce font if text exceeds this
PREVIEW_BG = (12, 19, 36, 255)  # dark navy #0C1324

SIZES = {
    "compact": 90,
    "standard": 120,
    "large": 150,
}


def slug(text):
    return text.lower().replace(" ", "-")


def render(text, font_px):
    """Return (transparent_img, width_pct, actual_font_px)."""
    while font_px > 30:
        font = ImageFont.truetype(str(FONT_PATH), font_px)
        char_imgs = []
        total_w = 0
        spacing_px = int(font_px * LETTER_SPACING_RATIO)
        for ch in text:
            if ch == " ":
                char_imgs.append((None, int(font_px * 0.6)))
                total_w += int(font_px * 0.6) + spacing_px
                continue
            bbox = font.getbbox(ch)
            cw = bbox[2] - bbox[0]
            ch_h = bbox[3] - bbox[1]
            c_img = Image.new("RGBA", (cw, ch_h), (0, 0, 0, 0))
            d = ImageDraw.Draw(c_img)
            d.text((-bbox[0], -bbox[1]), ch, font=font, fill=(255, 255, 255, 255))
            char_imgs.append((c_img, cw))
            total_w += cw + spacing_px
        total_w -= spacing_px
        width_pct = 100 * total_w / FRAME_W
        if width_pct <= MAX_WIDTH_PCT:
            break
        font_px -= 5  # auto-shrink and retry

    img = Image.new("RGBA", (FRAME_W, FRAME_H), (0, 0, 0, 0))
    x = (FRAME_W - total_w) // 2
    y = int(FRAME_H * TOP_PADDING_FRACTION)
    cur_x = x
    for c_img, cw in char_imgs:
        if c_img is not None:
            img.paste(c_img, (cur_x, y), c_img)
        cur_x += cw + spacing_px
    return img, round(width_pct), font_px


def main():
    parser = argparse.ArgumentParser(description="Generate series-brand overlay PNG.")
    parser.add_argument("text", help='Brand text, e.g. "POWER HOUR" or "HEALING HOUR"')
    parser.add_argument(
        "--size",
        choices=["compact", "standard", "large", "all"],
        default="all",
        help="Which size variant to generate (default: all)",
    )
    args = parser.parse_args()

    text = args.text.upper().strip()
    base = slug(text)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    targets = SIZES if args.size == "all" else {args.size: SIZES[args.size]}

    print(f"Font: {FONT_PATH.name}")
    for size_name, font_px in targets.items():
        img, pct, final_px = render(text, font_px)
        out = OUT_DIR / f"{base}-{size_name}.png"
        img.save(out, "PNG")
        bg = Image.new("RGBA", (FRAME_W, FRAME_H), PREVIEW_BG)
        bg.alpha_composite(img)
        bg.convert("RGB").save(OUT_DIR / f"{base}-{size_name}-preview.png", "PNG")
        flag = "" if final_px == font_px else f" (auto-shrunk from {font_px}px)"
        print(f"  {base}-{size_name}: {final_px}px font, {pct}% frame width{flag}")

    # Aliases: the default standard becomes <slug>-overlay.png
    if (OUT_DIR / f"{base}-standard.png").exists():
        shutil.copy(OUT_DIR / f"{base}-standard.png", OUT_DIR / f"{base}-overlay.png")
        shutil.copy(
            OUT_DIR / f"{base}-standard-preview.png", OUT_DIR / f"{base}-preview.png"
        )
        print(f"  aliases: {base}-overlay.png + {base}-preview.png written")


if __name__ == "__main__":
    main()
