#!/usr/bin/env python3
"""
check-build.py — «нарастает ли трек?»

Главное правило канала: музыка НИКОГДА не должна нарастать. Слушатель засыпает,
любой подъём его будит. На слух это ловится плохо и долго — 33 трека по два часа
никто не переслушает. Скрипт отвечает на вопрос числами.

Использование:
  python3 check-build.py <файл-или-папка> [--fade 3] [--quiet]

Что печатает по каждому треку:
  thirds   — средний RMS первой / второй / третьей трети. Это главный показатель.
  trend    — линейный тренд, дБ за минуту и дБ от начала к концу.
  windows  — самое тихое и самое громкое 30-секундное окно.
  sparkline — форма трека одной строкой.

Как читать:
  • Подъём В ПЕРВОЙ трети — норма: так входят инструменты по промту
    (вступление часто задумано как тишина / один звук).
  • Разница между ВТОРОЙ и ТРЕТЬЕЙ третями — вот это и есть нарастание.
    Больше +1.5 дБ — трек под подозрением, больше +3 дБ — в брак.
  • Разброс односекундного RMS в 12–18 дБ нормален для разреженного эмбиента:
    одиночный щипок против паузы. Смотреть надо на тренд, а не на разброс.
  • peak > 0 dBFS у mp3 — это про экспорт, не про музыку. Suno отдаёт mp3
    громче своего же wav. В монтаж брать только wav.

Требования: ffmpeg в PATH или `pip install imageio-ffmpeg`, плюс numpy.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np

SR = 8000            # моно 8 кГц достаточно для огибающей
WINDOW = 30          # секунд, для поиска самого тихого/громкого участка
EXTS = {".wav", ".mp3", ".flac", ".m4a", ".ogg", ".opus"}


def ffmpeg_exe():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("ffmpeg не найден. Поставь ffmpeg или `pip install imageio-ffmpeg`.")


def load_mono(path, exe):
    p = subprocess.run(
        [exe, "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
        capture_output=True,
    )
    if p.returncode != 0:
        raise RuntimeError(p.stderr.decode(errors="replace").strip()[:200])
    return np.frombuffer(p.stdout, dtype=np.float32)


def envelope_db(x):
    """Огибающая: RMS по односекундным окнам, в дБ."""
    n = len(x) // SR
    if n == 0:
        return np.empty(0)
    trimmed = x[: n * SR].reshape(n, SR)
    return 20 * np.log10(np.sqrt((trimmed.astype(np.float64) ** 2).mean(axis=1)) + 1e-12)


def sparkline(db, buckets=20):
    if len(db) == 0:
        return ""
    bm = np.array([b.mean() for b in np.array_split(db, buckets)])
    lo, hi = bm.min(), bm.max()
    chars = "▁▂▃▄▅▆▇█"
    span = hi - lo + 1e-9
    return "".join(chars[min(7, max(0, int((v - lo) / span * 7.99)))] for v in bm)


def analyse(path, exe, fade):
    x = load_mono(path, exe)
    dur = len(x) / SR
    peak = 20 * np.log10(np.max(np.abs(x)) + 1e-12)
    db = envelope_db(x)
    core = db[fade:-fade] if len(db) > 2 * fade + 6 else db
    if len(core) < 9:
        raise RuntimeError("слишком короткий трек")

    thirds = [t.mean() for t in np.array_split(core, 3)]
    slope = float(np.polyfit(np.arange(len(core)), core, 1)[0])
    back_half = thirds[2] - thirds[1]

    win = None
    if len(core) > 2 * WINDOW:
        means = np.array([core[i:i + WINDOW].mean() for i in range(len(core) - WINDOW)])
        win = (means.min(), means.max())

    if back_half > 3.0:
        verdict = "BUILDS — в брак"
    elif back_half > 1.5:
        verdict = "подозрительный — переслушать"
    else:
        verdict = "ровный"

    return dict(dur=dur, peak=peak, thirds=thirds, slope=slope, back_half=back_half,
                win=win, spark=sparkline(db), verdict=verdict, spread=core.max() - core.min())


def main():
    ap = argparse.ArgumentParser(description="Проверка треков на нарастание.")
    ap.add_argument("target", type=Path, help="файл или папка")
    ap.add_argument("--fade", type=int, default=3,
                    help="сколько секунд отрезать с краёв (фейды мастеринга), по умолчанию 3")
    ap.add_argument("--quiet", action="store_true", help="только вердикт по каждому треку")
    args = ap.parse_args()

    if args.target.is_dir():
        files = sorted(p for p in args.target.iterdir() if p.suffix.lower() in EXTS)
    else:
        files = [args.target]
    if not files:
        sys.exit(f"аудиофайлов не найдено в {args.target}")

    exe = ffmpeg_exe()
    flagged = []

    for f in files:
        try:
            r = analyse(f, exe, args.fade)
        except Exception as e:
            print(f"{f.name[:44]:<45}  ОШИБКА: {e}")
            continue

        if r["verdict"] != "ровный":
            flagged.append((f.name, r))

        if args.quiet:
            print(f"{f.name[:44]:<45} {r['back_half']:+5.1f} dB  {r['verdict']}")
            continue

        t = r["thirds"]
        print(f"\n{f.name}")
        print(f"  {int(r['dur'] // 60)}:{int(r['dur'] % 60):02d}   peak {r['peak']:+.2f} dBFS"
              f"{'   ⚠ выше 0 — это про экспорт, в монтаж брать wav' if r['peak'] > 0 else ''}")
        print(f"  thirds    {t[0]:+6.1f} → {t[1]:+6.1f} → {t[2]:+6.1f} dB")
        print(f"  trend     {r['slope'] * 60:+.2f} dB/мин   вторая→третья треть {r['back_half']:+.1f} dB")
        if r["win"]:
            print(f"  windows   тихое 30 с {r['win'][0]:+.1f}, громкое {r['win'][1]:+.1f} dB")
        print(f"  {r['spark']}")
        print(f"  → {r['verdict']}")

    if len(files) > 1:
        print(f"\n{len(files)} треков, под вопросом: {len(flagged)}")
        for name, r in flagged:
            print(f"  {name[:44]:<45} {r['back_half']:+5.1f} dB  {r['verdict']}")


if __name__ == "__main__":
    main()
