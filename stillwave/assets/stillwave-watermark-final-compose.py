#!/usr/bin/env python3
"""
StillWave watermark FINAL — 波 kanji mon, fully opaque navy disc.

Gold ring + navy fill + gold 波 inside.
No transparency inside the circle — fully covers NanoBanana watermark.
Corners outside the ring = transparent.

Outputs:
  stillwave-watermark-final.png         — 1920×1080 RGBA overlay for CapCut
  stillwave-stamp-final.png             — standalone stamp (512×512)
  stillwave-watermark-final-preview.jpg — preview on MAKOTO frame
"""

from pathlib import Path
from PIL import Image, ImageDraw

HERE   = Path(__file__).parent
MAKOTO = HERE / "makoto-the-last-samurai-source.jpg"
STAMP  = HERE / "stillwave-stamp-final.png"
WM     = HERE / "stillwave-watermark-final.png"
PREV   = HERE / "stillwave-watermark-final-preview.jpg"

GOLD  = (201, 168, 76)
NAVY  = (14, 22, 42)       # deep navy — opaque disc inside ring
SIZE  = 512                # stamp canvas
STAMP_PX = 130             # size in 1920×1080 frame
MARGIN   = 32


def build_stamp(size: int) -> Image.Image:
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx = cy = size // 2
    ring_w = max(6, size // 18)
    r = size // 2 - ring_w // 2 - 4

    # 1 — filled navy disc (opaque — kills the NB watermark underneath)
    draw.ellipse([cx - r - ring_w // 2, cy - r - ring_w // 2,
                  cx + r + ring_w // 2, cy + r + ring_w // 2],
                 fill=(*NAVY, 255))

    # 2 — gold ring on top
    draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                 outline=GOLD, width=ring_w)

    # 3 — 波 kanji centred
    try:
        from PIL import ImageFont
        fnt = ImageFont.truetype(
            "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf",
            int(size * 0.52))
    except OSError:
        from PIL import ImageFont
        fnt = ImageFont.load_default()

    bb = fnt.getbbox("波")
    tx = cx - (bb[2] - bb[0]) // 2 - bb[0]
    ty = cy - (bb[3] - bb[1]) // 2 - bb[1]
    # subtle dark shadow
    draw.text((tx + 2, ty + 2), "波", font=fnt, fill=(0, 0, 0, 180))
    draw.text((tx, ty), "波", font=fnt, fill=GOLD)

    return img


def main():
    stamp = build_stamp(SIZE)
    stamp.save(STAMP, "PNG")
    print(f"Wrote {STAMP} ({STAMP.stat().st_size // 1024} KB)")

    # Resize for video overlay
    s = stamp.resize((STAMP_PX, STAMP_PX), Image.LANCZOS)
    canvas = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    pos = (1920 - STAMP_PX - MARGIN, 1080 - STAMP_PX - MARGIN)
    canvas.alpha_composite(s, pos)
    canvas.save(WM, "PNG")
    print(f"Wrote {WM} ({WM.stat().st_size // 1024} KB)")

    # Preview on MAKOTO frame
    bg = Image.open(MAKOTO).convert("RGBA").resize((1920, 1080))
    bg.alpha_composite(canvas)
    bg.convert("RGB").save(PREV, "JPEG", quality=92, optimize=True)
    print(f"Wrote {PREV} ({PREV.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
