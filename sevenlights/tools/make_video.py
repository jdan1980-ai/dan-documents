"""Готовое видео для YouTube из петли + длинного звука + оверлея — без CapCut и без перекодирования всех 3 часов.

Идея: видео — это короткая бесшовная петля (make_loop.py, 8 с). Перекодировать 3 часа незачем:
  1. петля один раз перекодируется в «склеиваемый» вид (H.264 1080p30, ключевой кадр в начале каждой петли);
  2. интро (2 круга петли = 16 с) кодируется с оверлеем «Welcome to Seven Lights» (появление 2 с, исчезновение к 11 с);
  3. интро + петля × N склеиваются БЕЗ перекодирования (concat, -c copy), звук FLAC → AAC 320k.
Сборка 3-часового видео занимает минуты, а не часы.

  python make_video.py --loop loop.mp4 --audio album_3h.flac --overlay overlay_intro_welcome.png --out video.mp4
  python make_video.py --loop loop.mp4 --audio album_3h.flac --out video.mp4          # без оверлея

Нужен ffmpeg (ffprobe) в PATH.
"""
import argparse
import math
import os
import shutil
import subprocess
import tempfile
import time

FPS = 30


def probe(path, entry, stream=None):
    cmd = ['ffprobe', '-v', 'error']
    if stream:
        cmd += ['-select_streams', stream]
    cmd += ['-show_entries', entry, '-of', 'csv=p=0', path]
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout.strip().splitlines()[0]


def run(cmd):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + cmd, check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--loop', required=True, help='бесшовная петля (mp4)')
    ap.add_argument('--audio', required=True, help='длинный звук (flac/wav/mp3)')
    ap.add_argument('--overlay', help='прозрачный PNG 1920x1080 для начала видео')
    ap.add_argument('--out', required=True)
    ap.add_argument('--crf', type=int, default=20, help='качество петли (меньше — лучше и тяжелее)')
    ap.add_argument('--fade-in-at', type=float, default=2.0)
    ap.add_argument('--fade-in', type=float, default=1.5)
    ap.add_argument('--fade-out-at', type=float, default=8.5)
    ap.add_argument('--fade-out', type=float, default=2.0)
    a = ap.parse_args()

    t0 = time.time()
    audio_dur = float(probe(a.audio, 'format=duration'))
    tmp = tempfile.mkdtemp(prefix='makevideo_')
    try:
        # 1. Петля в склеиваемом виде: ровно целое число кадров, один ключевой кадр в начале
        loop_dur = float(probe(a.loop, 'format=duration'))
        frames = max(1, round(loop_dur * FPS))
        enc = ['-c:v', 'libx264', '-preset', 'medium', '-crf', str(a.crf), '-pix_fmt', 'yuv420p', '-r', str(FPS),
               '-g', str(frames), '-keyint_min', str(frames), '-sc_threshold', '0', '-profile:v', 'high', '-level', '4.1',
               '-video_track_timescale', '15360', '-an']
        loop_ready = os.path.join(tmp, 'loop.mp4')
        run(['-i', a.loop, '-vf', f'scale=1920:1080,setsar=1,fps={FPS}', '-frames:v', str(frames)] + enc + [loop_ready])

        # 2. Интро с оверлеем: целое число кругов петли, чтобы склейка с петлёй была бесшовной
        intro_loops = max(1, math.ceil((a.fade_out_at + a.fade_out + 0.5) * FPS / frames)) if a.overlay else 0
        parts = []
        if a.overlay:
            intro = os.path.join(tmp, 'intro.mp4')
            n = intro_loops * frames
            flt = (f'[0:v]scale=1920:1080,setsar=1,fps={FPS}[bg];'
                   f'[1:v]format=rgba,fade=t=in:st={a.fade_in_at}:d={a.fade_in}:alpha=1,'
                   f'fade=t=out:st={a.fade_out_at}:d={a.fade_out}:alpha=1[o];[bg][o]overlay=0:0:eof_action=pass[v]')
            run(['-stream_loop', str(intro_loops - 1), '-i', loop_ready, '-loop', '1', '-t', str(n / FPS), '-i', a.overlay,
                 '-filter_complex', flt, '-map', '[v]', '-frames:v', str(n)] + enc + [intro])
            parts.append(intro)
        intro_dur = intro_loops * frames / FPS
        reps = max(0, math.ceil((audio_dur - intro_dur) / (frames / FPS)))
        lst = os.path.join(tmp, 'list.txt')
        with open(lst, 'w') as f:
            for p in parts + [loop_ready] * reps:
                f.write(f"file '{p}'\n")

        # 3. Склейка без перекодирования + звук
        run(['-f', 'concat', '-safe', '0', '-i', lst, '-i', a.audio, '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
             '-c:a', 'aac', '-b:a', '320k', '-t', f'{audio_dur:.3f}', '-movflags', '+faststart', a.out])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    dur = float(probe(a.out, 'format=duration'))
    print(f'Готово: {a.out} — {dur / 3600:.2f} ч, {os.path.getsize(a.out) / 2 ** 30:.2f} ГБ, за {time.time() - t0:.0f} с')


if __name__ == '__main__':
    main()
