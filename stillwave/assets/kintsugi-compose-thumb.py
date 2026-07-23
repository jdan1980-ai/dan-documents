#!/usr/bin/env python3
"""KINTSUGI thumbnail — 金継ぎ + KINTSUGI (brush, gold) upper-center over the golden-seam macro."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = "/root/.claude/uploads/48780e4d-ee5f-5a8f-92df-523468e19c72/345c3f36-1000203709.jpg"
OUT = "/home/user/dan-documents/stillwave/assets/kintsugi-thumb.jpg"
FONT = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
GOLD = (228, 196, 108)
CREAM = (245, 234, 210)

img = Image.open(SRC).convert("RGB")
W, H = img.size

# darken the LEFT zone (where text goes) so gold text reads; leave the gold delta on the right untouched
veil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(veil).ellipse((-W*0.30, -H*0.20, W*0.62, H*1.20), fill=(0, 0, 0, 120))
img = Image.alpha_composite(img.convert("RGBA"), veil.filter(ImageFilter.GaussianBlur(80))).convert("RGB")

d = ImageDraw.Draw(img)

kanji = ImageFont.truetype(FONT, 200)
romaji = ImageFont.truetype(FONT, 82)

# kanji drawn glyph-by-glyph at a fixed pitch (fixes the brush font's uneven advance, esp. ぎ)
chars = ["金", "継", "ぎ"]
pitch = 196
x0, y0 = 72, int(H*0.13)
for i, ch in enumerate(chars):
    d.text((x0 + i*pitch, y0), ch, font=kanji, fill=GOLD)

# romaji left-aligned under the kanji block
d.text((x0 + 6, y0 + 232), "KINTSUGI", font=romaji, fill=CREAM)

img.save(OUT, quality=94)
print("saved", OUT, img.size)
