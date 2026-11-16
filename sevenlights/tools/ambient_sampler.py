"""Эмбиент для сна на НАСТОЯЩИХ записанных инструментах (VSCO 2 Community Edition, лицензия CC0).

Струнные ансамбли (виолончели, альты, скрипки) — медленные пэды по аккордам; мягкое пианино (upright, приглушённое);
редкая арфа; большой зал (свёртка с длинным хвостом). Строй A4 = 432 Гц (честный). Звук собирается из записей
живых инструментов по нашей партитуре, поэтому совпадений Content ID с чужими треками быть не должно.

Библиотека: git clone https://github.com/sgossner/vsco-2-ce (≈5 ГБ, CC0).
  python ambient_sampler.py --lib /home/user/sgossner/vsco-2-ce --seconds 128 --out demo.wav
"""
import argparse
import glob
import os
import subprocess

import numpy as np

SR = 44100
A4 = 432.0
# Аккорды v9 (до мажор): Fmaj9 → C → Am7 → G6, по 16 с; бас F2 → C2 → A1 → G2
CHORDS = [
    (41, [53, 57, 60, 64, 67]),   # F: F3 A3 C4 E4 G4
    (36, [52, 55, 60, 64, 67]),   # C: E3 G3 C4 E4 G4
    (33, [52, 57, 60, 64, 67]),   # Am7: E3 A3 C4 E4 G4
    (43, [55, 59, 62, 64, 67]),   # G6: G3 B3 D4 E4 G4
]
PENTA = [60, 62, 64, 67, 69, 72, 74, 76, 79, 81]   # до-мажорная пентатоника для пианино
# «cosmic»: ре минор, как у эталона Celestial: Dm9 → B♭maj7 → Cadd9 → Am7, ниже и темнее
CHORDS_COSMIC = [
    (38, [50, 53, 57, 60, 64]),   # Dm9:   D3 F3 A3 C4 E4
    (34, [46, 50, 53, 57, 60]),   # B♭maj7: B♭2 D3 F3 A3 C4
    (36, [48, 55, 60, 62, 64]),   # Cadd9: C3 G3 C4 D4 E4
    (33, [45, 52, 55, 60, 64]),   # Am7:   A2 E3 G3 C4 E4
]
PENTA_COSMIC = [57, 60, 62, 65, 67, 69, 72, 74, 77]  # ре-минорная пентатоника, ниже
# «drone» (по эталону «Элан Космическая Музыка», 14.11.2026): ля минор, аккорды по 18 с, сплошной тёплый пэд,
# низкий органный/контрабасовый бурдон «ля» под всем, колокольчики-искры, огромный зал, широкое «кружащее» стерео, без мелодии
CHORDS_DRONE = [
    (33, [45, 52, 55, 59, 60, 64]),   # Am9:   A2 E3 G3 B3 C4 E4
    (29, [45, 53, 57, 60, 64, 67]),   # Fmaj9: A2 F3 A3 C4 E4 G4
    (36, [48, 52, 55, 59, 64, 67]),   # Cmaj7: C3 E3 G3 B3 E4 G4
    (31, [47, 50, 55, 59, 62, 64]),   # Em7/G: B2 D3 G3 B3 D4 E4
]
PENTA_DRONE = [69, 72, 74, 76, 79, 81, 84, 86, 88]  # ля-минорная пентатоника, высоко — для колокольчиков


def load(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)


def est_midi(x):
    """Основной тон по участку 0.5–2.5 с (гармоническое произведение спектров)."""
    m = x[int(0.5 * SR):int(2.5 * SR)].mean(1)
    if len(m) < 4096:
        m = x.mean(1)
    N = 1 << 16
    sp = np.abs(np.fft.rfft(m * np.hanning(len(m)), N))
    hps = sp.copy()
    for k in (2, 3):
        d = sp[::k]
        hps[:len(d)] *= d
    fr = np.fft.rfftfreq(N, 1 / SR)
    band = (fr > 30) & (fr < 2000)
    f0 = fr[band][np.argmax(hps[band])]
    # защита от ошибки на октаву: если на f0/2 есть заметный пик — настоящий основной тон ниже
    for _ in range(2):
        lo = (fr > f0 / 2 * 0.97) & (fr < f0 / 2 * 1.03)
        hi = (fr > f0 * 0.97) & (fr < f0 * 1.03)
        if f0 / 2 > 30 and sp[lo].max() > 0.25 * sp[hi].max():
            f0 /= 2
        else:
            break
    return 69 + 12 * np.log2(f0 / 440.0)


