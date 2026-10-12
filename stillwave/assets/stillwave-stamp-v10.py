#!/usr/bin/env python3
"""
StillWave ензō stamp v10.

- Interior found by flood-fill: navy fills EXACTLY inside ензо, no leaking
- Thin geometric gold ring drawn first → closes the open gap of the brushstroke
- Source ензо brushstroke (gold) composited on top for organic texture
- Wave (bright blue) inside on navy
- Strict circular clip at outer edge
- Transparent outside

Output: stillwave-stamp-v10.png (800×800)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

HERE  = Path(__file__).parent
SRC   = HERE / "stillwave-logo-source-v2.jpg"
OUT   = HERE / "stillwave-stamp-v10.png"

NAVY      = (10, 14, 30)
GOLD      = (201, 168, 76)
WAVE_BLUE = (80, 150, 220)
BADGE     = 800


def extract_mark():
    img = Image.open(SRC).convert("RGBA")
    arr = np.array(img)
    h, w = arr.shape[:2]
    arr[:int(h * 0.10), :int(w * 0.10)] = [255, 255, 255, 255]
    rgb = arr[:, :, :3].astype(np.int16)
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    is_bg = ((r > 235) & (g > 235) & (b > 230)) & (np.abs(r-g) < 15) & (np.abs(g-b) < 15)
    brightness = (r.astype(np.float32) + g + b) / 3.0
    alpha = np.clip((245.0 - brightness) / 25.0 * 255, 0, 255).astype(np.uint8)
    alpha = np.where(is_bg, 0, alpha)
    is_gold = (r > 150) & (g > 110) & (b < 170) & (r > b + 20)
    is_blue = (b > r + 5) & (b > 130)
    alpha = np.where(is_gold | is_blue, 255, alpha)
    arr[:, :, 3] = alpha
    ys, xs = np.where(arr[:int(h * 0.62), :, 3] > 30)
    pad = 28
    x0, x1 = max(xs.min()-pad, 0), min(xs.max()+pad, w)
    y0, y1 = max(ys.min()-pad, 0), min(ys.max()+pad, int(h * 0.62))
    return Image.fromarray(arr, "RGBA").crop((x0, y0, x1, y1))


def get_interior(alpha_arr, mw, mh):
    """Flood-fill from all 4 corners through non-stroke pixels.
    Returns bool mask: True = inside the ензо ring."""
    # Dilate stroke to close brush gaps before flood fill
    stroke = Image.fromarray((alpha_arr > 30).astype(np.uint8) * 255, "L")
    stroke = stroke.filter(ImageFilter.MaxFilter(size=11))

    # Canvas: 255 = open space (fillable), 0 = stroke (barrier)
    fc = np.where(np.array(stroke) > 128, 0, 255).astype(np.uint8)
    fill_img = Image.fromarray(fc, "L")

    # Flood fill from all 4 corners — marks outside regions as 0
    for pt in [(0, 0), (mw-1, 0), (0, mh-1), (mw-1, mh-1)]:
        ImageDraw.floodfill(fill_img, pt, 0)

    # Remaining 255 pixels = inside the ензо ring
    return np.array(fill_img) > 128


def recolour(arr):
    """Force ензо → GOLD, wave → bright WAVE_BLUE."""
    arr = arr.copy()
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    ri, gi, bi = r.astype(np.int16), g.astype(np.int16), b.astype(np.int16)
    is_g = (ri > 100) & (gi > 80) & (bi < 160) & (ri > bi + 15) & (a > 30)
    is_b = (bi > ri + 5) & (bi > 100) & (a > 30)
    arr[:,:,0] = np.where(is_g, GOLD[0], np.where(is_b, WAVE_BLUE[0], r))
    arr[:,:,1] = np.where(is_g, GOLD[1], np.where(is_b, WAVE_BLUE[1], g))
    arr[:,:,2] = np.where(is_g, GOLD[2], np.where(is_b, WAVE_BLUE[2], b))
    return arr


def build():
    mark = extract_mark()
    mw, mh = mark.size
    ma = np.array(mark)[:, :, 3]

    ys, xs = np.where(ma > 50)
    cx = int((xs.min() + xs.max()) // 2)
    cy = int((ys.min() + ys.max()) // 2)
    outer_r = int(min(xs.max() - xs.min(), ys.max() - ys.min()) // 2)

    interior = get_interior(ma, mw, mh)
    mark_arr = recolour(np.array(mark))

    # ── Layer 1: navy exactly at interior pixels ──────────────────────────
    navy_arr = np.zeros((mh, mw, 4), dtype=np.uint8)
    navy_arr[interior, 0] = NAVY[0]
    navy_arr[interior, 1] = NAVY[1]
    navy_arr[interior, 2] = NAVY[2]
    navy_arr[interior, 3] = 255
    canvas = Image.fromarray(navy_arr, "RGBA")

    # ── Layer 2: geometric gold ring — closes the open brush gap ─────────
    ring_w = max(12, outer_r // 6)
    ring_img = Image.new("RGBA", (mw, mh), (0, 0, 0, 0))
    ImageDraw.Draw(ring_img).ellipse(
        [cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r],
        outline=(*GOLD, 255), width=ring_w)
    canvas.alpha_composite(ring_img)

    # ── Layer 3: brushstroke ензо (gold) + wave (blue) ───────────────────
    canvas.alpha_composite(Image.fromarray(mark_arr, "RGBA"))

    # ── Circular clip at outer_r ──────────────────────────────────────────
    circ = Image.new("L", (mw, mh), 0)
    ImageDraw.Draw(circ).ellipse(
        [cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r], fill=255)
    out_arr = np.array(canvas)
    out_arr[:, :, 3] = np.minimum(out_arr[:, :, 3], np.array(circ))
    result = Image.fromarray(out_arr, "RGBA")

    # ── Crop + resize ─────────────────────────────────────────────────────
    pad   = max(4, int(outer_r * 0.02))
    stamp = result.crop((cx - outer_r - pad, cy - outer_r - pad,
                         cx + outer_r + pad, cy + outer_r + pad))
    stamp = stamp.resize((BADGE, BADGE), Image.LANCZOS)
    stamp.save(OUT, "PNG")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build()
