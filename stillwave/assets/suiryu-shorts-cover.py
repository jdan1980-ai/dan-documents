#!/usr/bin/env python3
"""SUIRYU Shorts cover (9:16, 1080x1920) — full dragon + samurai hero shot
(fr6) with gold 水龍 + SUIRYU title, same gold treatment as the main thumbnail.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops

SRC = "/home/user/dan-documents/stillwave/assets/suiryu-shorts-fr6.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/suiryu-shorts-cover.jpg"
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
    im = ImageEnhance.Contrast(im).enhance(1.08)
    im = ImageEnhance.Color(im).enhance(1.05)
    blur = im.filter(ImageFilter.GaussianBlur(10))
    im = Image.blend(im, ImageChops.screen(im, blur), 0.20)
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


def gold_kanji(im, chars, size, cx, top_y, pitch, halo=22):
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    total = (len(chars) - 1) * pitch
    x0 = cx - total / 2
    top, bot = H, 0
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        cxi = x0 + i * pitch - (l + (r - l) / 2)
        md.text((cxi, top_y - t), ch, font=f, fill=255)
        top, bot = min(top, top_y + t), max(bot, top_y + b)
    sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sc).rounded_rectangle((x0 - 70, top - 40, x0 + total + 70, bot + 50),
                                         radius=100, fill=(6, 6, 9, 145))
    im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(75)))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste((250, 214, 140, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(halo)).point(lambda p: int(p * 0.55)))
    im.alpha_composite(glow)
    span = max(1, int(bot - top))
    col = Image.new("RGB", (1, span))
    for yy in range(span):
        col.putpixel((0, yy), _lerp_gold(yy / span))
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    grad.paste(col.resize((W, span)).convert("RGBA"), (0, int(top)))
    im.alpha_composite(Image.composite(grad, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))


def spaced_centre(im, text, size, cx, y, fill=GOLD, ls=14, font=SERIF, scrim=True):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(im)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    x = cx - total / 2
    if scrim:
        sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sc).rounded_rectangle((x - 50, y - 20, x + total + 50, y + size + 26),
                                             radius=60, fill=(6, 6, 9, 145))
        im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(50)))
    cx2 = x
    for c, w in zip(text, widths):
        d.text((cx2, y), c, font=f, fill=fill)
        cx2 += w + ls


im = base()
CX = 540
# 水龍 — gold, upper area over the dark sky/moon zone
gold_kanji(im, ["水", "龍"], 190, CX, 210, pitch=220)
# SUIRYU — large gold serif, low over the dark foreground rock
spaced_centre(im, "SUIRYU", 128, CX, 1660, fill=GOLD, ls=18, font=SERIF)
im.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
