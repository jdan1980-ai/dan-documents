#!/usr/bin/env python3
"""KINTSUGI wisdom overlay — transparent PNG, molten-gold, lower-left under the seam.
   傷も景色 / Kizu mo keshiki / Even the scar is scenery. Drop on CapCut top track, fade 0:03-0:14."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = "/home/user/dan-documents/stillwave/assets/kintsugi-wisdom-overlay.png"
FONT = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"

W, H = 1920, 1080
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

kanji = ImageFont.truetype(FONT, 150)
romaji = ImageFont.truetype(FONT, 66)
gloss = ImageFont.truetype(FONT, 46)
x0, y0 = 110, int(H * 0.55)

# --- kanji 傷も景色 into a mask at even glyph centres ---
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars = ["傷", "も", "景", "色"]
pitch = 162
l0, _, r0, _ = kanji.getbbox(chars[0])
c0 = x0 + (r0 - l0) / 2
for i, ch in enumerate(chars):
    l, t, r, b = kanji.getbbox(ch)
    cx = c0 + i * pitch
    md.text((cx - (l + (r - l) / 2), y0), ch, font=kanji, fill=255)

# --- molten-gold vertical gradient (same recipe as the thumbnail) ---
stops = [(0.00, (255, 240, 186)), (0.35, (240, 205, 112)),
         (0.62, (216, 168, 70)), (1.00, (150, 96, 32))]
def lerp(a, b, f): return tuple(int(a[i] + (b[i]-a[i])*f) for i in range(3))
def grad_color(f):
    f = max(0.0, min(1.0, f))
    for i in range(len(stops)-1):
        f0, c0c = stops[i]; f1, c1 = stops[i+1]
        if f <= f1:
            return lerp(c0c, c1, (f-f0)/(f1-f0))
    return stops[-1][1]

y_top, y_bot = y0 + 18, y0 + 156
col = Image.new("RGB", (1, H))
for y in range(H):
    col.putpixel((0, y), grad_color((y - y_top) / (y_bot - y_top)))
grad = col.resize((W, H)).convert("RGBA")

# soft warm glow behind the kanji (reads over the moving gold video)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((255, 196, 92, 255), (0, 0),
           mask.filter(ImageFilter.GaussianBlur(16)).point(lambda p: int(p * 0.6)))
img = Image.alpha_composite(img, glow)

# fill kanji with gradient through the mask
gold_kanji = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gold_kanji.paste(grad, (0, 0), mask)
img = Image.alpha_composite(img, gold_kanji)

# romaji + gloss — warm gold, left-aligned under the kanji
d = ImageDraw.Draw(img)
d.text((x0 + 4, y0 + 182), "Kizu mo keshiki", font=romaji, fill=(228, 196, 108, 255))
d.text((x0 + 4, y0 + 274), "Even the scar is scenery", font=gloss, fill=(235, 214, 168, 255))

img.save(OUT)
print("saved", OUT, img.size)
