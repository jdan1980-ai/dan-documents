#!/usr/bin/env python3
"""TSUKUYOMI Short text overlays — transparent PNGs (1080x1920), cream + gold.

🔒 SHORTS SAFE ZONE: glyphs inside y 150-1450, x 60-880 of 1080x1920. Verified by
measuring each overlay's opaque bounding box after render.

beat 1 hook (shot 1)    — "The moon asks for nothing. It only shines" (cream)
beat 2 concept (shot 4) — 月読 + TSUKUYOMI (gold) over the calm moonlit-sky frame
beat 3 wisdom (shot 6)  — 明月清風 / Meigetsu seifu / A bright moon, a clear wind (gold)
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad"
W, H = 1080, 1920
CREAM = (245, 234, 210, 255)
GOLD = (232, 197, 120, 255)
SUB = (231, 224, 205, 255)
X = 96
GSTOPS = [(0.0, (250, 200, 130)), (0.45, (232, 140, 60)), (1.0, (180, 80, 30))]


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


def scrim(img, top, bot, left=-140, right=760, alpha=175, blur=95):
    s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(s).rounded_rectangle((left, top, right, bot), radius=150, fill=(6, 5, 5, alpha))
    img.alpha_composite(s.filter(ImageFilter.GaussianBlur(blur)))


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
        top, bot = min(top, y0 + t), max(bot, y0 + (b - t))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste((250, 170, 90, 255), (0, 0),
               mask.filter(ImageFilter.GaussianBlur(22)).point(lambda p: int(p * 0.6)))
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


# ---- beat 1: hook (cream, SERIF) — over fr1 (monk + full moon-god manifestation) ----
b1 = new()
scrim(b1, 968, 1360)
d = ImageDraw.Draw(b1)
f1 = ImageFont.truetype(SERIF, 62)
for i, line in enumerate(["The moon asks for", "nothing. It only", "shines."]):
    d.text((X, 1010 + i * 104), line, font=f1, fill=CREAM)
b1.save(f"{OUT}/tsukv_hook.png")

# ---- beat 2: concept 月読 + TSUKUYOMI — over fr4 (calm moonlit sky) ----
b2 = new()
sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sc).rounded_rectangle((250, 300, 830, 900), radius=180, fill=(6, 5, 5, 150))
b2.alpha_composite(sc.filter(ImageFilter.GaussianBlur(110)))
gold_kanji(b2, ["月", "読"], 220, 0, 380, 240, cx0=470)
spaced(b2, "TSUKUYOMI", 84, 0, 720, GOLD, ls=14, font=SERIF, cx0=470)
b2.save(f"{OUT}/tsukv_concept.png")

# ---- beat 3: wisdom 明月清風 (4 chars) — over fr6 (extreme wide, moon + distant figures) ----
b3 = new()
scrim(b3, 1000, 1420, left=-140, right=880)
gold_kanji(b3, ["明", "月", "清", "風"], 118, X, 1036, 128)
spaced(b3, "Meigetsu seifu", 52, X + 4, 1226, GOLD, ls=3, font=SERIF)
ImageDraw.Draw(b3).text((X + 4, 1300), "A bright moon, a clear wind",
                        font=ImageFont.truetype(SERIF, 34), fill=SUB)
b3.save(f"{OUT}/tsukv_wisdom.png")

# ---- safe-zone check ----
ok = True
for name in ["tsukv_hook", "tsukv_concept", "tsukv_wisdom"]:
    a = np.asarray(Image.open(f"{OUT}/{name}.png"))[:, :, 3]
    ys, xs = np.where(a > 200)
    good = (ys.min() >= 150 and ys.max() <= 1450 and xs.min() >= 60 and xs.max() <= 880)
    ok = ok and good
    print(f"{name}: y {ys.min()}-{ys.max()}  x {xs.min()}-{xs.max()}", "OK" if good else "OUT OF ZONE")
print("ALL IN ZONE" if ok else "!!! FIX ZONE")
