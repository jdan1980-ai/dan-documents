#!/usr/bin/env python3
"""
Prepare StillWave logo derivatives from source PNG.

Inputs:
  stillwave-logo-source.png — 1024×1024 round slate badge

Outputs:
  stillwave-avatar-800.png        — YouTube channel avatar (800×800, circular crop)
  stillwave-watermark-overlay.png — Video watermark (1920×1080 RGBA, badge bottom-right)
"""

from pathlib import Path
from PIL import Image, ImageDraw

HERE   = Path(__file__).parent
SRC    = HERE / "stillwave-logo-source.png"
AVATAR = HERE / "stillwave-avatar-800.png"
WMARK  = HERE / "stillwave-watermark-overlay.png"


def circular_crop(img: Image.Image) -> Image.Image:
    """Crop a square RGBA image to a circle (transparent outside)."""
    size = img.size
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size[0] - 1, size[1] - 1], fill=255)
    out = img.convert("RGBA")
    out.putalpha(mask)
    return out


def make_avatar():
    src = Image.open(SRC).convert("RGB").resize((800, 800), Image.LANCZOS)
    src = src.convert("RGBA")
    out = circular_crop(src)
    out.save(AVATAR, "PNG")
    print(f"Wrote {AVATAR} ({AVATAR.stat().st_size // 1024} KB)")


def make_watermark():
    src = Image.open(SRC).convert("RGB")
    # Badge size in 1920×1080 frame — ~140px (clean, unobtrusive bottom-right stamp)
    BADGE = 140
    badge = src.resize((BADGE, BADGE), Image.LANCZOS).convert("RGBA")
    badge = circular_crop(badge)

    # Soften so it doesn't compete with content — 75% opacity
    alpha = badge.split()[-1].point(lambda p: int(p * 0.78))
    badge.putalpha(alpha)

    canvas = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    margin = 48
    pos = (1920 - BADGE - margin, 1080 - BADGE - margin)
    canvas.alpha_composite(badge, pos)
    canvas.save(WMARK, "PNG")
    print(f"Wrote {WMARK} ({WMARK.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    make_avatar()
    make_watermark()
