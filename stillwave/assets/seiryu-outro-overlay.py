#!/usr/bin/env python3
"""SEIRYU outro overlay — 1920x1080 transparent PNG for the end of the long-form.

"Thank You for Watching" / "Subscribe for More Japanese Zen Music" — white
Liberation Serif Bold (channel font), centred, soft dark scrim behind for
legibility over any end-frame. Drop on the top track in CapCut over the
final ~10-15s of the video, fade-in 2s.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = "/home/user/dan-documents/stillwave/assets/seiryu-2h-source.jpg"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
OUT = "/home/user/dan-documents/stillwave/assets/seiryu-outro-overlay.png"
SP = "/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad"
W, H = 1920, 1080
WHITE = (255, 255, 255, 255)
CENTRE = 960

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

f1 = ImageFont.truetype(SERIF, 84)
f2 = ImageFont.truetype(SERIF, 50)
line1 = "Thank You for Watching"
line2 = "Subscribe for More Japanese Zen Music"

w1 = d.textlength(line1, font=f1)
w2 = d.textlength(line2, font=f2)
y1, y2 = 470, 580

# soft dark scrim behind both lines so white reads over any end-frame
pad_x, pad_top, pad_bot = 90, 40, 30
left = CENTRE - max(w1, w2) / 2 - pad_x
right = CENTRE + max(w1, w2) / 2 + pad_x
sc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sc).rounded_rectangle((left, y1 - pad_top, right, y2 + 50 + pad_bot),
                                     radius=90, fill=(4, 5, 7, 165))
img.alpha_composite(sc.filter(ImageFilter.GaussianBlur(70)))

d.text((CENTRE - w1 / 2, y1), line1, font=f1, fill=WHITE)
d.text((CENTRE - w2 / 2, y2), line2, font=f2, fill=WHITE)

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
prev.save(f"{SP}/seiryu-outro-preview.jpg", quality=92)
print("preview saved")
