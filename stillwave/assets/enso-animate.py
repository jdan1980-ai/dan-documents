#!/usr/bin/env python3
"""ENSO (vertical 9:16) — animate the still frame without Flow (seamless loop, every motion is periodic).
Motions: the burning zen circle breathes (brightness + bloom), the moon glows, the two temple lanterns flicker,
the circle's reflection ripples in the water (rocks and the monk never move), fireflies drift up.
The mist is left still (lesson from OKAMI: mist over detail cannot be moved cleanly in code).
Usage: python3 enso-animate.py SRC.jpg OUT.mp4 [seconds=24] [width=1080]
"""
import sys, subprocess
import numpy as np, cv2
src, out = sys.argv[1], sys.argv[2]
T = float(sys.argv[3]) if len(sys.argv) > 3 else 24.0
FPS = 24; N = int(T * FPS)
ow = int(sys.argv[4]) if len(sys.argv) > 4 else 1080
B = np.clip(cv2.resize(cv2.imread(src).astype(np.float32), (ow, ow * 16 // 9 // 2 * 2), interpolation=cv2.INTER_LANCZOS4), 0, 255)
H, W = B.shape[:2]; S = W / 1080.0
rng = np.random.default_rng(3)
Yp, Xp = np.mgrid[0:H, 0:W].astype(np.float32); yy, xx = Yp / S, Xp / S
def pnoise(ks):
    ph = rng.uniform(0, 2 * np.pi, len(ks)); w = rng.uniform(0.5, 1, len(ks))
    return lambda t: sum(wi * np.sin(2 * np.pi * k * t / T + p) for k, p, wi in zip(ks, ph, w)) / sum(w)
def gauss(cx, cy, sx, sy=None):
    sy = sy or sx; return np.exp(-((xx - cx) ** 2 / (2 * sx * sx) + (yy - cy) ** 2 / (2 * sy * sy)))

# golden aura of the god: bright warm pixels inside his silhouette area
b, g, r = B[..., 0], B[..., 1], B[..., 2]
warm = np.clip((r - 170) / 60, 0, 1) * np.clip((r - b - 60) / 60, 0, 1)
rr = np.hypot(xx - 542, yy - 765)
god_box = (np.abs(rr - 300) < 80).astype(np.float32)                 # the circle's ring
aura = cv2.GaussianBlur((warm * god_box).astype(np.float32), (0, 0), 2 * S)
bloom = cv2.GaussianBlur(aura, (0, 0), 28 * S)
pulse = pnoise([1, 2])

# lanterns
LANTERNS = [(905, 963), (830, 1014)]
flick = [pnoise([5, 7, 11, 13]), pnoise([6, 9, 12, 15])]
lamp = [gauss(x, y, 40, 50) for x, y in LANTERNS] ; moon = gauss(808, 263, 90)

# water ripple: the reflection column below the rock, soft edges, away from the side rocks
water = np.clip((yy - 1365) / 40, 0, 1) * np.clip(1 - np.abs(xx - 545) / 330, 0, 1) ** 0.7
water = cv2.GaussianBlur(water.astype(np.float32), (0, 0), 8 * S)

NM = 50
m_x = rng.uniform(0, 1080, NM); m_y = rng.uniform(0, 1920, NM); m_k = rng.choice([1, 1, 2], NM)
m_r = rng.uniform(1.4, 4.0, NM); m_ph = rng.uniform(0, 2 * np.pi, NM); m_a = rng.uniform(0.35, 0.85, NM)
GOLD = np.array([80, 178, 236], np.float32)
def add_dust(frame, t):
    for i in range(NM):
        x = (m_x[i] + 20 * np.sin(2 * np.pi * t / T + m_ph[i])) % 1080
        y = (m_y[i] - 1920 * m_k[i] * t / T) % 1920
        bb = m_a[i] * (0.55 + 0.45 * np.sin(2 * np.pi * 3 * t / T + 3 * m_ph[i]))
        rr = m_r[i] * S; X, Y = x * S, y * S; R = int(rr * 3) + 2
        x0, x1, y0, y1 = max(int(X) - R, 0), min(int(X) + R + 1, W), max(int(Y) - R, 0), min(int(Y) + R + 1, H)
        if x0 >= x1 or y0 >= y1: continue
        frame[y0:y1, x0:x1] += (np.exp(-((Xp[y0:y1, x0:x1] - X) ** 2 + (Yp[y0:y1, x0:x1] - Y) ** 2) / (2 * rr * rr)) * bb)[..., None] * GOLD
    return frame

ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                       "-c:v", "libx264", "-crf", "14", "-preset", "slow", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
for i in range(N):
    t = i / FPS; ph = 2 * np.pi * t / T
    dx = water * (4.0 * np.sin(6 * ph - yy / 9) + 2.0 * np.sin(4 * ph + yy / 23))
    dy = water * (1.5 * np.sin(5 * ph - yy / 14))
    fr = cv2.remap(B, (Xp - dx * S).astype(np.float32), (Yp - dy * S).astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    p = 0.5 + 0.5 * pulse(t)
    gain = 1 + aura * (0.05 + 0.10 * p) + 0.10 * (flick[0](t) * lamp[0] + flick[1](t) * lamp[1]) + 0.05 * p * moon
    fr = fr * gain[..., None] + (bloom * (0.10 + 0.18 * p))[..., None] * np.array([90, 200, 255], np.float32)
    fr = add_dust(fr, t)
    ff.stdin.write(np.clip(fr, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait(); print("saved", out)
