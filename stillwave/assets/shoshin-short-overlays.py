#!/usr/bin/env python3
"""SHOSHIN Short text overlays — transparent PNGs (1080x1920), warm gold + cream.

🔒 SHORTS SAFE ZONE: glyphs inside y 150-1450, x 60-880 of 1080x1920. Verified by
measuring each overlay's opaque bounding box after render."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad"
W, H = 1080, 1920
CREAM = (245, 234, 210, 255)
GOLD = (232, 197, 120, 255)
SUB = (231, 224, 205, 255)
X = 82
GSTOPS = [(0.0, (250, 231, 170)), (0.45, (232, 196, 108)), (1.0, (180, 132, 58))]


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


def scrim(img, top, bot, alpha=175):
    s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(s).rounded_rectangle((-140, top, 760, bot), radius=150, fill=(8, 7, 6, alpha))
    img.alpha_composite(s.filter(ImageFilter.GaussianBlur(95)))


def gold_kanji(img, chars, size, x0, y0, pitch, cx0=None):
    if cx0 is not None:
        total = (len(chars) - 1) * pitch
        x0 = cx0 - total / 2
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    l0, _, r0, _ = f.getbbox(chars[0])
    c0 = x0 + (r0 - l0) / 2
    top, bot = H, 0
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        md.text((c0 + i * pitch - (l + (r - l) / 2), y0), ch, font=f, fill=255)
        top, bot = min(top, y0 + t), max(bot, y0 + b)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste((250, 214, 140, 255), (0, 0),
               mask.filter(ImageFilter.GaussianBlur(22)).point(lambda p: int(p * 0.55)))
    img.alpha_composite(glow)
    span = max(1, int(bot - top))
    col = Image.new("RGB", (1, span))
    for yy in range(span):
        col.putpixel((0, yy), gold(yy / span))
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    canvas.paste(col.resize((W, span)).convert("RGBA"), (0, int(top)))
    img.alpha_composite(Image.composite(canvas, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))


def spaced(img, text, size, x, y, fill=CREAM, ls=6, font=KANJI, cx0=None):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(img)
    if cx0 is not None:
        ws = [d.textlength(c, font=f) for c in text]
        x = cx0 - (sum(ws) + ls * (len(text) - 1)) / 2
    cx = x
    for ch in text:
        d.text((cx, y), ch, font=f, fill=fill)
        cx += d.textlength(ch, font=f) + ls


# ---- beat 1: hook ----
b1 = new()
scrim(b1, 980, 1330)
d = ImageDraw.Draw(b1)
f1 = ImageFont.truetype(KANJI, 80)
for i, line in enumerate(["Meet this moment", "as the first"]):
    d.text((X, 1040 + i * 98), line, font=f1, fill=CREAM)
b1.save(f"{OUT}/shov_hook.png")

# ---- beat 2: concept 初心 + SHOSHIN — high over the dark tokonoma ceiling ----
b2 = new()
sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sc).rounded_rectangle((40, 210, 1040, 760), radius=170, fill=(8, 7, 6, 165))
b2.alpha_composite(sc.filter(ImageFilter.GaussianBlur(100)))
gold_kanji(b2, ["初", "心"], 176, 0, 268, 190, cx0=470)
spaced(b2, "SHOSHIN", 96, 0, 500, GOLD, ls=8, font=SERIF, cx0=470)
b2.save(f"{OUT}/shov_concept.png")

# ---- beat 3: wisdom 初心忘るべからず (8 chars — smaller) ----
b3 = new()
scrim(b3, 1040, 1420)
gold_kanji(b3, ["初", "心", "忘", "る", "べ", "か", "ら", "ず"], 84, X, 1070, 92)
spaced(b3, "Shoshin wasuru bekarazu", 44, X + 4, 1216, GOLD, ls=2, font=SERIF)
ImageDraw.Draw(b3).text((X + 4, 1288), "Never forget the beginner's mind",
                        font=ImageFont.truetype(SERIF, 32), fill=SUB)
b3.save(f"{OUT}/shov_wisdom.png")

# ---- safe-zone check ----
for name in ["shov_hook", "shov_concept", "shov_wisdom"]:
    a = np.asarray(Image.open(f"{OUT}/{name}.png"))[:, :, 3]
    ys, xs = np.where(a > 200)
    print(f"{name}: y {ys.min()}-{ys.max()}  x {xs.min()}-{xs.max()}",
          "OK" if (ys.min() >= 150 and ys.max() <= 1450 and xs.min() >= 60 and xs.max() <= 880) else "OUT OF ZONE")
print("saved 3 overlays to", OUT)
