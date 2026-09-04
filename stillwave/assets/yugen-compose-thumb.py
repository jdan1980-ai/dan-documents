#!/usr/bin/env python3
"""YUGEN thumbnail — 幽玄 + YUGEN (brush, moonlit cream/silver) lower-left over the sea of fog."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = "/root/.claude/uploads/48780e4d-ee5f-5a8f-92df-523468e19c72/e7e4adb8-1000204015.jpg"
OUT = "/home/user/dan-documents/stillwave/assets/yugen-thumb.jpg"
FONT = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
CREAM = (245, 234, 210)
SILVER = (206, 216, 230)

img = Image.open(SRC).convert("RGB")
W, H = img.size

# gentle darkening of the lower-left so the pale text reads (fades out before the figure)
veil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(veil).ellipse((-W*0.30, H*0.42, W*0.52, H*1.30), fill=(0, 0, 0, 110))
img = Image.alpha_composite(img.convert("RGBA"),
                            veil.filter(ImageFilter.GaussianBlur(120))).convert("RGB")

kanji = ImageFont.truetype(FONT, 250)
romaji = ImageFont.truetype(FONT, 116)
x0, y0 = 150, int(H * 0.60)

# --- kanji at even glyph centres, soft moonlit glow, cream fill ---
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars = ["幽", "玄"]
pitch = 262
l0, _, r0, _ = kanji.getbbox(chars[0])
c0 = x0 + (r0 - l0) / 2
for i, ch in enumerate(chars):
    l, t, r, b = kanji.getbbox(ch)
    cx = c0 + i * pitch
    md.text((cx - (l + (r - l) / 2), y0), ch, font=kanji, fill=255)

glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((190, 205, 225, 255), (0, 0),
           mask.filter(ImageFilter.GaussianBlur(26)).point(lambda p: int(p * 0.45)))
img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")

fill = Image.new("RGB", (W, H), CREAM)
img.paste(fill, (0, 0), mask)

# romaji — silver, letter-spaced, under the kanji
d = ImageDraw.Draw(img)
cx = x0 + 6
for ch in "YUGEN":
    d.text((cx, y0 + 300), ch, font=romaji, fill=SILVER)
    cx += d.textlength(ch, font=romaji) + 14

img.save(OUT, quality=94)
print("saved", OUT, img.size)
