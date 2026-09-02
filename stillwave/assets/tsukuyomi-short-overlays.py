#!/usr/bin/env python3
"""TSUKUYOMI Short text overlays v3 — transparent PNGs (1080x1920), gold.

🔒 SHORTS SAFE ZONE: glyphs inside y 150-1450, x 60-880 of 1080x1920.
Per final user rule: frame 1 = existing 9:16 image + title (built separately
by tsukuyomi-shorts-cover.py). The wisdom text is SHORT (a few words each),
so frames 2-6 each get a DIFFERENT short Japanese wisdom/phrase — not the
same phrase repeated, not one phrase stretched across frames. All five are
distinct, thematically tied to Tsukuyomi (moon / night / stillness), and
positioned in the middle/upper band so the phone's YouTube Shorts UI
(bottom ~24%, right ~17%) never touches them.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiSyuku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad"
W, H = 1080, 1920
GOLD = (232, 197, 120, 255)
SUB = (231, 224, 205, 255)
CENTRE = 540
GSTOPS = [(0.0, (250, 231, 170)), (0.45, (232, 196, 108)), (1.0, (180, 132, 58))]

# five distinct short Japanese wisdoms, each fitting Tsukuyomi's domain
# (moon / night / stillness / the mind) — never the same phrase twice.
WISDOMS = [
    ("静寂", "Seijaku", "Silence is a teacher"),
    ("無心", "Mushin", "No mind, no burden"),
    ("明鏡止水", "Meikyo shisui", "A clear mirror, still water"),
    ("一期一会", "Ichigo ichie", "One moment, never again"),
    ("明月清風", "Meigetsu seifu", "A bright moon, a clear wind"),
]


def gold(f):
    f = max(0.0, min(1.0, f))
    for i in range(len(GSTOPS) - 1):
        f0, c0 = GSTOPS[i]
        f1, c1 = GSTOPS[i + 1]
        if f <= f1:
            t = (f - f0) / (f1 - f0)
            return tuple(int(c0[k] + (c1[k] - c0[k]) * t) for k in range(3))
    return GSTOPS[-1][1]


def new():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def gold_kanji_h(img, chars, size, cx, y0):
    """horizontal row of gold kanji, all drawn at the same y0 (no per-char
    offset) — bounds are therefore min(y0+t) / max(y0+b) across chars."""
    f = ImageFont.truetype(KANJI, size)
    boxes = [f.getbbox(c) for c in chars]
    widths = [b[2] - b[0] for b in boxes]
    gap = size * 0.12
    total = sum(widths) + gap * (len(chars) - 1)
    x0 = cx - total / 2
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    top, bot = H, 0
    x = x0
    for ch, (l, t, r, b) in zip(chars, boxes):
        md.text((x - l, y0), ch, font=f, fill=255)
        top, bot = min(top, y0 + t), max(bot, y0 + b)
        x += (r - l) + gap
    sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sc).rounded_rectangle((x0 - 60, top - 40, x0 + total + 60, bot + 40),
                                         radius=100, fill=(4, 5, 8, 150))
    img.alpha_composite(sc.filter(ImageFilter.GaussianBlur(70)))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste((250, 235, 190, 255), (0, 0),
               mask.filter(ImageFilter.GaussianBlur(24)).point(lambda p: int(p * 0.6)))
    img.alpha_composite(glow)
    span = max(1, int(bot - top))
    col = Image.new("RGB", (1, span))
    for yy in range(span):
        col.putpixel((0, yy), gold(yy / span))
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    canvas.paste(col.resize((W, span)).convert("RGBA"), (0, int(top)))
    img.alpha_composite(Image.composite(canvas, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))
    return top, bot


def spaced_centre(img, text, size, cx, y, fill=GOLD, ls=4, font=SERIF):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(img)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + ls * (len(text) - 1)
    x = cx - total / 2
    cx2 = x
    for c, w in zip(text, widths):
        d.text((cx2, y), c, font=f, fill=fill)
        cx2 += w + ls
    return y, y + size


# ---- shots 2-6: one distinct wisdom per frame, kanji + romaji + gloss,
# stacked in the upper-middle band (well above the lower-third UI zone) ----
Y0 = 620
for i, (kanji, romaji, gloss) in enumerate(WISDOMS, start=1):
    im = new()
    top, bot = gold_kanji_h(im, list(kanji), 150 if len(kanji) <= 2 else 110, CENTRE, Y0)
    ry0, ry1 = spaced_centre(im, romaji.upper(), 46, CENTRE, bot + 50, GOLD, ls=4, font=SERIF)
    d = ImageDraw.Draw(im)
    f2 = ImageFont.truetype(SERIF, 34)
    w2 = d.textlength(gloss, font=f2)
    d.text((CENTRE - w2 / 2, ry1 + 24), gloss, font=f2, fill=SUB)
    im.save(f"{OUT}/tsukv_w{i}.png")

# ---- safe-zone check ----
ok = True
for i in range(1, 6):
    name = f"tsukv_w{i}"
    a = np.asarray(Image.open(f"{OUT}/{name}.png"))[:, :, 3]
    ys, xs = np.where(a > 200)
    good = (ys.min() >= 150 and ys.max() <= 1450 and xs.min() >= 60 and xs.max() <= 880)
    ok = ok and good
    print(f"{name}: y {ys.min()}-{ys.max()}  x {xs.min()}-{xs.max()}", "OK" if good else "OUT OF ZONE")
print("ALL IN ZONE" if ok else "!!! FIX ZONE")
