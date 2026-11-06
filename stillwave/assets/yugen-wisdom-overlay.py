#!/usr/bin/env python3
"""YUGEN wisdom overlay — transparent PNG, moonlit cream/silver, lower-left.
   言わぬが花 / Iwanu ga hana / The unspoken is the flower. CapCut top track, fade 0:03-0:14."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = "/home/user/dan-documents/stillwave/assets/yugen-wisdom-overlay.png"
FONT = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
CREAM = (245, 234, 210, 255)
SILVER = (206, 216, 230, 255)
SUB = (222, 230, 240, 255)

W, H = 1920, 1080
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

kanji = ImageFont.truetype(FONT, 126)
romaji = ImageFont.truetype(FONT, 62)
gloss = ImageFont.truetype(FONT, 44)
x0, y0 = 110, int(H * 0.55)

# --- kanji 言わぬが花 at even glyph centres ---
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars = ["言", "わ", "ぬ", "が", "花"]
pitch = 134
l0, _, r0, _ = kanji.getbbox(chars[0])
c0 = x0 + (r0 - l0) / 2
for i, ch in enumerate(chars):
    l, t, r, b = kanji.getbbox(ch)
    md.text((c0 + i * pitch - (l + (r - l) / 2), y0), ch, font=kanji, fill=255)

# soft moonlit glow so it reads over drifting fog
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((188, 202, 222, 255), (0, 0),
           mask.filter(ImageFilter.GaussianBlur(18)).point(lambda p: int(p * 0.5)))
img = Image.alpha_composite(img, glow)

fill = Image.new("RGBA", (W, H), CREAM)
img = Image.alpha_composite(img, Image.composite(fill, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

d = ImageDraw.Draw(img)
# romaji — silver, letter-spaced
cx = x0 + 4
for ch in "Iwanu ga hana":
    d.text((cx, y0 + 158), ch, font=romaji, fill=SILVER)
    cx += d.textlength(ch, font=romaji) + 5
# english gloss
d.text((x0 + 4, y0 + 246), "The unspoken is the flower", font=gloss, fill=SUB)

img.save(OUT)
print("saved", OUT, img.size)