def name_midi(path):
    """Нота из имени файла VSCO (нотация, где C3 = до первой октавы = MIDI 60): ..._A2_... → 57."""
    import re
    m = re.search(r'_([A-G])(#?)(-?\d)(?:_|\.)', os.path.basename(path))
    if not m:
        return None
    pc = 'C D EF G A B'.index(m.group(1)) + (1 if m.group(2) else 0)
    return 12 * (int(m.group(3)) + 2) + pc


class Instrument:
    def __init__(self, files, keymap=None):
        """keymap: {путь: midi} — если известно из MappingChart, иначе нота определяется по звуку."""
        self.samples = []
        for f in files:
            x = load(f)
            x /= (np.abs(x).max() + 1e-9)
            self.samples.append((keymap[f] if keymap and f in keymap else est_midi(x), x))
        self.samples.sort(key=lambda t: t[0])
        self.rng = None   # если задан — среди записей одной ноты (v1/v2/v3) выбирается случайная: звук живее


    def render(self, midi, dur, attack=0.02, release=1.5, loop=False):
        best = min(abs(t[0] - midi) for t in self.samples)
        takes = [t for t in self.samples if abs(abs(t[0] - midi) - best) < 0.01]
        m0, x = takes[self.rng.integers(len(takes))] if self.rng is not None else takes[0]
        ratio = 2 ** ((midi - m0) / 12) * (A4 / 440.0)      # перенос на нужную ноту + строй 432
        n_out = int((dur + release) * SR)
        if loop:   # длинная нота: склеиваем середину сэмпла с перекрытием, чтобы держать звук сколько нужно
            a, b = int(1.0 * SR), len(x) - int(1.0 * SR)
            body = x[a:b]
            need = int(n_out * ratio) + SR
            xf = int(0.8 * SR)
            seg = x[:b].copy()
            while len(seg) < need:
                w = np.linspace(0, 1, xf)[:, None]
                seg[-xf:] = seg[-xf:] * np.sqrt(1 - w) + body[:xf] * np.sqrt(w)
                seg = np.concatenate([seg, body[xf:]])
            x = seg
        pos = np.arange(n_out) * ratio
        pos = pos[pos < len(x) - 1]
        i = pos.astype(int); f = (pos - i)[:, None]
        y = x[i] * (1 - f) + x[i + 1] * f
        env = np.ones(len(y))
        na = max(1, int(attack * SR)); env[:na] = np.linspace(0, 1, na)
        nr = int(release * SR); rs = max(0, len(y) - nr); env[rs:] *= np.linspace(1, 0, len(y) - rs)
        return y * env[:, None]


def lowpass(x, fc):
    """Мягкий ФНЧ через БПФ (без внешних библиотек)."""
    n = len(x)
    N = 1 << int(np.ceil(np.log2(n)))
    X = np.fft.rfft(x, N, axis=0)
    fr = np.fft.rfftfreq(N, 1 / SR)
    H = 1 / np.sqrt(1 + (fr / fc) ** 4)
    return np.fft.irfft(X * H[:, None], N, axis=0)[:n]


def highpass(x, fc):
    n = len(x)
    N = 1 << int(np.ceil(np.log2(n)))
    X = np.fft.rfft(x, N, axis=0)
    fr = np.fft.rfftfreq(N, 1 / SR)
    H = (fr / fc) ** 4 / (1 + (fr / fc) ** 4)
    return np.fft.irfft(X * np.sqrt(H)[:, None], N, axis=0)[:n]


