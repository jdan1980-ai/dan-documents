# Анализ звука: строй (432/440), ноты и тональность, бинауральные биения, баланс частот, события и пульсации
# Запуск:  pwsh -File analyze_audio.ps1 -Path etalon.wav [-Start 0] [-Length 600]
# Длинный файл разбирается не целиком, а отрезком: по умолчанию первые 10 мин (-Length 0 = весь файл).
param(
    [Parameter(Mandatory)][string]$Path,
    [double]$Start = 0,      # начало отрезка, с
    [double]$Length = 600    # длина отрезка, с (0 = до конца файла)
)

Add-Type -TypeDefinition @"
using System;
using System.IO;
using System.Linq;
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

public static class Analyzer
{
    static readonly string[] Names = { "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#" };

    public static string Run(string path, double start, double length)
    {
        var sb = new StringBuilder();
        int sr, ch; float[][] x;
        using (var wav = new WavReader(path))
        {
            sr = wav.SampleRate; ch = wav.Channels;
            long f0 = Math.Max(0, Math.Min(wav.Frames, (long)(start * sr)));
            long cnt = length > 0 ? Math.Min(wav.Frames - f0, (long)(length * sr)) : wav.Frames - f0;
            if (cnt > int.MaxValue / 2) throw new Exception("Отрезок слишком длинный для анализа: задайте -Length меньше");
            x = new float[ch][];
            for (int c = 0; c < ch; c++) x[c] = new float[cnt];
            wav.Read(f0, (int)cnt, x);
            sb.AppendLine(string.Format("Файл: {0} Гц, каналов: {1}, {2} бит, длительность: {3:F1} с", sr, ch, wav.Bits, (double)wav.Frames / sr));
            if (cnt < wav.Frames)
                sb.AppendLine(string.Format("Разбираю отрезок {0:F1}–{1:F1} с (параметры -Start и -Length; -Length 0 = весь файл)",
                    (double)f0 / sr, (double)(f0 + cnt) / sr));
        }
        int n = x[0].Length;

        // --- Громкость и стерео
        for (int c = 0; c < ch; c++)
        {
            double s2 = 0, pk = 0;
            foreach (var v in x[c]) { s2 += v * v; pk = Math.Max(pk, Math.Abs(v)); }
            sb.AppendLine(string.Format("Канал {0}: RMS {1:F1} dBFS, пик {2:F1} dBFS", c == 0 ? "L" : "R",
                20 * Math.Log10(Math.Sqrt(s2 / n) + 1e-12), 20 * Math.Log10(pk + 1e-12)));
        }
        if (ch == 2)
        {
            double sl = 0, sr2 = 0, slr = 0;
            for (int i = 0; i < n; i++) { sl += x[0][i] * x[0][i]; sr2 += x[1][i] * x[1][i]; slr += x[0][i] * x[1][i]; }
            sb.AppendLine(string.Format("Корреляция L/R: {0:F2}  (1 = моно, ~0.3–0.7 = широкое стерео, <0.2 = очень широкое/раздельные каналы)",
                slr / Math.Sqrt(sl * sr2 + 1e-20)));
        }

        // --- Усреднённый спектр (FFT 65536, Ханн, перекрытие 50%)
        int N = 65536;
        double df = (double)sr / N;
        double[][] spec = new double[ch][];
        for (int c = 0; c < ch; c++) spec[c] = AvgSpectrum(x[c], N);
        double[] mono = new double[N / 2];
        for (int k = 0; k < N / 2; k++) for (int c = 0; c < ch; c++) mono[k] += spec[c][k] / ch;

        // Баланс частот
        double[] edges = { 20, 60, 250, 1000, 4000, 20000 };
        string[] bands = { "Суб-бас 20–60", "Бас 60–250", "Низ-середина 250–1000", "Середина 1–4 кГц", "Верх 4–20 кГц" };
        double tot = 0; double[] be = new double[5];
        for (int k = 1; k < N / 2; k++)
        {
            double f = k * df;
            for (int b = 0; b < 5; b++) if (f >= edges[b] && f < edges[b + 1]) { be[b] += mono[k]; tot += mono[k]; }
        }
        sb.AppendLine("\nБаланс частот (доля энергии):");
        for (int b = 0; b < 5; b++) sb.AppendLine(string.Format("  {0,-24} {1,5:F1}%", bands[b], 100 * be[b] / tot));
        // спектральный центроид
        double cw = 0, cs = 0;
        for (int k = 1; k < N / 2; k++) { double f = k * df; if (f > 20) { cw += f * mono[k]; cs += mono[k]; } }
        sb.AppendLine(string.Format("  Спектральный центроид: {0:F0} Гц (чем ниже, тем темнее звук)", cw / cs));

        // --- Пики спектра 30–3000 Гц
        var peaks = FindPeaks(mono, df, 30, 3000, 25);
        sb.AppendLine("\nСильнейшие тональные пики (30–3000 Гц):");
        sb.AppendLine("  Частота    Уровень  Нота   откл. от A440   откл. от A432");
        double maxDb = peaks.Count > 0 ? peaks.Max(p => p.Item2) : 0;
        foreach (var p in peaks.OrderBy(p => p.Item1))
        {
            sb.AppendLine(string.Format("  {0,8:F2}  {1,6:F1} дБ  {2,-5}  {3,7:+0;-0} цент   {4,7:+0;-0} цент",
                p.Item1, p.Item2 - maxDb, NoteName(p.Item1, 440), Cents(p.Item1, 440), Cents(p.Item1, 432)));
        }

        // --- Оценка строя: взвешенное круговое среднее отклонений (в центах) от сетки A440
        double sx = 0, sy = 0;
        foreach (var p in peaks)
        {
            double w = Math.Pow(10, (p.Item2 - maxDb) / 20);
            double ang = Cents(p.Item1, 440) / 100.0 * 2 * Math.PI;
            sx += w * Math.Cos(ang); sy += w * Math.Sin(ang);
        }
        double off = Math.Atan2(sy, sx) / (2 * Math.PI) * 100;
        double conf = Math.Sqrt(sx * sx + sy * sy) / peaks.Sum(p => Math.Pow(10, (p.Item2 - maxDb) / 20));
        double aRef = 440 * Math.Pow(2, off / 1200);
        sb.AppendLine(string.Format("\nОценка строя: A4 ≈ {0:F1} Гц (сдвиг {1:+0.0;-0.0} цента от 440; согласованность пиков {2:F2} из 1)",
            aRef, off, conf));
        sb.AppendLine("  Для справки: 432 Гц = −31.8 цента от 440.");

        // --- Хрома и тональность (относительно найденного строя)
        double[] chroma = new double[12];
        for (int k = 1; k < N / 2; k++)
        {
            double f = k * df; if (f < 50 || f > 2000) continue;
            int pc = (int)Math.Round(12 * Math.Log(f / aRef, 2));
            pc = ((pc % 12) + 12) % 12;
            chroma[pc] += mono[k];
        }
        double cm = chroma.Max();
        sb.AppendLine("\nЭнергия по нотам (хрома, без учёта октавы):");
        for (int i = 0; i < 12; i++)
            sb.AppendLine(string.Format("  {0,-3} {1}", Names[i], new string('#', (int)Math.Round(30 * chroma[i] / cm))));
        sb.AppendLine("  Вероятная тональность: " + GuessKey(chroma));

        // --- Бинауральные биения: тон в L без пары в R на той же частоте, но с соседом на 1–40 Гц
        if (ch == 2)
        {
            sb.AppendLine("\nПоиск бинауральных биений (разные частоты в L и R):");
            var pl = FindPeaks(spec[0], df, 40, 1500, 30);
            var pr = FindPeaks(spec[1], df, 40, 1500, 30);
            double mL = pl.Max(p => p.Item2), mR = pr.Max(p => p.Item2);
            int found = 0;
            foreach (var a in pl)
            {
                if (a.Item2 - mL < -30) continue;
                bool same = pr.Any(b => Math.Abs(b.Item1 - a.Item1) < 0.5);
                if (same) continue;
                foreach (var b in pr)
                {
                    double d = Math.Abs(b.Item1 - a.Item1);
                    if (d >= 0.5 && d <= 40 && b.Item2 - mR > -30 && !pl.Any(q => Math.Abs(q.Item1 - b.Item1) < 0.5))
                    {
                        sb.AppendLine(string.Format("  L {0:F2} Гц  /  R {1:F2} Гц  →  биение {2:F2} Гц ({3})",
                            a.Item1, b.Item1, d, Wave(d)));
                        found++;
                    }
                }
            }
            if (found == 0) sb.AppendLine("  Явных бинауральных пар не найдено (тоны в L и R совпадают).");

            // Энергия разностного сигнала L-R по полосам — подсказка, где каналы различаются
            double dl = 0, ds = 0;
            for (int i = 0; i < n; i++) { double m = x[0][i] + x[1][i], s = x[0][i] - x[1][i]; dl += m * m; ds += s * s; }
            sb.AppendLine(string.Format("  Доля энергии Side (L−R) к Mid (L+R): {0:F2}", ds / (dl + 1e-20)));
        }

        // --- Огибающая: события (атаки нот) и периодические пульсации
        int hop = sr / 25; // 40 мс — длиннее периода самых низких нот, иначе колебания баса выглядят как "атаки"
        int frames = n / hop;
        double[] env = new double[frames];
        for (int fr = 0; fr < frames; fr++)
        {
            double s = 0;
            for (int i = fr * hop; i < (fr + 1) * hop; i++) for (int c = 0; c < ch; c++) s += x[c][i] * x[c][i];
            env[fr] = Math.Sqrt(s / (hop * ch));
        }
        // атаки: рост уровня > 3 дБ за 80 мс, не чаще раза в 0.5 с
        int onsets = 0; int last = -1000;
        var onsetTimes = new List<double>();
        for (int fr = 2; fr < frames; fr++)
        {
            double now = 20 * Math.Log10(env[fr] + 1e-9), before = 20 * Math.Log10(env[fr - 2] + 1e-9);
            if (now - before > 3 && fr - last > 12) { onsets++; last = fr; onsetTimes.Add(fr / 25.0); }
        }
        sb.AppendLine(string.Format("\nЗаметные атаки (новые ноты/удары): {0} шт., ≈ {1:F1} в минуту", onsets, onsets / ((double)n / sr / 60)));
        if (onsetTimes.Count > 1)
        {
            var gaps = onsetTimes.Zip(onsetTimes.Skip(1), (a, b) => b - a).OrderBy(g => g).ToList();
            sb.AppendLine(string.Format("  Интервал между атаками: медиана {0:F1} с, от {1:F1} до {2:F1} с",
                gaps[gaps.Count / 2], gaps.First(), gaps.Last()));
        }

        // пульсации: спектр огибающей 0.05–12 Гц
        double mean = env.Average();
        int M = 1; while (M < frames) M <<= 1;
        double[] re = new double[M], im = new double[M];
        for (int i = 0; i < frames; i++) re[i] = (env[i] - mean) * Hann(i, frames);
        FFT(re, im);
        double edf = 25.0 / M;
        var ep = new List<Tuple<double, double>>();
        for (int k = 2; k < M / 2 - 1; k++)
        {
            double f = k * edf; if (f < 0.05 || f > 12) continue;
            double m0 = re[k] * re[k] + im[k] * im[k];
            double m1 = re[k - 1] * re[k - 1] + im[k - 1] * im[k - 1], m2 = re[k + 1] * re[k + 1] + im[k + 1] * im[k + 1];
            if (m0 > m1 && m0 > m2) ep.Add(Tuple.Create(f, m0));
        }
        sb.AppendLine("  Сильнейшие периодичности громкости (пульсации/«дыхание»):");
        foreach (var p in ep.OrderByDescending(p => p.Item2).Take(5))
            sb.AppendLine(string.Format("    {0:F2} Гц  (период {1:F1} с){2}", p.Item1, 1 / p.Item1,
                p.Item1 >= 1 ? "  ← возможны изохронные импульсы, " + Wave(p.Item1) : ""));

        return sb.ToString();
    }

