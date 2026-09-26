#!/usr/bin/env python3
"""SHOSHIN wisdom overlay — 1920x1080 transparent PNG for the long-form intro.

初心忘るべからず / Shoshin wasuru bekarazu / Never forget the beginner's mind —
Zeami's famous line, exactly on-theme for 初心 (the beginner's mind).

LEFT-lower over the dark temple-floor zone. In CapCut: TEXT layer on the top
track, start 0:03, end 0:14, fade-in 2s / fade-out 2s, no glow/shadow/box.
Cream #F5EAD2, Liberation Serif Bold (the locked channel font). The kanji line is
8 characters, so it renders at a smaller size to sit cleanly in the lower-left.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/shoshin-shoshinwasuru-overlay.png"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SUB = (231, 224, 205, 255)
X = 118

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# soft scrim so cream reads over the dark tatami / shadow in the lower-left
s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(s).rounded_rectangle((-200, 632, 1010, 1060), radius=170, fill=(6, 6, 8, 150))
img.alpha_composite(s.filter(ImageFilter.GaussianBlur(100)))

# 初心忘るべからず — brush kanji (8 chars, smaller), cream, faint warm glow
f = ImageFont.truetype(KANJI, 92)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars, pitch, y0 = ["初", "心", "忘", "る", "べ", "か", "ら", "ず"], 98, 700
l0, _, r0, _ = f.getbbox(chars[0])
c0 = X + (r0 - l0) / 2
for i, ch in enumerate(chars):
    l, t, r, b = f.getbbox(ch)
    md.text((c0 + i * pitch - (l + (r - l) / 2), y0), ch, font=f, fill=255)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((250, 224, 166, 255), (0, 0),
           mask.filter(ImageFilter.GaussianBlur(18)).point(lambda p: int(p * 0.45)))
img.alpha_composite(glow)
img.alpha_composite(Image.composite(Image.new("RGBA", (W, H), CREAM),
                                    Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

d = ImageDraw.Draw(img)
d.text((X + 4, 858), "Shoshin wasuru bekarazu", font=ImageFont.truetype(SERIF, 56), fill=CREAM)
d.text((X + 4, 934), "Never forget the beginner's mind",
       font=ImageFont.truetype(SERIF, 40), fill=SUB)

img.save(OUT)
print("saved", OUT)

# preview on a dark mock background
mock = Image.new("RGB", (W, H), (18, 16, 14))
mock = Image.alpha_composite(mock.convert("RGBA"), img).convert("RGB")
mock.save("/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad/shoshin-overlay-mock.jpg", quality=92)
print("mock saved")
