#!/usr/bin/env python3
"""
StillWave logo: gold ensō + cream wave + dark navy bg.
Recolors the base mark and outputs a circular badge + preview on YouTube dark.

Outputs:
  stillwave-logo-gold-cream-navy.png  — 800×800 badge (for YouTube avatar)
  stillwave-logo-gold-cream-navy-preview.jpg — YouTube layout mockup
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np

HERE = Path(__file__).parent
SRC  = HERE / "stillwave-mark-v3.png"
OUT  = HERE / "stillwave-logo-gold-cream-navy.png"
PREV = HERE / "stillwave-logo-gold-cream-navy-preview.jpg"

GOLD_HEX  = "#C9A84C"   # warm premium gold
CREAM_HEX = "#EAE0C8"   # cream wave — high contrast on navy
NAVY_HEX  = "#12151E"   # deep navy — matches YouTube dark theme

BADGE_SIZE = 800


def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple(int(s[i:i+2], 16) for i in (0, 2, 4))


def recolor(src: Image.Image, ring_hex: str, wave_hex: str) -> Image.Image:
    arr = np.array(src, dtype=np.uint8)
    rgb = arr[:, :, :3].astype(np.float32) / 255.0
    a   = arr[:, :, 3]

    mx   = rgb.max(axis=2)
    mn   = rgb.min(axis=2)
    diff = mx - mn
    val  = mx

    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    rc = (mx - r) / np.maximum(diff, 1e-6)
    gc = (mx - g) / np.maximum(diff, 1e-6)
    bc = (mx - b) / np.maximum(diff, 1e-6)
    h = np.where(mx == r, (bc - gc) % 6,
        np.where(mx == g, 2.0 + rc - bc, 4.0 + gc - rc))
    h = (h * 60.0) % 360.0
    h = np.where(diff > 1e-6, h, 0)

    is_gold = (h >= 25) & (h <= 65)  & (diff > 0.15) & (a > 30)
    is_blue = (h >= 170) & (h <= 250) & (diff > 0.05) & (a > 30)

    ring_rgb = np.array(hex_to_rgb(ring_hex), dtype=np.float32) / 255.0
    wave_rgb = np.array(hex_to_rgb(wave_hex), dtype=np.float32) / 255.0

    out_rgb = rgb.copy()
    out_rgb = np.where(is_gold[..., None], ring_rgb * val[..., None], out_rgb)
    out_rgb = np.where(is_blue[..., None], wave_rgb * np.clip(val[..., None] * 1.3, 0, 1), out_rgb)

    out = arr.copy()
    out[:, :, :3] = np.clip(out_rgb * 255.0, 0, 255).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def make_badge(mark: Image.Image, bg_rgb, size=800) -> Image.Image:
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([0, 0, size-1, size-1], fill=(*bg_rgb, 255))

    inner = int(size * 0.74)
    mw, mh = mark.size
    ratio = min(inner / mw, inner / mh)
    nm = mark.resize((int(mw * ratio), int(mh * ratio)), Image.LANCZOS)
    px = (size - nm.size[0]) // 2
    py = (size - nm.size[1]) // 2 - int(size * 0.03)   # slight upward nudge
    img.alpha_composite(nm, (px, py))
    return img


def make_preview(badge: Image.Image):
    """Simple YouTube-style dark panel showing the badge in context."""
    W, H = 900, 260
    YT_DARK = (15, 15, 20)
    canvas = Image.new("RGB", (W, H), YT_DARK)
    draw   = ImageDraw.Draw(canvas)

    # Avatar at left
    av_size = 180
    av = badge.resize((av_size, av_size), Image.LANCZOS)
    # circular mask
    mask = Image.new("L", (av_size, av_size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, av_size-1, av_size-1], fill=255)
    av.putalpha(mask)
    canvas.paste(av.convert("RGB"), (40, 40), av)

    try:
        fn = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 28)
        fs = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 16)
        fi = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf", 14)
    except OSError:
        fn = fs = fi = ImageFont.load_default()

    tx = 40 + av_size + 24
    draw.text((tx, 52),  "StillWave",                                     font=fn, fill=(255,255,255))
    draw.text((tx, 90),  "@stillwavezen  ·  52 subscribers  ·  47 videos",font=fs, fill=(160,160,170))
    draw.text((tx, 114), "Welcome to StillWave — your sanctuary of sound.",font=fs, fill=(130,130,140))
    draw.text((tx, 148), "SLEEP  ·  FOCUS  ·  MEDITATION",                font=fi, fill=(140,140,150))

    # Color swatches annotation
    swatch_y = 200
    for i, (label, hexc) in enumerate([
        ("gold ензō", GOLD_HEX), ("cream wave", CREAM_HEX), ("navy bg", NAVY_HEX)
    ]):
        sx = 40 + i * 200
        draw.rectangle([sx, swatch_y, sx+24, swatch_y+16],
                       fill=hex_to_rgb(hexc), outline=(80,80,90))
        draw.text((sx+30, swatch_y), f"{label} {hexc}", font=fi, fill=(180,180,190))

    canvas.save(PREV, "JPEG", quality=93)
    print(f"Wrote {PREV} ({PREV.stat().st_size // 1024} KB)")


def main():
    mark  = recolor(Image.open(SRC).convert("RGBA"), GOLD_HEX, CREAM_HEX)
    badge = make_badge(mark, hex_to_rgb(NAVY_HEX), BADGE_SIZE)
    badge.save(OUT, "PNG")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")
    make_preview(badge)


if __name__ == "__main__":
    main()
