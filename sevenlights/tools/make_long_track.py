"""Длинный трек (1–10 ч) из нескольких коротких: умные бесшовные стыки, срез баса, круг повторяется до нужной длины.

Перенос режима Smart из make_long_track.ps1 на Python (numpy + ffmpeg): тот же поиск стыков, те же параметры и отчёт.
Нужен там, где нет PowerShell (облачная сессия Claude). На Windows можно пользоваться любым из двух скриптов.

  python make_long_track.py --in 396_01.mp3,396_02.mp3,... --trim-start 8 --trim-end 6 --hours 3 --out album_3h.flac
  python make_long_track.py --in a.mp3,b.mp3 --trim-start 8 --trim-end 6 --check --out check_1cycle.mp3   # один круг

Как ищется стык (для каждой пары «конец трека A → начало трека B»):
  1. в последних --search секундах A и первых --search секундах B (шаг 0.1 с) сравниваются «контексты» —
     лог-спектры 0–1 кГц четырёх окон по 0.5 с перед точкой (моно 8 кГц, после среза баса); берутся 60 лучших пар;
  2. для каждой пары подгоняется фаза ±30 мс по корреляции волны в окне 0.4 с; побеждает лучшая корреляция;
  3. длина стыка: сходство контекста ≥ 0.8 → 0.5 с, ≥ 0.6 → 3 с, иначе 8 с (или --fade вручную);
     кривая: линейная при корреляции волны ≥ 0.6, иначе равномощная (qsin). Смешивание afade + amix (normalize=0).
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np

SR = 8000
CTX, WIN, FINE, SHIFT = 2.0, 0.5, 0.4, 0.03


def F(x):
    return f'{x:.6f}'.rstrip('0').rstrip('.')


def T(s):
    h, r = divmod(s, 3600)
    m, sec = divmod(r, 60)
    return f'{int(h)}:{int(m):02d}:{sec:04.1f}'


def ffprobe_duration(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                         capture_output=True, text=True, check=True).stdout
    return float(out.strip().splitlines()[0])


def load_analysis(path, hpf):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-af', hpf + 'lowpass=f=1500', '-f', 'f32le', '-ac', '1',
                          '-ar', str(SR), '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).astype(np.float64)


def features(x, times):
    """Лог-спектры 4 окон по 0.5 с перед каждым моментом t (0–1 кГц), без среднего и нормированные."""
    n, N = int(WIN * SR), 4096
    bins = int(1000.0 / (SR / N))
    win = 0.5 - 0.5 * np.cos(2 * np.pi * np.arange(n) / (n - 1))
    out = np.zeros((len(times), bins * int(CTX / WIN)))
    for r, t in enumerate(times):
        parts = []
        for k in range(int(CTX / WIN)):
            e = int((t - k * WIN) * SR)
            seg = np.zeros(N)
            seg[:n] = x[e - n:e] * win
            parts.append(np.log(np.abs(np.fft.rfft(seg))[:bins] + 1e-4))
        f = np.concatenate(parts)
        f -= f.mean()
        out[r] = f / (np.linalg.norm(f) + 1e-12)
    return out


def find(xa, xb, e_min, e_max, s_min, s_max):
    """Лучший стык: (e, s, корреляция волны, сходство контекста)."""
    te = [t for t in np.arange(e_min, e_max + 1e-9, 0.1) if t * SR < len(xa) and t - CTX >= 0]
    ts = [t for t in np.arange(s_min, s_max + 1e-9, 0.1) if t * SR < len(xb) and t - CTX >= 0]
    if not te or not ts:
        return None
    fe, fs = features(xa, te), features(xb, ts)
    sim = fe @ fs.T
    flat = np.argsort(sim, axis=None)[::-1][:60]
    nf, sh = int(FINE * SR), int(SHIFT * SR)
    best = None
    for idx in flat:
        i, j = np.unravel_index(idx, sim.shape)
        e, s0 = te[i], ts[j]
        ie = int(e * SR)
        if ie - nf < 0 or ie > len(xa):
            continue
        a = xa[ie - nf:ie]
        ee = a @ a
        for d in range(-sh, sh + 1):
            i0 = int(s0 * SR) + d
            if i0 - nf < 0 or i0 > len(xb):
                continue
            b = xb[i0 - nf:i0]
            corr = (a @ b) / np.sqrt(ee * (b @ b) + 1e-12)
            if best is None or corr > best[2]:
                best = (e, i0 / SR, corr, sim[i, j])
    return best


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--in', dest='inputs', nargs='+', required=True, help='треки по порядку круга (через запятую или пробел)')
    ap.add_argument('--out', default='long.wav')
    ap.add_argument('--hours', type=float, default=3)
    ap.add_argument('--trim-start', type=float, default=0)
    ap.add_argument('--trim-end', type=float, default=0)
    ap.add_argument('--highpass', type=float, default=70)
    ap.add_argument('--fade', type=float, default=0, help='длина стыка, с; 0 = авто по сходству звука')
    ap.add_argument('--search', type=float, default=30)
    ap.add_argument('--fade-in', type=float, default=10)
    ap.add_argument('--fade-out', type=float, default=15)
    ap.add_argument('--check', action='store_true', help='собрать ровно один круг (проверка авторских прав на YouTube)')
    a = ap.parse_args()

    files = [p.strip() for arg in a.inputs for p in arg.split(',') if p.strip()]
    missing = [p for p in files if not os.path.exists(p)]
    if missing:
        sys.exit('Не найдены файлы: ' + ', '.join(missing))
    n = len(files)
    auto = a.fade <= 0
    fade = 8.0 if auto else a.fade
    if fade > 60:
        sys.exit('--fade должен быть не больше 60 секунд')
    lens = []
    for f in files:
        l = ffprobe_duration(f) - a.trim_start - a.trim_end
        if l < 2.5 * fade + 5:
            sys.exit(f"Трек '{f}' после обрезки ({l:.1f} с) слишком короткий для стыка {fade} с")
        lens.append(l)
    total = a.hours * 3600
    hpf = f'highpass=f={F(a.highpass)}:poles=2,highpass=f={F(a.highpass)}:poles=2,' if a.highpass > 0 else ''

    print('Анализ треков…', flush=True)
    xs = [load_analysis(f, hpf) for f in files]
    e, s, score = [], [], []
    for j in range(n):
        k = (j + 1) % n
        e_max = a.trim_start + lens[j]
        e_min = max(a.trim_start + 5, e_max - a.search)
        s_min = a.trim_start + max(2.0, fade) + 0.1
        s_max = min(a.trim_start + a.search, a.trim_start + lens[k] - 5)
        best = find(xs[j], xs[k], e_min, e_max, s_min, s_max)
        if best is None:
            sys.exit(f'Не удалось подобрать стык трека {j + 1} -> {k + 1}')
        e.append(best[0]); s.append(best[1]); score.append((best[2], best[3]))
    # стык j — после трека j; e_j ищется в треке j, s_{j+1} — в следующем: переставляем s так, чтобы s[i] относился к треку i
    s = [s[(i - 1) % n] for i in range(n)]
    cj = [(0.5 if sc[1] >= 0.8 else 3.0 if sc[1] >= 0.6 else 8.0) if auto else fade for sc in score]

    unit = sum(e[i] - s[i] for i in range(n))
    if a.check:
        total = unit
    lines = []
    for i in range(n):
        c_end, c_start = cj[i], cj[(i - 1) % n]
        lines.append(f'[{i}:a]{hpf}aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,asplit=3[b{i}][t{i}][g{i}];')
        lines.append(f'[b{i}]atrim=start={F(s[i])}:end={F(e[i] - c_end)},asetpts=PTS-STARTPTS[body{i}];')
        lines.append(f'[t{i}]atrim=start={F(e[i] - c_end)}:end={F(e[i])},asetpts=PTS-STARTPTS[tail{i}];')
        lines.append(f'[g{i}]atrim=start={F(s[i] - c_start)}:end={F(s[i])},asetpts=PTS-STARTPTS[ghost{i}];')
    parts = []
    for i in range(n):
        k = (i + 1) % n
        curve = 'tri' if score[i][0] >= 0.6 else 'qsin'
        lines.append(f'[tail{i}]afade=t=out:d={F(cj[i])}:curve={curve}[to{i}];')
        lines.append(f'[ghost{k}]afade=t=in:d={F(cj[i])}:curve={curve}[gi{i}];')
        lines.append(f'[to{i}][gi{i}]amix=inputs=2:duration=longest:normalize=0[join{i}];')
        parts.append(f'[body{i}][join{i}]')
    lines.append(''.join(parts) + f'concat=n={2 * n}:v=0:a=1[unit]')

    print(f"Треков: {n}; длина круга: {T(unit)}; повторов круга: {total / unit:.1f}; итог: {T(total)}; "
          f"срез баса: {F(a.highpass) + ' Гц' if a.highpass > 0 else 'нет'}")
    pos = 0.0
    for i in range(n):
        print(f'  Трек {i + 1} «{os.path.basename(files[i])}» начинается в круге на {T(pos)}')
        pos += e[i] - s[i]
        print(f'  Шов {i + 1}: конец «{os.path.basename(files[i])}» {T(e[i])} -> начало «{os.path.basename(files[(i + 1) % n])}» '
              f'{T(s[(i + 1) % n])}; волна {score[i][0]:.2f}, контекст {score[i][1]:.2f}; стык {F(cj[i])} с; в круге на {T(pos)}')
    if unit < 600:
        print(f'ВНИМАНИЕ: круг короче 10 минут, он повторится {round(total / unit)} раз — добавьте треки.')

    tmp = tempfile.mkdtemp(prefix='longtrack_')
    try:
        unit_wav = os.path.join(tmp, 'unit.wav')
        cmd = ['ffmpeg', '-y', '-loglevel', 'error']
        for f in files:
            cmd += ['-i', f]
        cmd += ['-filter_complex', ''.join(lines), '-map', '[unit]', '-c:a', 'pcm_f32le', unit_wav]
        subprocess.run(cmd, check=True)
        af = f'afade=t=in:d={F(a.fade_in)},afade=t=out:st={F(total - a.fade_out)}:d={F(a.fade_out)}'
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-stream_loop', '-1', '-i', unit_wav, '-t', F(total), '-af', af]
        low = a.out.lower()
        cmd += (['-c:a', 'pcm_s16le'] if low.endswith('.wav') else ['-c:a', 'flac'] if low.endswith('.flac')
                else ['-c:a', 'libmp3lame', '-b:a', '320k'] if low.endswith('.mp3') else [])
        subprocess.run(cmd + [a.out], check=True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f'Готово: {a.out} ({os.path.getsize(a.out) // 2 ** 20} МБ)')


if __name__ == '__main__':
    main()
