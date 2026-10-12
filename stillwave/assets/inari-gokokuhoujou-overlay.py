#!/usr/bin/env python3
"""INARI wisdom overlay — 1920x1080 transparent PNG for the long-form intro.

五穀豊穣 / Gokoku hōjō / "Abundant harvest of the five grains" — a classical
Shinto shrine-blessing phrase for agricultural abundance and prosperity,
directly Inari's own domain without naming him. Overlay ≠ title concept
(series rule, same logic as the rest of the KAMI scripts).

LEFT-lower over a calm dark zone (the misted foreground rice field works
in the actual long-form scene). In CapCut: TEXT layer on the top track,
start 0:03, end 0:14, fade-in 2s / fade-out 2s, no glow/shadow/box.
Cream #F5EAD2 (channel default), Liberation Serif Bold (the locked
channel font). 4 kanji, horizontal — same layout as the rest of the
KAMI series overlays."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/inari-gokokuhoujou-overlay.png"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SUB = (231, 224, 205, 255)
X = 96

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# soft scrim so cream reads over whatever sits in the lower-left of the actual scene
s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(s).rounded_rectangle((-200, 636, 950, 1060), radius=170, fill=(8, 6, 4, 175))
img.alpha_composite(s.filter(ImageFilter.GaussianBlur(100)))

# 五穀豊穣 — brush kanji (4 chars), cream, faint warm glow
f = ImageFont.truetype(KANJI, 108)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars, pitch, y0 = ["五", "穀", "豊", "穣"], 128, 692
l0, _, r0, _ = f.getbbox(chars[0])
c0 = X + (r0 - l0) / 2
for i, ch in enumerate(chars):
    l, t, r, b = f.getbbox(ch)
    md.text((c0 + i * pitch - (l + (r - l) / 2), y0), ch, font=f, fill=255)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((250, 220, 180, 255), (0, 0),
           mask.filter(ImageFilter.GaussianBlur(18)).point(lambda p: int(p * 0.45)))
img.alpha_composite(glow)
img.alpha_composite(Image.composite(Image.new("RGBA", (W, H), CREAM),
                                    Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

d = ImageDraw.Draw(img)
d.text((X + 4, 866), "Gokoku hojo", font=ImageFont.truetype(SERIF, 54), fill=CREAM)
d.text((X + 4, 940), "A bountiful harvest for all",
       font=ImageFont.truetype(SERIF, 34), fill=SUB)

img.save(OUT)
print("saved", OUT)
