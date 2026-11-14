#!/usr/bin/env python3
"""
StillWave watermark v7 — final.

Spec:
  - Real ензō brush IS the border (no extra perfect ring on top)
  - Blue fill inside the ензō (matches wave family, opaque to mask AI watermark)
  - Wave + ензō from original source logo, no text
  - Transparent outside the ензō

Outputs:
  stillwave-stamp-v7.png             — standalone 800×800 badge
  stillwave-watermark-v7.png         — 1920×1080 overlay
  stillwave-watermark-v7-preview.jpg — preview on MAKOTO frame
"""

from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np

HERE   = Path(__file__).parent
SRC    = HERE / "stillwave-logo-source-v2.jpg"   # white-bg gold ензō + blue wave
MAKOTO = HERE / "makoto-the-last-samurai-source.jpg"
STAMP  = HERE / "stillwave-stamp-v7.png"
WM     = HERE / "stillwave-watermark-v7.png"
PREV   = HERE / "stillwave-watermark-v7-preview.jpg"

INTERIOR_BLUE = (10, 14, 30)    # deep navy — nearly #0A0E1E
STAMP_PX      = 180
MARGIN        = 36
BADGE_SIZE    = 800


def extract_mark_only() -> Image.Image:
    """Remove white background from source, crop tight around ензō+wave only."""
    img = Image.open(SRC).convert("RGBA")
    arr = np.array(img)
    h, w = arr.shape[:2]

    # Mask out top-left "Ai" editor badge
    arr[:int(h * 0.10), :int(w * 0.10), :] = [255, 255, 255, 255]

    rgb = arr[:, :, :3].astype(np.int16)
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    # White background → transparent
    is_bright  = (r > 235) & (g > 235) & (b > 230)
    is_neutral = (np.abs(r - g) < 15) & (np.abs(g - b) < 15)
    bg_mask = is_bright & is_neutral

    brightness = (r.astype(np.float32) + g + b) / 3.0
    alpha = np.clip((245.0 - brightness) / 25.0 * 255.0, 0, 255).astype(np.uint8)
    alpha = np.where(bg_mask, 0, alpha)

    is_gold = (r > 150) & (g > 110) & (b < 170) & (r > b + 20)
    is_blue = (b > r + 5) & (b > 130)
    alpha = np.where(is_gold | is_blue, 255, alpha)

    arr[:, :, 3] = alpha
    out = Image.fromarray(arr, "RGBA")

    # Crop to upper portion (mark only, no text)
    ys, xs = np.where(arr[:int(h * 0.62), :, 3] > 30)
    if len(xs) > 0:
        pad = 28
        x0 = max(xs.min() - pad, 0)
        x1 = min(xs.max() + pad, w)
        y0 = max(ys.min() - pad, 0)
        y1 = min(ys.max() + pad, int(h * 0.62))
        out = out.crop((x0, y0, x1, y1))
    return out


def build_badge() -> Image.Image:
    """Mark on top of a blue disc sized to fit inside the ензō ring."""
    mark = extract_mark_only()
    arr  = np.array(mark)
    alpha = arr[:, :, 3]
    ys, xs = np.where(alpha > 50)
    y0, y1 = ys.min(), ys.max()
    x0, x1 = xs.min(), xs.max()
    cx = (x0 + x1) // 2
    cy = (y0 + y1) // 2
    outer_r = min((x1 - x0), (y1 - y0)) // 2
    inner_r = int(outer_r * 0.97)   # disc fills to inner edge of ензō brush

    disc = Image.new("RGBA", mark.size, (0, 0, 0, 0))
    ImageDraw.Draw(disc).ellipse(
        [cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r],
        fill=(*INTERIOR_BLUE, 255),
    )
    sealed = Image.alpha_composite(disc, mark)

    pad  = int(outer_r * 0.05)
    side = outer_r * 2 + pad * 2
    sealed = sealed.crop((cx - outer_r - pad, cy - outer_r - pad,
                          cx - outer_r - pad + side, cy - outer_r - pad + side))
    sealed = sealed.resize((BADGE_SIZE, BADGE_SIZE), Image.LANCZOS)
    sealed.save(STAMP, "PNG")
    print(f"Wrote {STAMP} ({sealed.size}, {STAMP.stat().st_size // 1024} KB)")
    return sealed


def main():
    badge = build_badge()
    s = badge.resize((STAMP_PX, STAMP_PX), Image.LANCZOS)
    canvas = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    canvas.alpha_composite(s, (1920 - STAMP_PX - MARGIN, 1080 - STAMP_PX - MARGIN))
    canvas.save(WM, "PNG")
    print(f"Wrote {WM} ({WM.stat().st_size // 1024} KB)")

    bg = Image.open(MAKOTO).convert("RGBA").resize((1920, 1080))
    bg.alpha_composite(canvas)
    bg.convert("RGB").save(PREV, "JPEG", quality=92, optimize=True)
    print(f"Wrote {PREV} ({PREV.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
