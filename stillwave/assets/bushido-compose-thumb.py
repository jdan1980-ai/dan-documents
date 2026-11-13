#!/usr/bin/env python3
"""BUSHIDO thumbnail — 1280x720.

The source frame is soft and muted, so the thumbnail lifts contrast and warmth a
little (only here, not in the video). 武士道 in black brush (YujiBoku) sits on the
sun; BUSHIDO in bold white on a darkened left shoji panel. Source:
bushido-2h-source.jpg (clean frame, no text).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HERE = Path(__file__).parent
SRC, OUT = HERE / "bushido-2h-source.jpg", HERE / "bushido-2h-thumb.jpg"
KANJI = str(HERE / "fonts" / "YujiBoku-Regular.ttf")
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
W, H = 1280, 720

img = Image.open(SRC).convert("RGB").resize((W, H), Image.LANCZOS)
img = ImageEnhance.Contrast(img).enhance(1.18)
img = ImageEnhance.Color(img).enhance(1.25)
r, g, b = img.split()  # gentle warm shift
img = Image.merge("RGB", (r.point(lambda v: min(255, int(v * 1.04))), g, b.point(lambda v: int(v * 0.95))))
bg = img.convert("RGBA")

# darken the left panel behind the title
sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sh).rectangle((-80, -80, 470, 300), fill=(6, 5, 4, 175))
bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(60)))

# 武士道 across the sun
f = ImageFont.truetype(KANJI, 54)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
text, cx, cy = "武士道", 640, 140
widths = [f.getbbox(c)[2] - f.getbbox(c)[0] for c in text]
gap = 6
x = cx - (sum(widths) + gap * (len(text) - 1)) / 2
for ch, wdt in zip(text, widths):
    l, t, rr, bb = f.getbbox(ch)
    md.text((x - l, cy - (t + bb) / 2), ch, font=f, fill=255)
    x += wdt + gap
halo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
halo.paste((255, 236, 200, 255), (0, 0), mask.filter(ImageFilter.GaussianBlur(5)).point(lambda p: min(255, int(p * 1.4))))
bg.alpha_composite(halo)
bg.alpha_composite(Image.composite(Image.new("RGBA", (W, H), (14, 10, 8, 255)), Image.new("RGBA", (W, H), (0, 0, 0, 0)), mask))

# BUSHIDO + subtitle, upper-left
d = ImageDraw.Draw(bg)
ft, fs = ImageFont.truetype(SANS, 90), ImageFont.truetype(SANS, 27)
def tracked(draw, xy, s, font, fill, track):
    x, y = xy
    for ch in s:
        draw.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + track
    return x
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
tracked(ImageDraw.Draw(shadow), (47, 49), "BUSHIDO", ft, (0, 0, 0, 230), 6)
bg.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(7)))
d = ImageDraw.Draw(bg)
right = tracked(d, (44, 44), "BUSHIDO", ft, (255, 255, 255, 255), 6)
tracked(d, (48, 150), "SAMURAI ZEN MUSIC", fs, (245, 234, 210, 255), 4)
bg.convert("RGB").save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
print("saved", OUT, "title right edge", int(right))
