# Космический амбиент в строе A = 432 Гц (без вокала, для сна и медитации)
# Запуск:  pwsh -File space_ambient_432.ps1 [-Seconds 150] [-Seed 7] [-Out space_ambient_432.wav] [-NoStars] [-NoBowls] [-NoWhales] [-NoPiano] [-NoBinaural] [-Dark] [-Calm]
#          [-PianoGain 1.0] [-PianoMin 3.5] [-PianoMax 7.5] [-Bright] [-KeyC]
param(
    [double]$Seconds = 150,
    [int]$Seed = 7,
    [string]$Out = "space_ambient_432.wav",
    [switch]$NoStars,
    [switch]$NoBowls,
    [switch]$NoWhales,
    [switch]$NoPiano,
    [switch]$NoBinaural,
    [switch]$Dark,         # тёмный вариант: ля-бемоль мажор, басовая линия, срез верхов (по анализу эталона)
    [switch]$Calm,         # спокойный (на основе тёмного): без суб-баса и диссонансов, больше воздуха, тета 5 Гц
    [double]$PianoGain = 1.0,   # громкость фортепиано (1 = как в v7a)
    [double]$PianoMin = 3.5,    # пауза между нотами фортепиано, от и до (с)
    [double]$PianoMax = 7.5,
    [switch]$Bright,       # чуть светлее: ярче пэды, верх открыт до ~3.5 кГц
    [switch]$KeyC          # до мажор по etalon1: аккорды F → C → Am → G, тёплый бас, тета 5 Гц (без -Dark/-Calm)
)

Add-Type -TypeDefinition @"
using System;
using System.IO;

public static class AmbientSynth
{
    const int SR = 44100;
    const double TAU = Math.PI * 2;

    // Тонкая настройка (задаётся из параметров скрипта)
    public static double PianoGain = 1.0, PianoMin = 3.5, PianoMax = 7.5;
    public static bool Bright = false;

