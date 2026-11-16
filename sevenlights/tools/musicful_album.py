"""Альбом из треков Musicful API: N запросов по одному промпту → опрос статуса → скачивание MP3.

Один запрос /v1/music/generate (action=auto) даёт 2 трека. Проверено 12.11.2026: MFV3.0, instrumental=1 —
2 трека по ~3:12–3:14 (MP3 128 кбит/с), списано 6 единиц с ключа (3 на трек), генерация ~1.5–2 мин.

Ключ API в коде и в переменных НЕ хранится: в облачной сессии его подставляет сетевой прокси для api.musicful.ai,
поэтому в заголовке уходит заглушка. Локально: задайте переменную MUSICFUL_API_KEY.
Нужные хосты в сети: api.musicful.ai (запросы), files.musicful.ai (скачивание).

  python musicful_album.py --prompt-file prompt.txt --requests 3 --out album4/        # 6 треков
  python musicful_album.py --ids 1605128,1605129 --out album4/                         # только скачать готовые
  python musicful_album.py --balance                                                    # остаток единиц
"""
import argparse
import json
import os
import time
import urllib.request

API = 'https://api.musicful.ai'
KEY = os.environ.get('MUSICFUL_API_KEY', 'proxy-injected')


def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method, headers={'x-api-key': KEY, 'Content-Type': 'application/json'},
                                 data=json.dumps(body).encode() if body is not None else None)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def balance():
    return call('GET', '/v1/get_api_key_info')['key_music_counts']


def generate(prompt, mv, instrumental=1):
    d = call('POST', '/v1/music/generate', {'action': 'auto', 'style': prompt, 'mv': mv, 'instrumental': instrumental})
    if d.get('status') != 200:
        raise RuntimeError(f'generate: {d}')
    return d['data']['ids']


def wait(ids, timeout=900, every=20):
    """Ждём, пока у каждого трека будет длительность > 0 (статус 0) или ошибка. Статусы: 4 — в работе, 2 — черновик, 0 — готово."""
    t0 = time.time()
    while True:
        songs = call('GET', '/v1/music/tasks?ids=' + ','.join(ids))['data']
        if all((s.get('duration') or 0) > 0 or s.get('fail_code') for s in songs):
            return songs
        if time.time() - t0 > timeout:
            raise TimeoutError('генерация не закончилась: ' + ' '.join(f"{s['id']}:{s['status']}" for s in songs))
        time.sleep(every)


def download(songs, out):
    os.makedirs(out, exist_ok=True)
    got = []
    for s in songs:
        if s.get('fail_code') or not s.get('audio_url'):
            print(f"  {s['id']}: ошибка {s.get('fail_code')} {s.get('fail_reason')}")
            continue
        path = os.path.join(out, f"{s['id']}.mp3")
        urllib.request.urlretrieve(s['audio_url'], path)
        got.append(path)
        print(f"  {s['id']}: {s['duration'] / 1000:.0f} с, «{s.get('title') or ''}» → {path}")
    return got


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--prompt-file')
    ap.add_argument('--requests', type=int, default=1, help='число запросов (каждый = 2 трека)')
    ap.add_argument('--mv', default='MFV3.0')
    ap.add_argument('--ids', help='скачать уже сгенерированные: id через запятую')
    ap.add_argument('--out', default='album')
    ap.add_argument('--balance', action='store_true')
    a = ap.parse_args()

    if a.balance:
        print('остаток:', balance())
        return
    ids = a.ids.split(',') if a.ids else []
    if not ids:
        prompt = open(a.prompt_file, encoding='utf-8').read().strip()
        print(f'остаток до: {balance()}')
        for i in range(a.requests):
            new = generate(prompt, a.mv)
            print(f'запрос {i + 1}/{a.requests}: {new}')
            ids += new
        with open(os.path.join(a.out if os.path.isdir(a.out) else '.', 'musicful_ids.txt'), 'a') as f:
            f.write(','.join(ids) + '\n')
    songs = []
    for k in range(0, len(ids), 10):
        songs += wait(ids[k:k + 10])
    download(songs, a.out)
    print(f'остаток после: {balance()}')


if __name__ == '__main__':
    main()
