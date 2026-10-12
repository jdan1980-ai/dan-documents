#!/usr/bin/env python3
"""
StillWave YouTube channel banner — 2560×1440.

- Deep navy background with subtle radial vignette
- "StillWave" — gold, thin serif, large, centred
- "Sleep · Focus · Meditation" — gold, thin serif, small, centred below
- Safe zone: 1546×423 centred in canvas
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np

HERE   = Path(__file__).parent
LOGO   = HERE / "stillwave-logo-final.png"
OUT    = HERE / "stillwave-banner.png"

W, H       = 2560, 1440
NAVY       = (10, 14, 30)
NAVY_MID   = (16, 22, 46)
GOLD       = (201, 168, 76)    # #C9A84C

FONT_REG   = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"


def make_banner():
    # ── Background: radial gradient (dark edges → slightly lighter centre) ──
    canvas = Image.new("RGB", (W, H), NAVY)
    arr = np.array(canvas, dtype=np.float32)
    cx, cy = W / 2, H / 2
    ys, xs = np.mgrid[0:H, 0:W]
    dist = np.sqrt(((xs - cx) / (W * 0.6)) ** 2 + ((ys - cy) / (H * 0.5)) ** 2)
    t = np.clip(1.0 - dist, 0, 1)[:, :, np.newaxis]
    navy_f   = np.array(NAVY,     dtype=np.float32)
    mid_f    = np.array(NAVY_MID, dtype=np.float32)
    arr = navy_f + (mid_f - navy_f) * t
    canvas = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")

    draw = ImageDraw.Draw(canvas)

    # ── "StillWave" — large gold serif ──────────────────────────────────────
    size_main = 210
    fnt_main  = ImageFont.truetype(FONT_REG, size_main)
    text_main = "StillWave"
    bb = fnt_main.getbbox(text_main)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    tx = (W - tw) // 2 - bb[0]
    ty = H // 2 - th // 2 - bb[1] - 60

    draw.text((tx, ty), text_main, font=fnt_main, fill=GOLD)

    # ── Tagline ──────────────────────────────────────────────────────────────
    size_tag = 72
    fnt_tag  = ImageFont.truetype(FONT_REG, size_tag)
    text_tag = "Sleep  ·  Focus  ·  Meditation"
    bb2 = fnt_tag.getbbox(text_tag)
    tw2 = bb2[2] - bb2[0]
    tx2 = (W - tw2) // 2 - bb2[0]
    ty2 = ty + th + 55

    draw.text((tx2, ty2), text_tag, font=fnt_tag, fill=GOLD)

    # ── Safe-zone guide lines (not saved — just debug) ─────────────────────
    # safe zone: 1546×423 centred → x 507..2053, y 509..931
    # (not drawn in output)

    canvas.save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT}  ({W}×{H}, {OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    make_banner()
