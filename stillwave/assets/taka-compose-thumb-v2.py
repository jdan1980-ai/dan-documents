#!/usr/bin/env python3
"""TAKA thumbnail v2 — same layout as BUSHIDO / DOJO / MUSHIN II / KATANA v2.

White brush 鷹, tracked serif "TAKA", thin rules with a small circle,
"SAMURAI MEDITATION MUSIC" over a dark scrim on the left bamboo doors.
The hawk's eyes get the same warm glow as in the animated video.
"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HERE = Path(__file__).parent
SRC, OUT = HERE / "taka-2h-source.jpg", HERE / "taka-2h-thumb-v2.jpg"
KANJI = str(HERE / "fonts" / "YujiBoku-Regular.ttf")
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
W, H = 1280, 720
WHITE, CREAM = (250, 247, 240, 255), (232, 222, 200, 255)

img = Image.open(SRC).convert("RGB").resize((W, H), Image.LANCZOS)
img = ImageEnhance.Contrast(img).enhance(1.12)
img = ImageEnhance.Brightness(img).enhance(1.05)

# glowing eyes (positions of the 1920 frame scaled to 1280)
a = np.asarray(img).astype(np.float32)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
k = W / 1920
glow = np.zeros((H, W), np.float32)
for ex, ey in [(917, 277), (975, 277)]:
    ex, ey = ex * k, ey * k
    for s, w in [(4, 1.0), (10, 0.5), (24, 0.2)]:
        glow += w * np.exp(-((xx - ex) ** 2 + (yy - ey) ** 2) / (2 * s * s))
a += glow[..., None] * np.array([240, 150, 45], np.float32) * 0.7
bg = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert("RGBA")

sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sh).rectangle((-100, -100, 430, H + 100), fill=(4, 3, 2, 175))
bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(70)))
d = ImageDraw.Draw(bg)
CX = 215

def centered(text, font, y, fill, track=0):
    w = sum(font.getlength(c) for c in text) + track * (len(text) - 1)
    x = CX - w / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += font.getlength(c) + track

fk = ImageFont.truetype(KANJI, 230)
l, t, r, b = fk.getbbox("鷹")
mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).text((CX - (l + r) / 2, 90 - t), "鷹", font=fk, fill=255)
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
shadow.paste((0, 0, 0, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(10)).point(lambda p: int(p * 0.8)))
bg.alpha_composite(shadow)
bg.alpha_composite(Image.composite(Image.new("RGBA", (W, H), WHITE), Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))
d = ImageDraw.Draw(bg)

centered("TAKA", ImageFont.truetype(SERIF, 66), 358, WHITE, track=18)
d.line((CX - 150, 453, CX - 30, 453), fill=CREAM, width=2)
d.line((CX + 30, 453, CX + 150, 453), fill=CREAM, width=2)
d.ellipse((CX - 5, 448, CX + 5, 458), outline=CREAM, width=2)
centered("SAMURAI MEDITATION MUSIC", ImageFont.truetype(SERIF, 21), 475, CREAM, track=3)

bg.convert("RGB").save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
print("saved", OUT)
