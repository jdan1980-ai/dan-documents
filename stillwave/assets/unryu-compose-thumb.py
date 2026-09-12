#!/usr/bin/env python3
"""UNRYU thumbnail — 雲龍 dark sumi ink + cream halo (bright cloud-sea sky needs
dark ink for contrast, same lesson as SHOSHIN/ICHIGO), VERTICAL stack in the
left corner, positioned right where the dragon's tail curl ends (user redirect
2026-08-26). UNRYU large gold serif low-centre on the dark foreground rock.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops

SRC = "/home/user/dan-documents/stillwave/assets/unryu-2h-source.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiSyuku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/unryu-2h-thumb.jpg"
W, H = 1920, 1080
GOLD = (232, 197, 120, 255)
INK = (20, 15, 13, 255)
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
    blur = im.filter(ImageFilter.GaussianBlur(9))
    im = Image.blend(im, ImageChops.screen(im, blur), 0.14)
    # soft bottom gradient only (seats the romaji on the dark rock)
    grad = Image.new("L", (1, H), 0)
    for yy in range(H):
        f = max(0.0, (yy - H * 0.66) / (H * 0.34))
        grad.putpixel((0, yy), int(95 * f))
    im = Image.composite(Image.new("RGB", (W, H), (6, 6, 7)), im, grad.resize((W, H)))
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


def sumi_v(im, chars, size, cx, top_y, pitch, halo=42, bold=9):
    """vertical (top-to-bottom) dark-sumi kanji with a soft cream halo."""
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        md.text((cx - (l + (r - l) / 2), top_y + i * pitch - t), ch, font=f, fill=255)
    if bold and bold >= 3:
        mask = mask.filter(ImageFilter.MaxFilter(bold))
    halo_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    halo_l.paste((248, 238, 216, 255), (0, 0),
                 mask.filter(ImageFilter.GaussianBlur(halo)).point(lambda p: int(p * 0.9)))
    im.alpha_composite(halo_l)
    im.alpha_composite(halo_l)
    ink_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ink_l.paste(INK, (0, 0), mask)
    im.alpha_composite(ink_l)


def sumi_h(im, chars, size, cx, top_y, pitch, halo=42, bold=9):
    """horizontal dark-sumi kanji with a soft cream halo (reads over bright sky)."""
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    total = (len(chars) - 1) * pitch
    x0 = cx - total / 2
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        md.text((x0 + i * pitch - (l + (r - l) / 2), top_y - t), ch, font=f, fill=255)
    if bold and bold >= 3:
        mask = mask.filter(ImageFilter.MaxFilter(bold))
    halo_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    halo_l.paste((248, 238, 216, 255), (0, 0),
                 mask.filter(ImageFilter.GaussianBlur(halo)).point(lambda p: int(p * 0.9)))
    im.alpha_composite(halo_l)
    im.alpha_composite(halo_l)
    ink_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ink_l.paste(INK, (0, 0), mask)
    im.alpha_composite(ink_l)


def spaced_centre(im, text, size, cx, y, fill=GOLD, ls=16, font=SERIF, scrim=True):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(im)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    x = cx - total / 2
    if scrim:
        sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sc).rounded_rectangle((x - 60, y - 24, x + total + 60, y + size + 32),
                                             radius=70, fill=(8, 7, 6, 150))
        im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(55)))
    cx2 = x
    for c, w in zip(text, widths):
        d.text((cx2, y), c, font=f, fill=fill)
        cx2 += w + ls


im = base()
CENTRE = 960
# 雲龍 — VERTICAL calligraphic brush ink + cream halo, left corner, up in the cloud/sky band
# Yuji Syuku is already a thick brush face — NO extra MaxFilter bolding (it blobs the strokes)
sumi_v(im, ["雲", "龍"], 220, 150, 130, pitch=250, halo=36, bold=0)
# UNRYU — large gold serif, low-centre on the dark foreground rock
spaced_centre(im, "UNRYU", 150, CENTRE, 880, fill=GOLD, ls=20, font=SERIF)
im.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
