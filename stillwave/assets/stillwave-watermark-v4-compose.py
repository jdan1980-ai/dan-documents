#!/usr/bin/env python3
"""
StillWave watermark v4 — gold ензō + cream wave + navy circle badge.
Designed to cover NanoBanana diamond watermark (bottom-right of 1920×1080).

Outputs:
  stillwave-watermark-v4.png         — 1920×1080 RGBA overlay
  stillwave-watermark-v4-preview.jpg — preview on MAKOTO frame
"""

from pathlib import Path
from PIL import Image

HERE   = Path(__file__).parent
BADGE  = HERE / "stillwave-logo-gold-cream-navy.png"
MAKOTO = HERE / "makoto-the-last-samurai-source.jpg"
WM     = HERE / "stillwave-watermark-v4.png"
PREV   = HERE / "stillwave-watermark-v4-preview.jpg"

# NanoBanana diamond sits ~bottom-right; cover with a ~170px badge.
BADGE_PX = 170
MARGIN   = 36   # distance from right + bottom edges
OPACITY  = 1.0  # fully opaque to mask the NB watermark cleanly


def main():
    badge = Image.open(BADGE).convert("RGBA").resize(
        (BADGE_PX, BADGE_PX), Image.LANCZOS)

    if OPACITY < 1.0:
        a = badge.split()[-1].point(lambda p: int(p * OPACITY))
        badge.putalpha(a)

    canvas = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    pos = (1920 - BADGE_PX - MARGIN, 1080 - BADGE_PX - MARGIN)
    canvas.alpha_composite(badge, pos)
    canvas.save(WM, "PNG")
    print(f"Wrote {WM} ({WM.stat().st_size // 1024} KB)")

    # Preview on MAKOTO
    bg = Image.open(MAKOTO).convert("RGBA").resize((1920, 1080))
    bg.alpha_composite(canvas)
    bg.convert("RGB").save(PREV, "JPEG", quality=92, optimize=True)
    print(f"Wrote {PREV} ({PREV.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
