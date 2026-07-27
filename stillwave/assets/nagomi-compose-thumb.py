#!/usr/bin/env python3
"""NAGOMI thumbnail — 和 + NAGOMI over the warm tatami room hero (1920x1080).

Text sits LOWER-LEFT: the upper-left of this hero is taken by the hanging scroll,
and the lower-left tatami is the calmest, most uniform area in the frame.
Bottom-right stays free for the channel logo.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = "/root/.claude/uploads/48780e4d-ee5f-5a8f-92df-523468e19c72/652d549f-1000204797.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/nagomi-2h-thumb.jpg"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
X = 116

im = Image.open(SRC).convert("RGB")
tw = im.height * W / H
if im.width > tw:
    x = (im.width - tw) / 2
    im = im.crop((int(x), 0, int(x + tw), im.height))
else:
    th = im.width * H / W
    y = (im.height - th) / 2
    im = im.crop((0, int(y), im.width, int(y + th)))
im = im.resize((W, H), Image.LANCZOS).convert("RGBA")

# gentle vignette — keeps the eye on the warm centre and helps the text read
vig = Image.new("L", (W, H), 0)
ImageDraw.Draw(vig).ellipse((-W * 0.30, -H * 0.42, W * 1.30, H * 1.42), fill=255)
vig = vig.filter(ImageFilter.GaussianBlur(200))
im = Image.composite(im, Image.new("RGBA", (W, H), (18, 12, 6, 255)), vig.point(lambda p: 60 + p * 0.76 // 1))

# soft scrim under the text block
s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(s).rounded_rectangle((-220, 440, 780, 1000), radius=200, fill=(22, 14, 6, 150))
im.alpha_composite(s.filter(ImageFilter.GaussianBlur(120)))

# 和 — glow + cream fill
f = ImageFont.truetype(KANJI, 330)
mask = Image.new("L", (W, H), 0)
l, t, r, b = f.getbbox("和")
ImageDraw.Draw(mask).text((X - l, 470), "和", font=f, fill=255)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((250, 214, 150, 255), (0, 0),
           mask.filter(ImageFilter.GaussianBlur(26)).point(lambda p: int(p * 0.55)))
im.alpha_composite(glow)
im.alpha_composite(Image.composite(Image.new("RGBA", (W, H), CREAM),
                                   Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

# NAGOMI — letter-spaced under the kanji
d = ImageDraw.Draw(im)
fn = ImageFont.truetype(KANJI, 118)
cx = X + 6
for ch in "NAGOMI":
    d.text((cx, 838), ch, font=fn, fill=CREAM)
    cx += d.textlength(ch, font=fn) + 13

im.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
