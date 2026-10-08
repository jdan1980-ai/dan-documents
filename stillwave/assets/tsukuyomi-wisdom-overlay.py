#!/usr/bin/env python3
"""TSUKUYOMI wisdom overlay — 1920x1080 transparent PNG for the long-form intro.

明月清風 / Meigetsu seifū / "A bright moon, a clear wind" — a classical Zen
phrase describing a mind as pure and unclouded as a moonlit night. Overlay ≠
title concept (series rule, same logic as the RYU/HACHIMAN scripts).

LEFT-lower over the dark foreground rock/water. In CapCut: TEXT layer on the
top track, start 0:03, end 0:14, fade-in 2s / fade-out 2s, no glow/shadow/box.
Cream #F5EAD2, Liberation Serif Bold (the locked channel font). 4 kanji."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = "/home/user/dan-documents/stillwave/assets/tsukuyomi-2h-source.jpg"
KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/tsukuyomi-meigetsuseifu-overlay.png"
SP = "/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SUB = (231, 224, 205, 255)
X = 96

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# soft scrim so cream reads over the dark foreground rock/water in the lower-left
s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(s).rounded_rectangle((-200, 636, 900, 1060), radius=170, fill=(5, 6, 9, 165))
img.alpha_composite(s.filter(ImageFilter.GaussianBlur(100)))

# 明月清風 — brush kanji (4 chars), cream, faint cool glow
f = ImageFont.truetype(KANJI, 108)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars, pitch, y0 = ["明", "月", "清", "風"], 128, 692
l0, _, r0, _ = f.getbbox(chars[0])
c0 = X + (r0 - l0) / 2
for i, ch in enumerate(chars):
    l, t, r, b = f.getbbox(ch)
    md.text((c0 + i * pitch - (l + (r - l) / 2), y0), ch, font=f, fill=255)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((220, 230, 250, 255), (0, 0),
           mask.filter(ImageFilter.GaussianBlur(18)).point(lambda p: int(p * 0.45)))
img.alpha_composite(glow)
img.alpha_composite(Image.composite(Image.new("RGBA", (W, H), CREAM),
                                    Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

d = ImageDraw.Draw(img)
d.text((X + 4, 866), "Meigetsu seifu", font=ImageFont.truetype(SERIF, 54), fill=CREAM)
d.text((X + 4, 940), "A bright moon, a clear wind",
       font=ImageFont.truetype(SERIF, 38), fill=SUB)

img.save(OUT)
print("saved", OUT)

# preview composited on the clean hero (already 16:9)
im = Image.open(SRC).convert("RGB")
tw = im.height * W / H
if im.width > tw:
    x = (im.width - tw) / 2
    im = im.crop((int(x), 0, int(x + tw), im.height))
else:
    th = im.width * H / W
    y = (im.height - th) / 2
    im = im.crop((0, int(y), im.width, int(y + th)))
im = im.resize((W, H), Image.LANCZOS)
prev = Image.alpha_composite(im.convert("RGBA"), img).convert("RGB")
prev.save(f"{SP}/tsukuyomi-overlay-preview.jpg", quality=92)
print("preview saved")
