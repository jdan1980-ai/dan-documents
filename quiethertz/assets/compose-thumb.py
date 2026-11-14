#!/usr/bin/env python3
"""Quiet Hertz thumbnail compose — parameterized template, NOT redesigned per video.

Layout matches the competitor pattern (see CLAUDE.md): large Hz number upper-left/
top, short benefit phrase lower, cream/white text, soft dark scrim for contrast.
Background is whatever hero image was generated for that video (character +
themed environment, per scripts/batch-01.md).

Usage: edit HZ_TEXT / TAGLINE / SRC / OUT for each video, then run.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# --- per-video params ---
SRC = "source.jpg"          # the generated hero image for this video
OUT = "thumb.jpg"
HZ_TEXT = "432 Hz"          # large, top
TAGLINE = "Deep Sleep Music"  # smaller, below

# --- fixed template ---
W, H = 1280, 720
WHITE = (255, 255, 255, 255)
CREAM = (245, 234, 210, 255)
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

HZ_SIZE = 140
TAGLINE_SIZE = 56


def main():
    bg = Image.open(SRC).convert("RGB")
    sw, sh = bg.size
    target = W / H
    if sw / sh > target:
        nw = int(sh * target)
        bg = bg.crop(((sw - nw) // 2, 0, (sw + nw) // 2, sh))
    else:
        nh = int(sw / target)
        bg = bg.crop((0, (sh - nh) // 2, sw, (sh + nh) // 2))
    bg = bg.resize((W, H), Image.LANCZOS).convert("RGBA")

    # soft scrim upper-left for the Hz number + tagline
    scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(scrim).rounded_rectangle((-100, -40, 620, 280), radius=120, fill=(5, 5, 10, 150))
    bg.alpha_composite(scrim.filter(ImageFilter.GaussianBlur(70)))

    d = ImageDraw.Draw(bg)
    hz_font = ImageFont.truetype(SERIF, HZ_SIZE)
    tag_font = ImageFont.truetype(SERIF, TAGLINE_SIZE)

    d.text((56, 40), HZ_TEXT, font=hz_font, fill=WHITE)
    d.text((60, 190), TAGLINE, font=tag_font, fill=CREAM)

    bg.convert("RGB").save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Saved -> {OUT}")


if __name__ == "__main__":
    main()
