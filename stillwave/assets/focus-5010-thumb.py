#!/usr/bin/env python3
"""
Pomodoro 50/10 — Focus Session thumbnail (16:9, 1280x720).
Text lower-left (figure-8 rule), GOLD #E4C46C (locked Pomodoro exception),
Liberation Serif Bold. Two lines: FOCUS SESSION / 50/10 - 2H.

Source: focus-5010-source.jpg (penthouse + laptop + hourglass + fireplace)
Output: focus-5010-thumb.jpg (1280x720, JPEG q92)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC  = HERE / "focus-5010-source.jpg"
OUT  = HERE / "focus-5010-thumb.jpg"

W, H = 1280, 720
GOLD = (228, 196, 108)           # #E4C46C — locked Pomodoro gold
FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

LINE1 = "FOCUS SESSION"
SIZE1 = 84
LINE2 = "50/10 - 2H"
SIZE2 = 56

X = 56
Y1 = 528
Y2 = 632
SPACING = 4


def track(d, xy, text, font, fill, spacing):
    x, y = xy
    for ch in text:
        bb = font.getbbox(ch)
        d.text((x - bb[0], y), ch, font=font, fill=fill)
        x += (bb[2] - bb[0]) + spacing


def main():
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")

    bg = Image.open(SRC).convert("RGB")
    if bg.size != (W, H):
        bg = bg.resize((W, H), Image.LANCZOS)

    d = ImageDraw.Draw(bg)
    f1 = ImageFont.truetype(FONT, SIZE1)
    f2 = ImageFont.truetype(FONT, SIZE2)

    track(d, (X, Y1), LINE1, f1, GOLD, SPACING)
    track(d, (X, Y2), LINE2, f2, GOLD, SPACING + 2)

    bg.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Saved → {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
