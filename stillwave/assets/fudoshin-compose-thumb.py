#!/usr/bin/env python3
"""FUDOSHIN thumbnail — 不動心 upper-centre over the waterfall + FUDOSHIN below.

Kanji-Concept canon (per CLAUDE.md): the KANJI goes LARGE upper-centre in dark
sumi ink brushed over the visual hero (here the waterfall), ROMAJI in cream LOW on the rock beneath the samurai (user pref 2026-07-28:
keep the romaji down on the stone, not tucked under the kanji — lets the frame breathe).
NOT the lower-left figure-8 rule — that's for Healing Hour / Pomodoro only.

The waterfall is bright (mean ~176), so the sumi kanji gets a soft DARK halo to
lift it off the busy white water, and the romaji sits over a faint dark scrim.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import numpy as np

SRC = "/home/user/dan-documents/stillwave/assets/fudoshin-2h-source.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/fudoshin-2h-thumb.jpg"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
INK = (14, 18, 22, 255)


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
    im = ImageEnhance.Color(im).enhance(1.04)
    # gentle vignette to seat the eye on the samurai + darken edges
    v = Image.new("L", (W, H), 0)
    ImageDraw.Draw(v).ellipse((-W * 0.28, -H * 0.42, W * 1.28, H * 1.42), fill=255)
    v = v.filter(ImageFilter.GaussianBlur(200))
    im = Image.composite(im.convert("RGBA"), Image.new("RGBA", (W, H), (10, 14, 16, 255)),
                         v.point(lambda p: 70 + p * 0.72))
    return im


def sumi(im, chars, size, cx_centre, y, pitch, halo=44):
    """dark sumi kanji, centred on cx_centre, with a soft dark halo for legibility"""
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    n = len(chars)
    total = (n - 1) * pitch
    x0 = cx_centre - total / 2
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        md.text((x0 + i * pitch - (l + (r - l) / 2), y - t), ch, font=f, fill=255)
    # dark halo so black ink separates from the white water
    halo_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    halo_l.paste((6, 9, 12, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(halo)).point(lambda p: int(p * 0.9)))
    im.alpha_composite(halo_l)
    im.alpha_composite(halo_l)  # double for denser shadow
    ink = Image.new("RGBA", (W, H), INK)
    im.alpha_composite(Image.composite(ink, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))


def spaced_centre(im, text, size, cx_centre, y, fill=CREAM, ls=16):
    f = ImageFont.truetype(KANJI, size)
    d = ImageDraw.Draw(im)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    x = cx_centre - total / 2
    # soft dark backing for the romaji
    sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sc).rounded_rectangle((x - 70, y - 24, x + total + 70, y + size + 34),
                                         radius=70, fill=(8, 12, 14, 165))
    im.alpha_composite(sc.filter(ImageFilter.GaussianBlur(60)))
    cx = x
    for c, w in zip(text, widths):
        d.text((cx, y), c, font=f, fill=fill)
        cx += w + ls


im = base()
CENTRE = 958   # slightly left of frame centre — samurai head sits just right of it
sumi(im, ["不", "動", "心"], 300, CENTRE, 70, pitch=310)
spaced_centre(im, "FUDOSHIN", 86, CENTRE, 946, ls=16)  # low, on the rock under the samurai
im.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