def reverb(x, rt60=7.0, wet=0.5, seed=3):
    """Большой зал: свёртка с затухающим стерео-шумом (декоррелированные каналы)."""
    rng = np.random.default_rng(seed)
    L = int(rt60 * 1.2 * SR)
    t = np.arange(L) / SR
    decay = np.exp(-6.91 * t / rt60)
    ir = rng.standard_normal((L, 2)) * decay[:, None]
    ir = lowpass(ir, 5000)
    ir[:int(0.03 * SR)] = 0                       # предзадержка 30 мс
    ir /= np.sqrt((ir ** 2).sum(0, keepdims=True))
    n = len(x) + L
    N = 1 << int(np.ceil(np.log2(n)))
    X = np.fft.rfft(x.mean(1), N)
    wetsig = np.stack([np.fft.irfft(X * np.fft.rfft(ir[:, c], N), N)[:n] for c in range(2)], 1)
    dry = np.zeros((n, 2)); dry[:len(x)] = x
    return dry * (1 - wet) + wetsig * wet * 1.6


def _fftconv_size(n):
    return 1 << int(np.ceil(np.log2(n)))


def reverb_stereo(x, rt60=13.0, wet=0.7, seed=3, send=None):
    """«Объёмный» зал: true-stereo (L и R отдельно + перекрёстные пути), ранние отражения 12–90 мс,
    верх затухает быстрее низа, хвост медленно «плывёт» (две разные IR плавно смешиваются, период 37 с).
    send — сигнал, который идёт ТОЛЬКО в зал (гранулы, шиммер)."""
    rng = np.random.default_rng(seed)
    L = int(rt60 * 1.15 * SR)
    t = np.arange(L) / SR
    def one_ir():
        nz = rng.standard_normal(L)
        ir = lowpass(nz[:, None], 1500)[:, 0] * np.exp(-6.91 * t / rt60) \
            + highpass(nz[:, None], 1500)[:, 0] * np.exp(-6.91 * t / (rt60 * 0.5))
        ir[:int(0.02 * SR)] = 0                          # предзадержка 20 мс
        ir[:int(0.09 * SR)] *= np.linspace(0, 1, int(0.09 * SR)) ** 2 * 0.5
        for _ in range(9):                               # ранние отражения: свои у каждого пути
            d = int(rng.uniform(0.012, 0.09) * SR)
            ir[d] += rng.uniform(0.3, 0.8) * rng.choice([-1, 1]) * np.sqrt((ir ** 2).sum() / SR) * 3
        ir = lowpass(ir[:, None], 7000)[:, 0]
        return ir / np.sqrt((ir ** 2).sum())
    n = len(x) + L
    N = _fftconv_size(n)
    src = x if send is None else x + send[:len(x)]
    XL, XR = np.fft.rfft(src[:, 0], N), np.fft.rfft(src[:, 1], N)
    tt = np.arange(n) / SR
    m = 0.5 + 0.5 * np.sin(2 * np.pi * tt / 37.0)
    out = np.zeros((n, 2))
    for w in (1 - m, m):                                  # две IR, плавно сменяют друг друга
        hLL, hRR, hLR, hRL = (np.fft.rfft(one_ir(), N) for _ in range(4))
        out[:, 0] += w * np.fft.irfft(XL * hLL + 0.35 * XR * hRL, N)[:n]
        out[:, 1] += w * np.fft.irfft(XR * hRR + 0.35 * XL * hLR, N)[:n]
    dry = np.zeros((n, 2)); dry[:len(x)] = x
    return dry * (1 - wet) + out * wet * 1.6


