#!/usr/bin/env python3
"""MUSASHI Short — motion-graphics version B (adapted from okami-short-motion.py), 26 s.
  0-2   COVER: Musashi under the full moon, 武蔵 written in a vertical column over the mist + MUSASHI
  2-10  HOOK: tight on the moon blazing, the camera tilts down to Musashi's face; "Sixty duels. / Never defeated."
  10-18 KANJI: 万理一空 written stroke by stroke in a vertical column over the misty lake + BANRI IKKŪ + gloss
  18-26 WIDE: Musashi by the lake, push-in; closing line + CTA
Silver moon-dust motes drift through every shot.
Usage: python3 musashi-short-motion.py LOOP.mp4 MUSIC.mp3 OUT.mp4 [music start s=40]
"""
import sys, subprocess, re
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from svgpathtools import parse_path

HERE = Path(__file__).parent
loop, music, out = sys.argv[1], sys.argv[2], sys.argv[3]
MUSIC_AT = float(sys.argv[4]) if len(sys.argv) > 4 else 40
W, H, FPS, DUR = 1080, 1920, 30, 26.0
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
WHITE, CREAM, GOLD = (250, 247, 240), (226, 230, 240), (236, 178, 80)
MOON = (205, 220, 245)
rng = np.random.default_rng(7)

def ease(u): u = min(max(u, 0.0), 1.0); return u * u * (3 - 2 * u)

# ---------- source: the seamless loop, decoded at output fps ----------
SW, SH = 1920, 1080
vproc = subprocess.Popen(["ffmpeg", "-v", "error", "-stream_loop", "-1", "-i", loop, "-vf",
                          f"scale={SW}:{SH},fps={FPS}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
def next_src(): return np.frombuffer(vproc.stdout.read(SW * SH * 3), np.uint8).reshape(SH, SW, 3)

MX, MY = 900, 100                                     # moon centre in the 1920x1080 frame
ey, ex = np.mgrid[0:300, 700:1100].astype(np.float32)
EYE_GLOW = sum(np.exp(-((ex - MX) ** 2 + (ey - MY) ** 2) / (2 * s * s)) * k for s, k in ((120, 0.35), (220, 0.15)))

def crop(src_img, cx, cy, z, ypos=0.5):
    """9:16 window of height SH/z centred on cx, with the point cy placed at ypos of the window."""
    ch = SH / z; cw = ch * 9 / 16
    x0 = min(max(cx - cw / 2, 0), SW - cw); y0 = min(max(cy - ch * ypos, 0), SH - ch)
    return src_img.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))

# shot functions: t is local time from the shot's start
def shot_face(t):
    f = next_src.cur.astype(np.float32)
    expo = 0.45 + 0.55 * ease(t / 1.6)
    flare = 0.9 * np.exp(-t / 1.3) + 0.25               # the moon blazes at the first frame, then settles
    f *= expo
    f[0:300, 700:1100] += (EYE_GLOW * flare)[..., None] * np.array(MOON, np.float32)
    img = Image.fromarray(np.clip(f, 0, 255).astype(np.uint8))
    u = ease(t / 8.0)
    return crop(img, 900 - 230 * u, 120 + 160 * u, 2.3 - 0.9 * u, ypos=0.32)

def shot_clouds(t):
    f = next_src.cur.astype(np.float32) * 0.55           # misty lake, dimmed under the kanji
    return crop(Image.fromarray(f.astype(np.uint8)), 1450, 560, 1.12 - 0.08 * ease(t / 8.0))

def shot_wide(t):
    return crop(Image.fromarray(next_src.cur), 760, 540, 1.00 + 0.07 * ease(t / 8.0))

# ---------- ink-bleed transition ----------
def fbm(shape, octaves=5, seed=3):
    r = np.random.default_rng(seed); acc = np.zeros(shape, np.float32); amp = 1.0
    for o in range(octaves):
        g = r.random((4 * 2 ** o, 3 * 2 ** o)).astype(np.float32)
        acc += amp * np.asarray(Image.fromarray(g).resize((shape[1], shape[0]), Image.BICUBIC)); amp *= 0.5
    return (acc - acc.mean()) / acc.std()
