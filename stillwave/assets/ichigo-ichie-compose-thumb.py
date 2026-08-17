#!/usr/bin/env python3
"""ICHIGO ICHIE thumbnail — 一期一会 gold vertical (縦書き) in the dark left frame,
ICHIGO ICHIE gold serif low. Warm grade + vignette + subtle bloom on the god-rays.

The hero already frames itself with a dark shoji doorway on the left → perfect clean
vertical zone for the 4-char kanji. Sunburst + pagoda + sakura stay clear on the right
(figure-8: text left, hero right)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

SRC = "/home/user/dan-documents/stillwave/assets/ichigo-ichie-2h-source.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/ichigo-ichie-2h-thumb.jpg"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
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
    im = ImageEnhance.Color(im).enhance(1.12)      # richer pink/gold
    im = ImageEnhance.Contrast(im).enhance(1.05)
    # subtle bloom: soft-screen the bright highlights back over the image (glowing rays/steam)
    blur = im.filter(ImageFilter.GaussianBlur(9))
    im = Image.blend(im, ImageChops_screen(im, blur), 0.18)
    # vignette — darken edges, focus centre, clean dark zones for text
    v = Image.new("L", (W, H), 0)
    ImageDraw.Draw(v).ellipse((-W * 0.30, -H * 0.44, W * 1.30, H * 1.44), fill=255)
    v = v.filter(ImageFilter.GaussianBlur(210))
    im = Image.composite(im.convert("RGBA"), Image.new("RGBA", (W, H), (6, 5, 6, 255)),
                         v.point(lambda p: 60 + p * 0.76))
    return im


def ImageChops_screen(a, b):
    from PIL import ImageChops
    return ImageChops.screen(a, b)


def _lerp_gold(f):
    f = max(0.0, min(1.0, f))
    for i in range(len(GOLD_STOPS) - 1):
        f0, c0 = GOLD_STOPS[i]
        f1, c1 = GOLD_STOPS[i + 1]
        if f <= f1:
            t = (f - f0) / (f1 - f0)
            return tuple(int(c0[k] + (c1[k] - c0[k]) * t) for k in range(3))
    return GOLD_STOPS[-1][1]


def sumi(im, chars, size, cx, y0, pitch, vertical=False, halo=44, scrim=None):
    f = ImageFont.truetype(KANJI, size)
    if scrim:
        sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sc).rounded_rectangle(scrim, radius=120, fill=(8, 7, 6, 155))
        im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(85)))
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    if vertical:
        for i, ch in enumerate(chars):
            l, t, r, b = f.getbbox(ch)
            md.text((cx - (l + (r - l) / 2), y0 + i * pitch - t), ch, font=f, fill=255)
    else:
        total = (len(chars) - 1) * pitch
        x0 = cx - total / 2
        for i, ch in enumerate(chars):
            l, t, r, b = f.getbbox(ch)
            md.text((x0 + i * pitch - (l + (r - l) / 2), y0 - t), ch, font=f, fill=255)
    halo_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    halo_l.paste((6, 5, 6, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(halo)).point(lambda p: int(p * 0.9)))
    im.alpha_composite(halo_l)
    im.alpha_composite(halo_l)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste((250, 214, 140, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(26)).point(lambda p: int(p * 0.55)))
    im.alpha_composite(glow)
    ys = [yy for yy in range(H) if mask.crop((0, yy, W, yy + 1)).getextrema()[1] > 0]
    top_y, bot_y = (min(ys), max(ys)) if ys else (y0, y0 + size)
    span = max(1, bot_y - top_y)
    col = Image.new("RGB", (1, span))
    for yy in range(span):
        col.putpixel((0, yy), _lerp_gold(yy / span))
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    grad.paste(col.resize((W, span)).convert("RGBA"), (0, top_y))
    im.alpha_composite(Image.composite(grad, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))


def spaced(im, text, size, x, y, fill=GOLD, ls=14, font=SERIF, scrim=True):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(im)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    if scrim:
        sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sc).rounded_rectangle((x - 60, y - 26, x + total + 60, y + size + 34),
                                             radius=70, fill=(8, 7, 6, 150))
        im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(55)))
    cx = x
    for c, w in zip(text, widths):
        d.text((cx, y), c, font=f, fill=fill)
        cx += w + ls


im = base()
# 一期一会 gold, VERTICAL in the dark left doorframe zone
sumi(im, ["一", "期", "一", "会"], 150, 210, 120, pitch=188, vertical=True, scrim=(70, 90, 360, 900))
# ICHIGO ICHIE gold serif, low-left on the dark veranda
spaced(im, "ICHIGO ICHIE", 92, 120, 940, fill=GOLD, ls=12, font=SERIF)
im.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
