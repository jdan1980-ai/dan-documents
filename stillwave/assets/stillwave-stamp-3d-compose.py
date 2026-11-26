#!/usr/bin/env python3
"""
StillWave 波 stamp — three 3D effect variants.

1. COIN     — convex metallic dome, gold ring, highlight top-left
2. SEAL     — flat navy + ring inner shadow + 波 recessed (deboss)
3. EMBOSS   — matte navy + gold 波 with specular highlight stripe

Outputs:
  stillwave-stamp-3d-coin.png
  stillwave-stamp-3d-seal.png
  stillwave-stamp-3d-emboss.png
  stillwave-stamp-3d-grid.jpg   — side-by-side comparison on MAKOTO
"""

import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE   = Path(__file__).parent
MAKOTO = HERE / "makoto-the-last-samurai-source.jpg"
SIZE   = 512


GOLD        = (201, 168, 76)
GOLD_DARK   = (100,  78, 20)
GOLD_LIGHT  = (255, 230, 130)
GOLD_MID    = (180, 145, 55)
NAVY        = (14,  22, 42)
NAVY_LIGHT  = (38,  58, 100)
NAVY_DARK   = (6,   10, 22)
BLACK       = (0,   0,  0)
WHITE       = (255, 255, 255)


def get_font(size_px):
    try:
        return ImageFont.truetype(
            "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf", size_px)
    except OSError:
        return ImageFont.load_default()


def draw_kanji(draw, img_size, font, color, offset=(0, 0)):
    cx = cy = img_size // 2
    bb = font.getbbox("波")
    tx = cx - (bb[2] - bb[0]) // 2 - bb[0] + offset[0]
    ty = cy - (bb[3] - bb[1]) // 2 - bb[1] + offset[1]
    draw.text((tx, ty), "波", font=font, fill=color)


