#!/usr/bin/env python3
"""KARYU thumbnail — 火龍 molten gold with a dark halo (dark night scene, gold
reads cleanly here — same case as SUIRYU), upper-left over the fire-dragon.
KARYU large gold serif low-centre on the dark foreground stone.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops

SRC = "/home/user/dan-documents/stillwave/assets/karyu-2h-source.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/karyu-2h-thumb.jpg"
W, H = 1920, 1080
GOLD = (232, 197, 120, 255)
GOLD_STOPS = [(0.00, (250, 200, 130)), (0.45, (232, 140, 60)), (1.00, (180, 80, 30))]


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
    im = ImageEnhance.Contrast(im).enhance(1.08)
    im = ImageEnhance.Color(im).enhance(1.05)
    blur = im.filter(ImageFilter.GaussianBlur(10))
    im = Image.blend(im, ImageChops.screen(im, blur), 0.20)
    grad = Image.new("L", (1, H), 0)
    for yy in range(H):
        f = max(0.0, (yy - H * 0.66) / (H * 0.34))
        grad.putpixel((0, yy), int(90 * f))
    im = Image.composite(Image.new("RGB", (W, H), (5, 4, 4)), im, grad.resize((W, H)))
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


def gold_kanji_h(im, chars, size, x0, top_y, pitch, halo=26):
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    total = (len(chars) - 1) * pitch
    top, bot = H, 0
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        md.text((x0 + i * pitch - (l + (r - l) / 2), top_y - t), ch, font=f, fill=255)
        top, bot = min(top, top_y + t), max(bot, top_y + b)
    sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sc).rounded_rectangle((x0 - 70, top - 40, x0 + total + 70, bot + 50),
                                         radius=110, fill=(6, 5, 5, 150))
    im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(80)))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste((250, 170, 90, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(halo)).point(lambda p: int(p * 0.6)))
    im.alpha_composite(glow)
    span = max(1, int(bot - top))
    col = Image.new("RGB", (1, span))
    for yy in range(span):
        col.putpixel((0, yy), _lerp_gold(yy / span))
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    grad.paste(col.resize((W, span)).convert("RGBA"), (0, int(top)))
    im.alpha_composite(Image.composite(grad, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))


def spaced_centre(im, text, size, cx, y, fill=GOLD, ls=16, font=SERIF, scrim=True):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(im)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    x = cx - total / 2
    if scrim:
        sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sc).rounded_rectangle((x - 60, y - 24, x + total + 60, y + size + 32),
                                             radius=70, fill=(6, 5, 5, 150))
        im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(55)))
    cx2 = x
    for c, w in zip(text, widths):
        d.text((cx2, y), c, font=f, fill=fill)
        cx2 += w + ls


im = base()
CENTRE = 960
# 火龍 — horizontal gold, upper-left with breathing room from the edge
gold_kanji_h(im, ["火", "龍"], 250, 175, 55, pitch=295, halo=30)
# KARYU — large gold serif, low-centre on the dark foreground stone
spaced_centre(im, "KARYU", 160, CENTRE, 880, fill=GOLD, ls=22, font=SERIF)
im.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
