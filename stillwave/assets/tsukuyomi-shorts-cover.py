#!/usr/bin/env python3
"""TSUKUYOMI Shorts frame 1 — native 9:16 title card (NOT the 16:9 thumbnail
letterboxed). Built on the full-composition vertical source image (monk +
god + rabbits + lotus + gohei + reflection), with the same title treatment
as the long-form thumbnail (月読 gold vertical + TSUKUYOMI gold serif) but
repositioned into the upper-middle band so the phone's YouTube Shorts UI
(which covers the bottom ~24% and right ~17%) never touches it.
SHORTS SAFE ZONE: y 150-1450, x 60-880 of 1080x1920.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops
import numpy as np

SRC = "/tmp/tsuku_fr1_base.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiSyuku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/tsukuyomi-shorts-fr1.jpg"
W, H = 1080, 1920
GOLD = (232, 197, 120, 255)
GOLD_STOPS = [(0.00, (250, 231, 170)), (0.45, (232, 196, 108)), (1.00, (180, 132, 58))]


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
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Color(im).enhance(1.05)
    blur = im.filter(ImageFilter.GaussianBlur(8))
    im = Image.blend(im, ImageChops.screen(im, blur), 0.16)
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


def gold_kanji_v(im, chars, size, cx, top_y, pitch, halo=26):
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    top, bot = H, 0
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        y = top_y + i * pitch
        md.text((cx - (l + (r - l) / 2), y - t), ch, font=f, fill=255)
        top, bot = min(top, y), max(bot, y + (b - t))
    sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sc).rounded_rectangle((cx - 110, top - 30, cx + 110, bot + 40),
                                         radius=90, fill=(4, 5, 8, 150))
    im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(65)))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste((250, 235, 190, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(halo)).point(lambda p: int(p * 0.6)))
    im.alpha_composite(glow)
    span = max(1, int(bot - top))
    col = Image.new("RGB", (1, span))
    for yy in range(span):
        col.putpixel((0, yy), _lerp_gold(yy / span))
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    grad.paste(col.resize((W, span)).convert("RGBA"), (0, int(top)))
    im.alpha_composite(Image.composite(grad, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))
    return top, bot


def spaced_left(im, text, size, x0, y, fill=GOLD, ls=8, font=SERIF, scrim=True):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(im)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    if scrim:
        sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sc).rounded_rectangle((x0 - 30, y - 16, x0 + total + 30, y + size + 22),
                                             radius=45, fill=(4, 5, 8, 150))
        im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(45)))
    cx2 = x0
    for c, w in zip(text, widths):
        d.text((cx2, y), c, font=f, fill=fill)
        cx2 += w + ls
    return y, y + size


im = base()
# 月読 vertical gold — upper-left corner, well clear of the deity/monk in the centre
top, bot = gold_kanji_v(im, ["月", "読"], 150, 130, 190, pitch=190, halo=26)
print("kanji block y:", top, bot)
# TSUKUYOMI — gold serif, left-aligned directly under the kanji (same "logo corner"
# block), never crossing over the figure in the centre of the frame
ty0, ty1 = spaced_left(im, "TSUKUYOMI", 54, 55, bot + 50, fill=GOLD, ls=6, font=SERIF)
print("title y:", ty0, ty1)
im.convert("RGB").save(OUT, quality=95)
print("saved", OUT)