# ── 1. COIN ────────────────────────────────────────────────────────────────────
def make_coin(size) -> Image.Image:
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx = cy = size // 2
    r  = size // 2 - 8

    # Base disc — radial gradient simulated with concentric ellipses
    # Dark edge → mid navy toward center (3D depth)
    steps = 40
    for i in range(steps, -1, -1):
        t   = i / steps
        cr  = int(r * (i + 1) / (steps + 1))
        col = (
            int(NAVY_DARK[0] + (NAVY_LIGHT[0] - NAVY_DARK[0]) * t),
            int(NAVY_DARK[1] + (NAVY_LIGHT[1] - NAVY_DARK[1]) * t),
            int(NAVY_DARK[2] + (NAVY_LIGHT[2] - NAVY_DARK[2]) * t),
            255,
        )
        draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=col)

    # Specular dome highlight — top-left ellipse, soft
    hi = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    hd = ImageDraw.Draw(hi)
    hx = int(cx - r * 0.22)
    hy = int(cy - r * 0.22)
    hr = int(r * 0.55)
    for s in range(20, 0, -1):
        alpha = int(80 * (s / 20))
        sr    = int(hr * s / 20)
        hd.ellipse([hx - sr, hy - sr, hx + sr, hy + sr],
                   fill=(255, 255, 255, alpha))
    hi = hi.filter(ImageFilter.GaussianBlur(radius=size // 18))
    img.alpha_composite(hi)

    # Gold ring — two-tone (light top, dark bottom = convex edge)
    ring_w = max(8, size // 18)
    draw2  = ImageDraw.Draw(img)
    # Dark base ring
    draw2.ellipse([cx - r, cy - r, cx + r, cy + r],
                  outline=GOLD_DARK, width=ring_w + 2)
    # Light ring on top
    draw2.ellipse([cx - r + 2, cy - r + 2, cx + r - 2, cy + r - 2],
                  outline=GOLD_LIGHT, width=ring_w - 4)
    # Mid gold fill
    draw2.ellipse([cx - r + ring_w // 4, cy - r + ring_w // 4,
                   cx + r - ring_w // 4, cy + r - ring_w // 4],
                  outline=GOLD_MID, width=2)

    # Shadow under kanji (slight depth)
    fnt = get_font(int(size * 0.50))
    draw_kanji(draw2, size, fnt, (*GOLD_DARK, 200), offset=(3, 3))
    draw_kanji(draw2, size, fnt, (*GOLD_LIGHT, 255), offset=(0, 0))

    # Circular mask — transparent corners
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size - 1, size - 1], fill=255)
    img.putalpha(mask)
    return img


# ── 2. SEAL ────────────────────────────────────────────────────────────────────
def make_seal(size) -> Image.Image:
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx = cy = size // 2
    r  = size // 2 - 8
    ring_w = max(8, size // 18)

    # Flat navy disc
    draw.ellipse([cx - r - ring_w, cy - r - ring_w,
                  cx + r + ring_w, cy + r + ring_w], fill=(*NAVY, 255))

    # Inner bevel shadow — dark inner rim (makes ring look raised)
    shadow_r = r - ring_w
    for i in range(8):
        alpha = int(160 * (1 - i / 8))
        draw.ellipse([cx - shadow_r - i, cy - shadow_r - i,
                      cx + shadow_r + i, cy + shadow_r + i],
                     outline=(0, 0, 0, alpha), width=1)

    # Gold ring
    draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                 outline=GOLD, width=ring_w)
    # Light glint top-left on ring
    draw.arc([cx - r, cy - r, cx + r, cy + r],
             start=210, end=310, fill=GOLD_LIGHT, width=max(2, ring_w // 4))

    # 波 debossed: dark shadow below+right, light above+left → recessed
    fnt = get_font(int(size * 0.50))
    draw_kanji(draw, size, fnt, (*NAVY_DARK,  255), offset=(2, 2))    # deep shadow
    draw_kanji(draw, size, fnt, (*NAVY_LIGHT, 200), offset=(-1, -1))  # highlight edge
    draw_kanji(draw, size, fnt, (*GOLD_DARK,  255), offset=(0, 0))    # base color

    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size - 1, size - 1], fill=255)
    img.putalpha(mask)
    return img


# ── 3. EMBOSS ──────────────────────────────────────────────────────────────────
def make_emboss(size) -> Image.Image:
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx = cy = size // 2
    r  = size // 2 - 8
    ring_w = max(8, size // 18)

    # Matte navy disc — slightly textured via subtle gradient
    steps = 30
    for i in range(steps, -1, -1):
        t   = i / steps
        cr  = int((r + ring_w) * (i + 1) / (steps + 1))
        col = (
            int(NAVY[0] + 8 * t),
            int(NAVY[1] + 12 * t),
            int(NAVY[2] + 18 * t),
            255,
        )
        draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=col)

    # Gold ring — matte with subtle bevel
    draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                 outline=GOLD_DARK,  width=ring_w + 3)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                 outline=GOLD,       width=ring_w)
    draw.ellipse([cx - r + 2, cy - r + 2, cx + r - 2, cy + r - 2],
                 outline=GOLD_LIGHT, width=max(2, ring_w // 5))

    # 波 embossed: bright highlight + long shadow = raised above surface
    fnt = get_font(int(size * 0.50))
    # Long shadow (raises)
    for d in range(5, 0, -1):
        alpha = int(180 * (1 - d / 6))
        draw_kanji(draw, size, fnt, (*NAVY_DARK, alpha), offset=(d, d))
    # Edge bright (top-left of each stroke)
    draw_kanji(draw, size, fnt, (*GOLD_LIGHT, 255), offset=(-1, -1))
    # Specular stripe — diagonal highlight across kanji
    # (simulate by drawing semi-transparent white rect clipped to circle)
    hi  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    hd  = ImageDraw.Draw(hi)
    stripe_w = int(size * 0.7)
    stripe_h = int(size * 0.28)
    hx = cx - stripe_w // 2
    hy = cy - int(size * 0.30)
    hd.ellipse([hx, hy, hx + stripe_w, hy + stripe_h],
               fill=(255, 255, 200, 55))
    hi = hi.filter(ImageFilter.GaussianBlur(radius=size // 10))
    img.alpha_composite(hi)
    # Gold base
    draw2 = ImageDraw.Draw(img)
    draw_kanji(draw2, size, fnt, GOLD, offset=(0, 0))

    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size - 1, size - 1], fill=255)
    img.putalpha(mask)
    return img


def build_grid(stamps):
    """Three stamps side by side on MAKOTO + dark label bar."""
    STAMP_PX = 150
    MARGIN   = 32
    bg_src   = Image.open(MAKOTO).convert("RGB").resize((1920, 1080))
    n        = len(stamps)
    W        = 1920 * n + 24 * (n - 1)
    canvas   = Image.new("RGB", (W, 1080 + 90), (12, 14, 20))

    try:
        lf = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 30)
    except OSError:
        lf = ImageFont.load_default()

    for i, (label, stamp) in enumerate(stamps):
        x_off = i * (1920 + 24)
        frame = bg_src.copy().convert("RGBA")
        s = stamp.resize((STAMP_PX, STAMP_PX), Image.LANCZOS)
        frame.alpha_composite(s, (1920 - STAMP_PX - MARGIN,
                                  1080 - STAMP_PX - MARGIN))
        canvas.paste(frame.convert("RGB"), (x_off, 0))

        draw = ImageDraw.Draw(canvas)
        draw.rectangle([x_off, 1080, x_off + 1920, 1170], fill=(18, 22, 34))
        draw.text((x_off + 24, 1090), label, font=lf, fill=GOLD)

    return canvas


def main():
    coin   = make_coin(SIZE)
    seal   = make_seal(SIZE)
    emboss = make_emboss(SIZE)

    coin.save(  HERE / "stillwave-stamp-3d-coin.png",   "PNG")
    seal.save(  HERE / "stillwave-stamp-3d-seal.png",   "PNG")
    emboss.save(HERE / "stillwave-stamp-3d-emboss.png", "PNG")
    print("Stamps saved.")

    grid = build_grid([
        ("1 — МОНЕТА (выпуклый купол + блик)",      coin),
        ("2 — ПЕЧАТЬ (металл + вдавленный 波)",      seal),
        ("3 — ТИСНЕНИЕ (матовый navy + gold specularity)", emboss),
    ])
    out = HERE / "stillwave-stamp-3d-grid.jpg"
    grid.save(out, "JPEG", quality=93, optimize=True)
    print(f"Wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
