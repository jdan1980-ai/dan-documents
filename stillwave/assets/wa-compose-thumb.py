#!/usr/bin/env python3
"""WA thumbnail — 和 LARGE dark-sumi (cream halo) upper-left over the bright dawn sky,
WA LARGE gold serif low-left on the dark foreground stone.

Bright warm sunrise sky → gold kanji would wash out, so 和 is rendered as dark sumi
ink with a soft cream halo (max contrast on a light sky, like a brush stroke on paper).
WA romaji stays molten gold (echoes the sunrise) on the dark stone slab (high contrast).
User asked for LARGE type → 和 ~470px, WA ~205px.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

SRC = "/home/user/dan-documents/stillwave/assets/wa-2h-source.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF2 = "/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf"  # elegant classic serif
SERIF3 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"  # wider + solid serif for WA
OUT = "/home/user/dan-documents/stillwave/assets/wa-2h-thumb.jpg"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
GOLD = (232, 197, 120, 255)
INK = (22, 17, 15, 255)
GOLD_STOPS = [(0.00, (250, 231, 170)),
              (0.45, (232, 196, 108)),
              (1.00, (180, 132, 58))]


def base():
    im = Image.open(SRC).convert("RGB")
    tw = im.height * W / H
    if im.width > tw:
        x = (im.width - tw) / 2
        im = im.crop((int(x), 0, int(x + tw), im.height))
    else:
        th = im.width * H / W
        y = (im.height - th) / 2
        im = im.crop((0, int(y), im.width, int(y + th)))
    im = im.resize((W, H), Image.LANCZOS)
    im = ImageEnhance.Contrast(im).enhance(1.05)
    im = ImageEnhance.Color(im).enhance(1.07)
    # gentle bottom darkening only (seats WA), sky untouched so dark 和 keeps a light ground
    grad = Image.new("L", (1, H), 0)
    for yy in range(H):
        f = max(0.0, (yy - H * 0.62) / (H * 0.38))
        grad.putpixel((0, yy), int(70 * f))
    dark = Image.new("RGBA", (W, H), (6, 5, 6, 255))
    im = Image.composite(dark, im.convert("RGBA"),
                         grad.resize((W, H)))
    return im.convert("RGBA")


def _lerp_gold(f):
    f = max(0.0, min(1.0, f))
    for i in range(len(GOLD_STOPS) - 1):
        f0, c0 = GOLD_STOPS[i]
        f1, c1 = GOLD_STOPS[i + 1]
        if f <= f1:
            t = (f - f0) / (f1 - f0)
            return tuple(int(c0[k] + (c1[k] - c0[k]) * t) for k in range(3))
    return GOLD_STOPS[-1][1]


def ink(im, char, size, left_x, top_y, halo=44):
    """LARGE dark sumi kanji with a soft cream halo — reads as brushed ink on a bright sky.
    left_x = desired visible LEFT edge of the glyph."""
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    l, t, r, b = f.getbbox(char)
    md.text((left_x - l, top_y - t), char, font=f, fill=255)
    # cream halo (light aura lifts the ink off the peach sky)
    halo_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    halo_l.paste((248, 238, 216, 255), (0, 0),
                 mask.filter(ImageFilter.GaussianBlur(halo)).point(lambda p: int(p * 0.85)))
    im.alpha_composite(halo_l)
    im.alpha_composite(halo_l)
    # dark ink fill
    ink_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ink_l.paste(INK, (0, 0), mask)
    im.alpha_composite(ink_l)


def spaced_centre(im, text, size, cx_centre, y, fill=GOLD, ls=20, font=SERIF, scrim=True):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(im)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    x = cx_centre - total / 2
    if scrim:
        sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sc).rounded_rectangle((x - 90, y - 30, x + total + 90, y + size + 40),
                                             radius=90, fill=(8, 7, 6, 150))
        im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(70)))
    cx = x
    for c, w in zip(text, widths):
        d.text((cx, y), c, font=f, fill=fill)
        cx += w + ls


def wa_left_edge(cx_centre, size, ls, font, text="WA"):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    return cx_centre - total / 2


im = base()
# 和 — LARGE dark sumi, shifted further left (with an edge margin, not touching the border)
ink(im, "和", 470, 160, 100, halo=46)
# WA — wider + solid gold serif (DejaVu Serif Bold, extra spacing), over the pier, shifted left too
spaced_centre(im, "WA", 188, 430, 735, fill=GOLD, ls=30, font=SERIF3)
im.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
