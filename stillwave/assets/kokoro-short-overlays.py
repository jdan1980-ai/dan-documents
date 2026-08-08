#!/usr/bin/env python3
"""KOKORO Short text overlays — transparent PNGs (1080x1920), warm gold + cream.

🔒 SHORTS SAFE ZONE: glyphs inside y 150-1450, x 60-880 of 1080x1920. Verified by
measuring each overlay's opaque bounding box after render."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

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


def scrim(img, top, bot, alpha=170):
    s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(s).rounded_rectangle((-140, top, 760, bot), radius=150, fill=(8, 8, 10, alpha))
    img.alpha_composite(s.filter(ImageFilter.GaussianBlur(95)))


def gold_kanji(img, chars, size, x0, y0, pitch):
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


def spaced(img, text, size, x, y, fill=CREAM, ls=6, font=KANJI):
    f = ImageFont.truetype(font, size)
    d = ImageDraw.Draw(img)
    cx = x
    for ch in text:
        d.text((cx, y), ch, font=f, fill=fill)
        cx += d.textlength(ch, font=f) + ls


# ---- beat 1: hook ----
b1 = new()
scrim(b1, 980, 1330)
d = ImageDraw.Draw(b1)
f1 = ImageFont.truetype(KANJI, 78)
for i, line in enumerate(["The heart that", "carries too much"]):
    d.text((X, 1040 + i * 96), line, font=f1, fill=CREAM)
b1.save(f"{OUT}/kokov_hook.png")

# ---- beat 2: concept 心 + KOKORO (shot 4 = dark upper hall) ----
b2 = new()
scrim(b2, 950, 1400)
gold_kanji(b2, ["心"], 210, X, 968, 0)
spaced(b2, "KOKORO", 80, X + 6, 1230, GOLD, ls=10, font=SERIF)
b2.save(f"{OUT}/kokov_concept.png")

# ---- beat 3: wisdom 安心立命 ----
b3 = new()
scrim(b3, 958, 1402)
gold_kanji(b3, ["安", "心", "立", "命"], 116, X, 978, 126)
spaced(b3, "Anjin ritsumei", 50, X + 4, 1142, GOLD, ls=3, font=SERIF)
ImageDraw.Draw(b3).text((X + 4, 1222), "Peace of mind, serene stability",
                        font=ImageFont.truetype(SERIF, 34), fill=SUB)
b3.save(f"{OUT}/kokov_wisdom.png")

# ---- safe-zone check ----
import numpy as np
for name in ["kokov_hook", "kokov_concept", "kokov_wisdom"]:
    a = np.asarray(Image.open(f"{OUT}/{name}.png"))[:, :, 3]
    ys, xs = np.where(a > 200)
    print(f"{name}: y {ys.min()}-{ys.max()}  x {xs.min()}-{xs.max()}",
          "OK" if (ys.min() >= 150 and ys.max() <= 1450 and xs.min() >= 60 and xs.max() <= 880) else "OUT OF ZONE")
print("saved 3 overlays to", OUT)
