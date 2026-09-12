#!/usr/bin/env python3
"""
Extract the ensō+wave mark from the slate badge.

Strategy: detect the slate gray range and convert to transparent.
Keep only the gold ensō ring and blue wave.

Output:
  stillwave-mark.png — ~600×600 RGBA, just the mark
  stillwave-watermark-v2.png — 1920×1080 overlay, mark bottom-right
"""

from pathlib import Path
from PIL import Image
import numpy as np

HERE = Path(__file__).parent
SRC  = HERE / "stillwave-logo-source.png"
MARK = HERE / "stillwave-mark.png"
WM   = HERE / "stillwave-watermark-v2.png"


def extract_mark():
    img = Image.open(SRC).convert("RGBA")
    a   = np.array(img)
    rgb = a[:, :, :3].astype(np.int16)

    # Slate background: dark gray, R≈G≈B in 30..80 range
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    is_dark   = (r < 95) & (g < 95) & (b < 100)
    is_neutral = (np.abs(r - g) < 25) & (np.abs(g - b) < 25) & (np.abs(r - b) < 25)
    slate_mask = is_dark & is_neutral

    # Gold (R>>B): keep
    is_gold = (r > 130) & (g > 100) & (b < 130) & (r > b + 30)
    # Blue (B>R): keep
    is_blue = (b > r) & (b > 90)
    keep = is_gold | is_blue

    # Final alpha: opaque where keep, transparent where slate-and-not-keep
    alpha = np.where(keep, 255,
            np.where(slate_mask, 0, 255)).astype(np.uint8)
    a[:, :, 3] = alpha

    out = Image.fromarray(a, "RGBA")

    # Crop tight around non-transparent pixels (upper portion, ignore text)
    # We only want the ensō+wave, not the "StillWave" text below.
    # Find bounding box of gold+blue pixels in upper half
    upper = a[:int(a.shape[0] * 0.62), :, :]
    ys, xs = np.where(upper[:, :, 3] > 0)
    if len(xs) > 0:
        x0, x1 = max(xs.min() - 20, 0), min(xs.max() + 20, a.shape[1])
        y0, y1 = max(ys.min() - 20, 0), min(ys.max() + 20, int(a.shape[0] * 0.62))
        out = out.crop((x0, y0, x1, y1))

    out.save(MARK, "PNG")
    print(f"Wrote {MARK} ({out.size}, {MARK.stat().st_size // 1024} KB)")
    return out


def make_overlay(mark: Image.Image):
    # Scale mark to ~120px height for corner watermark
    target_h = 120
    ratio = target_h / mark.size[1]
    new_w = int(mark.size[0] * ratio)
    mark = mark.resize((new_w, target_h), Image.LANCZOS)

    # 85% opacity
    alpha = mark.split()[-1].point(lambda p: int(p * 0.85))
    mark.putalpha(alpha)

    canvas = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    margin = 56
    pos = (1920 - new_w - margin, 1080 - target_h - margin)
    canvas.alpha_composite(mark, pos)
    canvas.save(WM, "PNG")
    print(f"Wrote {WM} ({WM.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    mark = extract_mark()
    make_overlay(mark)