    public static void Render(string path, double seconds, int seed, bool stars_on, bool bowls_on, bool whales_on, bool piano_on, bool binaural_on, bool dark, bool calm, bool keyC)
    {
        int n = (int)(seconds * SR);
        double[] L = new double[n], R = new double[n];
        var rnd = new Random(seed);
        double A4 = 432.0;
        Func<double, double> note = s => A4 * Math.Pow(2, s / 12.0);

        // 1. Низкий дрон
        if (!dark && !keyC)
        {
            // A1 (54 Гц) и A2 (108 Гц), медленное "дыхание"
            for (int i = 0; i < n; i++)
            {
                double t = (double)i / SR;
                double breath = 0.8 + 0.2 * Math.Sin(TAU * t / 40.0);
                double s = breath * (0.30 * Math.Sin(TAU * 54.0 * t) + 0.15 * Math.Sin(TAU * 108.0 * t + 1.3));
                L[i] += s; R[i] += s;
            }
        }
        else
        {
            // Медленная басовая линия Ab1 → Bb1 → C2 → G1 (как у эталона), каждая нота 16 с.
            // Ноты сменяются плавным перекрёстным затуханием за 5 с — без скольжения высоты.
            // спокойный вариант: только устойчивые ноты Ab2 ↔ Eb2, на октаву выше — без давящего суб-баса
            // до мажор (по etalon1): F2 → C2 → A1 → G2, синхронно со сменой аккордов пэдов
            double[] bass = keyC ? new double[] { 8, 3, 0, 10 }
                          : calm ? new double[] { 11, 6 } : new double[] { -1, 1, 3, -2 };   // полутоны от A1 = 54 Гц
            double seg = keyC ? ChordSeg : calm ? 20.0 : 16.0, xf = keyC ? ChordXf : calm ? 7.0 : 5.0;
            double fundLvl = keyC ? 0.45 : calm ? 0.35 : 0.40, octLvl = keyC ? 0.28 : calm ? 0.12 : 0.24;
            for (int i = 0; i < n; i++)
            {
                double t = (double)i / SR;
                double breath = 0.85 + 0.15 * Math.Sin(TAU * t / 12.0);   // "дыхание" ~12 с, как у эталона
                int j = (int)(t / seg);
                double s = 0;
                for (int q = j - 1; q <= j; q++)
                {
                    if (q < 0) continue;
                    double u = t - q * seg, env;
                    if (u < xf) env = 0.5 - 0.5 * Math.Cos(Math.PI * u / xf);
                    else if (u < seg) env = 1;
                    else if (u < seg + xf) env = 0.5 + 0.5 * Math.Cos(Math.PI * (u - seg) / xf);
                    else env = 0;
                    if (q == 0 && u < xf) env = 1;   // первая нота звучит сразу (общее появление трека и так плавное)
                    double f = 54.0 * Math.Pow(2, bass[q % bass.Length] / 12.0);
                    // Суб-бас умеренный: при 0.65 небольшие динамики/наушники хрипели ("как пластинка").
                    // Октава выше (0.24) несёт ноту на устройствах, которые не тянут 50 Гц.
                    s += env * (fundLvl * Math.Sin(TAU * f * t) + octLvl * Math.Sin(TAU * 2 * f * t + 1.3));
                }
                s *= breath;
                L[i] += s; R[i] += s;
            }
        }

        // 2. Тёплые пэды, по 3 расстроенных голоса на ноту
        // светлый вариант: Am7 (A2 E3 A3 C4 E4 G4); тёмный: Ab add9 (Ab2 Eb3 Ab3 Bb3 C4 Eb4)
        // спокойный: Bb поднят на октаву (Bb4), чтобы внизу не было близких "шершавых" нот
        double[] pad = calm ? new double[] { -25, -18, -13, -9, -6, 1 }
                     : dark ? new double[] { -25, -18, -13, -11, -9, -6 } : new double[] { -24, -17, -12, -9, -5, -2 };
        double briBase = (calm ? 0.20 : dark ? 0.15 : 0.30) + (Bright ? 0.05 : 0), briRange = calm ? 0.14 : dark ? 0.12 : 0.20;
        int harmonics = calm ? 5 : dark ? 4 : 6;
        if (keyC) ChordPads(L, R, seconds, rnd, note);
        else foreach (double semi in pad)
        {
            double f = note(semi);
            double ampPeriod = 25 + rnd.NextDouble() * 30, ampPhase = rnd.NextDouble() * TAU;
            double briPeriod = 30 + rnd.NextDouble() * 40, briPhase = rnd.NextDouble() * TAU;
            double level = semi < -14 ? (dark ? 0.06 : 0.10) : 0.07;
            for (int v = -1; v <= 1; v++)
            {
                double fv = f * Math.Pow(2, v * 5 / 1200.0);   // ±5 центов — мягкий хорус
                double panL = Math.Sqrt(0.5 - v * 0.3), panR = Math.Sqrt(0.5 + v * 0.3);
                double ph0 = rnd.NextDouble() * TAU;
                for (int i = 0; i < n; i++)
                {
                    double t = (double)i / SR;
                    double a = 0.5 + 0.5 * Math.Sin(TAU * t / ampPeriod + ampPhase);
                    a = 0.25 + 0.75 * a * a;
                    double bright = briBase + briRange * (0.5 + 0.5 * Math.Sin(TAU * t / briPeriod + briPhase));
                    double sum = 0, w = 1;
                    for (int h = 1; h <= harmonics; h++)
                    {
                        sum += w * Math.Sin(TAU * fv * h * t + ph0 * h);
                        w *= bright;
                    }
                    double s = level * a * sum;
                    L[i] += s * panL; R[i] += s * panR;
                }
            }
        }

        // 3. Мерцающие "звёзды": A5, C6, E6 — редкие тихие всплески, высота тона неизменна
        double[] stars = { 12, 15, 19 };
        for (int k = 0; stars_on && k < stars.Length; k++)
        {
            double f = note(stars[k]);
            double period = 18 + rnd.NextDouble() * 20, ph = rnd.NextDouble() * TAU;
            double pan = k % 2 == 0 ? 0.3 : 0.7;
            for (int i = 0; i < n; i++)
            {
                double t = (double)i / SR;
                double env = Math.Max(0, Math.Sin(TAU * t / period + ph));
                env = env * env * env;
                double s = 0.018 * env * Math.Sin(TAU * f * t);
                L[i] += s * Math.Sqrt(1 - pan); R[i] += s * Math.Sqrt(pan);
            }
        }

        // 4. Поющие чаши: A3, C4, E4 — удар мягкой колотушкой раз в 14–24 с
        // Негармонические обертоны (1 : 2.76 : 5.40 : 8.93), каждый раздвоен на 0.6–2.4 Гц — даёт "пульсацию" чаши
        double[] bowls = { -12, -9, -5 };
        double[] ratio = { 1.0, 2.76, 5.40, 8.93 };
        double[] pAmp = { 1.0, 0.45, 0.18, 0.07 };
        double[] tau = { 11.0, 6.0, 3.2, 1.8 };
        double strike = 5.0;
        while (bowls_on && strike < seconds - 18)
        {
            double f0 = note(bowls[rnd.Next(bowls.Length)]);
            double vel = 0.10 + rnd.NextDouble() * 0.04;
            double pan = 0.3 + rnd.NextDouble() * 0.4;
            double gl = Math.Sqrt(1 - pan), gr = Math.Sqrt(pan);
            double[] beat = new double[ratio.Length];
            for (int p = 0; p < ratio.Length; p++) beat[p] = 0.6 + rnd.NextDouble() * 1.8;
            int start = (int)(strike * SR), len = Math.Min(n - start, 30 * SR);
            for (int j = 0; j < len; j++)
            {
                double t = (double)j / SR;
                double attack = Math.Min(1.0, t / 0.008);
                double s = 0;
                for (int p = 0; p < ratio.Length; p++)
                {
                    double f = f0 * ratio[p];
                    s += pAmp[p] * Math.Exp(-t / tau[p]) *
                         (Math.Sin(TAU * f * t) + Math.Sin(TAU * (f + beat[p]) * t)) * 0.5;
                }
                s *= vel * attack;
                L[start + j] += s * gl; R[start + j] += s * gr;
            }
            strike += 14 + rnd.NextDouble() * 10;
        }

        // 5. Далёкие киты: редкие фразы из 1–3 протяжных "стонов" раз в 22–38 с
        // Стон = плавная дуга высоты тона (120–240 Гц) + обертоны с формантой ~450 Гц.
        // Дальность: два полюса низкочастотного фильтра (~700 Гц), подводное эхо 0.7 и 1.5 с, низкая громкость.
        if (whales_on)
        {
            double[] wl = new double[n], wr = new double[n];
            double phrase = 12.0;
            while (phrase < seconds - 20)
            {
                double pan = 0.25 + rnd.NextDouble() * 0.5;
                double gl = Math.Sqrt(1 - pan), gr = Math.Sqrt(pan);
                int calls = 1 + rnd.Next(3);
                double tc = phrase;
                for (int c = 0; c < calls; c++)
                {
                    double d = 2.5 + rnd.NextDouble() * 2.5;
                    double f0 = 120 + rnd.NextDouble() * 120;
                    double arc = -3 + rnd.NextDouble() * 8;     // подъём/спад в середине, полутона
                    double tilt = -4 + rnd.NextDouble() * 6;    // общий уклон к концу, полутона
                    double vel = 0.6 + rnd.NextDouble() * 0.4;
                    int start = (int)(tc * SR), len = Math.Min(n - start, (int)(d * SR));
                    double phase = 0;
                    for (int j = 0; j < len; j++)
                    {
                        double x = (double)j / len;
                        double semi = arc * Math.Sin(Math.PI * x) + tilt * x;
                        double f = f0 * Math.Pow(2, semi / 12.0);
                        phase += TAU * f / SR;
                        double env = Math.Pow(Math.Sin(Math.PI * x), 1.5);
                        double s = 0;
                        for (int h = 1; h <= 8; h++)
                        {
                            double fh = f * h;
                            double w = Math.Exp(-Math.Pow((fh - 450) / 250, 2)) + 0.35 / h;
                            s += w * Math.Sin(phase * h);
                        }
                        s *= 0.05 * vel * env;
                        wl[start + j] += s * gl; wr[start + j] += s * gr;
                    }
                    tc += d + 0.6 + rnd.NextDouble() * 1.2;
                }
                phrase = tc + 22 + rnd.NextDouble() * 16;
            }
            Distant(wl, 0.7, 1.5); Distant(wr, 0.75, 1.45);
            for (int i = 0; i < n; i++) { L[i] += wl[i]; R[i] += wr[i]; }
        }

        // 6. Тихое "фетровое" фортепиано: редкие ноты ля-минорной пентатоники раз в 3.5–7.5 с
        // Чуть растянутые обертоны (как у настоящей струны), две струны на ноту, верха быстро гаснут
        // светлый: A3 C4 D4 E4 G4 A4 C5 E5;  тёмный (ля-бемоль мажорная пентатоника): Ab3 Bb3 C4 Eb4 F4 Ab4 Bb4 C5
        // до мажор: до-мажорная пентатоника C4 D4 E4 G4 A4 C5 D5 E5
        double[] scale = keyC ? new double[] { -9, -7, -5, -2, 0, 3, 5, 7 }
                       : dark ? new double[] { -13, -11, -9, -6, -4, -1, 1, 3 } : new double[] { -12, -9, -7, -5, -2, 0, 3, 7 };
        double pianoTop = keyC ? 4000 : calm ? (Bright ? 4000 : 3000) : dark ? 1500 : 5000;
        int pos = 4;
        double tn = 8.0;
        while (piano_on && tn < seconds - 12)
        {
            pos = Math.Max(0, Math.Min(scale.Length - 1, pos + rnd.Next(-2, 3)));
            PianoNote(L, R, (int)(tn * SR), note(scale[pos]), PianoGain * (0.07 + rnd.NextDouble() * 0.03), 0.4 + rnd.NextDouble() * 0.2, pianoTop);
            if (rnd.NextDouble() < 0.25 && pos >= 3)
                PianoNote(L, R, (int)((tn + 0.04) * SR), note(scale[pos - 3]), PianoGain * 0.05, 0.45, pianoTop);
            tn += PianoMin + rnd.NextDouble() * (PianoMax - PianoMin);
        }

        // 7. Длинная реверберация (Freeverb-подобная)
        Reverb(L, 0); Reverb(R, 23);

        // В тёмном варианте срезаем верха (~1100 Гц, 2 полюса), как у эталона, где выше 1 кГц почти ничего нет
        // Спокойный вариант: верх приоткрыт до ~2.5 кГц (больше "воздуха") и всё ниже ~65 Гц убрано
        // до мажор (по etalon1): тёплый бас без суб-баса, верх до ~3.5 кГц
        if (keyC) { LowPass(L, 3500); LowPass(R, 3500); HighPass(L, 45); HighPass(R, 45); }
        else if (calm)
        {
            double lp = Bright ? 3500 : 2500;
            LowPass(L, lp); LowPass(R, lp); HighPass(L, 65); HighPass(R, 65);
        }
        else if (dark) { LowPass(L, 1100); LowPass(R, 1100); }

        // 8. Бинауральные биения (только в наушниках). Добавляются после реверберации, чтобы каналы не смешивались.
        // светлый: альфа 10 Гц от A3 = 216 Гц; тёмный: альфа 10 Гц от Ab3 ≈ 203.9 Гц;
        // спокойный: тета 5 Гц от C4 ≈ 256.9 Гц — медленнее, тише и выше зоны "гула"
        bool soft = calm || keyC;   // в до мажоре тоже тета 5 Гц от C4
        double carrier = soft ? note(-9) : dark ? note(-13) : 216.0;
        double beatHz = soft ? 5.0 : 10.0, binLvl = soft ? 0.025 : 0.035;
        for (int i = 0; binaural_on && i < n; i++)
        {
            double t = (double)i / SR;
            L[i] += binLvl * Math.Sin(TAU * carrier * t);
            R[i] += binLvl * Math.Sin(TAU * (carrier + beatHz) * t);
        }

        // 6. Плавное появление и затухание, нормализация
        int fadeIn = 10 * SR, fadeOut = 15 * SR;
        double peak = 1e-9;
        for (int i = 0; i < n; i++)
        {
            double g = 1;
            if (i < fadeIn) g = Math.Pow((double)i / fadeIn, 2);
            if (i > n - fadeOut) g = Math.Pow((double)(n - i) / fadeOut, 2);
            L[i] *= g; R[i] *= g;
            peak = Math.Max(peak, Math.Max(Math.Abs(L[i]), Math.Abs(R[i])));
        }
        double norm = 0.63 / peak;   // ≈ −4 дБ: запас, чтобы не перегружать динамики на низах

        using (var bw = new BinaryWriter(File.Create(path)))
        {
            int dataLen = n * 4;
            bw.Write("RIFF".ToCharArray()); bw.Write(36 + dataLen);
            bw.Write("WAVEfmt ".ToCharArray()); bw.Write(16); bw.Write((short)1); bw.Write((short)2);
            bw.Write(SR); bw.Write(SR * 4); bw.Write((short)4); bw.Write((short)16);
            bw.Write("data".ToCharArray()); bw.Write(dataLen);
            for (int i = 0; i < n; i++)
            {
                bw.Write((short)Math.Round(Math.Max(-1, Math.Min(1, L[i] * norm)) * 32767));
                bw.Write((short)Math.Round(Math.Max(-1, Math.Min(1, R[i] * norm)) * 32767));
            }
        }
    }

