#!/usr/bin/env python3
"""MUSHIN II thumbnail v2 — same typography as BUSHIDO / DOJO v2.

White brush kanji 無心, tracked serif "MUSHIN II", thin rules with a small circle,
"SAMURAI MEDITATION MUSIC" (the title keyword), all in the dark starry left third.
The frame stays cool (moonlight): no warm grade, only a little contrast.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HERE = Path(__file__).parent
SRC, OUT = HERE / "mushin-ii-2h-source.jpg", HERE / "mushin-ii-2h-thumb-v2.jpg"
KANJI = str(HERE / "fonts" / "YujiBoku-Regular.ttf")
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
W, H = 1280, 720
WHITE, CREAM = (250, 249, 245, 255), (226, 228, 232, 255)

img = Image.open(SRC).convert("RGB").resize((W, H), Image.LANCZOS)
img = ImageEnhance.Contrast(img).enhance(1.10)
img = ImageEnhance.Brightness(img).enhance(1.06)
bg = img.convert("RGBA")

# light extra shade on the left third (it is already dark night sky and water)
sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sh).rectangle((-100, -100, 470, H + 100), fill=(3, 4, 8, 80))
bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(70)))
d = ImageDraw.Draw(bg)
CX = 245

def centered(text, font, y, fill, track=0):
    w = sum(font.getlength(c) for c in text) + track * (len(text) - 1)
    x = CX - w / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += font.getlength(c) + track

fk = ImageFont.truetype(KANJI, 150)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
chars = "無心"
widths = [fk.getbbox(c)[2] - fk.getbbox(c)[0] for c in chars]
gap = 10
x = CX - (sum(widths) + gap) / 2
for c, wdt in zip(chars, widths):
    l, t, rr, bb = fk.getbbox(c)
    md.text((x - l, 165 - t), c, font=fk, fill=255)
    x += wdt + gap
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow.paste((200, 215, 255, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(16)).point(lambda p: int(p * 0.35)))
bg.alpha_composite(glow)
bg.alpha_composite(Image.composite(Image.new("RGBA", (W, H), WHITE), Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))
d = ImageDraw.Draw(bg)

centered("MUSHIN II", ImageFont.truetype(SERIF, 62), 352, WHITE, track=14)
d.line((CX - 160, 446, CX - 30, 446), fill=CREAM, width=2)
d.line((CX + 30, 446, CX + 160, 446), fill=CREAM, width=2)
d.ellipse((CX - 5, 441, CX + 5, 451), outline=CREAM, width=2)
centered("SAMURAI MEDITATION MUSIC", ImageFont.truetype(SERIF, 21), 468, CREAM, track=3)

bg.convert("RGB").save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
print("saved", OUT)
