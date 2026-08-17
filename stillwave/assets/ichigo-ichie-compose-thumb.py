#!/usr/bin/env python3
"""ICHIGO ICHIE thumbnail v2 — 一期一会 HORIZONTAL dark-sumi (cream halo) top-centre,
ICHIGO ICHIE gold serif low-centre. Cropped in to trim the dark doorframe, NO heavy
vignette (only a soft bottom gradient for the romaji). Warm grade + gentle bloom.

Horizontal kanji: the two 一 (ichi = "one") read inline as part of the word 一期一会,
not as stray dashes. Dark sumi + cream halo reads over the bright blossom canopy."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops

SRC = "/home/user/dan-documents/stillwave/assets/ichigo-ichie-2h-source.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/ichigo-ichie-2h-thumb.jpg"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
GOLD = (232, 197, 120, 255)
INK = (20, 15, 13, 255)
GOLD_STOPS = [(0.00, (250, 231, 170)), (0.45, (232, 196, 108)), (1.00, (180, 132, 58))]
CROP_IN = 0.86  # keep central 86% → trims the dark shoji doorframe on the sides


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
    # crop in to reduce the dark doorframe bars
    cw, ch = im.width * CROP_IN, im.height * CROP_IN
    x0, y0 = (im.width - cw) / 2, (im.height - ch) / 2
    im = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch)))
    im = im.resize((W, H), Image.LANCZOS)
    im = ImageEnhance.Color(im).enhance(1.10)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    # gentle bloom on highlights (rays/steam glow)
    blur = im.filter(ImageFilter.GaussianBlur(9))
    im = Image.blend(im, ImageChops.screen(im, blur), 0.16)
    # ONLY a soft bottom gradient (seats the romaji) — no edge vignette, no black frame
    grad = Image.new("L", (1, H), 0)
    for yy in range(H):
        f = max(0.0, (yy - H * 0.66) / (H * 0.34))
        grad.putpixel((0, yy), int(90 * f))
    im = Image.composite(Image.new("RGB", (W, H), (6, 5, 6)), im, grad.resize((W, H)))
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


def sumi_h(im, chars, size, cx, top_y, pitch, halo=40):
    """horizontal dark-sumi kanji with a soft cream halo (reads over bright blossoms)."""
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    total = (len(chars) - 1) * pitch
    x0 = cx - total / 2
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        md.text((x0 + i * pitch - (l + (r - l) / 2), top_y - t), ch, font=f, fill=255)
    halo_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    halo_l.paste((248, 238, 216, 255), (0, 0),
                 mask.filter(ImageFilter.GaussianBlur(halo)).point(lambda p: int(p * 0.9)))
    im.alpha_composite(halo_l)
    im.alpha_composite(halo_l)
    ink_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ink_l.paste(INK, (0, 0), mask)
    im.alpha_composite(ink_l)


def spaced_centre(im, text, size, cx, y, fill=GOLD, ls=14, font=SERIF, scrim=True):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(im)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    x = cx - total / 2
    if scrim:
        sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sc).rounded_rectangle((x - 60, y - 24, x + total + 60, y + size + 32),
                                             radius=70, fill=(8, 7, 6, 130))
        im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(55)))
    cx2 = x
    for c, w in zip(text, widths):
        d.text((cx2, y), c, font=f, fill=fill)
        cx2 += w + ls


im = base()
CENTRE = 960
# 一期一会 — horizontal dark sumi, top-centre, over the blossom canopy
sumi_h(im, ["一", "期", "一", "会"], 210, CENTRE, 70, pitch=300, halo=42)
# ICHIGO ICHIE — gold serif, low-centre on the darkened foreground
spaced_centre(im, "ICHIGO ICHIE", 96, CENTRE, 936, fill=GOLD, ls=14, font=SERIF)
im.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