    // "Издалека": двухполюсный НЧ-фильтр (~700 Гц) и два затухающих подводных эха
    // Смена аккордов (до мажор): каждый аккорд 16 с, переход перекрёстным затуханием 6 с
    const double ChordSeg = 16.0, ChordXf = 6.0;

    static void ChordPads(double[] L, double[] R, double seconds, Random rnd, Func<double, double> note)
    {
        double[][] chords = {
            new double[] { -16, -12, -9, -5, -2 },   // Fmaj9: F3 A3 C4 E4 G4
            new double[] { -21, -14, -5, -2, 3 },    // C:     C3 G3 E4 G4 C5
            new double[] { -24, -17, -14, -9, -5 },  // Am7:   A2 E3 G3 C4 E4
            new double[] { -26, -19, -10, -5, -2 },  // G6:    G2 D3 B3 E4 G4
        };
        int n = L.Length;
        for (int k = 0; k * ChordSeg < seconds; k++)
        {
            var chord = chords[k % chords.Length];
            int i0 = (int)(k * ChordSeg * SR), i1 = Math.Min(n, (int)(((k + 1) * ChordSeg + ChordXf) * SR));
            foreach (double semi in chord)
            {
                double f = note(semi);
                double ampPeriod = 20 + rnd.NextDouble() * 20, ampPhase = rnd.NextDouble() * TAU;
                double level = semi < -14 ? 0.06 : 0.07;
                for (int v = -1; v <= 1; v++)
                {
                    double fv = f * Math.Pow(2, v * 5 / 1200.0);
                    double panL = Math.Sqrt(0.5 - v * 0.3), panR = Math.Sqrt(0.5 + v * 0.3);
                    double ph0 = rnd.NextDouble() * TAU;
                    for (int i = i0; i < i1; i++)
                    {
                        double t = (double)i / SR, u = t - k * ChordSeg, env;
                        if (u < ChordXf) env = k == 0 ? 1 : 0.5 - 0.5 * Math.Cos(Math.PI * u / ChordXf);
                        else if (u < ChordSeg) env = 1;
                        else env = 0.5 + 0.5 * Math.Cos(Math.PI * (u - ChordSeg) / ChordXf);
                        double a = 0.5 + 0.5 * Math.Sin(TAU * t / ampPeriod + ampPhase);
                        a = 0.4 + 0.6 * a * a;
                        double sum = 0, w = 1;
                        for (int h = 1; h <= 5; h++) { sum += w * Math.Sin(TAU * fv * h * t + ph0 * h); w *= 0.3; }
                        double s = level * env * a * sum;
                        L[i] += s * panL; R[i] += s * panR;
                    }
                }
            }
        }
    }