    static string Wave(double f)
    {
        if (f < 4) return "дельта";
        if (f < 8) return "тета";
        if (f < 13) return "альфа";
        if (f < 30) return "бета";
        return "гамма";
    }

    static double Cents(double f, double a)
    {
        double c = 1200 * Math.Log(f / a, 2);
        c = c - 100 * Math.Round(c / 100);
        return c;
    }

    static string NoteName(double f, double a)
    {
        int semi = (int)Math.Round(12 * Math.Log(f / a, 2));
        int pc = ((semi % 12) + 12) % 12;
        int midi = 69 + semi;
        return Names[pc] + (midi / 12 - 1);
    }

    static string GuessKey(double[] chroma)
    {
        // Профили Крумхансла (от C); наша хрома начинается с A, поэтому сдвигаем
        double[] maj = { 6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88 };
        double[] min = { 6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17 };
        string best = ""; double bs = double.MinValue; string second = ""; double ss = double.MinValue;
        for (int root = 0; root < 12; root++)
            for (int mode = 0; mode < 2; mode++)
            {
                var prof = mode == 0 ? maj : min;
                double[] p = new double[12];
                for (int i = 0; i < 12; i++) p[(root + i) % 12] = prof[i];
                double r = Corr(chroma, p);
                string name = Names[root] + (mode == 0 ? " мажор" : " минор");
                if (r > bs) { second = best; ss = bs; best = name; bs = r; }
                else if (r > ss) { second = name; ss = r; }
            }
        return string.Format("{0} (r={1:F2}), второй вариант: {2} (r={3:F2})", best, bs, second, ss);
    }

