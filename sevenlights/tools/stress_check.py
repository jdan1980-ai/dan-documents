"""Проверочное видео для Content ID: каждый трек звучит N раз подряд (по умолчанию 3) — Content ID ловит
совпадение не в каждом повторе, а так шанс поймать «грязный» трек до сборки 3 часов намного выше.

Картинка — одна (обложка канала), видео почти ничего не весит. Рядом пишется таблица `<out>.txt`:
трек → интервалы. По тайм-коду заявки из YouTube Студии сразу видно, какой трек выкинуть.

  python stress_check.py --in a.mp3,b.mp3,c.mp3 --image thumb.jpg --out check.mp4 [--repeats 3]
"""
import argparse
import os
import subprocess
import tempfile


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                                capture_output=True, text=True, check=True).stdout.strip())


def ts(s):
    s = int(round(s))
    return f'{s // 3600}:{s // 60 % 60:02d}:{s % 60:02d}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='inp', required=True, help='треки через запятую')
    ap.add_argument('--image', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--repeats', type=int, default=3)
    ap.add_argument('--label', help='крупная надпись на картинке, например "ВИДЕО 6 · ПРОВЕРКА 2" — чтобы в Студии было видно, что это')
    a = ap.parse_args()
    files = [f.strip() for f in a.inp.split(',') if f.strip()]
    rows = []
    t = 0.0
    with tempfile.TemporaryDirectory() as tmp:
        image = a.image
        if a.label:
            from PIL import Image, ImageDraw, ImageFont
            im = Image.open(a.image).convert('RGB').resize((1280, 720))
            d = ImageDraw.Draw(im)
            try:
                f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 64)
            except OSError:
                f = ImageFont.load_default()
            d.rectangle([0, 600, 1280, 720], fill=(160, 0, 0))
            d.text((640, 660), a.label, font=f, fill='white', anchor='mm')
            image = os.path.join(tmp, 'label.jpg'); im.save(image, quality=92)
        lst = os.path.join(tmp, 'list.txt')
        with open(lst, 'w') as f:
            for p in files:
                d = dur(p)
                rows.append((os.path.basename(p), [(t + k * d, t + (k + 1) * d) for k in range(a.repeats)]))
                for _ in range(a.repeats):
                    f.write("file '" + os.path.abspath(p).replace("'", "'\\''") + "'\n")
                t += a.repeats * d
        audio = os.path.join(tmp, 'a.m4a')
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst,
                        '-c:a', 'aac', '-b:a', '256k', audio], check=True)
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-framerate', '1', '-i', image, '-i', audio,
                        '-vf', 'scale=1280:720,setsar=1,format=yuv420p', '-c:v', 'libx264', '-tune', 'stillimage',
                        '-r', '1', '-c:a', 'copy', '-shortest', '-movflags', '+faststart', a.out], check=True)
    lines = [f'Проверочное видео: {os.path.basename(a.out)} — {ts(t)}, каждый трек × {a.repeats}', '']
    for name, iv in rows:
        lines.append(f'{name:40s} ' + '  '.join(f'{ts(s)}–{ts(e)}' for s, e in iv))
    txt = os.path.splitext(a.out)[0] + '.txt'
    open(txt, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))
    print(f'\nТаблица: {txt}')


if __name__ == '__main__':
    main()
