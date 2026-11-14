"""Проверка треков альбома перед склейкой: строй, тональность, сверхнизкий бас, громкость и сходство треков.

  python album_check.py a.mp3 b.mp3 c.mp3 ...                       # анализ + сходство внутри альбома
  python album_check.py album5/*.mp3 --compare album4/*.mp3          # + сравнение с прошлым альбомом (повторы/копии)
  python album_check.py album5/*.mp3 --order                         # + предложение порядка по кругу квинт

Сходство — косинус лог-спектров по секундам (60–3500 Гц) с лучшим сдвигом ±200 с. Треки одного промпта: 0.6–0.85
(это нормально, так задумано); копия/вариация того же трека: ≈0.95+.
Нужны numpy и ffmpeg.
"""
import argparse
import itertools
import os
import subprocess

import numpy as np

NOTES = 'C C# D D# E F F# G G# A A# B'.split()
MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])


def load(path, sr):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', path, '-ac', '1', '-ar', str(sr), '-f', 'f32le', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).astype(np.float64)


def analyze(path):
    sr = 22050
    x = load(path, sr)
    N = 16384
    spec = np.zeros(N // 2 + 1)
    for i in range(0, len(x) - N, N):
        spec += np.abs(np.fft.rfft(x[i:i + N] * np.hanning(N))) ** 2
    fr = np.fft.rfftfreq(N, 1 / sr)
    sub = spec[(fr > 20) & (fr < 60)].sum() / spec[fr > 20].sum()
    idx = np.where((fr > 80) & (fr < 2000))[0]
    pk = [i for i in idx if spec[i] > spec[i - 1] and spec[i] > spec[i + 1]]
    pk = sorted(pk, key=lambda i: -spec[i])[:60]
    cents, w = [], []
    for i in pk:
        a, b, c = np.log(spec[i - 1:i + 2])
        f0 = (i + 0.5 * (a - c) / (a - 2 * b + c)) * sr / N
        m = 12 * np.log2(f0 / 440)
        cents.append((m - round(m)) * 100); w.append(spec[i])
    tune = np.angle(np.sum(np.array(w) * np.exp(1j * np.array(cents) / 100 * 2 * np.pi))) / (2 * np.pi) * 100
    chroma = np.zeros(12)
    for i in np.where((fr > 60) & (fr < 2000))[0]:
        chroma[(int(round(12 * np.log2(fr[i] / 440) - tune / 100)) + 9) % 12] += spec[i]
    best = max(((np.corrcoef(chroma, np.roll(p, k))[0, 1], k, mode) for k in range(12)
                for mode, p in (('major', MAJ), ('minor', MIN))))
    rms = 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-12)
    return dict(dur=len(x) / sr, tune=tune, key=best[1], mode=best[2], r=best[0], sub=sub, rms=rms)


def features(path):
    sr, N = 8000, 4096
    x = load(path, sr)
    fr = np.fft.rfftfreq(N, 1 / sr)
    edges = np.geomspace(60, 3500, 49)
    F = []
    for i in range(0, len(x) - N, sr):
        s = np.abs(np.fft.rfft(x[i:i + N] * np.hanning(N))) ** 2
        F.append(np.log(np.array([s[(fr >= edges[k]) & (fr < edges[k + 1])].sum() for k in range(48)]) + 1e-9))
    F = np.array(F)
    F -= F.mean(1, keepdims=True)
    return F / (np.linalg.norm(F, axis=1, keepdims=True) + 1e-9)


def similarity(A, B):
    best = -1
    for off in range(-200, 201, 2):
        a0, b0 = max(0, off), max(0, -off)
        n = min(len(A) - a0, len(B) - b0)
        if n >= 60:
            best = max(best, float(np.mean(np.sum(A[a0:a0 + n] * B[b0:b0 + n], 1))))
    return best


def fifths_dist(k1, k2):
    """Расстояние по кругу квинт между мажорными тониками (минор переводится в параллельный мажор)."""
    pos = lambda k: (k * 7) % 12
    d = abs(pos(k1) - pos(k2)) % 12
    return min(d, 12 - d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tracks', nargs='+')
    ap.add_argument('--compare', nargs='*', default=[], help='треки прошлых альбомов для поиска повторов')
    ap.add_argument('--order', action='store_true', help='предложить порядок треков по кругу квинт')
    a = ap.parse_args()
    names = [os.path.basename(t) for t in a.tracks]
    info = {}
    print(f"{'трек':28s} {'длина':>6s} {'строй':>7s}  тональность     бас<60Гц  RMS")
    for t, n in zip(a.tracks, names):
        r = analyze(t)
        info[t] = r
        key = NOTES[r['key']] + (' мажор' if r['mode'] == 'major' else ' минор')
        print(f"{n[:28]:28s} {r['dur'] / 60:5.2f}м {r['tune']:+6.1f}ц  {key:10s}({r['r']:.2f})  {100 * r['sub']:5.1f}%  {r['rms']:5.1f} дБ")
    F = {t: features(t) for t in a.tracks}
    print('\nСходство внутри альбома (копия ≈ 0.95+):')
    worst = max(((similarity(F[x], F[y]), x, y) for x, y in itertools.combinations(a.tracks, 2)), default=None)
    for x, y in itertools.combinations(a.tracks, 2):
        print(f'  {os.path.basename(x)} ~ {os.path.basename(y)}: {similarity(F[x], F[y]):.2f}')
    if a.compare:
        print('\nСходство с прошлыми треками (максимум по каждому):')
        G = {c: features(c) for c in a.compare}
        for t in a.tracks:
            s, c = max((similarity(F[t], G[c]), c) for c in a.compare)
            print(f'  {os.path.basename(t)}: {s:.2f} (с {os.path.basename(c)})' + ('  ← ВОЗМОЖНАЯ КОПИЯ' if s >= 0.9 else ''))
    if a.order and len(a.tracks) > 2:
        tonic = {t: (info[t]['key'] + (3 if info[t]['mode'] == 'minor' else 0)) % 12 for t in a.tracks}
        best = min(itertools.permutations(a.tracks[1:]), key=lambda p: (
            lambda seq: (sum(fifths_dist(tonic[seq[i]], tonic[seq[(i + 1) % len(seq)]]) for i in range(len(seq))),
                         max(fifths_dist(tonic[seq[i]], tonic[seq[(i + 1) % len(seq)]]) for i in range(len(seq)))))(
            (a.tracks[0],) + p))
        order = (a.tracks[0],) + best
        print('\nПорядок по кругу квинт (меньше скачков тональности):')
        print('  ' + ' → '.join(f"{os.path.basename(t)} ({NOTES[tonic[t]]})" for t in order) + ' → снова первый')


if __name__ == '__main__':
    main()
