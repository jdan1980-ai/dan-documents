#!/usr/bin/env python3
"""RONIN thumbnail — 1280x720.

浪人 in black sumi brush (YujiBoku) stacked on the full moon, the frame's visual
hook, and RONIN in bold white in the dark upper-left over the cedars, clear of
the figure's hat. Source: ronin-2h-source.jpg (clean frame, no text).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).parent
SRC = HERE / "ronin-2h-source.jpg"
OUT = HERE / "ronin-2h-thumb.jpg"
KANJI = str(HERE / "fonts" / "YujiBoku-Regular.ttf")
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
W, H = 1280, 720

bg = Image.open(SRC).convert("RGB").resize((W, H), Image.LANCZOS).convert("RGBA")

# 浪人 on the moon: black ink with a faint light halo so strokes stay readable over the dark maria
f = ImageFont.truetype(KANJI, 104)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
cx, y = 656, 8
for ch in "浪人":
    l, t, r, b = f.getbbox(ch)
    md.text((cx - (l + r) / 2, y - t), ch, font=f, fill=255)
    y += (b - t) + 14
halo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
halo.paste((235, 238, 245, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(7)).point(lambda p: min(255, int(p * 1.6))))
bg.alpha_composite(halo)
bg.alpha_composite(Image.composite(Image.new("RGBA", (W, H), (12, 10, 12, 255)), Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

# RONIN upper-left, bold white, soft dark shadow
d = ImageDraw.Draw(bg)
ft = ImageFont.truetype(SANS, 124)
text, x, ty, track = "RONIN", 52, 44, 10
sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(sh)
xx = x
for ch in text:
    sd.text((xx + 3, ty + 5), ch, font=ft, fill=(0, 0, 0, 230))
    xx += ft.getlength(ch) + track
bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
d = ImageDraw.Draw(bg)
xx = x
for ch in text:
    d.text((xx, ty), ch, font=ft, fill=(255, 255, 255, 255))
    xx += ft.getlength(ch) + track
fs = ImageFont.truetype(SANS, 34)
xx = x + 4
for ch in "SAMURAI ZEN MUSIC":
    d.text((xx, ty + 140), ch, font=fs, fill=(245, 234, 210, 255))
    xx += fs.getlength(ch) + 5

bg.convert("RGB").save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
print("saved", OUT, "RONIN right edge", int(xx))
