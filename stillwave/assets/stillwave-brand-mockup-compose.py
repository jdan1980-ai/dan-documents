#!/usr/bin/env python3
"""
YouTube channel page mockup — StillWave brand refresh.
Shows banner + new logo v2 (gold ensō) in YouTube layout.
Output: stillwave-brand-mockup.jpg (1280×560)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
OUT  = HERE / "stillwave-brand-mockup.jpg"

W, H = 1280, 560

SLATE       = (48, 50, 58)
DARK_BG     = (15, 15, 20)
PANEL_BG    = (22, 22, 28)
GOLD        = (201, 168, 76)
CREAM       = (245, 234, 210)
WHITE       = (255, 255, 255)
GRAY        = (140, 140, 150)
LIGHT_GRAY  = (200, 200, 210)
YT_RED      = (255, 0, 0)


def draw_banner(draw: ImageDraw.ImageDraw, x, y, w, h):
    """Recreate the StillWave banner look."""
    # Dark gradient background
    for i in range(h):
        t = i / h
        r = int(18 + 10 * t)
        g = int(20 + 8  * t)
        b = int(28 + 12 * t)
        draw.line([(x, y + i), (x + w, y + i)], fill=(r, g, b))

    # Subtle star/particle dots
    import random
    rng = random.Random(42)
    for _ in range(80):
        px = x + rng.randint(0, w)
        py = y + rng.randint(0, h)
        alpha = rng.randint(60, 160)
        r = rng.randint(1, 2)
        draw.ellipse([px - r, py - r, px + r, py + r],
                     fill=(alpha, alpha, alpha + 20))

    # "YOUR SANCTUARY OF SOUND" — small spaced caps
    try:
        small_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 13)
        big_font   = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf", 62)
        tag_font   = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 16)
    except OSError:
        small_font = big_font = tag_font = ImageFont.load_default()

    tagline = "YOUR SANCTUARY OF SOUND"
    tb = small_font.getbbox(tagline)
    draw.text((x + w // 2 - (tb[2] - tb[0]) // 2, y + 30),
              tagline, font=small_font, fill=(180, 180, 190))

    # "StillWave" big serif
    title = "StillWave"
    nb = big_font.getbbox(title)
    draw.text((x + w // 2 - (nb[2] - nb[0]) // 2 - nb[0], y + 50 - nb[1]),
              title, font=big_font, fill=WHITE)

    # Divider line
    lw = 120
    draw.line([(x + w // 2 - lw, y + 128), (x + w // 2 + lw, y + 128)],
              fill=(100, 100, 110), width=1)

    # "SLEEP · FOCUS · MEDITATION"
    sub = "SLEEP  ·  FOCUS  ·  MEDITATION"
    sb = tag_font.getbbox(sub)
    draw.text((x + w // 2 - (sb[2] - sb[0]) // 2, y + 138),
              sub, font=tag_font, fill=GRAY)


def draw_logo_circle(img: Image.Image, cx, cy, r):
    """Paste new logo v2 circle, scaled to avatar size."""
    logo_path = HERE / "stillwave-logo-v2-circle.png"
    if not logo_path.exists():
        return
    logo = Image.open(logo_path).convert("RGBA")
    size = r * 2
    logo = logo.resize((size, size), Image.LANCZOS)

    # Circular mask
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size - 1, size - 1], fill=255)
    logo.putalpha(mask)

    img.paste(logo, (cx - r, cy - r), logo)


def draw_old_logo_circle(img: Image.Image, cx, cy, r):
    """Draw approximate old logo (torii gate + water) for comparison."""
    draw = ImageDraw.Draw(img)
    # White circle bg
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255))
    # Thin dark blue border
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(60, 90, 120), width=3)

    # Torii gate (simplified)
    tc = (50, 100, 140)
    # Two pillars
    pw = max(3, r // 12)
    ph = r // 2
    left_x  = cx - r // 3
    right_x = cx + r // 3
    base_y  = cy + r // 4
    draw.rectangle([left_x - pw, base_y - ph, left_x + pw, base_y], fill=tc)
    draw.rectangle([right_x - pw, base_y - ph, right_x + pw, base_y], fill=tc)
    # Top horizontal bar (kasagi)
    draw.rectangle([cx - r // 2, base_y - ph - pw * 3,
                    cx + r // 2, base_y - ph], fill=tc)
    # Second horizontal bar (nuki)
    draw.rectangle([left_x - pw * 2, base_y - ph // 2 - pw,
                    right_x + pw * 2, base_y - ph // 2 + pw], fill=tc)

    # Water ripples below torii
    wy = base_y + pw * 2
    for i in range(3):
        wr = r // 3 + i * (r // 8)
        wh = r // 12
        draw.arc([cx - wr, wy, cx + wr, wy + wh * 2],
                 start=0, end=180, fill=(80, 140, 180), width=2)

    # "StillWave" text
    try:
        f = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
            max(12, r // 5))
    except OSError:
        f = ImageFont.load_default()
    t = "StillWave"
    bb = f.getbbox(t)
    tx = cx - (bb[2] - bb[0]) // 2 - bb[0]
    ty = cy + r - (bb[3] - bb[1]) - 10
    draw.text((tx, ty), t, font=f, fill=(40, 80, 120))


def main():
    img  = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    # ── LEFT: old logo ──────────────────────────────────────────────
    # Banner strip top-left
    banner_w = W // 2 - 20
    draw_banner(draw, 10, 10, banner_w, 175)

    # Label
    try:
        label_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 14)
        name_font  = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 18)
        sub_font   = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 13)
    except OSError:
        label_font = name_font = sub_font = ImageFont.load_default()

    # Avatar area old
    avatar_r_old = 52
    ax_old = 65
    ay_old = 215
    draw_old_logo_circle(img, ax_old, ay_old, avatar_r_old)

    # Channel info
    draw.text((ax_old + avatar_r_old + 16, ay_old - 14),
              "StillWave", font=name_font, fill=WHITE)
    draw.text((ax_old + avatar_r_old + 16, ay_old + 8),
              "@stillwavezen  ·  50 subscribers  ·  46 videos",
              font=sub_font, fill=GRAY)

    # "ТЕКУЩИЙ" tag
    draw.rounded_rectangle([ax_old - avatar_r_old, ay_old + avatar_r_old + 14,
                             ax_old + avatar_r_old, ay_old + avatar_r_old + 32],
                            radius=4, fill=(70, 70, 80))
    draw.text((ax_old - avatar_r_old + 8, ay_old + avatar_r_old + 16),
              "ТЕКУЩИЙ", font=label_font, fill=LIGHT_GRAY)

    # ── RIGHT: new logo ─────────────────────────────────────────────
    draw_banner(draw, W // 2 + 10, 10, banner_w, 175)

    avatar_r_new = 52
    ax_new = W // 2 + 65
    ay_new = 215
    draw_logo_circle(img, ax_new, ay_new, avatar_r_new)

    draw.text((ax_new + avatar_r_new + 16, ay_new - 14),
              "StillWave", font=name_font, fill=WHITE)
    draw.text((ax_new + avatar_r_new + 16, ay_new + 8),
              "@stillwavezen  ·  50 subscribers  ·  46 videos",
              font=sub_font, fill=GRAY)

    # "НОВЫЙ" tag — gold
    draw.rounded_rectangle([ax_new - avatar_r_new, ay_new + avatar_r_new + 14,
                             ax_new + avatar_r_new, ay_new + avatar_r_new + 32],
                            radius=4, fill=(80, 65, 20))
    draw.text((ax_new - avatar_r_new + 14, ay_new + avatar_r_new + 16),
              "НОВЫЙ", font=label_font, fill=GOLD)

    # Centre divider
    draw.line([(W // 2, 0), (W // 2, H)], fill=(50, 50, 60), width=2)

    # Bottom note
    try:
        note_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf", 13)
    except OSError:
        note_font = ImageFont.load_default()
    note = "Логотип сгенерирован программно — финальный PNG загрузишь из Канвы / логотип-файла"
    nb = note_font.getbbox(note)
    draw.text((W // 2 - (nb[2] - nb[0]) // 2, H - 26),
              note, font=note_font, fill=(80, 80, 90))

    img.save(OUT, "JPEG", quality=94)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
