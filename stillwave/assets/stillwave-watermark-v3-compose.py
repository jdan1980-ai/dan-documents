#!/usr/bin/env python3
"""
Build StillWave watermark v3 from clean source logo (white-bg JPG).

Source: stillwave-logo-source-v2.jpg — gold ensō+wave + "StillWave" text on white
Steps:
  1. Crop out "Ai" editor badge (top-left)
  2. Remove white background -> transparent
  3. Tight-crop around mark
  4. Output:
     - stillwave-mark-v3.png  : just the mark, transparent
     - stillwave-watermark-v3.png : 1920×1080 overlay, mark bottom-right
"""

from pathlib import Path
from PIL import Image
import numpy as np

HERE = Path(__file__).parent
SRC  = HERE / "stillwave-logo-source-v2.jpg"
MARK = HERE / "stillwave-mark-v3.png"
WM   = HERE / "stillwave-watermark-v3.png"


def extract():
    img = Image.open(SRC).convert("RGBA")
    w, h = img.size

    # Crop out top-left "Ai" badge (~10% × 10%)
    arr = np.array(img)
    arr[:int(h * 0.10), :int(w * 0.10), :] = [255, 255, 255, 255]

    rgb = arr[:, :, :3].astype(np.int16)
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    # White/cream background mask: bright + neutral
    is_bright  = (r > 235) & (g > 235) & (b > 230)
    is_neutral = (np.abs(r - g) < 15) & (np.abs(g - b) < 15)
    bg_mask = is_bright & is_neutral

    # Soft alpha: linear ramp 220..245 for anti-aliased edges
    brightness = (r.astype(np.float32) + g + b) / 3.0
    alpha = np.clip((245.0 - brightness) / 25.0 * 255.0, 0, 255).astype(np.uint8)
    alpha = np.where(bg_mask, 0, alpha)

    # Where pixel is clearly colored (gold/blue), force full opacity
    is_gold = (r > 150) & (g > 110) & (b < 170) & (r > b + 20)
    is_blue = (b > r + 5) & (b > 130)
    alpha = np.where(is_gold | is_blue, 255, alpha)

    arr[:, :, 3] = alpha

    out = Image.fromarray(arr, "RGBA")

    # Tight crop around non-transparent pixels
    ys, xs = np.where(arr[:, :, 3] > 30)
    if len(xs) > 0:
        pad = 30
        x0 = max(xs.min() - pad, 0)
        x1 = min(xs.max() + pad, w)
        y0 = max(ys.min() - pad, 0)
        y1 = min(ys.max() + pad, h)
        out = out.crop((x0, y0, x1, y1))

    out.save(MARK, "PNG")
    print(f"Wrote {MARK} ({out.size}, {MARK.stat().st_size // 1024} KB)")
    return out


def overlay(mark: Image.Image):
    # Scale mark to ~160px height (logo + text reads at this size)
    target_h = 160
    ratio = target_h / mark.size[1]
    new_w = int(mark.size[0] * ratio)
    mark = mark.resize((new_w, target_h), Image.LANCZOS)

    # 90% opacity
    alpha = mark.split()[-1].point(lambda p: int(p * 0.90))
    mark.putalpha(alpha)

    canvas = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    margin = 56
    pos = (1920 - new_w - margin, 1080 - target_h - margin)
    canvas.alpha_composite(mark, pos)
    canvas.save(WM, "PNG")
    print(f"Wrote {WM} ({WM.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    overlay(extract())
