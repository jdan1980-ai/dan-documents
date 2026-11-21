#!/usr/bin/env python3
"""SHOGUN — animate the still frame without Flow (seamless loop, every motion is periodic).

Motions: two candle flames flicker and sway, their warm light trembles on the gold leaf and on the floor;
the painted tiger's gold eyes glow and slowly breathe brighter; a slow sheen of candlelight passes over the
tiger's ink stripes; the tiger's body breathes (sub-percent swell, frozen at the door rails and around the
shogun); a spark runs along the golden crescent once per loop; gold dust drifts up. The shogun stays still.
Usage: python3 shogun-animate.py SRC.jpg OUT.mp4 [seconds=24] [output width, e.g. 3840] [frame limit]
       VERT=1 for the native 9:16 frame (shogun-916-source.jpg), output width e.g. 1080.
"""
import sys, subprocess
import numpy as np, cv2

src, out = sys.argv[1], sys.argv[2]
T = float(sys.argv[3]) if len(sys.argv) > 3 else 24.0
FPS = 24; N = int(T * FPS)
import os; NODUST = os.environ.get("NODUST") == "1"; VERT = os.environ.get("VERT") == "1"
BW, BH = (1080, 1920) if VERT else (1920, 1080)          # design grid
LIMIT = int(sys.argv[5]) if len(sys.argv) > 5 else N          # optional: render only the first frames (preview)
B = cv2.imread(src).astype(np.float32)  # BGR
ow = int(sys.argv[4]) if len(sys.argv) > 4 else BW
B = np.clip(cv2.resize(B, (ow, ow * BH // BW // 2 * 2), interpolation=cv2.INTER_LANCZOS4), 0, 255)
H, W = B.shape[:2]
S = W / BW                                 # positions below are given on the design grid
rng = np.random.default_rng(11)
Yp, Xp = np.mgrid[0:H, 0:W].astype(np.float32)
yy, xx = Yp / S, Xp / S

def pnoise(ks, amp=1.0):
    ph = rng.uniform(0, 2 * np.pi, len(ks)); w = rng.uniform(0.5, 1, len(ks))
    return lambda t: amp * sum(wi * np.sin(2 * np.pi * k * t / T + p) for k, p, wi in zip(ks, ph, w)) / sum(w)
def gauss(cx, cy, s, sy=None):
    sy = sy or s
    return np.exp(-((xx - cx) ** 2 / (2 * s * s) + (yy - cy) ** 2 / (2 * sy * sy)))

# ---------- candle flames ----------
FLAMES = [(91, 1115, 1131), (1006, 1115, 1132)] if VERT else [(135, 507, 525), (1787, 511, 526)]   # x, flame centre y, base y
core = np.zeros((H, W), np.uint8)
for fx, fy, fb in FLAMES:
    cv2.ellipse(core, (round(fx * S), round((fy - 2) * S)), (round(9 * S), round(22 * S)), 0, 0, 360, 255, -1)
bg = cv2.inpaint(B.astype(np.uint8), cv2.dilate(core, np.ones((round(5 * S), round(5 * S)))), 5, cv2.INPAINT_TELEA).astype(np.float32)
lum = B.mean(2)
flame_alpha = np.clip((lum - 120) / 100, 0, 1) * (cv2.GaussianBlur(core.astype(np.float32), (0, 0), 3 * S) / 255 > 0.05)
for fx, fy, fb in FLAMES:
    flame_alpha[round((fb - 1) * S):, round((fx - 30) * S):round((fx + 30) * S)] = 0   # the wax is not flame
flame_alpha = cv2.GaussianBlur(flame_alpha.astype(np.float32), (0, 0), 1.2 * S)
flick = [pnoise([5, 7, 11, 13, 17]), pnoise([6, 9, 12, 15, 19])]
sway = [pnoise([3, 4, 7]), pnoise([2, 5, 8])]
FLOOR_Y = 1760 if VERT else 960
light = [gauss(fx, fy, 380) + 0.8 * gauss(fx, FLOOR_Y, 120, 70) for fx, fy, _ in FLAMES]   # wall + floor reflection

# ---------- tiger eyes ----------
EYES = [(200, 885), (340, 875)] if VERT else [(725, 472), (819, 470)]
eye_glow = sum(1.0 * gauss(x, y, 7) + 0.5 * gauss(x, y, 17) + 0.2 * gauss(x, y, 40) for x, y in EYES)
eye_pulse = pnoise([1, 2])

# ---------- areas that must never move: door rails, the door bottom, the shogun and his crest, the sword rack ----------
RAILS = [540] if VERT else [473, 960, 1441]
DOOR_BOTTOM = 1470 if VERT else 842
dist = np.min(np.abs(xx[None] - np.array(RAILS, np.float32)[:, None, None]), axis=0)
still = np.clip((dist - 10) / 35, 0, 1) * np.clip((DOOR_BOTTOM - yy) / 30, 0, 1)
shog = np.zeros((BH, BW), np.float32)
if VERT:
    cv2.ellipse(shog, (560, 1250), (330, 450), 0, 0, 360, 1, -1)
    cv2.rectangle(shog, (350, 715), (810, 890), 1, -1)
    cv2.rectangle(shog, (830, 1390), (1080, 1570), 1, -1)
else:
    cv2.ellipse(shog, (1000, 650), (230, 330), 0, 0, 360, 1, -1)          # shogun body + helmet
    cv2.rectangle(shog, (830, 300), (1145, 440), 1, -1)                    # crescent
    cv2.rectangle(shog, (1150, 740), (1720, 900), 1, -1)                   # katana + rack
shog = cv2.resize(cv2.GaussianBlur(shog, (0, 0), 25), (W, H), interpolation=cv2.INTER_LINEAR)
still *= np.clip(1 - 1.6 * shog, 0, 1)

# tiger body breath (two breaths per loop)
TC = (700, 650, 300, 250, 1150) if VERT else (1330, 360, 300, 200, 640)   # torso centre x, y, sigmas, belly line
torso = (gauss(TC[0], TC[1], TC[2], TC[3]) * still).astype(np.float32)

# candle sheen passing over the tiger's stripes: a soft diagonal band crosses the doors once per loop
ink = np.clip((110 - lum) / 70, 0, 1)                                    # dark ink strokes
gold = np.clip((lum - 90) / 60, 0, 1) * np.clip((235 - lum) / 40, 0, 1)
sheen_w = cv2.GaussianBlur((0.6 * gold + 0.9 * ink).astype(np.float32), (0, 0), 1.5 * S) * np.clip(1 - 1.4 * shog, 0, 1) * (yy < DOOR_BOTTOM)

# spark along the golden crescent
CREST = np.array([(367, 800), (400, 825), (440, 847), (480, 865), (520, 872), (560, 872), (600, 865),
                  (650, 845), (700, 815), (740, 780), (787, 732)], np.float32) if VERT else np.array([(842, 362), (870, 387), (905, 407), (940, 420), (970, 424), (1005, 417),
                  (1040, 402), (1075, 380), (1105, 352), (1130, 322)], np.float32)
seg = np.cumsum(np.r_[0, np.hypot(*np.diff(CREST, axis=0).T)]); CL = seg[-1]
cmask = np.zeros((BH, BW), np.uint8)
cv2.polylines(cmask, [CREST.astype(np.int32)], False, 255, 26)
cmask = cv2.resize(cmask, (W, H), interpolation=cv2.INTER_LINEAR).astype(np.float32) / 255
cmask *= np.clip((lum - 120) / 50, 0, 1)
def crest_point(s):
    s = np.clip(s, 0, CL); i = min(np.searchsorted(seg, s) , len(seg) - 1); i = max(i, 1)
    u = (s - seg[i - 1]) / (seg[i] - seg[i - 1]); return CREST[i - 1] + u * (CREST[i] - CREST[i - 1])

# ---------- gold dust ----------
NM = 55
m_x = rng.uniform(0, BW, NM); m_y = rng.uniform(0, BH, NM)
m_k = rng.choice([1, 1, 2], NM)
m_r = rng.uniform(1.4, 4.2, NM) * np.where(m_k == 2, 1.25, 1.0)
m_ph = rng.uniform(0, 2 * np.pi, NM); m_sw = rng.integers(1, 3, NM)
m_a = rng.uniform(0.35, 0.9, NM)
GOLD = np.array([80, 178, 236], np.float32)
def add_dust(frame, t):
    for i in range(NM):
        x = (m_x[i] + 22 * np.sin(2 * np.pi * m_sw[i] * t / T + m_ph[i])) % BW
        y = (m_y[i] - BH * m_k[i] * t / T) % BH
        b = m_a[i] * (0.55 + 0.45 * np.sin(2 * np.pi * 3 * t / T + 3 * m_ph[i]))
        r = m_r[i] * S; X, Y = x * S, y * S; R = int(r * 3) + 2
        x0, x1, y0, y1 = max(int(X) - R, 0), min(int(X) + R + 1, W), max(int(Y) - R, 0), min(int(Y) + R + 1, H)
        if x0 >= x1 or y0 >= y1: continue
        g = np.exp(-((Xp[y0:y1, x0:x1] - X) ** 2 + (Yp[y0:y1, x0:x1] - Y) ** 2) / (2 * r * r)) * b
        frame[y0:y1, x0:x1] += g[..., None] * GOLD
    return frame

ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
                       "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "12", "-preset", "slow", "-profile:v", "high", "-tune", "film",
                       "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
for i in range(min(N, LIMIT)):
    t = i / FPS; ph = 2 * np.pi * t / T
    br = 0.0045 * np.sin(2 * ph)
    dy = torso * br * (yy - TC[4]); dx = torso * br * 0.5 * (xx - TC[0])
    frame = cv2.remap(bg, (Xp - dx * S).astype(np.float32), (Yp - dy * S).astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    for k, (fx, fy, fb) in enumerate(FLAMES):
        f = flick[k](t); s = 1 + 0.12 * f; sw = 1.6 * sway[k](t); sh = 0.03 * sway[k](t)
        X0, Y0 = fx * S, fb * S
        M = np.float32([[1 - 0.04 * f, sh, X0 * 0.04 * f + sw * S - sh * Y0], [0, s, Y0 * (1 - s)]])
        Mf = cv2.warpAffine(B, M, (W, H), flags=cv2.INTER_LINEAR)
        Ma = cv2.warpAffine(flame_alpha, M, (W, H), flags=cv2.INTER_LINEAR) * (np.abs(xx - fx) < 40) * (np.abs(yy - fy) < 60)
        frame = frame * (1 - Ma[..., None]) + Mf * (1 + 0.08 * f) * Ma[..., None]
    # candle sheen: a soft diagonal band sweeps left -> right once per loop (off-frame at both loop ends)
    cx = (-500 + 3000 * t / T) if VERT else (-700 + 3300 * t / T)
    band = np.exp(-(((xx + 0.45 * yy) - cx) / 260) ** 2)
    gain = 1 + 0.055 * (flick[0](t) * light[0] + flick[1](t) * light[1]) + 0.07 * band * sheen_w
    frame = frame * gain[..., None]
    e = 0.6 + 0.4 * (0.5 + 0.5 * eye_pulse(t))
    frame += (eye_glow * e)[..., None] * np.array([40, 150, 245], np.float32) * 0.5
    # spark along the crescent, between 35% and 55% of the loop
    u = (t / T - 0.35) / 0.2
    if 0 < u < 1:
        px, py = crest_point(u * CL)
        sp = np.exp(-((xx - px) ** 2 + (yy - py) ** 2) / (2 * 22 ** 2)) * np.sin(np.pi * u)
        frame += (sp * cmask)[..., None] * np.array([150, 220, 255], np.float32) * 1.5
        frame += (np.exp(-((xx - px) ** 2 + (yy - py) ** 2) / (2 * 5 ** 2)) * np.sin(np.pi * u) * cmask)[..., None] * 120
    if not NODUST: frame = add_dust(frame, t)
    ff.stdin.write(np.clip(frame, 0, 255).astype(np.uint8).tobytes())
    if i % 48 == 0: print(f"{t:5.1f}s", flush=True)
ff.stdin.close(); ff.wait()
print("saved", out)
