#!/usr/bin/env python3
"""KARYU thumbnail — 火龍 molten gold, VERTICAL stack in the left corner.
Font switched to Noto Serif JP Bold (2026-08-28) — matches the serif spirit of
the English KARYU wordmark (a Mincho serif, the CJK equivalent of a Western
serif) with classic complete brush-serif strokes. The Yuji brush fonts (both
Boku and Syuku) draw 火's top strokes as flat-cut tips that read as "clipped"
at this isolated scale (confirmed in both fonts' raw glyphs, survives blur
softening); plain IPA Gothic fixed that but read as too plain/sans. Noto Serif
JP gives calligraphic weight AND a complete, unambiguous shape. KARYU large
gold serif low-centre on the dark foreground stone.

2026-08-28 round 2: user reported 龍 still looked "cut off" even with a
complete glyph — root cause was the gradient's dark bottom stop (near-brown)
losing contrast against the night sky, not the glyph shape. Lightened
GOLD_STOPS' bottom stop and lowered the kanji block to the frame's vertical
middle per user request ("опусти иероглиф ниже в середину").
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops

SRC = "/home/user/dan-documents/stillwave/assets/karyu-2h-source.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/NotoSerifJP-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/karyu-2h-thumb.jpg"
W, H = 1920, 1080
GOLD = (232, 197, 120, 255)
GOLD_STOPS = [(0.00, (250, 205, 135)), (0.45, (238, 160, 80)), (1.00, (222, 130, 60))]


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


def gold_kanji_v(im, chars, size, cx, top_y, pitch, halo=26):
    """vertical (top-to-bottom) gold kanji stack, centred on cx."""
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    top, bot = H, 0
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        y = top_y + i * pitch
        md.text((cx - (l + (r - l) / 2), y - t), ch, font=f, fill=255)
        top, bot = min(top, y), max(bot, y + (b - t))
    total = bot - top
    sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sc).rounded_rectangle((cx - 140, top - 40, cx + 140, bot + 50),
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
# 火龍 — VERTICAL calligraphic gold, left corner, centred on the frame's vertical middle
gold_kanji_v(im, ["火", "龍"], 200, 150, 326, pitch=240, halo=34)
# KARYU — large gold serif, low-centre on the dark foreground stone
spaced_centre(im, "KARYU", 160, CENTRE, 880, fill=GOLD, ls=22, font=SERIF)
im.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
