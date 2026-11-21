#!/usr/bin/env python3
"""NAGOMI wisdom overlay — 1920x1080 transparent PNG for the long-form intro.

和敬清寂 / Wa-kei-sei-jaku / Harmony, respect, purity, stillness — the four
principles of Sen no Rikyū's tea ceremony; 和 is the first of them.

Lower-left over the warm-dark corner the §3 hero keeps free. In the edit:
fade-in 2s -> hold ~5s -> fade-out 2s, over the 0:00-0:03 scene only.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/nagomi-wakeiseijaku-overlay.png"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
GOLD = (238, 205, 138, 255)
SUB = (233, 219, 192, 255)
X = 118

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# soft scrim so cream reads over warm tatami light
s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(s).rounded_rectangle((-200, 560, 980, 1010), radius=180, fill=(24, 16, 8, 150))
img.alpha_composite(s.filter(ImageFilter.GaussianBlur(110)))

# 和敬清寂 — even glyph centres, honey-gold glow, cream fill
f = ImageFont.truetype(KANJI, 132)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars, pitch, y0 = ["和", "敬", "清", "寂"], 142, 620
l0, _, r0, _ = f.getbbox(chars[0])
c0 = X + (r0 - l0) / 2
for i, ch in enumerate(chars):
    l, t, r, b = f.getbbox(ch)
    md.text((c0 + i * pitch - (l + (r - l) / 2), y0), ch, font=f, fill=255)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((250, 214, 150, 255), (0, 0),
           mask.filter(ImageFilter.GaussianBlur(20)).point(lambda p: int(p * 0.5)))
img.alpha_composite(glow)
fill = Image.new("RGBA", (W, H), CREAM)
img.alpha_composite(Image.composite(fill, Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

d = ImageDraw.Draw(img)
d.text((X + 4, 810), "Wa-kei-sei-jaku", font=ImageFont.truetype(SERIF, 62), fill=GOLD)
d.text((X + 4, 890), "Harmony, respect, purity, stillness",
       font=ImageFont.truetype(SERIF, 46), fill=SUB)

img.save(OUT)
print("saved", OUT)
