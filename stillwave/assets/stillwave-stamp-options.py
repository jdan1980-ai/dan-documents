#!/usr/bin/env python3
"""
StillWave mono-stamp watermark options — designed to naturally replace
the NanoBanana diamond watermark in the bottom-right corner.

Three candidates:
  A — 波 kanji in a thin circle (Japanese mon style)
  B — wave tilde ≋ in a circle
  C — SW initials ligature in a circle
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

HERE   = Path(__file__).parent
MAKOTO = HERE / "makoto-the-last-samurai-source.jpg"
OUT    = HERE / "stillwave-mono-stamp-options.jpg"

GOLD   = (201, 168, 76)
CREAM  = (245, 234, 210)
NAVY   = (18, 26, 46)
WHITE  = (255, 255, 255)
DARK   = (12, 14, 20)

STAMP_PX = 120   # close to NanoBanana diamond size


def draw_stamp_A(size: int) -> Image.Image:
    """波 kanji mon — thin gold ring + wave kanji inside."""
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx = cy = size // 2
    r = size // 2 - 4

    # Thin gold ring
    draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                 outline=GOLD, width=max(3, size // 28))

    # 波 kanji centred inside
    try:
        fnt = ImageFont.truetype(
            "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf",
            int(size * 0.56))
    except OSError:
        fnt = ImageFont.load_default()
    bb = fnt.getbbox("波")
    tx = cx - (bb[2] - bb[0]) // 2 - bb[0]
    ty = cy - (bb[3] - bb[1]) // 2 - bb[1]
    draw.text((tx + 1, ty + 1), "波", font=fnt, fill=(0, 0, 0, 140))
    draw.text((tx, ty), "波", font=fnt, fill=GOLD)
    return img


def draw_stamp_B(size: int) -> Image.Image:
    """Sine wave drawn programmatically inside a thin gold circle."""
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx = cy = size // 2
    r  = size // 2 - 4
    lw = max(3, size // 28)

    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=lw)

    # Draw sine wave across the centre
    inner = int(r * 0.62)
    amp   = int(r * 0.25)
    pts   = []
    steps = 120
    for i in range(steps + 1):
        t  = i / steps          # 0..1
        x  = cx - inner + int(2 * inner * t)
        y  = cy + int(amp * math.sin(t * 2 * math.pi))
        pts.append((x, y))
    draw.line(pts, fill=CREAM, width=max(3, size // 24))
    return img


def draw_stamp_C(size: int) -> Image.Image:
    """SW monogram in a circle."""
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx = cy = size // 2
    r  = size // 2 - 4
    lw = max(3, size // 28)

    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=lw)

    try:
        fnt = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf",
            int(size * 0.40))
    except OSError:
        fnt = ImageFont.load_default()
    txt = "SW"
    bb  = fnt.getbbox(txt)
    tx  = cx - (bb[2] - bb[0]) // 2 - bb[0]
    ty  = cy - (bb[3] - bb[1]) // 2 - bb[1]
    draw.text((tx + 1, ty + 1), txt, font=fnt, fill=(0, 0, 0, 140))
    draw.text((tx, ty), txt, font=fnt, fill=GOLD)
    return img


def build_preview(stamps: list[tuple[str, Image.Image]]) -> Image.Image:
    """Show each stamp bottom-right on the MAKOTO frame, side by side."""
    bg_src = Image.open(MAKOTO).convert("RGB").resize((1920, 1080))

    n = len(stamps)
    W = 1920 * n + 20 * (n - 1)
    canvas = Image.new("RGB", (W, 1080 + 80), DARK)

    try:
        lf = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 28)
    except OSError:
        lf = ImageFont.load_default()

    for i, (label, stamp) in enumerate(stamps):
        x_off = i * (1920 + 20)
        frame = bg_src.copy().convert("RGBA")
        s = stamp.resize((STAMP_PX, STAMP_PX), Image.LANCZOS)
        frame.alpha_composite(s, (1920 - STAMP_PX - 30, 1080 - STAMP_PX - 30))
        canvas.paste(frame.convert("RGB"), (x_off, 0))

        # Label bar
        draw = ImageDraw.Draw(canvas)
        draw.rectangle([x_off, 1080, x_off + 1920, 1160], fill=(22, 24, 32))
        draw.text((x_off + 20, 1088), label, font=lf, fill=GOLD)

    return canvas


def main():
    A = draw_stamp_A(512)
    B = draw_stamp_B(512)
    C = draw_stamp_C(512)

    A.save(HERE / "stillwave-stamp-A-wave-kanji.png", "PNG")
    B.save(HERE / "stillwave-stamp-B-sine.png",       "PNG")
    C.save(HERE / "stillwave-stamp-C-SW.png",         "PNG")
    print("Stamps written.")

    preview = build_preview([
        ("A — 波 кандзи в кольце (mon-стиль)", A),
        ("B — синусоида в кольце",              B),
        ("C — SW монограмма в кольце",          C),
    ])
    preview.save(OUT, "JPEG", quality=92, optimize=True)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
