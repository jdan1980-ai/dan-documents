#!/usr/bin/env python3
"""KOMOREBI wisdom overlay — 1920x1080 transparent PNG for the long-form intro.

一期一会 / Ichigo ichie / This moment, once, never again — a yojijukugo about the
once-in-a-lifetime nature of any single encounter, exactly on-theme for komorebi:
the precise pattern of light through the leaves will never fall the same way twice.

LEFT side over the calm dark forest-shadow zone. In CapCut: TEXT layer on the top
track, start 0:03, end 0:14, fade-in 2s / fade-out 2s, no glow/shadow/box.
Cream #F5EAD2, Liberation Serif Bold (the locked channel font).
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/komorebi-ichigoichie-overlay.png"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SUB = (231, 226, 210, 255)
X = 120

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# soft scrim so cream reads over the dark forest / ferns on the left
s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(s).rounded_rectangle((-200, 360, 900, 800), radius=180, fill=(8, 12, 8, 140))
img.alpha_composite(s.filter(ImageFilter.GaussianBlur(110)))

# 一期一会 — brush kanji, cream, with a faint warm glow for legibility over foliage
f = ImageFont.truetype(KANJI, 150)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars, pitch, y0 = ["一", "期", "一", "会"], 162, 400
l0, _, r0, _ = f.getbbox(chars[0])
c0 = X + (r0 - l0) / 2
for i, ch in enumerate(chars):
    l, t, r, b = f.getbbox(ch)
    md.text((c0 + i * pitch - (l + (r - l) / 2), y0), ch, font=f, fill=255)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((250, 226, 168, 255), (0, 0),
           mask.filter(ImageFilter.GaussianBlur(20)).point(lambda p: int(p * 0.45)))
img.alpha_composite(glow)
img.alpha_composite(Image.composite(Image.new("RGBA", (W, H), CREAM),
                                    Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

d = ImageDraw.Draw(img)
d.text((X + 4, 600), "Ichigo ichie", font=ImageFont.truetype(SERIF, 64), fill=CREAM)
d.text((X + 4, 684), "This moment, once, never again",
       font=ImageFont.truetype(SERIF, 46), fill=SUB)

img.save(OUT)
print("saved", OUT)
