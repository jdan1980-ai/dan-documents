#!/usr/bin/env python3
"""KATANA thumbnail v2 — same layout as BUSHIDO / DOJO / MUSHIN II v2, but in dark ink.

The left third of this frame is bright mist (mean ~110-160), so white type would not read.
Instead: a large black sumi-ink brush 刀, dark tracked serif "KATANA", thin rules with a
small circle, "SAMURAI MEDITATION MUSIC". A soft light haze is laid behind the type.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HERE = Path(__file__).parent
SRC, OUT = HERE / "katana-2h-source.jpg", HERE / "katana-2h-thumb-v2.jpg"
KANJI = str(HERE / "fonts" / "YujiBoku-Regular.ttf")
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
W, H = 1280, 720
INK, INK2 = (16, 18, 24, 255), (34, 38, 46, 255)

img = Image.open(SRC).convert("RGB").resize((W, H), Image.LANCZOS)
img = ImageEnhance.Contrast(img).enhance(1.12)
bg = img.convert("RGBA")

# soft light haze behind the type so the ink reads on the misty sky
hz = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(hz).ellipse((-180, 40, 560, 600), fill=(222, 228, 236, 105))
bg.alpha_composite(hz.filter(ImageFilter.GaussianBlur(80)))
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
bg.alpha_composite(Image.composite(Image.new("RGBA", (W, H), INK), Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))
d = ImageDraw.Draw(bg)

centered("KATANA", ImageFont.truetype(SERIF, 64), 355, INK, track=16)
d.line((CX - 150, 450, CX - 30, 450), fill=INK2, width=2)
d.line((CX + 30, 450, CX + 150, 450), fill=INK2, width=2)
d.ellipse((CX - 5, 445, CX + 5, 455), outline=INK2, width=2)
centered("SAMURAI MEDITATION MUSIC", ImageFont.truetype(SERIF, 21), 472, INK2, track=3)

bg.convert("RGB").save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
print("saved", OUT)
