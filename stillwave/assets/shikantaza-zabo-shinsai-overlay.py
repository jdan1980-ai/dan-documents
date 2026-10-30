#!/usr/bin/env python3
"""SHIKANTAZA album wisdom overlay — 1920x1080 transparent PNG for the long-form intro.

坐忘心斎 / Zabō shinsai / "Sit, forget, empty the mind" — from Zhuangzi: sitting
until the self is forgotten, the mind emptied like a fasting vessel. It is the
inner side of shikantaza (just sitting): the figure on the rock is not reaching
for anything, only sitting under the full moon in the rain.

LEFT-lower over the dark rock ledge (measured mean brightness ~23 for the lower-
left zone of the delivered hero, but the moon and cloud bands raise the upper-
left, so the scrim is set heavier than the other overlays). In CapCut: TEXT layer
on the top track, start 0:03, end 0:14, fade-in 2s / fade-out 2s, no glow/shadow/box.
Cream #F5EAD2 (channel default), Liberation Serif Bold (locked channel font).
4 kanji, horizontal — same layout as the rest of the channel's overlays.

Kanji font: a Japanese gothic substitute, because YujiBoku (brush) is not in
the repo or this environment. Swap back if YujiBoku is restored.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KANJI = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/shikantaza-zabo-shinsai-overlay.png"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SUB = (231, 224, 205, 255)
X = 96

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# heavier scrim: the cloud bands behind the kanji row are mid-grey
s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(s).rounded_rectangle((-200, 620, 980, 1070), radius=170, fill=(6, 5, 8, 200))
img.alpha_composite(s.filter(ImageFilter.GaussianBlur(100)))

# 坐忘心斎 — kanji (4 chars), cream, faint warm glow
f = ImageFont.truetype(KANJI, 108)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars, pitch, y0 = ["坐", "忘", "心", "斎"], 128, 692
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
d.text((X + 4, 866), "Zabō shinsai", font=ImageFont.truetype(SERIF, 54), fill=CREAM)
d.text((X + 4, 940), "Sit, forget, empty the mind",
       font=ImageFont.truetype(SERIF, 34), fill=SUB)

img.save(OUT)
print("saved", OUT)
