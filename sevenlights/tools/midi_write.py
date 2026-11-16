"""Минимальный писатель MIDI (SMF формат 1) без зависимостей + читатель для проверки.

Темп 60 BPM: 1 доля = 1 секунда, 480 тиков на долю — время в секундах переводится в тики умножением на 480.
  from midi_write import write_midi
  write_midi('out.mid', {'Piano': (0, [(60, 1.0, 2.0, 80), ...])})   # дорожка: (программа GM, [(нота, старт_с, длит_с, velocity)])
"""
import struct

TPQ = 480


def _vlq(n):
    out = [n & 0x7F]
    n >>= 7
    while n:
        out.append((n & 0x7F) | 0x80)
        n >>= 7
    return bytes(reversed(out))


def _track(events):
    data = b''
    last = 0
    for tick, ev in sorted(events, key=lambda e: (e[0], e[1][0] & 0xF0 == 0x90)):   # note off раньше note on в один тик
        data += _vlq(tick - last) + ev
        last = tick
    data += _vlq(0) + b'\xff\x2f\x00'
    return b'MTrk' + struct.pack('>I', len(data)) + data


def write_midi(path, tracks, bpm=60):
    """tracks: {имя: (program, [(note, start_s, dur_s, velocity)])}. Каналы 0..15, 9 (ударные) пропускается."""
    tempo = int(60_000_000 / bpm)
    chunks = [_track([(0, b'\xff\x51\x03' + tempo.to_bytes(3, 'big')),
                      (0, b'\xff\x03' + _vlq(len(b'Seven Lights')) + b'Seven Lights')])]
    ch = 0
    for name, (program, notes) in tracks.items():
        if ch == 9:
            ch += 1
        nm = name.encode('utf-8')
        ev = [(0, b'\xff\x03' + _vlq(len(nm)) + nm), (0, bytes([0xC0 | ch, program & 0x7F]))]
        for note, start, dur, vel in notes:
            n = int(round(note))
            if not 0 <= n <= 127:
                continue
            t0 = max(0, int(round(start * TPQ * bpm / 60)))
            t1 = max(t0 + 1, int(round((start + dur) * TPQ * bpm / 60)))
            v = int(max(1, min(127, vel)))
            ev.append((t0, bytes([0x90 | ch, n, v])))
            ev.append((t1, bytes([0x80 | ch, n, 0])))
        chunks.append(_track(ev))
        ch += 1
    hdr = b'MThd' + struct.pack('>IHHH', 6, 1, len(chunks), TPQ)
    with open(path, 'wb') as f:
        f.write(hdr + b''.join(chunks))


def read_summary(path):
    """Для проверки: {имя дорожки: (число нот, последний тик)}."""
    b = open(path, 'rb').read()
    assert b[:4] == b'MThd'
    ntr = struct.unpack('>H', b[10:12])[0]
    pos = 14
    out = {}
    for _ in range(ntr):
        assert b[pos:pos + 4] == b'MTrk'
        ln = struct.unpack('>I', b[pos + 4:pos + 8])[0]
        d = b[pos + 8:pos + 8 + ln]
        pos += 8 + ln
        i = 0; tick = 0; name = ''; notes = 0; status = 0
        while i < len(d):
            v = 0
            while True:
                c = d[i]; i += 1; v = (v << 7) | (c & 0x7F)
                if not c & 0x80:
                    break
            tick += v
            if d[i] == 0xFF:
                typ = d[i + 1]; i += 2
                L = 0
                while True:
                    c = d[i]; i += 1; L = (L << 7) | (c & 0x7F)
                    if not c & 0x80:
                        break
                if typ == 0x03:
                    name = d[i:i + L].decode('utf-8', 'replace')
                i += L
                continue
            status = d[i]; i += 1
            if status & 0xF0 in (0xC0, 0xD0):
                i += 1
            else:
                if status & 0xF0 == 0x90 and d[i + 1] > 0:
                    notes += 1
                i += 2
        out[name or f'track{len(out)}'] = (notes, tick)
    return out
