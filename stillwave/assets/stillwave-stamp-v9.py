#!/usr/bin/env python3
"""
StillWave ензō stamp v9 — exactly as sketched.

  - ензō brushstroke = GOLD ring
  - Inside = deep navy fill
  - Wave = bright blue on navy (visible contrast)
  - Outside = transparent

Output: stillwave-stamp-v9.png (800×800 RGBA)
"""

from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np

HERE  = Path(__file__).parent
SRC   = HERE / "stillwave-logo-source-v2.jpg"
OUT   = HERE / "stillwave-stamp-v9.png"

NAVY       = (10, 14, 30)       # deep navy fill
GOLD       = (201, 168, 76)     # #C9A84C brand gold
WAVE_BLUE  = (80, 150, 220)     # bright blue so wave reads on navy
BADGE      = 800


def extract_mark():
    img = Image.open(SRC).convert("RGBA")
    arr = np.array(img)
    h, w = arr.shape[:2]

    # Mask AI editor badge top-left
    arr[:int(h * 0.10), :int(w * 0.10)] = [255, 255, 255, 255]

    rgb = arr[:, :, :3].astype(np.int16)
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    # White bg → transparent
    is_bg = ((r > 235) & (g > 235) & (b > 230)) & (np.abs(r - g) < 15) & (np.abs(g - b) < 15)
    brightness = (r.astype(np.float32) + g + b) / 3.0
    alpha = np.clip((245.0 - brightness) / 25.0 * 255, 0, 255).astype(np.uint8)
    alpha = np.where(is_bg, 0, alpha)

    is_gold = (r > 150) & (g > 110) & (b < 170) & (r > b + 20)
    is_blue = (b > r + 5) & (b > 130)
    alpha = np.where(is_gold | is_blue, 255, alpha)
    arr[:, :, 3] = alpha

    # Crop to mark only (upper 62% — no text)
    ys, xs = np.where(arr[:int(h * 0.62), :, 3] > 30)
    pad = 28
    x0 = max(xs.min() - pad, 0);  x1 = min(xs.max() + pad, w)
    y0 = max(ys.min() - pad, 0);  y1 = min(ys.max() + pad, int(h * 0.62))
    return Image.fromarray(arr, "RGBA").crop((x0, y0, x1, y1))


def recolour(mark: Image.Image) -> Image.Image:
    """Force ензō pixels → GOLD, wave pixels → WAVE_BLUE."""
    arr = np.array(mark).copy()
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]

    ri, gi, bi = r.astype(np.int16), g.astype(np.int16), b.astype(np.int16)

    is_gold_src = (ri > 100) & (gi > 80)  & (bi < 160) & (ri > bi + 15) & (a > 30)
    is_blue_src = (bi > ri + 5) & (bi > 100) & (a > 30)

    # Paint ензō → brand gold
    arr[:,:,0] = np.where(is_gold_src, GOLD[0], r)
    arr[:,:,1] = np.where(is_gold_src, GOLD[1], g)
    arr[:,:,2] = np.where(is_gold_src, GOLD[2], b)

    # Paint wave → bright blue
    arr[:,:,0] = np.where(is_blue_src, WAVE_BLUE[0], arr[:,:,0])
    arr[:,:,1] = np.where(is_blue_src, WAVE_BLUE[1], arr[:,:,1])
    arr[:,:,2] = np.where(is_blue_src, WAVE_BLUE[2], arr[:,:,2])

    return Image.fromarray(arr, "RGBA")


def build():
    mark = extract_mark()
    mark = recolour(mark)

    ma = np.array(mark)[:, :, 3]
    ys, xs = np.where(ma > 50)
    cx = int((xs.min() + xs.max()) // 2)
    cy = int((ys.min() + ys.max()) // 2)
    outer_r = int(min(xs.max() - xs.min(), ys.max() - ys.min()) // 2)
    inner_r = outer_r  # disc fills all the way to ензō ring
    mw, mh  = mark.size

    # Navy disc sized to fill inside ензō
    disc = Image.new("RGBA", (mw, mh), (0, 0, 0, 0))
    ImageDraw.Draw(disc).ellipse(
        [cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r],
        fill=(*NAVY, 255))

    # Composite: navy disc below, gold ензō + wave on top
    result = Image.alpha_composite(disc, mark)

    # Strict circular clip — nothing outside ензō bounding circle
    circ = Image.new("L", (mw, mh), 0)
    ImageDraw.Draw(circ).ellipse(
        [cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r], fill=255)
    out_arr = np.array(result)
    out_arr[:, :, 3] = np.minimum(out_arr[:, :, 3], np.array(circ))
    result = Image.fromarray(out_arr, "RGBA")

    # Crop tight + resize to 800×800
    pad   = max(4, int(outer_r * 0.02))
    stamp = result.crop((cx - outer_r - pad, cy - outer_r - pad,
                         cx + outer_r + pad, cy + outer_r + pad))
    stamp = stamp.resize((BADGE, BADGE), Image.LANCZOS)
    stamp.save(OUT, "PNG")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build()