    static void LowPass(double[] x, double fc)
    {
        double k = 1 - Math.Exp(-TAU * fc / SR), a = 0, b = 0;
        for (int i = 0; i < x.Length; i++) { a += k * (x[i] - a); b += k * (a - b); x[i] = b; }
    }

    // ФВЧ 2-го порядка (два каскада по 6 дБ/окт)
    static void HighPass(double[] x, double fc)
    {
        double k = 1 - Math.Exp(-TAU * fc / SR), a = 0, b = 0;
        for (int i = 0; i < x.Length; i++)
        {
            a += k * (x[i] - a); double y = x[i] - a;
            b += k * (y - b); x[i] = y - b;
        }
    }

    static void PianoNote(double[] L, double[] R, int start, double f, double vel, double pan, double top)
    {
        // Нота звучит до 20 с и последние 2 с плавно уходит в ноль: обрыв ещё звучащей ноты давал щелчок
        int n = L.Length, len = Math.Min(n - start, 20 * SR), rel = 2 * SR;
        double gl = Math.Sqrt(1 - pan), gr = Math.Sqrt(pan);
        for (int h = 1; h <= 10; h++)
        {
            double fh = f * h * Math.Sqrt(1 + 0.0004 * h * h);
            if (fh > top) break;
            double amp = vel * Math.Pow(h, -1.3) * Math.Exp(-(h - 1) * 0.35);
            double tauH = 5.0 / (1 + 0.6 * (h - 1));
            for (int j = 0; j < len; j++)
            {
                double t = (double)j / SR;
                double tail = j < len - rel ? 1.0 : 0.5 + 0.5 * Math.Cos(Math.PI * (j - (len - rel)) / rel);
                double s = amp * tail * Math.Min(1.0, t / 0.012) * Math.Exp(-t / tauH) *
                           0.5 * (Math.Sin(TAU * fh * t) + Math.Sin(TAU * fh * 1.0007 * t));
                L[start + j] += s * gl; R[start + j] += s * gr;
            }
        }
    }

