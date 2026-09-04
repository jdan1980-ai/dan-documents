#!/usr/bin/env python3
"""KOKORO wisdom overlay — 1920x1080 transparent PNG for the long-form intro.

安心立命 / Anjin ritsumei / Peace of mind, serene stability — a Buddhist yojijukugo
about resting the heart in complete spiritual peace, exactly on-theme for kokoro
(心, the heart-mind) and emotional healing.

LEFT side over the calm dark temple-pillar zone. In CapCut: TEXT layer on the top
track, start 0:03, end 0:14, fade-in 2s / fade-out 2s, no glow/shadow/box.
Cream #F5EAD2, Liberation Serif Bold (the locked channel font).
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KANJI = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/kokoro-anjinritsumei-overlay.png"
W, H = 1920, 1080
CREAM = (245, 234, 210, 255)
SUB = (231, 224, 205, 255)
X = 120

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# soft scrim so cream reads over the dark tatami / shadow in the lower-left
s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(s).rounded_rectangle((-200, 660, 820, 1060), radius=170, fill=(6, 6, 9, 150))
img.alpha_composite(s.filter(ImageFilter.GaussianBlur(100)))

# 安心立命 — brush kanji, cream, faint warm glow for legibility over the wood
f = ImageFont.truetype(KANJI, 132)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars, pitch, y0 = ["安", "心", "立", "命"], 144, 720
l0, _, r0, _ = f.getbbox(chars[0])
c0 = X + (r0 - l0) / 2
for i, ch in enumerate(chars):
    l, t, r, b = f.getbbox(ch)
    md.text((c0 + i * pitch - (l + (r - l) / 2), y0), ch, font=f, fill=255)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((250, 224, 166, 255), (0, 0),
           mask.filter(ImageFilter.GaussianBlur(20)).point(lambda p: int(p * 0.45)))
img.alpha_composite(glow)
img.alpha_composite(Image.composite(Image.new("RGBA", (W, H), CREAM),
                                    Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

d = ImageDraw.Draw(img)
d.text((X + 4, 878), "Anjin ritsumei", font=ImageFont.truetype(SERIF, 58), fill=CREAM)
d.text((X + 4, 952), "Peace of mind, serene stability",
       font=ImageFont.truetype(SERIF, 42), fill=SUB)

img.save(OUT)
print("saved", OUT)
