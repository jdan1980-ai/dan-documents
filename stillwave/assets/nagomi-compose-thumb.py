#!/usr/bin/env python3
"""NAGOMI thumbnail — 和 + NAGOMI over the engawa tea-for-two hero (1920x1080).

Locked layout = V2: a stacked lockup on the shadowed veranda boards, LEFT side.
The frame is symmetric, so the only calm zone is the lower band; the scrim reaches
up into the ferns so the kanji can stay large enough to read at feed size.
Grade pulls the daylight green towards honey gold — warmth is half of what NAGOMI means.
V1 (horizontal) and V3 (+ EVERYDAY CALM) are kept below as alternates.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import numpy as np

SRC = "/home/user/dan-documents/stillwave/assets/nagomi-2h-source.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SP = "/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SUB = (226, 212, 184, 255)


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
    # warm grade — pull the daylight green towards honey gold
    a = np.asarray(im, dtype=np.float32)
    a[:, :, 0] *= 1.10
    a[:, :, 1] *= 0.995
    a[:, :, 2] *= 0.905
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    im = ImageEnhance.Color(im).enhance(1.04)
    im = ImageEnhance.Contrast(im).enhance(1.12)
    # vignette so the eye lands on the table
    v = Image.new("L", (W, H), 0)
    ImageDraw.Draw(v).ellipse((-W * 0.30, -H * 0.44, W * 1.30, H * 1.44), fill=255)
    v = v.filter(ImageFilter.GaussianBlur(200))
    im = Image.composite(im.convert("RGBA"), Image.new("RGBA", (W, H), (14, 10, 5, 255)),
                         v.point(lambda p: 52 + p * 0.795))
    return glow(glow(im, 980, 660, 250, (255, 196, 120), 0.20), 330, 520, 240, (255, 176, 90), 0.16)


def glow(im, cx, cy, r, colour, amount):
    g = Image.new("L", (W, H), 0)
    ImageDraw.Draw(g).ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)
    g = g.filter(ImageFilter.GaussianBlur(r * 0.6))
    layer = Image.new("RGBA", (W, H), colour + (255,))
    layer.putalpha(g.point(lambda p: int(p * amount)))
    out = im.convert("RGBA")
    out.alpha_composite(layer)
    return out


def scrim(im, box, alpha=160, blur=110, radius=190):
    s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(s).rounded_rectangle(box, radius=radius, fill=(18, 12, 5, alpha))
    im.alpha_composite(s.filter(ImageFilter.GaussianBlur(blur)))
    return im


def kanji(im, ch, size, x, y, glow_amt=0.65, blur=30):
    f = ImageFont.truetype(KANJI, size)
    m = Image.new("L", (W, H), 0)
    l, t, r, b = f.getbbox(ch)
    ImageDraw.Draw(m).text((x - l, y - t), ch, font=f, fill=255)
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g.paste((252, 214, 148, 255), (0, 0),
            m.filter(ImageFilter.GaussianBlur(blur)).point(lambda p: int(p * glow_amt)))
    im.alpha_composite(g)
    im.alpha_composite(Image.composite(Image.new("RGBA", (W, H), CREAM),
                                       Image.new("RGBA", (W, H), (0, 0, 0, 0)), m))
    return (r - l), (b - t)


def spaced(im, text, size, x, y, fill=CREAM, ls=12):
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(KANJI, size)
    cx = x
    for c in text:
        d.text((cx, y), c, font=f, fill=fill)
        cx += d.textlength(c, font=f) + ls
    return cx - x


# ── V1 — горизонтальная связка на досках, сад не тронут ─────────────────────
im = base()
scrim(im, (-260, 830, 800, 1120), alpha=175, blur=120)
kanji(im, "和", 200, 108, 862)
spaced(im, "NAGOMI", 74, 330, 900)
im.convert("RGB").save(f"{SP}/nagomi2-thumb-v1.jpg", quality=94)

# ── V2 — вертикальная связка, крупный иероглиф, скрим заходит в папоротники ─
im = base()
scrim(im, (-260, 560, 700, 1110), alpha=178, blur=125)
kanji(im, "和", 258, 112, 606)
spaced(im, "NAGOMI", 80, 118, 896)
im.convert("RGB").save("/home/user/dan-documents/stillwave/assets/nagomi-2h-thumb.jpg", quality=94)  # LOCKED

# ── V3 — V2 + третья строка-обещание ────────────────────────────────────────
im = base()
scrim(im, (-260, 520, 720, 1110), alpha=180, blur=125)
kanji(im, "和", 236, 112, 556)
spaced(im, "NAGOMI", 76, 118, 812)
spaced(im, "EVERYDAY CALM", 40, 122, 912, fill=SUB, ls=6)
im.convert("RGB").save(f"{SP}/nagomi2-thumb-v3.jpg", quality=94)

print("saved v1 v2 v3")
