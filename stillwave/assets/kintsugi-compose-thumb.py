#!/usr/bin/env python3
"""KINTSUGI thumbnail — 金継ぎ (molten-gold gradient, like the seam) + KINTSUGI, lower-left under the seam."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = "/root/.claude/uploads/48780e4d-ee5f-5a8f-92df-523468e19c72/345c3f36-1000203709.jpg"
OUT = "/home/user/dan-documents/stillwave/assets/kintsugi-thumb.jpg"
FONT = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
CREAM = (245, 234, 210)

img = Image.open(SRC).convert("RGB")
W, H = img.size

# darken the LOWER-LEFT zone (under the seam) so the text reads
veil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(veil).ellipse((-W*0.35, H*0.30, W*0.60, H*1.35), fill=(0, 0, 0, 130))
img = Image.alpha_composite(img.convert("RGBA"), veil.filter(ImageFilter.GaussianBlur(80))).convert("RGB")

kanji = ImageFont.truetype(FONT, 188)
romaji = ImageFont.truetype(FONT, 96)
x0, y0 = 70, int(H * 0.44)

# --- kanji into a mask, packed tight by ink width (kills the brush font's ぎ gap) ---
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
cursor, gap = x0, 30
for ch in ["金", "継", "ぎ"]:
    l, t, r, b = kanji.getbbox(ch)
    md.text((cursor - l, y0), ch, font=kanji, fill=255)
    cursor += (r - l) + gap

# --- molten-gold vertical gradient (like the seam: hot core, amber, deep bronze) ---
stops = [(0.00, (255, 240, 186)), (0.35, (240, 205, 112)),
         (0.62, (216, 168, 70)), (1.00, (138, 86, 26))]
def lerp(a, b, f): return tuple(int(a[i] + (b[i]-a[i])*f) for i in range(3))
def grad_color(f):
    f = max(0.0, min(1.0, f))
    for i in range(len(stops)-1):
        f0, c0 = stops[i]; f1, c1 = stops[i+1]
        if f <= f1:
            return lerp(c0, c1, (f-f0)/(f1-f0))
    return stops[-1][1]

y_top, y_bot = y0 + 24, y0 + 196
col = Image.new("RGB", (1, H))
for y in range(H):
    col.putpixel((0, y), grad_color((y - y_top) / (y_bot - y_top)))
grad = col.resize((W, H))

# soft warm glow behind the kanji (glows from within, like the gold)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((255, 196, 92), (0, 0), mask.filter(ImageFilter.GaussianBlur(14)).point(lambda p: int(p*0.55)))
img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")

# fill the kanji with the gradient through the mask
img.paste(grad, (0, 0), mask)

# romaji — cream, left-aligned under the kanji
ImageDraw.Draw(img).text((x0 + 6, y0 + 210), "KINTSUGI", font=romaji, fill=CREAM)

img.save(OUT, quality=94)
print("saved", OUT, img.size)
