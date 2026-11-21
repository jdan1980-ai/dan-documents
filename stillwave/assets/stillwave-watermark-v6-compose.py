#!/usr/bin/env python3
"""
StillWave watermark v6 — sealed badge.

Structure:
  - Gold ензō ring = visible border
  - Filled dark-blue disc INSIDE the ензō ring = opaque mask covering AI watermark
  - Blue/cream wave sits on top of the disc
  - Outside the ензō ring = transparent (video shows through corners)

Outputs:
  stillwave-watermark-v6.png         — 1920×1080 RGBA overlay
  stillwave-watermark-v6-preview.jpg — preview on MAKOTO frame
  stillwave-badge-v6.png             — standalone badge (for reuse)
"""

from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np

HERE   = Path(__file__).parent
MARK   = HERE / "stillwave-mark-v3.png"
MAKOTO = HERE / "makoto-the-last-samurai-source.jpg"
BADGE  = HERE / "stillwave-badge-v6.png"
WM     = HERE / "stillwave-watermark-v6.png"
PREV   = HERE / "stillwave-watermark-v6-preview.jpg"

DISC_RGB = (24, 38, 64)      # deep navy-blue interior — covers any underlying pixels
BADGE_PX = 200               # final badge size in 1920×1080 frame
MARGIN   = 36


def build_badge() -> Image.Image:
    """Create a square RGBA badge with disc inside the ензō and transparent corners."""
    mark = Image.open(MARK).convert("RGBA")
    arr  = np.array(mark)
    alpha = arr[:, :, 3]

    # Bounding box of the visible mark = ензō extent
    ys, xs = np.where(alpha > 50)
    y0, y1 = ys.min(), ys.max()
    x0, x1 = xs.min(), xs.max()

    cx = (x0 + x1) // 2
    cy = (y0 + y1) // 2
    # Radius slightly inside the gold ензō ring so the gold stays as the visible border
    outer_r = min((x1 - x0), (y1 - y0)) // 2
    inner_r = int(outer_r * 0.88)

    # Disc layer
    disc = Image.new("RGBA", mark.size, (0, 0, 0, 0))
    ImageDraw.Draw(disc).ellipse(
        [cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r],
        fill=(*DISC_RGB, 255),
    )

    # Composite: disc behind, mark on top → gold ензō + blue wave + filled blue interior
    sealed = Image.alpha_composite(disc, mark)

    # Crop tight to a square around the ензō
    pad = int(outer_r * 0.06)
    side = outer_r * 2 + pad * 2
    bx0 = cx - outer_r - pad
    by0 = cy - outer_r - pad
    sealed = sealed.crop((bx0, by0, bx0 + side, by0 + side))

    sealed.save(BADGE, "PNG")
    print(f"Wrote {BADGE} ({sealed.size}, {BADGE.stat().st_size // 1024} KB)")
    return sealed


def build_overlay(badge: Image.Image):
    badge = badge.resize((BADGE_PX, BADGE_PX), Image.LANCZOS)
    canvas = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    pos = (1920 - BADGE_PX - MARGIN, 1080 - BADGE_PX - MARGIN)
    canvas.alpha_composite(badge, pos)
    canvas.save(WM, "PNG")
    print(f"Wrote {WM} ({WM.stat().st_size // 1024} KB)")

    bg = Image.open(MAKOTO).convert("RGBA").resize((1920, 1080))
    bg.alpha_composite(canvas)
    bg.convert("RGB").save(PREV, "JPEG", quality=92, optimize=True)
    print(f"Wrote {PREV} ({PREV.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build_overlay(build_badge())