NOISE = fbm((H, W))
YY, XX = np.mgrid[0:H, 0:W].astype(np.float32)
def ink_mix(a, b, u, seed_xy):
    """b soaks through a spreading ink blot over a; dark wet rim at the blot edge"""
    d = np.hypot(XX - seed_xy[0], YY - seed_xy[1]) + 230 * NOISE
    R = -300 + 2700 * ease(u)
    m = np.clip((R - d) / 60, 0, 1)[..., None]
    rim = np.exp(-((R - d) / 90) ** 2)[..., None]
    A, B = np.asarray(a, np.float32), np.asarray(b, np.float32)
    mix = A * (1 - m) + B * m
    mix *= 1 - 0.88 * rim                                # ink edge
    return Image.fromarray(np.clip(mix, 0, 255).astype(np.uint8))

# ---------- brush-written kanji (KanjiVG stroke order) ----------
def load(code): return [parse_path(d) for d in re.findall(r'<path[^>]*\sd="([^"]+)"', (HERE / "kanjivg" / f"{code}.svg").read_text())]
def build_strokes(chars, ks, kx, ky, step):
    out = []
    for j, code in enumerate(chars):
        for p in load(code):
            L = p.length(); n = max(int(L * ks / 1.6), 20)
            pts = [p.point(i / (n - 1)) for i in range(n)]
            out.append((L, [(kx + q.real * ks, ky + j * step + q.imag * ks) for q in pts]))
    return out
KS = 2.45                                              # 109 units -> 267 px per kanji
strokes = build_strokes(["04e07", "07406", "04e00", "07a7a"], KS, 540 - 54.5 * KS, 175, 245)
W0, W1 = 9.4, 14.2                                     # writing window (s)
tot = sum(L ** 0.7 for L, _ in strokes); gap = 0.07
avail = (W1 - W0) - gap * (len(strokes) - 1)
times, t0 = [], W0
for L, _ in strokes:
    d = avail * L ** 0.7 / tot; times.append((t0, t0 + d)); t0 += d + gap

PAPER = np.clip(0.5 + 0.18 * fbm((H, W), 4, seed=11), 0, 1)
def brush_mask(t, strokes=strokes, ks=KS):
    m = Image.new("L", (W, H), 0); dr = ImageDraw.Draw(m); tip = None
    for (L, pts), (s0, s1) in zip(strokes, times):
        if t <= s0: break
        u = ease((t - s0) / (s1 - s0)) if t < s1 else 1.0
        k = max(2, int(len(pts) * u))
        for i in range(k):
            s = i / (len(pts) - 1)
            prof = (0.55 + 0.45 * ease(s / 0.12)) * (1 - 0.65 * ease((s - 0.72) / 0.28))
            r = 3.3 * ks * prof * (1 + 0.05 * np.sin(i * 0.9))
            x, y = pts[i]; dr.ellipse((x - r, y - r, x + r, y + r), fill=255)
        if u < 1: tip = pts[k - 1]
    a = np.asarray(m.filter(ImageFilter.GaussianBlur(2.2)), np.float32) / 255
    a = np.clip((a - 0.5 + 0.35 * (PAPER - 0.5)) / 0.12 + 0.5, 0, 1)   # ragged dry-brush edge
    return a, tip

