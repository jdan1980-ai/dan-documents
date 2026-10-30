#!/usr/bin/env python3
"""KARESANSUI wisdom overlay — 1920x1080 transparent PNG for the long-form intro.

寂然不動 / Jakunen fudō / "Utterly still, unmoved" — the mind as still as the
central stone of a dry rock garden while the raked sand "flows" around it.
Does not name 枯山水 itself (series rule) and avoids Ma (MA already published).

LEFT-lower, standard channel layout with its own blurred dark scrim, built
before the hero image arrived; re-check placement against the delivered hero
(the dark veranda boards should sit under the text). In CapCut: TEXT layer on
the top track, start 0:03, end 0:14, fade-in 2s / fade-out 2s, no glow/shadow/box.
Cream #F5EAD2 (channel default), Liberation Serif Bold (locked channel font).

Kanji font: a Japanese gothic substitute, because YujiBoku (brush) is not in
the repo or this environment. Swap back if YujiBoku is restored.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KANJI = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/karesansui-jakunen-fudo-overlay.png"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SUB = (231, 224, 205, 255)
X = 96

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# soft scrim so cream reads over the dark veranda boards in the lower-left
s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(s).rounded_rectangle((-200, 636, 950, 1060), radius=170, fill=(8, 6, 4, 165))
img.alpha_composite(s.filter(ImageFilter.GaussianBlur(100)))

# 寂然不動 — kanji (4 chars), cream, faint warm glow
f = ImageFont.truetype(KANJI, 108)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars, pitch, y0 = ["寂", "然", "不", "動"], 128, 692
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
d.text((X + 4, 866), "Jakunen fudō", font=ImageFont.truetype(SERIF, 54), fill=CREAM)
d.text((X + 4, 940), "Utterly still, unmoved",
       font=ImageFont.truetype(SERIF, 34), fill=SUB)

img.save(OUT)
print("saved", OUT)
