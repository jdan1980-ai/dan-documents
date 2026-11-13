#!/usr/bin/env python3
"""BUSHIDO thumbnail v2 — competitor-style typography (GAN / JAKU / TAO pattern).

White brush kanji, widely tracked serif romaji, thin rules and a small
"JAPANESE ZEN MUSIC" line, set in the darkened left panel. No bold sans.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HERE = Path(__file__).parent
SRC, OUT = HERE / "bushido-2h-source.jpg", HERE / "bushido-2h-thumb-v2.jpg"
KANJI = str(HERE / "fonts" / "YujiBoku-Regular.ttf")
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
W, H = 1280, 720
WHITE, CREAM = (250, 247, 240, 255), (232, 222, 200, 255)

img = Image.open(SRC).convert("RGB").resize((W, H), Image.LANCZOS)
img = ImageEnhance.Contrast(img).enhance(1.22)
img = ImageEnhance.Color(img).enhance(1.3)
r, g, b = img.split()
img = Image.merge("RGB", (r.point(lambda v: min(255, int(v * 1.05))), g, b.point(lambda v: int(v * 0.93))))
bg = img.convert("RGBA")

# darken the whole left third so white type reads
sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sh).rectangle((-100, -100, 470, H + 100), fill=(5, 4, 3, 200))
bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(70)))
d = ImageDraw.Draw(bg)
CX = 215

def centered(text, font, y, fill, track=0):
    w = sum(font.getlength(c) for c in text) + track * (len(text) - 1)
    x = CX - w / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += font.getlength(c) + track

# kanji 武士道, horizontal, large white brush with soft shadow
fk = ImageFont.truetype(KANJI, 118)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
widths = [fk.getbbox(c)[2] - fk.getbbox(c)[0] for c in "武士道"]
gap = 4
x = CX - (sum(widths) + gap * 2) / 2
for c, wdt in zip("武士道", widths):
    l, t, rr, bb = fk.getbbox(c)
    md.text((x - l, 190 - t), c, font=fk, fill=255)
    x += wdt + gap
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
shadow.paste((0, 0, 0, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(10)).point(lambda p: int(p * 0.8)))
bg.alpha_composite(shadow)
bg.alpha_composite(Image.composite(Image.new("RGBA", (W, H), WHITE), Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))
d = ImageDraw.Draw(bg)

centered("BUSHIDO", ImageFont.truetype(SERIF, 66), 345, WHITE, track=16)
d.line((CX - 150, 440, CX - 30, 440), fill=CREAM, width=2)
d.line((CX + 30, 440, CX + 150, 440), fill=CREAM, width=2)
d.ellipse((CX - 5, 435, CX + 5, 445), outline=CREAM, width=2)
centered("JAPANESE ZEN MUSIC", ImageFont.truetype(SERIF, 24), 462, CREAM, track=6)

bg.convert("RGB").save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
print("saved", OUT)
