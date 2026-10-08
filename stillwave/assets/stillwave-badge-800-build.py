#!/usr/bin/env python3
"""
Build clean 800×800 round badge + transparency proof image.

stillwave-badge-800.png — clean PNG, gold ензō + blue wave + navy disc,
                          transparent corners. Ready for CapCut import.

stillwave-badge-800-transparency-proof.jpg — same badge on checkerboard
                          background — proves alpha is truly transparent.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE  = Path(__file__).parent
SRC   = HERE / "stillwave-badge-v6.png"
OUT   = HERE / "stillwave-badge-800.png"
PROOF = HERE / "stillwave-badge-800-transparency-proof.jpg"


def main():
    badge = Image.open(SRC).convert("RGBA").resize((800, 800), Image.LANCZOS)
    badge.save(OUT, "PNG")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")

    # Checkerboard background to visually prove transparency
    cb = Image.new("RGB", (900, 900), (255, 255, 255))
    draw = ImageDraw.Draw(cb)
    cell = 30
    for y in range(0, 900, cell):
        for x in range(0, 900, cell):
            if ((x // cell) + (y // cell)) % 2 == 0:
                draw.rectangle([x, y, x + cell, y + cell], fill=(200, 200, 210))
    # paste centered
    cb_rgba = cb.convert("RGBA")
    cb_rgba.alpha_composite(badge, (50, 50))

    # Annotation
    draw = ImageDraw.Draw(cb_rgba)
    try:
        fnt = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 22)
    except OSError:
        fnt = ImageFont.load_default()
    label = "Углы прозрачные — шахматка просвечивает"
    bb = fnt.getbbox(label)
    draw.text((450 - (bb[2] - bb[0]) // 2, 20),
              label, font=fnt, fill=(40, 40, 60))

    cb_rgba.convert("RGB").save(PROOF, "JPEG", quality=92)
    print(f"Wrote {PROOF} ({PROOF.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