    static void Distant(double[] x, double echo1, double echo2)
    {
        int n = x.Length;
        double k = 1 - Math.Exp(-TAU * 700.0 / SR), a = 0, b = 0;
        for (int i = 0; i < n; i++) { a += k * (x[i] - a); b += k * (a - b); x[i] = b; }
        int d1 = (int)(echo1 * SR), d2 = (int)(echo2 * SR);
        for (int i = n - 1; i >= d1; i--)
            x[i] += 0.35 * x[i - d1] + (i >= d2 ? 0.2 * x[i - d2] : 0);
    }

    static void Reverb(double[] x, int spread)
    {
        int[] combs = { 1557, 1617, 1491, 1422, 1277, 1356, 1188, 1116 };
        int[] aps = { 556, 441, 341, 225 };
        double feedback = 0.90, damp = 0.35, wet = 0.55, dry = 0.6;
        int n = x.Length;
        double[] outp = new double[n];
        // Вход ревербератора без баса (ФВЧ ~400 Гц): низ остаётся сухим и одинаковым в обоих каналах,
        // иначе резонансы гребенчатых фильтров по-разному раскачивают басовые ноты слева и справа
        double[] inp = new double[n];
        double hk = 1 - Math.Exp(-TAU * 400.0 / SR), h1 = 0, h2 = 0;
        for (int i = 0; i < n; i++)
        {
            h1 += hk * (x[i] - h1); double y1 = x[i] - h1;   // ФВЧ 1-го порядка
            h2 += hk * (y1 - h2); inp[i] = y1 - h2;            // ещё один каскад: 12 дБ/окт
        }
        foreach (int c in combs)
        {
            double[] buf = new double[c + spread]; int idx = 0; double store = 0;
            for (int i = 0; i < n; i++)
            {
                double o = buf[idx];
                store = o * (1 - damp) + store * damp;
                buf[idx] = inp[i] * 0.015 + store * feedback;
                idx = (idx + 1) % buf.Length;
                outp[i] += o;
            }
        }
        foreach (int a in aps)
        {
            double[] buf = new double[a + spread]; int idx = 0;
            for (int i = 0; i < n; i++)
            {
                double b = buf[idx];
                buf[idx] = outp[i] + b * 0.5;
                outp[i] = b - outp[i];
                idx = (idx + 1) % buf.Length;
            }
        }
        for (int i = 0; i < n; i++) x[i] = x[i] * dry + outp[i] * wet * 8;
    }
}
"@

$path = Join-Path (Get-Location) $Out
$sw = [Diagnostics.Stopwatch]::StartNew()
[AmbientSynth]::PianoGain = $PianoGain
[AmbientSynth]::PianoMin = $PianoMin
[AmbientSynth]::PianoMax = $PianoMax
[AmbientSynth]::Bright = [bool]$Bright
[AmbientSynth]::Render($path, $Seconds, $Seed, -not $NoStars, -not $NoBowls, -not $NoWhales, -not $NoPiano, -not $NoBinaural, [bool]($Dark -or $Calm), [bool]$Calm, [bool]$KeyC)
"Готово: $path ($([math]::Round($sw.Elapsed.TotalSeconds,1)) с)"
