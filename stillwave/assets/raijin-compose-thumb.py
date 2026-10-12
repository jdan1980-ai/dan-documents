#!/usr/bin/env python3
"""RAIJIN thumbnail — 雷神 WHITE calligraphic (white reads clean against
this hero's deep violet storm-cloud spirit, same lesson as AMATERASU/
HACHIMAN/BENZAITEN/KANNON/FUJIN), VERTICAL stack in the upper-left
corner (dark roof/stormy sky there, clear of the musician and the
spirit who fills the right side). RAIJIN large white serif low-centre
on the dark wet courtyard stone.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops

SRC = "/home/user/dan-documents/stillwave/assets/raijin-1h-source.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiSyuku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/raijin-1h-thumb.jpg"
W, H = 1920, 1080
WHITE = (255, 255, 255, 255)
WHITE_STOPS = [(0.00, (255, 255, 255)), (0.5, (250, 249, 246)), (1.00, (238, 235, 228))]


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
    blur = im.filter(ImageFilter.GaussianBlur(10))
    im = Image.blend(im, ImageChops.screen(im, blur), 0.18)
    grad = Image.new("L", (1, H), 0)
    for yy in range(H):
        f = max(0.0, (yy - H * 0.66) / (H * 0.34))
        grad.putpixel((0, yy), int(90 * f))
    im = Image.composite(Image.new("RGB", (W, H), (4, 5, 8)), im, grad.resize((W, H)))
    return im.convert("RGBA")


def _lerp_white(f):
    f = max(0.0, min(1.0, f))
    for i in range(len(WHITE_STOPS) - 1):
        f0, c0 = WHITE_STOPS[i]
        f1, c1 = WHITE_STOPS[i + 1]
        if f <= f1:
            t = (f - f0) / (f1 - f0)
            return tuple(int(c0[k] + (c1[k] - c0[k]) * t) for k in range(3))
    return WHITE_STOPS[-1][1]


def white_kanji_v(im, chars, size, cx, top_y, pitch, halo=30):
    """vertical (top-to-bottom) white kanji stack, centred on cx.
    🔒 FIXED bounds formula — do not revert:
    actual ink top/bottom = y / y+(b-t), NOT y+t / y+b, because each
    character is drawn at (x, y - t) to normalize its own ink-top."""
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
    ImageDraw.Draw(sc).rounded_rectangle((cx - 140, top - 40, cx + 140, bot + 50),
                                         radius=110, fill=(4, 5, 8, 150))
    im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(80)))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste((255, 255, 255, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(halo)).point(lambda p: int(p * 0.6)))
    im.alpha_composite(glow)
    span = max(1, int(bot - top))
    col = Image.new("RGB", (1, span))
    for yy in range(span):
        col.putpixel((0, yy), _lerp_white(yy / span))
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    grad.paste(col.resize((W, span)).convert("RGBA"), (0, int(top)))
    im.alpha_composite(Image.composite(grad, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))
    print("kanji block y:", top, bot)
    return top, bot


def spaced_centre(im, text, size, cx, y, fill=WHITE, ls=16, font=SERIF, scrim=True):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(im)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    x = cx - total / 2
    if scrim:
        sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sc).rounded_rectangle((x - 60, y - 24, x + total + 60, y + size + 32),
                                             radius=70, fill=(4, 5, 8, 150))
        im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(55)))
    cx2 = x
    for c, w in zip(text, widths):
        d.text((cx2, y), c, font=f, fill=fill)
        cx2 += w + ls


im = base()
CENTRE = 960
# 雷神 — VERTICAL calligraphic white, upper-left corner (dark roof/stormy sky,
# clear of the musician and the spirit who fills the right side)
white_kanji_v(im, ["雷", "神"], 240, 150, 120, pitch=288, halo=32)
# RAIJIN — large white serif, low-centre on the dark wet courtyard stone
spaced_centre(im, "RAIJIN", 120, CENTRE, 920, fill=WHITE, ls=18, font=SERIF)
im.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
