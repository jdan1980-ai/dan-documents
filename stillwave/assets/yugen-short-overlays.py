#!/usr/bin/env python3
"""YUGEN Short text overlays — transparent PNGs (1080x1920), moonlit cream/silver.

🔒 SHORTS SAFE ZONE (locked 2026-07-26): the YouTube Shorts player covers the
bottom ~24% of the frame (title, channel, description, music ticker), the right
~17% (like / comment / share buttons) and the top ~7%. ALL glyphs must therefore
sit inside  y 150-1450  and  x 60-880  of 1080x1920. Text placed below y~1450 is
invisible on a phone. Verified after every build by measuring the opaque-pixel
bounding box of each overlay."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
OUT = "/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad"
W, H = 1080, 1920
CREAM = (245, 234, 210, 255)
SILVER = (206, 216, 230, 255)
SUB = (222, 230, 240, 255)
X = 78

def new(): return Image.new("RGBA", (W, H), (0, 0, 0, 0))

def scrim(img, top, bot):
    """soft dark backing on the LEFT so pale text reads over bright fog"""
    s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(s).rounded_rectangle((-140, top, 700, bot), radius=150, fill=(10, 14, 22, 150))
    img.alpha_composite(s.filter(ImageFilter.GaussianBlur(90)))

def kanji_row(img, chars, size, x0, y0, pitch, fill=CREAM, glow=(190, 205, 225)):
    f = ImageFont.truetype(FONT, size)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    l0, _, r0, _ = f.getbbox(chars[0])
    c0 = x0 + (r0 - l0) / 2
    for i, ch in enumerate(chars):
        l, t, r, b = f.getbbox(ch)
        md.text((c0 + i * pitch - (l + (r - l) / 2), y0), ch, font=f, fill=255)
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g.paste(glow + (255,), (0, 0), mask.filter(ImageFilter.GaussianBlur(16)).point(lambda p: int(p * 0.5)))
    img.alpha_composite(g)
    fl = Image.new("RGBA", (W, H), fill)
    img.alpha_composite(Image.composite(fl, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

def spaced(img, text, size, x, y, fill, ls=4):
    f = ImageFont.truetype(FONT, size)
    d = ImageDraw.Draw(img)
    cx = x
    for ch in text:
        d.text((cx, y), ch, font=f, fill=fill)
        cx += d.textlength(ch, font=f) + ls

# ---- beat 1: hook line ----  (safe zone: glyphs 1050-1290)
b1 = new()
scrim(b1, 1000, 1330)
d = ImageDraw.Draw(b1)
f1 = ImageFont.truetype(FONT, 78)
for i, line in enumerate(["What the mist", "half-shows"]):
    d.text((X, 1060 + i * 96), line, font=f1, fill=CREAM)
b1.save(f"{OUT}/yov_hook.png")

# ---- beat 2: concept 幽玄 + YUGEN ----  (safe zone: glyphs 1010-1340)
b2 = new()
scrim(b2, 950, 1400)
kanji_row(b2, ["幽", "玄"], 190, X, 940, 200)
spaced(b2, "YUGEN", 86, X + 4, 1180, SILVER, ls=8)
b2.save(f"{OUT}/yov_concept.png")

# ---- beat 3: wisdom 言わぬが花 ----  (safe zone: glyphs 1040-1310; shown on the
# final dissolving-fog shot, so it never fights the samurai silhouette)
b3 = new()
scrim(b3, 980, 1380)
kanji_row(b3, ["言", "わ", "ぬ", "が", "花"], 98, X, 1000, 105)
spaced(b3, "Iwanu ga hana", 48, X + 4, 1140, SILVER, ls=3)
ImageDraw.Draw(b3).text((X + 4, 1222), "The unspoken is the flower",
                        font=ImageFont.truetype(FONT, 38), fill=SUB)
b3.save(f"{OUT}/yov_wisdom.png")

print("saved 3 overlays to", OUT)
