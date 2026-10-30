#!/usr/bin/env python3
"""
Generate StillWave logo color variants.

Source: stillwave-mark-v3.png (gold ensō + blue wave, transparent bg)
Approach: HSV-based recoloring — find gold pixels, remap to target ring hue;
find blue pixels, remap to target wave hue. Preserve luminance/texture.

Outputs a grid mockup + individual PNGs per variant.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import colorsys

HERE = Path(__file__).parent
SRC  = HERE / "stillwave-mark-v3.png"
GRID = HERE / "stillwave-logo-color-variants.jpg"


VARIANTS = [
    # (label, ring_hex, wave_hex, bg_hex)
    ("Current — Gold + Blue",      "#C9A84C", "#7FB3D5", "#F5EAD2"),  # baseline
    ("Moonlight — Silver + Indigo","#C9CDD4", "#3D5A80", "#1B1F2A"),
    ("Sunset — Copper + Amber",    "#B87333", "#D9874E", "#F5EAD2"),
    ("Sumi-e — Ink + Indigo",      "#1A1A1A", "#2E4A6B", "#F2EBD8"),
    ("Bamboo — Jade + Teal",       "#5A8A6E", "#7FB3A8", "#F5EAD2"),
    ("Sakura — Rose + Lilac",      "#D4849C", "#A89BC9", "#FBEFEF"),
    ("Night — Charcoal + Teal",    "#3A3F4A", "#5AC8B8", "#0A0A12"),
    ("Royal — Deep Gold + Cobalt", "#B8923A", "#2E5BAA", "#1A1A24"),
]


def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple(int(s[i:i+2], 16) for i in (0, 2, 4))


def recolor_mark(src: Image.Image, ring_hex: str, wave_hex: str) -> Image.Image:
    """Remap gold ring pixels → ring color, blue wave pixels → wave color."""
    arr = np.array(src, dtype=np.uint8)
    rgb = arr[:, :, :3].astype(np.float32) / 255.0
    a   = arr[:, :, 3]

    # Convert to HSV per-pixel
    mx = rgb.max(axis=2)
    mn = rgb.min(axis=2)
    val = mx
    diff = mx - mn
    sat = np.where(mx > 0, diff / np.maximum(mx, 1e-6), 0)

    # Hue (0..360)
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    h = np.zeros_like(mx)
    mask = diff > 1e-6
    rc = (mx - r) / np.maximum(diff, 1e-6)
    gc = (mx - g) / np.maximum(diff, 1e-6)
    bc = (mx - b) / np.maximum(diff, 1e-6)
    h_r = (bc - gc) % 6
    h_g = 2.0 + rc - bc
    h_b = 4.0 + gc - rc
    h = np.where(mx == r, h_r, np.where(mx == g, h_g, h_b))
    h = (h * 60.0) % 360.0
    h = np.where(mask, h, 0)

    # Gold pixels: hue 30..60 with sat > 0.25
    is_gold = (h >= 25) & (h <= 65) & (sat > 0.20) & (a > 30)
    # Blue pixels: hue 180..240 with sat > 0.10
    is_blue = (h >= 170) & (h <= 245) & (sat > 0.08) & (a > 30)

    ring_rgb = np.array(hex_to_rgb(ring_hex), dtype=np.float32)
    wave_rgb = np.array(hex_to_rgb(wave_hex), dtype=np.float32)

    out = arr.copy()
    # Apply ring color preserving original brightness
    v_ring = val[..., None]
    new_ring = ring_rgb / 255.0 * v_ring
    new_wave = wave_rgb / 255.0 * v_ring

    # blend by mask, modulated by saturation (so light highlights stay light)
    out_rgb = rgb.copy()
    out_rgb = np.where(is_gold[..., None], new_ring, out_rgb)
    out_rgb = np.where(is_blue[..., None], new_wave, out_rgb)
    out[:, :, :3] = np.clip(out_rgb * 255.0, 0, 255).astype(np.uint8)

    return Image.fromarray(out, "RGBA")


def make_badge(mark: Image.Image, bg_hex: str, size: int = 360) -> Image.Image:
    """Place recolored mark on a circular background of bg_hex."""
    bg_rgb = hex_to_rgb(bg_hex)
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([0, 0, size - 1, size - 1], fill=(*bg_rgb, 255))

    # Fit mark inside, leave ~12% padding
    inner = int(size * 0.76)
    mw, mh = mark.size
    ratio = min(inner / mw, inner / mh)
    nm = mark.resize((int(mw * ratio), int(mh * ratio)), Image.LANCZOS)
    px = (size - nm.size[0]) // 2
    py = (size - nm.size[1]) // 2
    img.alpha_composite(nm, (px, py))
    return img


def build_grid():
    src = Image.open(SRC).convert("RGBA")
    cols = 4
    rows = 2
    cell = 360
    label_h = 50
    pad = 20
    W = cols * cell + (cols + 1) * pad
    H = rows * (cell + label_h) + (rows + 1) * pad + 40  # header

    canvas = Image.new("RGB", (W, H), (24, 24, 30))
    draw = ImageDraw.Draw(canvas)

    try:
        title_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 22)
        label_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 16)
    except OSError:
        title_font = label_font = ImageFont.load_default()

    draw.text((pad, 10), "StillWave — color variants", font=title_font, fill=(245, 234, 210))

    for i, (label, ring_hex, wave_hex, bg_hex) in enumerate(VARIANTS):
        col = i % cols
        row = i // cols
        x = pad + col * (cell + pad)
        y = 40 + pad + row * (cell + label_h + pad)

        recolored = recolor_mark(src, ring_hex, wave_hex)
        badge = make_badge(recolored, bg_hex, size=cell)
        canvas.paste(badge.convert("RGB"), (x, y))

        # label below
        draw.text((x, y + cell + 6),
                  label, font=label_font, fill=(220, 220, 230))
        draw.text((x, y + cell + 26),
                  f"ring {ring_hex}   wave {wave_hex}   bg {bg_hex}",
                  font=label_font, fill=(150, 150, 160))

        # Save individual badge
        slug = label.split(" —")[0].lower().replace(" ", "-")
        badge.save(HERE / f"stillwave-logo-variant-{i:02d}-{slug}.png", "PNG")

    canvas.save(GRID, "JPEG", quality=92, optimize=True)
    print(f"Wrote {GRID} ({GRID.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build_grid()
