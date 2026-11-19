#!/usr/bin/env python3
"""Samurai-series Shorts — one 9:16 Short per published long-form, built from its 16:9 hero frame.

Three slow shots cut out of the same frame (float-precision crop boxes, LANCZOS -> jitter-free
Ken Burns, per the 2026-07-26 rule), crossfaded; three text beats (hook / kanji concept / CTA)
inside the Shorts safe zone (glyphs within x 60-880, y 150-1450 of 1080x1920); ~24 s of the
album's own music. Usage: python3 samurai-short-build.py <slug> <music.mp3> <out.mp4>
"""
import sys, subprocess
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).parent
KANJI = str(HERE / "fonts" / "YujiBoku-Regular.ttf")
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
W, H, FPS = 1080, 1920, 30
WHITE, CREAM = (250, 247, 240), (232, 222, 200)

# shots: (centre x as a fraction of the frame width, zoom start, zoom end); y always full height
CFG = {
    "bushido": dict(src="bushido-2h-source.jpg", music_at=40,
        shots=[(0.78, 1.18, 1.06), (0.66, 1.00, 1.07), (0.56, 1.10, 1.00)],
        hook=["The samurai code", "was never about winning."],
        kanji="武士道", romaji="Bushido", gloss="the way of the warrior",
        line3=["It was about how you act", "when no one is watching."]),
    "dojo": dict(src="dojo-2h-source.jpg", music_at=40,
        shots=[(0.62, 1.18, 1.06), (0.66, 1.00, 1.07), (0.56, 1.10, 1.00)],
        hook=["A dojo has", "one rule."],
        kanji="道場", romaji="Dojo", gloss="the place of the way",
        line3=["Leave everything", "at the door."]),
    "ronin": dict(src="ronin-2h-source.jpg", music_at=40,
        shots=[(0.51, 1.15, 1.05), (0.38, 1.00, 1.07), (0.43, 1.10, 1.00)],
        hook=["A samurai", "with no master."],
        kanji="浪人", romaji="Ronin", gloss="a wave man, free as the sea",
        line3=["No lord. No home.", "Only the road."]),
    "mushin-ii": dict(src="mushin-ii-2h-source.jpg", music_at=40,
        shots=[(0.69, 1.18, 1.06), (0.66, 1.00, 1.07), (0.62, 1.12, 1.00)],
        hook=["Old masters said", "the mind should be like water."],
        kanji="無心", romaji="Mushin", gloss="the mind without mind",
        line3=["Calm enough", "to reflect the moon."]),
}
SHOT, XF = 8.6, 0.9                     # seconds per shot, crossfade
DUR = SHOT * 3 - XF * 2                 # ~24 s

slug, music, out = sys.argv[1], sys.argv[2], sys.argv[3]
c = CFG[slug]
src = Image.open(HERE / c["src"]).convert("RGB")
SW, SH = src.size

def shot_frame(cx, z, ):
    ch = SH / z; cw = ch * 9 / 16
    x0 = min(max(cx * SW - cw / 2, 0), SW - cw); y0 = (SH - ch) / 2
    return src.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))   # float box: no 1-px stepping

def ease(u): return u * u * (3 - 2 * u)

def text_layer(lines_spec):
    """lines_spec: list of (text, font, fill, y, track)"""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # soft dark band behind the block for contrast
    ys = [y for _, _, _, y, _ in lines_spec]; y0, y1 = min(ys) - 60, max(ys) + 140
    band = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(band).rectangle((0, y0, W, y1), fill=(0, 0, 0, 120))
    lay.alpha_composite(band.filter(ImageFilter.GaussianBlur(60)))
    d = ImageDraw.Draw(lay)
    for text, font, fill, y, track in lines_spec:
        w = sum(font.getlength(ch) for ch in text) + track * (len(text) - 1)
        x = (60 + 880) / 2 - w / 2
        for ch in text:
            d.text((x + 2, y + 3), ch, font=font, fill=(0, 0, 0, 160))
            d.text((x, y), ch, font=font, fill=fill + (255,))
            x += font.getlength(ch) + track
    return lay

def fit(lines, path, size, maxw=800):
    """largest font size <= size at which every line fits in maxw px"""
    while size > 30:
        f = ImageFont.truetype(path, size)
        if max(f.getlength(t) for t in lines) <= maxw: return f
        size -= 2
    return ImageFont.truetype(path, size)

f_hook = fit(c["hook"], SERIF, 84)
f_line = fit(c["line3"], SERIF, 78)
f_kanji = ImageFont.truetype(KANJI, 230)
f_rom = ImageFont.truetype(SERIF_R, 74)
f_gloss = fit([c["gloss"]], SERIF_R, 44)
f_cta = ImageFont.truetype(SERIF_R, 46)
Y = 620                                   # upper-middle: over the mural, above the figure
T1 = text_layer([(s, f_hook, WHITE, Y + i * int(f_hook.size * 1.25), 0) for i, s in enumerate(c["hook"])])
T2 = text_layer([(c["kanji"], f_kanji, WHITE, Y - 200, 8),
                 (c["romaji"].upper(), f_rom, WHITE, Y + 90, 16),
                 (c["gloss"], f_gloss, CREAM, Y + 190, 2)])
T3 = text_layer([(s, f_line, WHITE, Y + i * int(f_line.size * 1.25), 0) for i, s in enumerate(c["line3"])] +
                [("Full 2 hours on the channel", f_cta, CREAM, Y + int(f_line.size * 1.25) * len(c["line3"]) + 40, 1)])
BEATS = [(T1, 0.6, 7.6), (T2, 8.6, 15.4), (T3, 16.4, DUR - 0.4)]   # (layer, in, out)

# safe-zone check on the opaque text pixels
for L, *_ in BEATS:
    a = np.asarray(L)[..., 3]; ys, xs = np.where(a > 200)
    assert 60 <= xs.min() and xs.max() <= 880 and 150 <= ys.min() and ys.max() <= 1450, (xs.min(), xs.max(), ys.min(), ys.max())

ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
    "-r", str(FPS), "-i", "-", "-ss", str(c["music_at"]), "-t", f"{DUR:.2f}", "-i", music,
    "-filter_complex", f"[1:a]afade=t=in:d=1,afade=t=out:st={DUR-2.5:.2f}:d=2.5,loudnorm=I=-14:TP=-1.5[a]",
    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-crf", "17", "-preset", "slow", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-shortest", out], stdin=subprocess.PIPE)
N = int(DUR * FPS)
for i in range(N):
    t = i / FPS
    k = min(int(t // (SHOT - XF)), 2)
    def at(k):
        cx, z0, z1 = c["shots"][k]; u = min(max((t - k * (SHOT - XF)) / SHOT, 0), 1)
        return shot_frame(cx, z0 + (z1 - z0) * ease(u))
    fr = at(k)
    if k < 2:
        tx = t - (k + 1) * (SHOT - XF)
        if tx > -XF:  # entering the crossfade into the next shot
            a = ease(min(1, (tx + XF) / XF)); fr = Image.blend(fr, at(k + 1), a)
    fr = fr.convert("RGBA")
    for L, ti, to in BEATS:
        a = min(1, (t - ti) / 0.8, (to - t) / 0.8)
        if a > 0:
            La = L.copy(); La.putalpha(L.getchannel("A").point(lambda p: int(p * a))); fr.alpha_composite(La)
    ff.stdin.write(fr.convert("RGB").tobytes())
ff.stdin.close(); ff.wait()
print("saved", out, f"{DUR:.1f}s")
