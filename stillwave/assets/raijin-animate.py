#!/usr/bin/env python3
"""RAIJIN (vertical 9:16) — animate the still frame without Flow (seamless loop, every motion is periodic).
Motions: the lightning arcs around the drums flash in sharp bursts, each burst briefly lights up the storm clouds;
the god's eyes glow and breathe; fine slanted rain falls over the whole frame; nothing is warped, so the priestess,
the wolf, the torii and the shrines never move.
Usage: python3 raijin-animate.py SRC.jpg OUT.mp4 [seconds=24] [width=1080]
"""
import sys, subprocess
import numpy as np, cv2
src, out = sys.argv[1], sys.argv[2]
T = float(sys.argv[3]) if len(sys.argv) > 3 else 24.0
FPS = 24; N = int(T * FPS)
ow = int(sys.argv[4]) if len(sys.argv) > 4 else 1080
B = np.clip(cv2.resize(cv2.imread(src).astype(np.float32), (ow, ow * 16 // 9 // 2 * 2), interpolation=cv2.INTER_LANCZOS4), 0, 255)
H, W = B.shape[:2]; S = W / 1080.0
rng = np.random.default_rng(9)
Yp, Xp = np.mgrid[0:H, 0:W].astype(np.float32); yy, xx = Yp / S, Xp / S
def gauss(cx, cy, sx, sy=None):
    sy = sy or sx; return np.exp(-((xx - cx) ** 2 / (2 * sx * sx) + (yy - cy) ** 2 / (2 * sy * sy)))
b, g, r = B[..., 0], B[..., 1], B[..., 2]
lum = B.mean(2)
# lightning arcs: bright, bluish-white thin lines in the upper part (not the eyes)
EYES = [(465, 405), (560, 396)]
eyezone = sum(gauss(x, y, 30) for x, y in EYES)
arcs = np.clip((lum - 175) / 50, 0, 1) * np.clip((b - r + 15) / 30, 0, 1) * (yy < 1000) * (eyezone < 0.2)
arcs = cv2.GaussianBlur(arcs.astype(np.float32), (0, 0), 0.8 * S)
arc_glow = cv2.GaussianBlur(arcs, (0, 0), 14 * S)
clouds = np.clip((1250 - yy) / 200, 0, 1).astype(np.float32)            # sky + god, fades out above the shrine
eye_glow = sum(1.0 * gauss(x, y, 6) + 0.5 * gauss(x, y, 15) + 0.2 * gauss(x, y, 40) for x, y in EYES)

# lightning bursts: 4 per loop, each a quick double flicker; periodic by construction
BURSTS = [(1.5, 1.0), (7.3, 0.7), (13.0, 1.0), (18.6, 0.8)]
def flash(t):
    v = 0.0
    for t0, a in BURSTS:
        d = (t - t0) % T
        v += a * (np.exp(-d / 0.09) + 0.6 * np.exp(-max(d - 0.18, 0) / 0.12) * (d > 0.18))
    return v
def breathe(t): return 0.5 + 0.5 * np.sin(2 * np.pi * 2 * t / T)

# rain: thin slanted streaks, each falls whole frame heights per loop
NR = 260
r_x = rng.uniform(-200, 1080, NR); r_y = rng.uniform(0, 1920, NR); r_k = rng.choice([6, 7, 8], NR)
r_l = rng.uniform(18, 38, NR); r_a = rng.uniform(0.10, 0.28, NR)
def add_rain(fr, t):
    lay = np.zeros((H, W), np.float32)
    for i in range(NR):
        y = (r_y[i] + 1920 * r_k[i] * t / T) % 1920; x = r_x[i] + 0.25 * y
        x0, y0 = x * S, y * S; x1, y1 = (x + 0.25 * r_l[i]) * S, (y + r_l[i]) * S
        cv2.line(lay, (int(x0), int(y0)), (int(x1), int(y1)), float(r_a[i]), max(1, int(S)), cv2.LINE_AA)
    return fr + lay[..., None] * np.array([215, 200, 190], np.float32)

ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                       "-c:v", "libx264", "-crf", "14", "-preset", "slow", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
for i in range(N):
    t = i / FPS; f = flash(t)
    fr = B * (1 + (0.18 * f) * clouds)[..., None]
    fr = fr * (1 + 0.9 * f * arcs)[..., None] + (arc_glow * (0.15 + 0.9 * f))[..., None] * np.array([255, 215, 190], np.float32)
    fr += (eye_glow * (0.25 + 0.25 * breathe(t) + 0.3 * min(f, 1)))[..., None] * np.array([255, 230, 200], np.float32)
    fr = add_rain(fr, t)
    ff.stdin.write(np.clip(fr, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait(); print("saved", out)
