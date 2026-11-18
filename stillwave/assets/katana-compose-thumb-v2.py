#!/usr/bin/env python3
"""KATANA thumbnail v2 — same layout as BUSHIDO / DOJO / MUSHIN II v2, but in dark ink.

The left third of this frame is bright mist (mean ~110-160), so white type would not read.
Instead: a large black sumi-ink brush 刀, dark tracked serif "KATANA", thin rules with a
small circle, "SAMURAI MEDITATION MUSIC". A soft light haze is laid behind the type.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HERE = Path(__file__).parent
WHITE_MODE = "--white" in sys.argv   # white type on a darkened left third (BUSHIDO/DOJO look)
SRC = HERE / "katana-2h-source.jpg"
OUT = HERE / ("katana-2h-thumb-v2-white.jpg" if WHITE_MODE else "katana-2h-thumb-v2.jpg")
KANJI = str(HERE / "fonts" / "YujiBoku-Regular.ttf")
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
W, H = 1280, 720
INK, INK2 = ((250, 247, 240, 255), (232, 228, 220, 255)) if WHITE_MODE else ((16, 18, 24, 255), (34, 38, 46, 255))

img = Image.open(SRC).convert("RGB").resize((W, H), Image.LANCZOS)
img = ImageEnhance.Contrast(img).enhance(1.12)
bg = img.convert("RGBA")

# soft light haze behind the type so the ink reads on the misty sky
hz = Image.new("RGBA", (W, H), (0, 0, 0, 0))
if WHITE_MODE:   # darken the misty left third so white type reads
    ImageDraw.Draw(hz).rectangle((-120, -100, 480, H + 100), fill=(6, 8, 14, 170))
    hz = hz.filter(ImageFilter.GaussianBlur(90))
else:            # soft light haze so the dark ink reads
    ImageDraw.Draw(hz).ellipse((-180, 40, 560, 600), fill=(222, 228, 236, 105))
    hz = hz.filter(ImageFilter.GaussianBlur(80))
bg.alpha_composite(hz)
d = ImageDraw.Draw(bg)
CX = 215

def centered(text, font, y, fill, track=0):
    w = sum(font.getlength(c) for c in text) + track * (len(text) - 1)
    x = CX - w / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += font.getlength(c) + track

fk = ImageFont.truetype(KANJI, 230)
l, t, r, b = fk.getbbox("刀")
mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).text((CX - (l + r) / 2, 95 - t), "刀", font=fk, fill=255)
if WHITE_MODE:
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh.paste((0, 0, 0, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(10)).point(lambda p: int(p * 0.7)))
    bg.alpha_composite(sh)
bg.alpha_composite(Image.composite(Image.new("RGBA", (W, H), INK), Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))
d = ImageDraw.Draw(bg)

centered("KATANA", ImageFont.truetype(SERIF, 64), 355, INK, track=16)
d.line((CX - 150, 450, CX - 30, 450), fill=INK2, width=2)
d.line((CX + 30, 450, CX + 150, 450), fill=INK2, width=2)
d.ellipse((CX - 5, 445, CX + 5, 455), outline=INK2, width=2)
centered("SAMURAI MEDITATION MUSIC", ImageFont.truetype(SERIF, 21), 472, INK2, track=3)

bg.convert("RGB").save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
print("saved", OUT)
