#!/usr/bin/env python3
"""
StillWave full logo (ensō + wave) with 3D emboss treatment.

Takes the source logo PNG and applies:
  - Matte navy dome base (radial gradient, convex feel)
  - Specular highlight stripe across top-left (gold sheen)
  - Gold ring bevel (dark outer / light inner)
  - Logo graphic composited with brightness boost for specularity

Outputs:
  stillwave-logo-emboss.png              — 800×800 RGBA stamp
  stillwave-logo-emboss-watermark.png    — 1920×1080 RGBA overlay
  stillwave-logo-emboss-preview.jpg      — on MAKOTO frame
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

HERE   = Path(__file__).parent
SRC    = HERE / "stillwave-logo-source-v2.jpg"   # original white-bg logo
MAKOTO = HERE / "makoto-the-last-samurai-source.jpg"
OUT    = HERE / "stillwave-logo-emboss.png"
WM     = HERE / "stillwave-logo-emboss-watermark.png"
PREV   = HERE / "stillwave-logo-emboss-preview.jpg"

SIZE     = 800
STAMP_PX = 180
MARGIN   = 36

GOLD       = (201, 168, 76)
GOLD_DARK  = (90,  68, 15)
GOLD_LIGHT = (255, 235, 140)
NAVY       = (12,  19, 38)
NAVY_MID   = (28,  44, 82)
NAVY_LIGHT = (48,  72, 128)


def remove_white_bg(img: Image.Image, threshold=240) -> Image.Image:
    """Convert white/near-white pixels to transparent."""
    import numpy as np
    arr = np.array(img.convert("RGBA"), dtype=np.uint8)
    r, g, b = arr[:,:,0].astype(int), arr[:,:,1].astype(int), arr[:,:,2].astype(int)
    is_white = (r > threshold) & (g > threshold) & (b > threshold)
    # Soft alpha ramp for anti-aliased edges
    brightness = (r + g + b) / 3.0
    arr[:,:,3] = np.where(is_white,
                          np.clip((threshold - brightness) / 15 * 255, 0, 0).astype(int),
                          255).astype(np.uint8)
    return Image.fromarray(arr, "RGBA")


def make_emboss_base(size: int) -> Image.Image:
    """Matte navy convex disc with specular sheen."""
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx = cy = size // 2
    r  = size // 2 - 6

    # Radial gradient: dark edge → mid navy centre (matte dome feel)
    steps = 50
    for i in range(steps, -1, -1):
        t  = i / steps
        cr = int(r * (i + 1) / (steps + 1))
        col = (
            int(NAVY[0] + (NAVY_MID[0] - NAVY[0]) * t),
            int(NAVY[1] + (NAVY_MID[1] - NAVY[1]) * t),
            int(NAVY[2] + (NAVY_MID[2] - NAVY[2]) * t),
            255,
        )
        draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=col)

    # Specular highlight — soft ellipse top-left (gold sheen on convex surface)
    hi = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    hd = ImageDraw.Draw(hi)
    hx = int(cx - r * 0.18)
    hy = int(cy - r * 0.25)
    for s in range(30, 0, -1):
        alpha = int(90 * (s / 30))
        sw    = int(r * 0.75 * s / 30)
        sh    = int(r * 0.40 * s / 30)
        hd.ellipse([hx - sw, hy - sh, hx + sw, hy + sh],
                   fill=(*GOLD_LIGHT, alpha))
    hi = hi.filter(ImageFilter.GaussianBlur(radius=size // 12))
    img.alpha_composite(hi)

    # Gold bevel ring
    ring_w = max(10, size // 22)
    draw2  = ImageDraw.Draw(img)
    draw2.ellipse([cx - r, cy - r, cx + r, cy + r],
                  outline=GOLD_DARK,  width=ring_w + 3)
    draw2.ellipse([cx - r + 3, cy - r + 3, cx + r - 3, cy + r - 3],
                  outline=GOLD_LIGHT, width=ring_w - 5)
    draw2.ellipse([cx - r + ring_w // 3, cy - r + ring_w // 3,
                   cx + r - ring_w // 3, cy + r - ring_w // 3],
                  outline=GOLD,       width=2)

    # Circular mask
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size - 1, size - 1], fill=255)
    img.putalpha(mask)
    return img


def paste_logo(base: Image.Image, size: int) -> Image.Image:
    """Remove white bg from source logo, boost contrast, composite."""
    logo = Image.open(SRC).convert("RGBA")
    logo = remove_white_bg(logo, threshold=238)

    # Fit inside base with padding
    ring_w = max(10, size // 22)
    inner  = size - ring_w * 3
    lw, lh = logo.size
    ratio  = min(inner / lw, inner / lh)
    logo   = logo.resize((int(lw * ratio), int(lh * ratio)), Image.LANCZOS)

    # Boost saturation/brightness so it pops on dark navy
    logo_rgb = logo.convert("RGB")
    logo_rgb = ImageEnhance.Color(logo_rgb).enhance(1.4)
    logo_rgb = ImageEnhance.Brightness(logo_rgb).enhance(1.15)
    logo.paste(logo_rgb, mask=logo.split()[3])

    # Centre on base
    cx = cy = size // 2
    px = cx - logo.size[0] // 2
    py = cy - logo.size[1] // 2
    result = base.copy()
    result.alpha_composite(logo, (px, py))
    return result


def main():
    base  = make_emboss_base(SIZE)
    stamp = paste_logo(base, SIZE)
    stamp.save(OUT, "PNG")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")

    # Watermark overlay
    s = stamp.resize((STAMP_PX, STAMP_PX), Image.LANCZOS)
    canvas = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    canvas.alpha_composite(s, (1920 - STAMP_PX - MARGIN, 1080 - STAMP_PX - MARGIN))
    canvas.save(WM, "PNG")
    print(f"Wrote {WM} ({WM.stat().st_size // 1024} KB)")

    # Preview on MAKOTO
    bg = Image.open(MAKOTO).convert("RGBA").resize((1920, 1080))
    bg.alpha_composite(canvas)
    bg.convert("RGB").save(PREV, "JPEG", quality=92, optimize=True)
    print(f"Wrote {PREV} ({PREV.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
