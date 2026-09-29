#!/usr/bin/env python3
"""
StillWave watermark v5 — gold ензō + blue wave ONLY (no badge bg).
Transparent everywhere except the brush strokes themselves.

Size tuned so the wave shape sits directly over the NanoBanana diamond
watermark in the bottom-right corner, hiding it without a navy disc.

Outputs:
  stillwave-watermark-v5.png         — 1920×1080 RGBA overlay
  stillwave-watermark-v5-preview.jpg — preview on MAKOTO frame
"""

from pathlib import Path
from PIL import Image

HERE   = Path(__file__).parent
MARK   = HERE / "stillwave-mark-v3.png"          # gold ензō + blue wave, transparent bg
MAKOTO = HERE / "makoto-the-last-samurai-source.jpg"
WM     = HERE / "stillwave-watermark-v5.png"
PREV   = HERE / "stillwave-watermark-v5-preview.jpg"

MARK_H  = 220     # bigger than badge to ensure the wave fully covers the NB diamond
MARGIN  = 30


def main():
    mark = Image.open(MARK).convert("RGBA")
    mw, mh = mark.size
    ratio = MARK_H / mh
    new_w = int(mw * ratio)
    mark = mark.resize((new_w, MARK_H), Image.LANCZOS)

    canvas = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    pos = (1920 - new_w - MARGIN, 1080 - MARK_H - MARGIN)
    canvas.alpha_composite(mark, pos)
    canvas.save(WM, "PNG")
    print(f"Wrote {WM} ({WM.stat().st_size // 1024} KB)")

    bg = Image.open(MAKOTO).convert("RGBA").resize((1920, 1080))
    bg.alpha_composite(canvas)
    bg.convert("RGB").save(PREV, "JPEG", quality=92, optimize=True)
    print(f"Wrote {PREV} ({PREV.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