    static double Corr(double[] a, double[] b)
    {
        double ma = a.Average(), mb = b.Average(), s = 0, sa = 0, sb = 0;
        for (int i = 0; i < a.Length; i++) { s += (a[i] - ma) * (b[i] - mb); sa += (a[i] - ma) * (a[i] - ma); sb += (b[i] - mb) * (b[i] - mb); }
        return s / Math.Sqrt(sa * sb + 1e-30);
    }

    static List<Tuple<double, double>> FindPeaks(double[] s, double df, double fmin, double fmax, int count)
    {
        var res = new List<Tuple<double, double>>();
        int k0 = Math.Max(3, (int)(fmin / df)), k1 = Math.Min(s.Length - 4, (int)(fmax / df));
        for (int k = k0; k <= k1; k++)
        {
            bool isMax = true;
            for (int j = -3; j <= 3; j++) if (j != 0 && s[k + j] >= s[k]) { isMax = false; break; }
            if (!isMax) continue;
            // выступ над локальным фоном (±40 бинов) минимум 6 дБ
            double bg = 0; int cnt = 0;
            for (int j = -40; j <= 40; j++) { int q = k + j; if (q > 0 && q < s.Length && Math.Abs(j) > 4) { bg += s[q]; cnt++; } }
            bg /= cnt;
            if (10 * Math.Log10(s[k] / (bg + 1e-30)) < 6) continue;
            double a = Math.Log(s[k - 1] + 1e-30), b = Math.Log(s[k] + 1e-30), c = Math.Log(s[k + 1] + 1e-30);
            double d = 0.5 * (a - c) / (a - 2 * b + c);
            res.Add(Tuple.Create((k + d) * df, 10 * Math.Log10(s[k] + 1e-30)));
        }
        return res.OrderByDescending(p => p.Item2).Take(count).ToList();
    }

