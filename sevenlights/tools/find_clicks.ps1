# Поиск щелчков: резкие скачки второй разности сигнала относительно локального фона
# Запуск:  pwsh -File find_clicks.ps1 -Path track.wav
# Файл читается кусками, поэтому подходят и многочасовые треки (WAV и RF64, 16/24/32 бит, float32).
param([Parameter(Mandatory)][string]$Path)

Add-Type -TypeDefinition @"
using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

// Чтение WAV: RIFF и RF64 (больше 4 ГБ), PCM 16/24/32 бит и float32.
// Чанки fmt/data ищутся по заголовкам, а не по фиксированному смещению 44 байта (у Audacity бывают LIST и др.)
public sealed class WavReader : IDisposable
{
    public int SampleRate, Channels, Bits, Format;
    public long Frames;
    long dataStart; int blockAlign; FileStream fs; byte[] buf = new byte[0];

    public WavReader(string path)
    {
        fs = new FileStream(path, FileMode.Open, FileAccess.Read, FileShare.Read, 1 << 20);
        var br = new BinaryReader(fs);
        string riff = Id(br); br.ReadUInt32();
        if ((riff != "RIFF" && riff != "RF64") || Id(br) != "WAVE") throw new Exception("Не WAV-файл");
        long ds64Data = -1; bool fmt = false;
        while (fs.Position + 8 <= fs.Length)
        {
            string id = Id(br); uint size = br.ReadUInt32(); long body = fs.Position;
            if (id == "ds64") { br.ReadInt64(); ds64Data = br.ReadInt64(); }
            else if (id == "fmt ")
            {
                Format = br.ReadUInt16(); Channels = br.ReadInt16(); SampleRate = br.ReadInt32(); br.ReadInt32(); br.ReadInt16(); Bits = br.ReadInt16();
                if (Format == 0xFFFE && size >= 26) { fs.Position = body + 24; Format = br.ReadUInt16(); }   // WAVE_FORMAT_EXTENSIBLE
                fmt = true;
            }
            else if (id == "data")
            {
                if (!fmt) throw new Exception("Чанк data раньше fmt");
                long len = size == uint.MaxValue && ds64Data >= 0 ? ds64Data : size;
                if (size == uint.MaxValue && ds64Data < 0 || size == 0) len = fs.Length - body;   // размер не записан
                len = Math.Min(len, fs.Length - body);                                          // файл обрезан
                if (Bits != 16 && Bits != 24 && Bits != 32 || Format == 3 && Bits != 32 || Format != 1 && Format != 3)
                    throw new Exception("Неподдерживаемый формат: код " + Format + ", " + Bits + " бит");
                blockAlign = Bits / 8 * Channels;
                dataStart = body; Frames = len / blockAlign;
                return;
            }
            fs.Position = body + size + (size & 1);
        }
        throw new Exception("В файле нет звуковых данных (чанк data)");
    }

    static string Id(BinaryReader br) { return Encoding.ASCII.GetString(br.ReadBytes(4)); }

    // Читает count кадров начиная с frame0 в dst[канал][0..]; возвращает число прочитанных кадров
    public int Read(long frame0, int count, float[][] dst)
    {
        count = (int)Math.Max(0, Math.Min(count, Frames - frame0));
        int need = count * blockAlign;
        if (buf.Length < need) buf = new byte[need];
        fs.Position = dataStart + frame0 * blockAlign;
        int got = 0;
        while (got < need) { int r = fs.Read(buf, got, need - got); if (r <= 0) break; got += r; }
        count = got / blockAlign;
        int bps = Bits / 8, p = 0;
        for (int i = 0; i < count; i++)
            for (int c = 0; c < Channels; c++, p += bps)
            {
                float v;
                if (Format == 3) v = BitConverter.ToSingle(buf, p);
                else if (Bits == 16) v = BitConverter.ToInt16(buf, p) / 32768f;
                else if (Bits == 24) v = (buf[p] | (buf[p + 1] << 8) | ((sbyte)buf[p + 2] << 16)) / 8388608f;
                else v = BitConverter.ToInt32(buf, p) / 2147483648f;
                dst[c][i] = v;
            }
        return count;
    }

    public void Dispose() { fs.Dispose(); }
}

public static class ClickFinder
{
    public static string Run(string path)
    {
        var times = new List<double>();
        using (var wav = new WavReader(path))
        {
            int sr = wav.SampleRate, ch = wav.Channels;
            int win = sr / 20, half = win / 2;      // фон: среднее по окну 50 мс с центром в проверяемом сэмпле
            const int Chunk = 1 << 16;
            var x = new float[ch][];
            for (int c = 0; c < ch; c++) x[c] = new float[Chunk];
            // Для каждого канала: два предыдущих сэмпла, кольцо последних win значений второй разности и их сумма
            var p1 = new double[ch]; var p2 = new double[ch];
            var ring = new double[ch][]; var acc = new double[ch]; var last = new long[ch];
            for (int c = 0; c < ch; c++) { ring[c] = new double[win]; last[c] = -sr; }

            for (long f0 = 0; f0 < wav.Frames; f0 += Chunk)
            {
                int cnt = wav.Read(f0, Chunk, x);
                if (cnt == 0) break;
                for (int c = 0; c < ch; c++)
                {
                    double[] rg = ring[c];
                    for (int i = 0; i < cnt; i++)
                    {
                        long m = f0 + i;
                        double s = x[c][i];
                        double d = m >= 2 ? Math.Abs(s - 2 * p1[c] + p2[c]) : 0;
                        p2[c] = p1[c]; p1[c] = s;
                        int slot = (int)(m % win);
                        acc[c] += d - rg[slot]; rg[slot] = d;
                        if (m % 1000000 == 0) { double a = 0; foreach (var v in rg) a += v; acc[c] = a; }   // без накопления ошибки
                        if (m < win - 1) continue;
                        // Окно [m − win + 1, m] целиком в кольце; проверяем его центр
                        long k = m - win + 1 + half;
                        double dk = rg[(int)(k % win)], bg = acc[c] / win;
                        if (dk > 12 * bg + 2e-4 && k - last[c] > sr / 4) { times.Add((double)k / sr); last[c] = k; }
                    }
                }
            }
        }
        times.Sort();
        var sb = new StringBuilder();
        sb.AppendLine("Найдено щелчков: " + times.Count);
        foreach (var t in times) sb.AppendLine(string.Format("  {0:F3} с", t));
        return sb.ToString();
    }
}
"@

[ClickFinder]::Run((Resolve-Path $Path).Path)
