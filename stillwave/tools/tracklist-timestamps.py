#!/usr/bin/env python3
"""
tracklist-timestamps.py — автоматический тайм-лайн трека для YouTube описания.

Использование:
  python3 tracklist-timestamps.py <папка_с_mp3> [--names names.txt]

Аргументы:
  <папка_с_mp3>     папка с MP3-файлами (Suno-экспорт)
  --names <file>    текстовый файл с именами треков (по одному на строку),
                    в том же порядке что и файлы. Если не указан — берёт имя файла.
  --offset <secs>   начальный офсет в секундах (если после wisdom-intro есть fade-in)

Вывод:
  0:00 Название трека 1
  3:24 Название трека 2
  ...

Требования:
  pip install mutagen       (быстро, без ffprobe)
  ИЛИ ffprobe в PATH        (часть ffmpeg)
"""

import sys
import os
import argparse
import subprocess
import json
from pathlib import Path


# ── Получить длительность через mutagen (предпочтительно) ─────────────────
def duration_mutagen(path: Path) -> float:
    try:
        from mutagen import File
        audio = File(str(path))
        if audio and audio.info:
            return float(audio.info.length)
    except ImportError:
        pass
    return None


# ── Получить длительность через ffprobe (запасной вариант) ────────────────
def duration_ffprobe(path: Path) -> float:
    try:
        cmd = [
            "ffprobe", "-v", "quiet",
            "-print_format", "json",
            "-show_streams",
            str(path)
        ]
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        data = json.loads(out)
        for stream in data.get("streams", []):
            d = stream.get("duration")
            if d:
                return float(d)
    except Exception:
        pass
    return None


def get_duration(path: Path) -> float:
    d = duration_mutagen(path)
    if d is None:
        d = duration_ffprobe(path)
    if d is None:
        raise RuntimeError(f"Не удалось определить длительность: {path}")
    return d


# ── Форматирование времени ────────────────────────────────────────────────
def fmt_time(seconds: float) -> str:
    total = int(round(seconds))
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


# ── Основная логика ───────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="YouTube tracklist timestamps")
    parser.add_argument("folder", help="Папка с MP3/M4A файлами")
    parser.add_argument("--names", help="Файл с именами треков (одно имя на строку)")
    parser.add_argument("--offset", type=float, default=0.0,
                        help="Начальный офсет в секундах (default: 0)")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        sys.exit(f"Папка не найдена: {folder}")

    # Поддерживаемые форматы
    extensions = {".mp3", ".m4a", ".wav", ".flac", ".ogg", ".aac"}
    files = sorted(
        [f for f in folder.iterdir() if f.suffix.lower() in extensions],
        key=lambda f: f.name
    )

    if not files:
        sys.exit(f"MP3/M4A файлы не найдены в {folder}")

    # Пользовательские имена треков
    custom_names = []
    if args.names:
        with open(args.names, encoding="utf-8") as fh:
            custom_names = [line.strip() for line in fh if line.strip()]
        if len(custom_names) < len(files):
            print(f"⚠️  Имён ({len(custom_names)}) меньше чем файлов ({len(files)}) — "
                  f"остаток заполним именем файла", file=sys.stderr)

    print(f"\n🎵 Трэклист — {len(files)} треков\n")
    print("─" * 50)

    cursor = args.offset
    total_dur = 0.0
    lines = []

    for i, f in enumerate(files):
        dur = get_duration(f)

        if custom_names and i < len(custom_names):
            name = custom_names[i]
        else:
            name = f.stem  # имя файла без расширения

        lines.append(f"{fmt_time(cursor)} {name}")
        print(f"  {fmt_time(cursor)}  {name}  ({fmt_time(dur)})")

        cursor += dur
        total_dur += dur

    print("─" * 50)
    print(f"  Итого: {fmt_time(total_dur)}\n")

    print("\n📋 Готово для YouTube Description:\n")
    print("🎵 Tracklist")
    for line in lines:
        print(line)
    print()


if __name__ == "__main__":
    main()