def synth_pad(notes, dur, rng, attack=6.0, release=6.0):
    """Тёплый синт-пэд: на каждую ноту 3 голоса с расстройкой ±7–12 центов, разведены по панораме;
    «фильтр» открывается за ~8 с и медленно дышит (LFO 0.05 Гц) — сделано аддитивно, без алиасинга."""
    n = int((dur + release) * SR)
    out = np.zeros((n, 2))
    tt = np.arange(n) / SR
    env = np.minimum(1, tt / attack) ** 2
    rs = int(dur * SR); env[rs:] *= np.linspace(1, 0, n - rs)
    ph = rng.uniform(0, 2 * np.pi)
    fc = (250 + 1100 * (1 - np.exp(-tt / 8))) * (0.8 + 0.2 * np.sin(2 * np.pi * 0.05 * tt + ph))
    for midi in notes:
        for det, pan in ((-rng.uniform(7, 12), -0.7), (rng.uniform(-2, 2), 0.0), (rng.uniform(7, 12), 0.7)):
            f0 = 440 * 2 ** ((midi - 69 + det / 100) / 12) * (A4 / 440.0)
            K = int(min(3500, SR / 2 - 1000) // f0)
            phi = 2 * np.pi * f0 * tt + rng.uniform(0, 2 * np.pi)
            y = np.zeros(n)
            for k in range(1, K + 1):
                y += np.sin(k * phi) * np.exp(-k * f0 / fc) / k ** 1.2
            y *= env
            out[:, 0] += y * np.sqrt(0.5 * (1 - pan)); out[:, 1] += y * np.sqrt(0.5 * (1 + pan))
    return out


def chorus(x, rng):
    """Хорус: на каждый канал — своя медленно «плавающая» задержка 15–25 мс."""
    n = len(x); tt = np.arange(n) / SR
    out = x.copy()
    for c, (rate, ph) in enumerate(((0.13, 0.0), (0.17, 1.7))):
        d = (0.020 + 0.005 * np.sin(2 * np.pi * rate * tt + ph + rng.uniform(0, 1))) * SR
        pos = np.arange(n) - d
        pos = np.clip(pos, 0, n - 2); i = pos.astype(int); f = pos - i
        out[:, c] = 0.7 * x[:, c] + 0.5 * (x[i, 1 - c] * (1 - f) + x[i + 1, 1 - c] * f)
    return out


def grains(src, rng, seconds, rate=20.0):
    """Гранулярное облако: короткие кусочки (80–300 мс) уже сыгранного звука, иногда на октаву выше,
    случайная панорама. Идёт только в зал — даёт «мерцающий» объём."""
    out = np.zeros_like(src)
    t = 1.0
    while t < seconds:
        ln = int(rng.uniform(0.08, 0.3) * SR)
        r = 2.0 if rng.random() < 0.3 else 1.0
        s0 = int(max(0, t - rng.uniform(0.2, 3.0)) * SR)
        idx = s0 + (np.arange(ln) * r).astype(int)
        idx = idx[idx < len(src)]
        g = src[idx].mean(1) * np.hanning(len(idx))
        pan = rng.uniform(-0.9, 0.9)
        i = int(t * SR); j = min(len(out), i + len(g))
        out[i:j, 0] += g[:j - i] * np.sqrt(0.5 * (1 - pan)); out[i:j, 1] += g[:j - i] * np.sqrt(0.5 * (1 + pan))
        t += rng.exponential(1 / rate)
    return out


def movavg(x, w):
    c = np.cumsum(np.concatenate([[0], x]))
    y = (c[w:] - c[:-w]) / w
    return np.concatenate([np.full(w // 2, y[0]), y, np.full(len(x) - len(y) - w // 2, y[-1])])


def master(mix):
    """Мастер: тёплый наклон EQ, мягкая компрессия, M/S-расширение (сторона +2 дБ выше 300 Гц), лёгкое насыщение."""
    n = len(mix); N = _fftconv_size(n)
    fr = np.fft.rfftfreq(N, 1 / SR)
    gdb = 1.5 / (1 + (fr / 200) ** 2) - 2.0 * (fr / 5000) ** 2 / (1 + (fr / 5000) ** 2)
    mix = np.fft.irfft(np.fft.rfft(mix, N, axis=0) * (10 ** (gdb / 20))[:, None], N, axis=0)[:n]
    M = (mix[:, 0] + mix[:, 1]) / 2; S = (mix[:, 0] - mix[:, 1]) / 2
    S = S + 0.26 * highpass(S[:, None], 300)[:, 0]
    S *= min(1.0, np.sqrt(0.7 * np.mean(M ** 2) / (np.mean(S ** 2) + 1e-12)))   # не шире S/M ≈ −1.5 дБ: в моно (телефон) звук не пропадает
    mix = np.stack([M + S, M - S], 1)
    env = np.sqrt(movavg((mix ** 2).mean(1), int(0.5 * SR)) + 1e-12)
    thr = np.sqrt(np.mean(mix ** 2)) * 1.4
    gain = np.where(env > thr, (env / thr) ** (1 / 2.0 - 1), 1.0)       # 2:1 выше порога
    mix *= movavg(gain, int(1.0 * SR))[:, None]
    mix *= 0.12 / (np.sqrt(np.mean(mix ** 2)) + 1e-9)
    return np.tanh(mix / 0.6) * 0.6


def loudness(path):
    r = subprocess.run(['ffmpeg', '-nostats', '-i', path, '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    import re
    I = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r)[-1]); tp = float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS', r)[-1])
    return I, tp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lib', default='/home/user/sgossner/vsco-2-ce')
    ap.add_argument('--seconds', type=float, default=128)
    ap.add_argument('--out', required=True)
    ap.add_argument('--seed', type=int, default=11)
    ap.add_argument('--piano-gain', type=float, default=0.55)
    ap.add_argument('--pad-gain', type=float, default=1.0)
    ap.add_argument('--preset', choices=['warm', 'cosmic', 'drone'], default='warm',
                    help='warm — до мажор, светлый; cosmic — ре минор, темнее, контрабас, орган, колокольчики, гонг, шиммер, мелодия-мотивы')
    ap.add_argument('--organ-gain', type=float, default=1.0)
    ap.add_argument('--midi', help='сохранить партитуру в MIDI (темп 60: 1 доля = 1 с; в DAW поставить A = 432 Гц)')
    ap.add_argument('--bells-gain', type=float, default=1.0)
    ap.add_argument('--depth', action='store_true',
                    help='«объём»: стерео-зал с отражениями, синт-пэд с хорусом, гранулярное облако, живые дубли, мастеринг до −16 LUFS')
    ap.add_argument('--synth-gain', type=float, default=0.55, help='синт-пэд относительно струнных (с --depth)')
    ap.add_argument('--grain-gain', type=float, default=0.4, help='гранулярное облако (с --depth)')
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    rng2 = np.random.default_rng(a.seed + 1000)   # всё случайное для --depth: партитура та же, что без него
    L = a.lib
    def named(pat):
        fs = glob.glob(pat)
        return Instrument(fs, keymap={f: name_midi(f) for f in fs if name_midi(f) is not None})
    vv = '*' if a.depth else '*v1'
    cello = named(f'{L}/Strings/Cello Section/susvib/{vv}*.wav')
    viola = named(f'{L}/Strings/Viola Section/susvib/{vv}*.wav')
    violin = named(f'{L}/Strings/Violin Section/susVib/{vv}.wav')
    if a.depth:
        for ins in (cello, viola, violin):
            ins.rng = rng2
    pf = sorted(glob.glob(f'{L}/Keys/Upright Piano/Player_dyn1_rr1_*.wav'))
    chart = {}
    for line in open(f'{L}/Keys/Upright Piano/MappingChart.txt'):
        if '=' in line and line[:3].isdigit():
            k, v = line.strip().split('=')
            chart[int(k)] = int(v)
    pmap = {f: chart[int(os.path.basename(f)[-7:-4])] for f in pf if int(os.path.basename(f)[-7:-4]) in chart}
    piano = Instrument([f for f in pf if f in pmap and 48 <= pmap[f] <= 88], keymap=pmap)
    harp = named(f'{L}/Strings/Harp/*.wav')
    drone = a.preset == 'drone'
    cosmic = a.preset in ('cosmic', 'drone')
    chords, penta = ((CHORDS_DRONE, PENTA_DRONE) if drone else (CHORDS_COSMIC, PENTA_COSMIC)) if cosmic else (CHORDS, PENTA)
    if cosmic:
        cbass = named(f'{L}/Strings/Solo Contrabass/SusVib/*.wav')
        of = glob.glob(f'{L}/Keys/Organ/Quiet/NT5_Man3Quiet_*_rr1.wav')
        organ = Instrument(of, keymap={f: int(os.path.basename(f).split('_')[2]) - 86 for f in of})
        bf = [f for f in glob.glob(f'{L}/Miscellania Raw/Misc 2/NepaleseBells/*.wav')
              if 'fx_long' in f or 'fx_med' in f or 'fx2_short_r0' in f or 'fx3_short_r02' in f]
        bells = [load(f) for f in bf]
        bells = [(b / (np.abs(b).max() + 1e-9), est_midi(b)) for b in bells]
        gong = load(f'{L}/Miscellania Raw/Misc 1/cymbgong_pp.wav')
        gong = gong / (np.abs(gong).max() + 1e-9)

    total = int((a.seconds + 10) * SR)
    pads = np.zeros((total, 2)); keys = np.zeros((total, 2)); syn = np.zeros((total, 2))

    ev = {}   # партитура для экспорта в MIDI: дорожка → [(нота, старт, длительность, velocity)]

    def rec(track, m, t, d, g):
        ev.setdefault(track, []).append((m, t, d, int(np.clip(40 + 220 * g, 1, 127))))

    def add(buf, y, t, g, swirl=False):
        i = int(t * SR); j = min(len(buf), i + len(y))
        if j > i:
            y = y[:j - i] * g
            if a.depth and buf is pads:   # живость: ±2 дБ и медленная волна громкости у каждого голоса
                tt = np.arange(len(y)) / SR
                y = y * 10 ** (rng2.uniform(-2, 2) / 20) * (1 + 0.18 * np.sin(2 * np.pi * tt / rng2.uniform(9, 17) + rng2.uniform(0, 6.3)))[:, None]
            if swirl:   # медленное «кружение» по панораме: свой период 20–40 с у каждого голоса
                per = rng.uniform(20, 40); ph0 = rng.uniform(0, 2 * np.pi)
                tt = (np.arange(len(y)) / SR + t)
                pan = 0.55 * np.sin(2 * np.pi * tt / per + ph0)
                y = y * np.stack([np.sqrt(0.5 * (1 - pan)), np.sqrt(0.5 * (1 + pan))], 1) * np.sqrt(2)
            buf[i:j] += y

    chord_len = 18.0 if drone else (20.0 if cosmic else 16.0)
    if drone:   # бурдон «ля» под всей пьесой: контрабас A1 + орган A2, непрерывно
        add(pads, cbass.render(33, a.seconds + 6, attack=8, release=6, loop=True), 0, 0.34)
        add(pads, organ.render(45, a.seconds + 6, attack=8, release=6, loop=True), 0, 0.12 * a.organ_gain)
        rec('Contrabass', 33, 0, a.seconds, 0.34); rec('Organ', 45, 0, a.seconds, 0.12 * a.organ_gain)
    t = 0.0; k = 0
    while t < a.seconds:
        bass, notes = chords[k % len(chords)]
        dur = chord_len + 3
        add(pads, cello.render(bass + 12, dur, attack=3.5, release=4, loop=True), t, 0.32)
        rec('Cello', bass + 12, t, dur, 0.32)
        if a.depth:
            add(syn, synth_pad(sorted(notes)[:4] if cosmic else notes[:4], dur, rng2,
                               attack=7.0 if cosmic else 5.0, release=6.0 if cosmic else 4.0), t, 1.0)
        if cosmic and not drone:
            add(pads, cbass.render(bass, dur, attack=5, release=5, loop=True), t, 0.30)          # глубокий низ
            rec('Contrabass', bass, t, dur, 0.30)
            for iv, g in ((12, 0.10), (19, 0.07), (24, 0.06)):                                   # тихий орган: основа, квинта, октава
                add(pads, organ.render(bass + iv, dur, attack=6, release=6, loop=True), t + 0.5, g * a.organ_gain)
                rec('Organ', bass + iv, t + 0.5, dur, g * a.organ_gain)
            if k % 2 == 0:   # гонг задом наперёд: мягкое нарастание «вдоха» в смену аккорда
                g = gong[::-1][-int(7 * SR):]
                g = g * np.linspace(0, 1, len(g))[:, None] ** 2
                add(keys, g, max(0, t - 6.5), 0.22)
                rec('FX (reverse gong)', 38, max(0, t - 6.5), 7, 0.22)
        for n in notes:
            inst = viola if n < 60 else violin
            if cosmic and not drone and n >= 62 and rng.random() < 0.4:      # темнее: верхние голоса реже
                continue
            dt = rng.random() * 0.8
            add(pads, inst.render(n, dur, attack=(7.0 if drone else 6.0 if cosmic else 4.0) + rng.random(),
                                  release=6 if drone else 5 if cosmic else 4, loop=True),
                t + dt, 0.16, swirl=drone)
            rec('Strings', n, t + dt, dur, 0.16)
        # арфа: тихое арпеджио раз в аккорд
        for j, n in enumerate([] if drone else sorted(rng.choice(notes, 3, replace=False))):
            add(keys, harp.render(n + 12, 6, release=3), t + 2 + j * 0.45, 0.10)
            rec('Harp', n + 12, t + 2 + j * 0.45, 3, 0.10)
        t += chord_len; k += 1
    if cosmic:
        # мелодия: два мотива (A и B) по 4–5 нот, A на 1-м и 3-м аккорде, B на 2-м и 4-м; каждый раз с небольшой вариацией.
        # Ноты — из пентатоники; первая и последняя ноты фразы — звуки текущего аккорда, поэтому мелодия всегда в гармонии.
        rhythms = [[2.0, 2.0, 4.0, 6.0], [1.5, 1.5, 1.0, 4.0, 6.0], [3.0, 1.0, 4.0, 6.0]]
        def motif():
            r = rhythms[rng.integers(len(rhythms))]
            steps = [int(rng.choice([-2, -1, 1, 1, 2])) for _ in r[1:]]
            return r, steps
        motifs = [motif(), motif()]
        t0 = 0.0; k = 0
        while t0 < a.seconds and not drone:
            bass, notes = chords[k % len(chords)]
            r, steps = motifs[k % 2]
            if k % 8 in (6, 7):            # каждые 8 аккордов — пауза, мелодия «дышит»
                t0 += chord_len; k += 1; continue
            top = [n + 12 for n in notes if 57 <= n + 12 <= 76]
            start = min(top, key=lambda n: abs(n - 67)) if top else 67
            idx = int(np.argmin([abs(p - start) for p in penta]))
            tt = t0 + 1.5
            seq = [idx] + [None] * len(steps)
            for j, st in enumerate(steps):
                v = st if rng.random() > 0.25 else -st            # вариация: иногда шаг в другую сторону
                seq[j + 1] = int(np.clip(seq[j] + v, 0, len(penta) - 1))
            for j, (ni, d) in enumerate(zip(seq, r)):
                note = penta[ni]
                if j == len(seq) - 1:                              # последняя нота — звук аккорда
                    cands = [n for n in [x + 12 for x in notes] + notes if 57 <= n <= 79]
                    note = min(cands, key=lambda n: abs(n - note)) if cands else note
                add(keys, piano.render(note, d + 3, release=4), tt, a.piano_gain * (0.85 if j == 0 else 0.7))
                rec('Piano', note, tt, d, a.piano_gain * (0.85 if j == 0 else 0.7))
                tt += d
            t0 += chord_len; k += 1
        # тибетские (непальские) колокольчики: редкие удары, каждый подстроен к ближайшей ноте пентатоники
        t = 9.0
        while t < a.seconds:
            b, m0 = bells[rng.integers(len(bells))]
            target = min(penta + [p + 12 for p in penta], key=lambda p: abs(p - m0))
            ratio = 2 ** ((target - m0) / 12) * (A4 / 440.0)
            pos = np.arange(int(len(b) / ratio)) * ratio; pos = pos[pos < len(b) - 1]
            i = pos.astype(int); f = (pos - i)[:, None]
            y = b[i] * (1 - f) + b[i + 1] * f
            pan = rng.uniform(-0.6, 0.6)
            y = y * np.array([1 - max(0, pan), 1 + min(0, pan)])
            add(keys, y, t, 0.16 * a.bells_gain, swirl=drone)
            rec('Bells', target, t, 4, 0.16 * a.bells_gain)
            t += rng.uniform(6, 16) if drone else rng.uniform(12, 26)
    # пианино: редкие ноты пентатоники, мелодия ходит маленькими шагами
    t = 3.0 if not cosmic else a.seconds + 1; idx = 4
    while t < a.seconds:
        idx = int(np.clip(idx + rng.choice([-2, -1, 1, 2]), 0, len(penta) - 1))
        gp = a.piano_gain * (0.7 + 0.3 * rng.random())
        add(keys, piano.render(penta[idx], 8, release=4), t, gp)
        rec('Piano', penta[idx], t, 4, gp)
        t += rng.uniform(4.0, 8.0) if cosmic else rng.uniform(3.0, 6.0)

    if a.depth:
        rp = np.sqrt(np.mean(pads ** 2)) + 1e-12
        syn = chorus(syn, rng2)
        pads = pads + syn * (a.synth_gain * rp / (np.sqrt(np.mean(syn ** 2)) + 1e-12))
    mix = pads * a.pad_gain + lowpass(keys, 2600 if cosmic else 3200)  # приглушённое «фетровое» пианино
    mix = highpass(lowpass(mix, 5200 if drone else 4200 if cosmic else 7000), 40)
    n_out = int(a.seconds * SR)
    if cosmic:
        # шиммер: октава вверх, только в реверберации — «свечение звёзд» над звуком
        up = mix[::2]; up = np.concatenate([up, up])[:len(mix)] * 0
        pos = np.arange(len(mix)) * 2.0; pos = pos[pos < len(mix) - 1]
        i = pos.astype(int); f = (pos - i)[:, None]
        oct_up = np.zeros_like(mix); oct_up[:len(i)] = mix[i] * (1 - f) + mix[i + 1] * f
        oct_up = lowpass(highpass(oct_up, 600), 6000)
        if a.depth:
            wet = 0.7 if drone else 0.55
            gr = grains(mix, rng2, a.seconds)
            gr *= a.grain_gain * np.sqrt(np.mean(mix ** 2)) / (np.sqrt(np.mean(gr ** 2)) + 1e-12)
            send = gr + oct_up * ((0.15 if drone else 0.10) / wet)
            mix = reverb_stereo(mix, rt60=14.0 if drone else 12.0, wet=wet, send=send)[:n_out]
        else:
            shimmer = reverb(oct_up, rt60=14.0 if drone else 12.0, wet=1.0, seed=9)[:n_out] * (0.15 if drone else 0.10)
            mix = reverb(mix, rt60=14.0 if drone else 11.0, wet=0.7 if drone else 0.55)[:n_out] + shimmer[:n_out]
    elif a.depth:
        mix = reverb_stereo(mix, rt60=8.0, wet=0.45, send=grains(mix, rng2, a.seconds) * a.grain_gain)[:n_out]
    else:
        mix = reverb(mix, rt60=7.0, wet=0.45)[:n_out]
    fade = int(6 * SR)
    mix[:fade] *= np.linspace(0, 1, fade)[:, None]; mix[-fade:] *= np.linspace(1, 0, fade)[:, None]
    if a.depth:
        mix = master(mix)
    else:
        mix *= 0.12 / (np.sqrt(np.mean(mix ** 2)) + 1e-9)                   # громкость ≈ −16 LUFS
        mix = np.tanh(mix / 0.7) * 0.7                                    # мягкий лимитер, пик ≤ −3 дБ
    def write(m):
        y = (np.clip(m, -1, 1) * 32767).astype(np.int16)
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', '-', a.out],
                       input=y.tobytes(), check=True)
    write(mix)
    if a.depth:   # точная громкость: −16 LUFS, истинный пик не выше −1 дБ
        I, tp = loudness(a.out)
        g = min(-16 - I, -1 - tp)
        write(mix * 10 ** (g / 20))
        I, tp = loudness(a.out)
        print(f'Громкость: {I:.1f} LUFS, пик {tp:.1f} дБ')
    print(f'Готово: {a.out} ({a.seconds:.0f} с)')
    if a.midi:
        import sys
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from midi_write import write_midi
        gm = {'Contrabass': 43, 'Cello': 42, 'Strings': 48, 'Organ': 19, 'Piano': 0, 'Harp': 46, 'Bells': 14,
              'FX (reverse gong)': 99}
        write_midi(a.midi, {k: (gm.get(k, 0), v) for k, v in ev.items()})
        print(f'MIDI: {a.midi} — дорожки: ' + ', '.join(f'{k} ({len(v)})' for k, v in ev.items()))


if __name__ == '__main__':
    main()
