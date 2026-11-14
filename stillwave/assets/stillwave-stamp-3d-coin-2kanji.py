#!/usr/bin/env python3
"""
StillWave coin stamp with 静波 (2 kanji = StillWave in Japanese).
静 = still/quiet   波 = wave

Two layouts:
  A — horizontal  静 波  (side by side)
  B — vertical    静
                  波  (tategaki style)

Grid comparison on MAKOTO frame.
"""

import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE   = Path(__file__).parent
MAKOTO = HERE / "makoto-the-last-samurai-source.jpg"
SIZE   = 512

GOLD       = (201, 168, 76)
GOLD_DARK  = (100,  78, 20)
GOLD_LIGHT = (255, 230, 130)
GOLD_MID   = (180, 145, 55)
NAVY       = (14,  22, 42)
NAVY_LIGHT = (38,  58, 100)
NAVY_DARK  = (6,   10, 22)


def get_font(size_px):
    try:
        return ImageFont.truetype(
            "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf", size_px)
    except OSError:
        return ImageFont.load_default()


def make_coin_base(size) -> Image.Image:
    """Radial gradient navy disc + specular dome + gold ring."""
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx = cy = size // 2
    r  = size // 2 - 8

    # Radial gradient base
    steps = 40
    for i in range(steps, -1, -1):
        t  = i / steps
        cr = int(r * (i + 1) / (steps + 1))
        col = (
            int(NAVY_DARK[0] + (NAVY_LIGHT[0] - NAVY_DARK[0]) * t),
            int(NAVY_DARK[1] + (NAVY_LIGHT[1] - NAVY_DARK[1]) * t),
            int(NAVY_DARK[2] + (NAVY_LIGHT[2] - NAVY_DARK[2]) * t),
            255,
        )
        draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=col)

    # Specular dome highlight
    hi = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    hd = ImageDraw.Draw(hi)
    hx = int(cx - r * 0.22)
    hy = int(cy - r * 0.22)
    hr = int(r * 0.55)
    for s in range(20, 0, -1):
        alpha = int(75 * (s / 20))
        sr    = int(hr * s / 20)
        hd.ellipse([hx - sr, hy - sr, hx + sr, hy + sr],
                   fill=(255, 255, 255, alpha))
    hi = hi.filter(ImageFilter.GaussianBlur(radius=size // 18))
    img.alpha_composite(hi)

    # Gold ring (two-tone bevel)
    ring_w = max(8, size // 18)
    draw2  = ImageDraw.Draw(img)
    draw2.ellipse([cx - r, cy - r, cx + r, cy + r],
                  outline=GOLD_DARK, width=ring_w + 2)
    draw2.ellipse([cx - r + 2, cy - r + 2, cx + r - 2, cy + r - 2],
                  outline=GOLD_LIGHT, width=ring_w - 4)
    draw2.ellipse([cx - r + ring_w // 4, cy - r + ring_w // 4,
                   cx + r - ring_w // 4, cy + r - ring_w // 4],
                  outline=GOLD_MID, width=2)

    # Circular mask
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size - 1, size - 1], fill=255)
    img.putalpha(mask)
    return img


def add_kanji_horizontal(img: Image.Image, size: int) -> Image.Image:
    """静 波 side by side, centred."""
    draw = ImageDraw.Draw(img)
    cx = cy = size // 2
    fnt  = get_font(int(size * 0.36))   # slightly smaller to fit two chars
    gap  = int(size * 0.04)

    total_w = 0
    char_data = []
    for ch in "静波":
        bb = fnt.getbbox(ch)
        w  = bb[2] - bb[0]
        char_data.append((ch, bb, w))
        total_w += w
    total_w += gap

    x = cx - total_w // 2
    for ch, bb, w in char_data:
        tx = x - bb[0]
        ty = cy - (bb[3] - bb[1]) // 2 - bb[1]
        draw.text((tx + 2, ty + 2), ch, font=fnt, fill=(*GOLD_DARK, 200))
        draw.text((tx, ty),         ch, font=fnt, fill=(*GOLD_LIGHT, 255))
        x += w + gap

    return img


def add_kanji_vertical(img: Image.Image, size: int) -> Image.Image:
    """静 over 波, vertically centred (tategaki)."""
    draw = ImageDraw.Draw(img)
    cx = cy = size // 2
    fnt  = get_font(int(size * 0.36))
    gap  = int(size * 0.02)

    heights = []
    for ch in "静波":
        bb = fnt.getbbox(ch)
        heights.append(bb[3] - bb[1])

    total_h = sum(heights) + gap
    y = cy - total_h // 2

    for ch in "静波":
        bb = fnt.getbbox(ch)
        w  = bb[2] - bb[0]
        tx = cx - w // 2 - bb[0]
        ty = y - bb[1]
        draw.text((tx + 2, ty + 2), ch, font=fnt, fill=(*GOLD_DARK, 200))
        draw.text((tx, ty),         ch, font=fnt, fill=(*GOLD_LIGHT, 255))
        y += (bb[3] - bb[1]) + gap

    return img


def build_grid(variants):
    STAMP_PX = 160
    MARGIN   = 36
    bg_src   = Image.open(MAKOTO).convert("RGB").resize((1920, 1080))
    n        = len(variants)
    W        = 1920 * n + 24 * (n - 1)
    canvas   = Image.new("RGB", (W, 1080 + 90), (12, 14, 20))

    try:
        lf = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 30)
    except OSError:
        lf = ImageFont.load_default()

    for i, (label, stamp) in enumerate(variants):
        x_off = i * (1920 + 24)
        frame = bg_src.copy().convert("RGBA")
        s     = stamp.resize((STAMP_PX, STAMP_PX), Image.LANCZOS)
        frame.alpha_composite(s, (1920 - STAMP_PX - MARGIN,
                                  1080 - STAMP_PX - MARGIN))
        canvas.paste(frame.convert("RGB"), (x_off, 0))
        draw = ImageDraw.Draw(canvas)
        draw.rectangle([x_off, 1080, x_off + 1920, 1170], fill=(18, 22, 34))
        draw.text((x_off + 24, 1090), label, font=lf, fill=GOLD)

    return canvas


def main():
    base_h = make_coin_base(SIZE)
    base_v = make_coin_base(SIZE)

    coin_h = add_kanji_horizontal(base_h.copy(), SIZE)
    coin_v = add_kanji_vertical(base_v.copy(), SIZE)

    coin_h.save(HERE / "stillwave-stamp-coin-静波-horizontal.png", "PNG")
    coin_v.save(HERE / "stillwave-stamp-coin-静波-vertical.png",   "PNG")
    print("Stamps saved.")

    grid = build_grid([
        ("A — 静波 горизонтально (side by side)", coin_h),
        ("B — 静波 вертикально  (tategaki)",      coin_v),
    ])
    out = HERE / "stillwave-stamp-coin-静波-grid.jpg"
    grid.save(out, "JPEG", quality=93, optimize=True)
    print(f"Wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
