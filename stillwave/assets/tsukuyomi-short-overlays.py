#!/usr/bin/env python3
"""TSUKUYOMI Short text overlays v2 — transparent PNGs (1080x1920), gold.

🔒 SHORTS SAFE ZONE: glyphs inside y 150-1450, x 60-880 of 1080x1920.

Redesign per user feedback: frame 1 is now the thumbnail itself (title
already baked in — no overlay needed there), so the wisdom phrase 明月清風
is broken into ONE PIECE PER REMAINING FRAME (2-6) instead of one giant
overlay stretched across the whole video (which collided with the concept
beat and read as too long on screen at once):
  shot 2 -> 明          shot 3 -> 月          shot 4 -> 清
  shot 5 -> 風          shot 6 -> Meigetsu seifu / A bright moon, a clear wind
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad"
W, H = 1080, 1920
GOLD = (232, 197, 120, 255)
SUB = (231, 224, 205, 255)
CENTRE = 540
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


def gold_char(img, ch, size, cx, y0):
    """single large gold kanji, centred on cx, with soft dark scrim + glow."""
    f = ImageFont.truetype(KANJI, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    l, t, r, b = f.getbbox(ch)
    x = cx - (l + (r - l) / 2)
    md.text((x, y0 - t), ch, font=f, fill=255)
    top, bot = y0, y0 + (b - t)

    sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sc).rounded_rectangle((cx - 180, top - 60, cx + 180, bot + 60),
                                         radius=130, fill=(6, 5, 5, 150))
    img.alpha_composite(sc.filter(ImageFilter.GaussianBlur(85)))

    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste((250, 170, 90, 255), (0, 0),
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


# ---- shots 2-5: one kanji of 明月清風 each, centred mid-frame ----
Y0 = 760
for name, ch in [("tsukv_c1", "明"), ("tsukv_c2", "月"), ("tsukv_c3", "清"), ("tsukv_c4", "風")]:
    im = new()
    gold_char(im, ch, 220, CENTRE, Y0)
    im.save(f"{OUT}/{name}.png")

# ---- shot 6: romaji + gloss (full phrase resolves here) ----
b5 = new()
sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sc).rounded_rectangle((100, 760, 980, 1000), radius=150, fill=(6, 5, 5, 150))
b5.alpha_composite(sc.filter(ImageFilter.GaussianBlur(90)))
spaced_centre(b5, "Meigetsu seifu", 62, CENTRE, 800, GOLD, ls=3, font=SERIF)
ImageDraw.Draw(b5).text((0, 0), "", font=ImageFont.truetype(SERIF, 10))  # noop keep import
d = ImageDraw.Draw(b5)
f2 = ImageFont.truetype(SERIF, 38)
w2 = d.textlength("A bright moon, a clear wind", font=f2)
d.text((CENTRE - w2 / 2, 890), "A bright moon, a clear wind", font=f2, fill=SUB)
b5.save(f"{OUT}/tsukv_c5.png")

# ---- safe-zone check ----
ok = True
for name in ["tsukv_c1", "tsukv_c2", "tsukv_c3", "tsukv_c4", "tsukv_c5"]:
    a = np.asarray(Image.open(f"{OUT}/{name}.png"))[:, :, 3]
    ys, xs = np.where(a > 200)
    good = (ys.min() >= 150 and ys.max() <= 1450 and xs.min() >= 60 and xs.max() <= 880)
    ok = ok and good
    print(f"{name}: y {ys.min()}-{ys.max()}  x {xs.min()}-{xs.max()}", "OK" if good else "OUT OF ZONE")
print("ALL IN ZONE" if ok else "!!! FIX ZONE")
