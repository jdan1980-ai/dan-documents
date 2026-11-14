#!/usr/bin/env python3
"""MUSASHI wisdom overlay — 1920x1080 transparent PNG for the long-form intro.

万理一空 / Banri ikkū / "Ten thousand truths, one emptiness" — Miyamoto Musashi's
own phrase, which he brushed as calligraphy and which closes the Book of Five
Rings: every principle and technique returns to the empty, still mind. It is
the "mind before the strike" the album is built around.

LEFT-lower, standard channel layout with its own blurred dark scrim, built
before the hero image arrived; re-check placement against the delivered hero.
In CapCut: TEXT layer on the top track, start 0:03, end 0:14, fade-in 2s /
fade-out 2s, no glow/shadow/box.
Cream #F5EAD2 (channel default), Liberation Serif Bold (locked channel font).
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/musashi-banri-ikku-overlay.png"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SUB = (231, 224, 205, 255)
X = 96

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# soft scrim so cream reads over the lower-left of the frame
s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(s).rounded_rectangle((-200, 636, 950, 1060), radius=170, fill=(8, 6, 4, 165))
img.alpha_composite(s.filter(ImageFilter.GaussianBlur(100)))

# 万理一空 — kanji (4 chars), cream, faint warm glow
f = ImageFont.truetype(KANJI, 108)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars, pitch, y0 = ["万", "理", "一", "空"], 128, 692
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
d.text((X + 4, 866), "Banri ikkū", font=ImageFont.truetype(SERIF, 54), fill=CREAM)
d.text((X + 4, 940), "Ten thousand truths, one emptiness",
       font=ImageFont.truetype(SERIF, 34), fill=SUB)

img.save(OUT)
print("saved", OUT)