    static double Hann(int i, int n) { return 0.5 - 0.5 * Math.Cos(2 * Math.PI * i / (n - 1)); }

    static double[] AvgSpectrum(float[] x, int N)
    {
        double[] acc = new double[N / 2];
        double[] re = new double[N], im = new double[N];
        int frames = 0;
        for (int start = 0; start + N <= x.Length; start += N / 2)
        {
            for (int i = 0; i < N; i++) { re[i] = x[start + i] * Hann(i, N); im[i] = 0; }
            FFT(re, im);
            for (int k = 0; k < N / 2; k++) acc[k] += re[k] * re[k] + im[k] * im[k];
            frames++;
        }
        for (int k = 0; k < N / 2; k++) acc[k] /= Math.Max(1, frames);
        return acc;
    }

    static void FFT(double[] re, double[] im)
    {
        int n = re.Length;
        for (int i = 1, j = 0; i < n; i++)
        {
            int bit = n >> 1;
            for (; (j & bit) != 0; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) { double t = re[i]; re[i] = re[j]; re[j] = t; t = im[i]; im[i] = im[j]; im[j] = t; }
        }
        for (int len = 2; len <= n; len <<= 1)
        {
            double ang = -2 * Math.PI / len, wr = Math.Cos(ang), wi = Math.Sin(ang);
            for (int i = 0; i < n; i += len)
            {
                double cr = 1, ci = 0;
                for (int k = 0; k < len / 2; k++)
                {
                    int a = i + k, b = i + k + len / 2;
                    double tr = re[b] * cr - im[b] * ci, ti = re[b] * ci + im[b] * cr;
                    re[b] = re[a] - tr; im[b] = im[a] - ti; re[a] += tr; im[a] += ti;
                    double ncr = cr * wr - ci * wi; ci = cr * wi + ci * wr; cr = ncr;
                }
            }
        }
    }
}
"@

[Analyzer]::Run((Resolve-Path $Path).Path, $Start, $Length)
