#!/usr/bin/env python3
"""
StillWave ензō emboss stamp v8.

- Deep navy convex dome inside the ензō circle (radial gradient + specular)
- ензō + wave embossed on dome surface (shadow right-down, highlight left-up)
- Wave blue recoloured → gold for contrast on navy
- Circular mask: nothing outside the ензō bounding circle
- Transparent background

Output: stillwave-stamp-v8-emboss.png (800×800)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

HERE = Path(__file__).parent
SRC  = HERE / "stillwave-logo-source-v2.jpg"
OUT  = HERE / "stillwave-stamp-v8-emboss.png"

NAVY     = (10, 14, 30)
NAVY_MID = (20, 32, 60)
BADGE    = 800


def extract_mark():
    img = Image.open(SRC).convert("RGBA")
    arr = np.array(img)
    h, w = arr.shape[:2]
    arr[:int(h * 0.10), :int(w * 0.10)] = [255, 255, 255, 255]

    rgb = arr[:, :, :3].astype(np.int16)
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    is_bg = ((r > 235) & (g > 235) & (b > 230)) & ((np.abs(r - g) < 15) & (np.abs(g - b) < 15))
    brightness = (r.astype(np.float32) + g + b) / 3.0
    alpha = np.clip((245.0 - brightness) / 25.0 * 255, 0, 255).astype(np.uint8)
    alpha = np.where(is_bg, 0, alpha)
    is_gold = (r > 150) & (g > 110) & (b < 170) & (r > b + 20)
    is_blue = (b > r.astype(np.int16) + 5) & (b > 130)
    alpha = np.where(is_gold | is_blue, 255, alpha)
    arr[:, :, 3] = alpha

    ys, xs = np.where(arr[:int(h * 0.62), :, 3] > 30)
    pad = 28
    x0 = max(xs.min() - pad, 0)
    x1 = min(xs.max() + pad, w)
    y0 = max(ys.min() - pad, 0)
    y1 = min(ys.max() + pad, int(h * 0.62))
    return Image.fromarray(arr, "RGBA").crop((x0, y0, x1, y1))


def build():
    mark = extract_mark()
    ma   = np.array(mark)[:, :, 3]
    ys, xs = np.where(ma > 50)
    cx = int((xs.min() + xs.max()) // 2)
    cy = int((ys.min() + ys.max()) // 2)
    outer_r = int(min(xs.max() - xs.min(), ys.max() - ys.min()) // 2)
    inner_r = int(outer_r * 0.97)
    mw, mh  = mark.size

    # ── Navy convex dome ──────────────────────────────────────────────────
    dome = Image.new("RGBA", (mw, mh), (0, 0, 0, 0))
    dd   = ImageDraw.Draw(dome)
    steps = 50
    for i in range(steps, -1, -1):
        t  = i / steps
        cr = int(inner_r * (i + 1) / (steps + 1))
        col = (
            int(NAVY[0] + (NAVY_MID[0] - NAVY[0]) * t),
            int(NAVY[1] + (NAVY_MID[1] - NAVY[1]) * t),
            int(NAVY[2] + (NAVY_MID[2] - NAVY[2]) * t),
            255,
        )
        dd.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=col)

    # Specular highlight top-left
    hi = Image.new("RGBA", (mw, mh), (0, 0, 0, 0))
    hd = ImageDraw.Draw(hi)
    hx, hy = int(cx - inner_r * 0.20), int(cy - inner_r * 0.25)
    for s in range(22, 0, -1):
        av = int(60 * (s / 22))
        sw = int(inner_r * 0.55 * s / 22)
        sh = int(inner_r * 0.32 * s / 22)
        hd.ellipse([hx - sw, hy - sh, hx + sw, hy + sh], fill=(255, 235, 180, av))
    hi = hi.filter(ImageFilter.GaussianBlur(radius=mw // 14))
    dome.alpha_composite(hi)

    # ── Prepare mark: recolour wave blue → gold ───────────────────────────
    mark_arr = np.array(mark).copy()
    r8, g8, b8, a8 = (mark_arr[:, :, c] for c in range(4))
    is_wave = (b8.astype(int) > r8.astype(int) + 5) & (b8 > 100) & (a8 > 30)
    mark_arr[:, :, 0] = np.where(is_wave, 200, r8)
    mark_arr[:, :, 1] = np.where(is_wave, 162, g8)
    mark_arr[:, :, 2] = np.where(is_wave,  48, b8)
    mark_gold = Image.fromarray(mark_arr, "RGBA")

    # Shadow: dark, shifted +3 +3 (bottom-right depth)
    shd = mark_arr.copy()
    shd[:, :, :3] = [4, 6, 15]
    shd[:, :, 3]  = (a8.astype(float) * 0.55).astype(np.uint8)
    shd_img = Image.fromarray(shd, "RGBA")

    # Highlight: bright gold, shifted -2 -2 (top-left light)
    hil = mark_arr.copy()
    hil[:, :, :3] = [255, 245, 170]
    hil[:, :, 3]  = (a8.astype(float) * 0.45).astype(np.uint8)
    hil_img = Image.fromarray(hil, "RGBA")

    # ── Composite: dome → shadow → highlight → mark ───────────────────────
    result = dome.copy()

    shd_canvas = Image.new("RGBA", (mw, mh), (0, 0, 0, 0))
    shd_canvas.alpha_composite(shd_img, (3, 3))
    result.alpha_composite(shd_canvas)

    hil_canvas = Image.new("RGBA", (mw, mh), (0, 0, 0, 0))
    hil_canvas.paste(hil_img, (-2, -2))
    result.alpha_composite(hil_canvas)

    result.alpha_composite(mark_gold)

    # ── Circular mask: nothing outside ензō bounding circle ───────────────
    circ = Image.new("L", (mw, mh), 0)
    ImageDraw.Draw(circ).ellipse(
        [cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r], fill=255)
    out_arr = np.array(result)
    out_arr[:, :, 3] = np.minimum(out_arr[:, :, 3], np.array(circ))
    result = Image.fromarray(out_arr, "RGBA")

    # ── Crop + resize ─────────────────────────────────────────────────────
    pad   = max(4, int(outer_r * 0.02))
    stamp = result.crop((cx - outer_r - pad, cy - outer_r - pad,
                         cx + outer_r + pad, cy + outer_r + pad))
    stamp = stamp.resize((BADGE, BADGE), Image.LANCZOS)
    stamp.save(OUT, "PNG")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")
    return stamp


if __name__ == "__main__":
    build()
