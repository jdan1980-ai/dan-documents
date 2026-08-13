#!/usr/bin/env python3
"""SHOSHIN thumbnail — 初心 gold upper-centre over the autumn maple + SHOSHIN below.

Kanji-Concept canon: KANJI large upper-centre in molten GOLD over the visual hero
(here the round marumado window + crimson maple). GOLD kanji + dark halo lifts it
off the busy red canopy. SHOSHIN = large legible Liberation Serif Bold (NOT the
brush font — locked 2026-08-07), low, centred on the dark tatami floor.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

SRC = "/home/user/dan-documents/stillwave/assets/shoshin-2h-source.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/shoshin-2h-thumb.jpg"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
GOLD = (232, 197, 120, 255)
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
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Color(im).enhance(1.06)
    v = Image.new("L", (W, H), 0)
    ImageDraw.Draw(v).ellipse((-W * 0.28, -H * 0.42, W * 1.28, H * 1.42), fill=255)
    v = v.filter(ImageFilter.GaussianBlur(200))
    im = Image.composite(im.convert("RGBA"), Image.new("RGBA", (W, H), (8, 6, 6, 255)),
                         v.point(lambda p: 66 + p * 0.74))
    return im


def _lerp_gold(f):
    f = max(0.0, min(1.0, f))
    for i in range(len(GOLD_STOPS) - 1):
        f0, c0 = GOLD_STOPS[i]
        f1, c1 = GOLD_STOPS[i + 1]
        if f <= f1:
            t = (f - f0) / (f1 - f0)
            return tuple(int(c0[k] + (c1[k] - c0[k]) * t) for k in range(3))
    return GOLD_STOPS[-1][1]


def sumi(im, chars, size, cx_centre, y, pitch, halo=46):
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    n = len(chars)
    total = (n - 1) * pitch
    x0 = cx_centre - total / 2
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        md.text((x0 + i * pitch - (l + (r - l) / 2), y - t), ch, font=f, fill=255)
    halo_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    halo_l.paste((6, 5, 6, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(halo)).point(lambda p: int(p * 0.95)))
    im.alpha_composite(halo_l)
    im.alpha_composite(halo_l)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste((250, 214, 140, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(26)).point(lambda p: int(p * 0.55)))
    im.alpha_composite(glow)
    ys = [yy for yy in range(H) if mask.crop((0, yy, W, yy + 1)).getextrema()[1] > 0]
    top_y, bot_y = (min(ys), max(ys)) if ys else (y, y + size)
    span = max(1, bot_y - top_y)
    col = Image.new("RGB", (1, span))
    for yy in range(span):
        col.putpixel((0, yy), _lerp_gold(yy / span))
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    grad.paste(col.resize((W, span)).convert("RGBA"), (0, top_y))
    im.alpha_composite(Image.composite(grad, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))


def spaced_centre(im, text, size, cx_centre, y, fill=CREAM, ls=16, font=KANJI):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(im)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    x = cx_centre - total / 2
    sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sc).rounded_rectangle((x - 70, y - 24, x + total + 70, y + size + 34),
                                         radius=70, fill=(8, 7, 6, 175))
    im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(60)))
    cx = x
    for c, w in zip(text, widths):
        d.text((cx, y), c, font=f, fill=fill)
        cx += w + ls


im = base()
CENTRE = 960
# 初心 gold high, over the top of the maple canopy — above the monk's head
sumi(im, ["初", "心"], 210, CENTRE, 40, pitch=232)
spaced_centre(im, "SHOSHIN", 138, CENTRE, 880, fill=GOLD, ls=16, font=SERIF)  # low on dark tatami
im.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
