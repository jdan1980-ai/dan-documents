#!/usr/bin/env python3
"""NAGOMI Short text overlays — transparent PNGs (1080x1920), warm cream + honey gold.

🔒 SHORTS SAFE ZONE (locked 2026-07-26): the YouTube Shorts player covers the
bottom ~24% of the frame (title, channel, description, music ticker), the right
~17% (like / comment / share buttons) and the top ~7%. ALL glyphs must therefore
sit inside  y 150-1450  and  x 60-880  of 1080x1920. Verified after every build by
measuring the opaque-pixel bounding box of each overlay."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
OUT = "/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad"
W, H = 1080, 1920
CREAM = (245, 234, 210, 255)
GOLD = (238, 205, 138, 255)
SUB = (233, 219, 192, 255)
X = 78

# honey-gold gradient for the kanji — warmer and softer than the KINTSUGI molten gold
STOPS = [(0.00, (252, 232, 178)), (0.45, (240, 205, 132)), (1.00, (198, 152, 82))]


def lerp(a, b, f):
    return tuple(int(a[i] + (b[i] - a[i]) * f) for i in range(3))


def gcol(f):
    f = max(0.0, min(1.0, f))
    for i in range(len(STOPS) - 1):
        f0, c0 = STOPS[i]
        f1, c1 = STOPS[i + 1]
        if f <= f1:
            return lerp(c0, c1, (f - f0) / (f1 - f0))
    return STOPS[-1][1]


def new():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def scrim(img, top, bot):
    """soft dark backing on the LEFT so warm text reads over sunlit tatami"""
    s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(s).rounded_rectangle((-140, top, 700, bot), radius=150, fill=(24, 16, 8, 165))
    img.alpha_composite(s.filter(ImageFilter.GaussianBlur(90)))


def kanji_row(img, chars, size, x0, y0, pitch, gradient=True):
    """glyphs at even centres + soft glow; optional honey-gold gradient fill"""
    f = ImageFont.truetype(FONT, size)
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
    glow.paste((250, 214, 150, 255), (0, 0),
               mask.filter(ImageFilter.GaussianBlur(16)).point(lambda p: int(p * 0.5)))
    img.alpha_composite(glow)
    if gradient:
        span = max(1, int(bot - top))
        col = Image.new("RGB", (1, span))
        for y in range(span):
            col.putpixel((0, y), gcol(y / span))
        canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        canvas.paste(col.resize((W, span)).convert("RGBA"), (0, int(top)))
        img.alpha_composite(Image.composite(canvas, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))
    else:
        fl = Image.new("RGBA", (W, H), CREAM)
        img.alpha_composite(Image.composite(fl, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))


def spaced(img, text, size, x, y, fill, ls=4):
    f = ImageFont.truetype(FONT, size)
    d = ImageDraw.Draw(img)
    cx = x
    for ch in text:
        d.text((cx, y), ch, font=f, fill=fill)
        cx += d.textlength(ch, font=f) + ls


# ---- beat 1: hook ----  (glyphs land ~1030-1300)
b1 = new()
scrim(b1, 980, 1340)
d = ImageDraw.Draw(b1)
f1 = ImageFont.truetype(FONT, 80)
for i, line in enumerate(["Warmth. Balance.", "Enough."]):
    d.text((X, 1040 + i * 98), line, font=f1, fill=CREAM)
b1.save(f"{OUT}/nov_hook.png")

# ---- beat 2: concept 和 + NAGOMI ---- (the empty-room frame is built for this)
b2 = new()
scrim(b2, 930, 1400)
kanji_row(b2, ["和"], 250, X, 900, 0)
spaced(b2, "NAGOMI", 84, X + 6, 1200, CREAM, ls=9)
b2.save(f"{OUT}/nov_concept.png")

# ---- beat 3: wisdom 和敬清寂 ---- (on the closing man-at-rest shot)
b3 = new()
scrim(b3, 960, 1400)
kanji_row(b3, ["和", "敬", "清", "寂"], 108, X, 980, 116)
spaced(b3, "Wa-kei-sei-jaku", 50, X + 4, 1132, GOLD, ls=3)
ImageDraw.Draw(b3).text((X + 4, 1218), "Harmony, respect, purity, stillness",
                        font=ImageFont.truetype(FONT, 38), fill=SUB)
b3.save(f"{OUT}/nov_wisdom.png")

print("saved 3 overlays to", OUT)
