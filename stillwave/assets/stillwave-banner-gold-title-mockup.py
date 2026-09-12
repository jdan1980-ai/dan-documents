#!/usr/bin/env python3
"""
StillWave brand cohesion mockup — banner with GOLD "StillWave" title + new logo avatar.

Recreates the channel banner approximation (dark misty bg + starfield) with the
title recolored to gold #C9A84C, paired with the new gold-ensō avatar to show how
the brand reads when colors are unified.

Output: stillwave-banner-gold-title-mockup.jpg
"""

import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE   = Path(__file__).parent
LOGO   = HERE / "stillwave-logo-gold-cream-navy.png"
OUT    = HERE / "stillwave-banner-gold-title-mockup.jpg"

W, H        = 1500, 700
BANNER_H    = 380

GOLD        = (201, 168, 76)        # #C9A84C — matches logo ring
GOLD_LIGHT  = (230, 200, 110)       # subtle highlight
CREAM       = (245, 234, 210)
GRAY        = (160, 160, 170)
DIM_GRAY    = (130, 130, 145)
WHITE       = (255, 255, 255)
YT_BG       = (15, 15, 20)


def draw_banner(canvas: Image.Image, x: int, y: int, w: int, h: int):
    """Misty dark banner with star particles."""
    draw = ImageDraw.Draw(canvas)
    # Vertical gradient: deep navy → slightly lighter
    for i in range(h):
        t = i / h
        r = int(14 + 12 * t)
        g = int(16 + 10 * t)
        b = int(24 + 14 * t)
        draw.line([(x, y + i), (x + w, y + i)], fill=(r, g, b))

    # Star particles
    rng = random.Random(7)
    for _ in range(140):
        px = x + rng.randint(0, w)
        py = y + rng.randint(0, int(h * 0.65))
        a  = rng.randint(80, 200)
        r  = rng.randint(1, 2)
        draw.ellipse([px - r, py - r, px + r, py + r],
                     fill=(a, a, a + 15))

    # Soft horizontal mist near bottom
    for i in range(int(h * 0.4)):
        t = i / (h * 0.4)
        alpha = int(40 * (1 - t))
        if alpha < 1:
            continue
        overlay = Image.new("RGBA", (w, 1), (40, 50, 70, alpha))
        canvas.paste(overlay, (x, y + h - i), overlay)


def draw_banner_text(canvas: Image.Image, x: int, y: int, w: int, h: int):
    draw = ImageDraw.Draw(canvas)
    try:
        small  = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 18)
        big    = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf", 110)
        tag    = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 22)
    except OSError:
        small = big = tag = ImageFont.load_default()

    cx = x + w // 2

    # Top tagline
    tagline = "YOUR  SANCTUARY  OF  SOUND"
    bb = small.getbbox(tagline)
    draw.text((cx - (bb[2] - bb[0]) // 2, y + 50),
              tagline, font=small, fill=DIM_GRAY)

    # GOLD title with subtle inner highlight
    title = "StillWave"
    tb = big.getbbox(title)
    tx = cx - (tb[2] - tb[0]) // 2 - tb[0]
    ty = y + 80 - tb[1]
    # soft shadow
    draw.text((tx + 3, ty + 3), title, font=big, fill=(0, 0, 0, 180))
    # main gold fill
    draw.text((tx, ty), title, font=big, fill=GOLD)

    # Thin divider
    lw = 180
    draw.line([(cx - lw, y + 245), (cx + lw, y + 245)],
              fill=(110, 95, 50), width=1)

    # Sub-tagline
    sub = "SLEEP    ·    FOCUS    ·    MEDITATION"
    sb = tag.getbbox(sub)
    draw.text((cx - (sb[2] - sb[0]) // 2, y + 260),
              sub, font=tag, fill=GRAY)


def paste_avatar(canvas: Image.Image, logo_path: Path, cx: int, cy: int, r: int):
    if not logo_path.exists():
        return
    logo = Image.open(logo_path).convert("RGBA")
    size = r * 2
    logo = logo.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size - 1, size - 1], fill=255)
    logo.putalpha(mask)
    canvas.paste(logo, (cx - r, cy - r), logo)


def main():
    canvas = Image.new("RGB", (W, H), YT_BG)

    # Banner top
    margin = 40
    bx, by = margin, 30
    bw, bh = W - 2 * margin, BANNER_H
    draw_banner(canvas, bx, by, bw, bh)
    draw_banner_text(canvas, bx, by, bw, bh)

    # Avatar + channel row below banner
    av_r = 88
    av_cx = margin + 30 + av_r
    av_cy = by + bh + 50 + av_r
    paste_avatar(canvas, LOGO, av_cx, av_cy, av_r)

    draw = ImageDraw.Draw(canvas)
    try:
        fn = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 34)
        fs = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 18)
        fi = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf", 16)
    except OSError:
        fn = fs = fi = ImageFont.load_default()

    tx = av_cx + av_r + 32
    draw.text((tx, av_cy - 50), "StillWave",                                       font=fn, fill=WHITE)
    draw.text((tx, av_cy - 8),  "@stillwavezen   ·   52 subscribers   ·   47 videos", font=fs, fill=GRAY)
    draw.text((tx, av_cy + 22), "Welcome to StillWave — your sanctuary of sound.", font=fs, fill=DIM_GRAY)

    # Footer note
    note = "Mockup: gold #C9A84C title in banner unifies brand with new logo (same gold ензō)."
    nb = fi.getbbox(note)
    draw.text((W // 2 - (nb[2] - nb[0]) // 2, H - 28),
              note, font=fi, fill=(95, 95, 110))

    canvas.save(OUT, "JPEG", quality=93, optimize=True)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
