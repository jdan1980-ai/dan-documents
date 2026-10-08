#!/usr/bin/env python3
"""BENZAITEN wisdom overlay — 1920x1080 transparent PNG for the long-form intro.

行雲流水 / Kōun ryūsui / "Drifting clouds, flowing water" — a classical idiom
for a free, unattached mind that moves naturally, mirroring both her water
domain and the free ametric flow of the music itself. Overlay ≠ title
concept (series rule, same logic as AMATERASU/TSUKUYOMI/HACHIMAN scripts).

LEFT-lower over the dark foreground platform wood, clear of the goddess and
the biwa hōshi. In CapCut: TEXT layer on the top track, start 0:03, end
0:14, fade-in 2s / fade-out 2s, no glow/shadow/box. Cream #F5EAD2,
Liberation Serif Bold (the locked channel font). 4 kanji, horizontal —
same SAME-Y horizontal layout as amaterasu/tsukuyomi-wisdom-overlay.py."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/benzaiten-kounryusui-overlay.png"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SUB = (231, 224, 205, 255)
X = 96

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# soft scrim so cream reads over the dark foreground platform wood in the lower-left
s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(s).rounded_rectangle((-200, 636, 950, 1060), radius=170, fill=(8, 6, 4, 175))
img.alpha_composite(s.filter(ImageFilter.GaussianBlur(100)))

# 行雲流水 — brush kanji (4 chars), cream, faint warm glow
f = ImageFont.truetype(KANJI, 108)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars, pitch, y0 = ["行", "雲", "流", "水"], 128, 692
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
d.text((X + 4, 866), "Koun ryusui", font=ImageFont.truetype(SERIF, 54), fill=CREAM)
d.text((X + 4, 940), "Drifting clouds, flowing water",
       font=ImageFont.truetype(SERIF, 38), fill=SUB)

img.save(OUT)
print("saved", OUT)