def draw_kanji(fr, t):
    if t < W0: return fr
    a, tip = brush_mask(t)
    F = np.asarray(fr, np.float32)
    glow = np.asarray(Image.fromarray((a * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(22)), np.float32)[..., None] / 255
    F = F * (1 - 0.35 * glow) + 0.0                                    # darken behind for contrast
    F += glow * 0.55 * np.array(GOLD, np.float32)
    F = F * (1 - a[..., None]) + a[..., None] * np.array(WHITE, np.float32)
    if tip is not None:                                                # wet gold point at the brush tip
        g = np.exp(-((XX - tip[0]) ** 2 + (YY - tip[1]) ** 2) / (2 * 26 ** 2))[..., None]
        F += g * np.array(GOLD, np.float32) * 0.9
    return Image.fromarray(np.clip(F, 0, 255).astype(np.uint8))

# ---------- kinetic type ----------
def words_layer(lines, font, y, color, t_in, step=0.22, t_out=None, band=True):
    """returns f(t)->RGBA layer; words rise 24 px and fade in one after another"""
    items = []; k = 0
    for li, line in enumerate(lines):
        ws = line.split(" "); sp = font.getlength(" ")
        wsum = sum(font.getlength(w) for w in ws) + sp * (len(ws) - 1)
        x = (60 + 880) / 2 - wsum / 2 + 70
        for w in ws:
            items.append((w, x, y + li * int(font.size * 1.25), t_in + k * step)); x += font.getlength(w) + sp; k += 1
    y0, y1 = y - 70, y + len(lines) * int(font.size * 1.25) + 60
    def f(t):
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        out_a = 1.0 if t_out is None else 1 - ease((t - t_out) / 0.6)
        if band:
            ba = ease((t - t_in + 0.2) / 0.6) * out_a
            b = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(b).rectangle((0, y0, W, y1), fill=(0, 0, 0, int(125 * ba)))
            lay.alpha_composite(b.filter(ImageFilter.GaussianBlur(60)))
        d = ImageDraw.Draw(lay)
        for w, x, yy, ti in items:
            u = ease((t - ti) / 0.45) * out_a
            if u <= 0: continue
            dy = 24 * (1 - ease((t - ti) / 0.45))
            d.text((x + 2, yy + dy + 3), w, font=font, fill=(0, 0, 0, int(160 * u)))
            d.text((x, yy + dy), w, font=font, fill=color + (int(255 * u),))
        return lay
    return f

f_hook = ImageFont.truetype(SERIF, 86)
f_line = ImageFont.truetype(SERIF, 76)
f_rom = ImageFont.truetype(SERIF_R, 74)
f_gloss = ImageFont.truetype(SERIF_R, 44)
f_cta = ImageFont.truetype(SERIF_R, 46)
TXT = [
    words_layer(["Sixty duels.", "Never defeated."], f_hook, 1150, WHITE, 0.35, t_out=7.3),
    words_layer(["B A N R I   I K K Ū"], f_gloss, 1210, WHITE, 14.4, step=0.0, t_out=15.6, band=False),
    words_layer(["ten thousand truths, one emptiness"], f_gloss, 1290, CREAM, 14.8, step=0.12, t_out=15.6, band=False),
    words_layer(["Then he put down the sword", "and sat with the moon."], f_line, 1060, WHITE, 17.4, t_out=None),
    words_layer(["Full 2 hours on the channel"], f_cta, 1290, CREAM, 19.6, step=0.1, band=False),
]

# ---------- gold dust motes ----------
NM = 45
mx, my = rng.uniform(0, W, NM), rng.uniform(0, H, NM)
mv, msz, mph = rng.uniform(18, 60, NM), rng.uniform(1.5, 5.5, NM), rng.uniform(0, 6.28, NM)
def dust(fr, t):
    lay = Image.new("RGB", (W, H), 0); d = ImageDraw.Draw(lay)
    for i in range(NM):
        x = (mx[i] + 30 * np.sin(t * 0.5 + mph[i])) % W; y = (my[i] - mv[i] * t) % H
        b = 0.5 + 0.5 * np.sin(t * 2.1 + mph[i] * 3); r = msz[i]
        d.ellipse((x - r, y - r, x + r, y + r), fill=tuple(int(c * (0.25 + 0.5 * b)) for c in MOON))
    lay = lay.filter(ImageFilter.GaussianBlur(1.6))
    return Image.fromarray(np.clip(np.asarray(fr, np.int16) + np.asarray(lay, np.int16) * 0.8, 0, 255).astype(np.uint8))

# ---------- COVER beat (0-2 s): wide scene + big kanji + name; frame 1 = the Short's cover ----------
OFF = 2.0
CKS = 2.0                                               # ~218 px per kanji
CSTR = build_strokes(["06b66", "08535"], CKS, 870 - 54.5 * CKS, 400, 230)
CMASK, _ = brush_mask(99.0, CSTR, CKS)
CGLOW = np.asarray(Image.fromarray((CMASK * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(18)), np.float32)[..., None] / 255
SCRIM = (np.exp(-(((XX - 870) / 260) ** 2 + ((YY - 720) / 420) ** 2)) * 0.5)[..., None]
f_cname = ImageFont.truetype(SERIF, 70); f_csub = ImageFont.truetype(SERIF_R, 36)
def cover_text():
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for txt, f, y, col in (("MUSASHI", f_cname, 885, WHITE), ("SAMURAI ZEN MUSIC", f_csub, 995, CREAM)):
        x = min(870 - f.getlength(txt) / 2, 1010 - f.getlength(txt))
        d.text((x + 2, y + 3), txt, font=f, fill=(0, 0, 0, 170)); d.text((x, y), txt, font=f, fill=col + (255,))
    return lay
CTEXT = cover_text()
def shot_cover(t):
    F = np.asarray(crop(Image.fromarray(next_src.cur), 760, 540, 1.0), np.float32)
    F *= 1 - SCRIM
    F = F * (1 - 0.35 * CGLOW) + CGLOW * 0.6 * np.array(GOLD, np.float32)
    F = F * (1 - CMASK[..., None]) + CMASK[..., None] * np.array(WHITE, np.float32)
    im = Image.fromarray(np.clip(F, 0, 255).astype(np.uint8)).convert("RGBA")
    im.alpha_composite(CTEXT); return im.convert("RGB")

# ---------- render ----------
def shot_kanji(t): return draw_kanji(shot_clouds(t), t + 8.0)          # kanji timed in absolute seconds
SEGS = [(0.0, shot_face), (8.0, shot_kanji), (16.0, shot_wide)]       # shot k starts (its local t=0) here
TRANS = [(8.0, 9.0, (540, 300)), (16.0, 17.0, (900, 1300))]          # ink blot: (start, end, seed point)
ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
    "-r", str(FPS), "-i", "-", "-ss", str(MUSIC_AT), "-t", f"{DUR:.2f}", "-i", music,
    "-filter_complex", f"[1:a]afade=t=in:d=0.6,afade=t=out:st={DUR-2.5:.2f}:d=2.5,loudnorm=I=-14:TP=-1.5[a]",
    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-crf", "17", "-preset", "slow", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-shortest", out], stdin=subprocess.PIPE)
for i in range(int(DUR * FPS)):
    T = i / FPS; t = T - OFF
    next_src.cur = next_src()
    if t < 0:                                           # cover beat
        fr = dust(shot_cover(T), T).convert("RGBA"); ff.stdin.write(fr.convert("RGB").tobytes()); continue
    k = 0 if t < 8.0 else (1 if t < 16.0 else 2)
    fr = SEGS[k][1](t - SEGS[k][0])
    for j, (s0, s1, seed) in enumerate(TRANS):
        if s0 <= t < s1:   # outgoing shot j keeps running under the spreading blot of shot j+1
            fr = ink_mix(SEGS[j][1](t - SEGS[j][0]), fr, (t - s0) / (s1 - s0), seed)
    if t < 0.9:                                         # cover -> hook: the face soaks through an ink blot
        fr = ink_mix(shot_cover(T), fr, t / 0.9, (870, 300))
    fr = dust(fr, T).convert("RGBA")
    for L in TXT: fr.alpha_composite(L(t))
    ff.stdin.write(fr.convert("RGB").tobytes())
    if i % 90 == 0: print(f"{t:5.1f}s", flush=True)
ff.stdin.close(); ff.wait(); vproc.kill()
print("saved", out)
