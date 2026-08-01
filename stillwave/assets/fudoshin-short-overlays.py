#!/usr/bin/env python3
"""FUDOSHIN Short text overlays — transparent PNGs (1080x1920), gold + cream.

🔒 SHORTS SAFE ZONE: glyphs must sit inside y 150-1450, x 60-880 of 1080x1920
(the player hides the bottom ~24% / right ~17% / top ~7%). Verified by measuring
each overlay's opaque bounding box after render."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
OUT = "/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad"
W, H = 1080, 1920
CREAM = (245, 234, 210, 255)
GOLD = (232, 197, 120, 255)
SUB = (223, 230, 233, 255)
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


def scrim(img, top, bot):
    s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(s).rounded_rectangle((-140, top, 720, bot), radius=150, fill=(8, 12, 14, 155))
    img.alpha_composite(s.filter(ImageFilter.GaussianBlur(90)))


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
               mask.filter(ImageFilter.GaussianBlur(20)).point(lambda p: int(p * 0.55)))
    img.alpha_composite(glow)
    span = max(1, int(bot - top))
    col = Image.new("RGB", (1, span))
    for yy in range(span):
        col.putpixel((0, yy), gold(yy / span))
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    canvas.paste(col.resize((W, span)).convert("RGBA"), (0, int(top)))
    img.alpha_composite(Image.composite(canvas, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))


def spaced(img, text, size, x, y, fill=CREAM, ls=6):
    f = ImageFont.truetype(KANJI, size)
    d = ImageDraw.Draw(img)
    cx = x
    for ch in text:
        d.text((cx, y), ch, font=f, fill=fill)
        cx += d.textlength(ch, font=f) + ls


# ---- beat 1: hook ----
b1 = new()
scrim(b1, 980, 1330)
d = ImageDraw.Draw(b1)
f1 = ImageFont.truetype(KANJI, 82)
for i, line in enumerate(["The storm", "cannot move you"]):
    d.text((X, 1040 + i * 100), line, font=f1, fill=CREAM)
b1.save(f"{OUT}/fov_hook.png")

# ---- beat 2: concept 不動心 + FUDOSHIN ----
b2 = new()
scrim(b2, 940, 1400)
gold_kanji(b2, ["不", "動", "心"], 210, X, 960, 226)
spaced(b2, "FUDOSHIN", 80, X + 4, 1210, GOLD, ls=10)
b2.save(f"{OUT}/fov_concept.png")

# ---- beat 3: wisdom 泰然自若 ----
b3 = new()
scrim(b3, 960, 1400)
gold_kanji(b3, ["泰", "然", "自", "若"], 118, X, 980, 128)
spaced(b3, "Taizen jijaku", 50, X + 4, 1146, GOLD, ls=3)
ImageDraw.Draw(b3).text((X + 4, 1228), "Calm and composed, unshaken",
                        font=ImageFont.truetype(KANJI, 38), fill=SUB)
b3.save(f"{OUT}/fov_wisdom.png")

print("saved 3 overlays to", OUT)
