# Космический амбиент в строе A = 432 Гц (без вокала, для сна и медитации)
# Запуск:  pwsh -File space_ambient_432.ps1 [-Seconds 150] [-Seed 7] [-Out space_ambient_432.wav] [-NoStars] [-NoBowls] [-NoWhales] [-NoPiano] [-NoBinaural] [-Dark] [-Calm]
#          [-PianoGain 1.0] [-PianoMin 3.5] [-PianoMax 7.5] [-Bright] [-KeyC] [-Hours 0] [-Threads 0] [-TwoPass]
#          [-Celestial] [-Chakra 1] [-Tonic 396] [-Segments "528,432,396"] [-SegmentFade 30]
#
# Трек считается блоками по 10 с и сразу пишется на диск, поэтому длина не ограничена памятью (1–10 ч и больше).
# Состояние ревербератора и фильтров переносится между блоками: результат тот же, что у прежней версии,
# которая держала весь трек в памяти (при том же -Seed и параметрах).
# Нормализация до −4 дБ требует пик всего трека, поэтому:
#   по умолчанию — один проход в промежуточный файл <Out>.part.f32 (≈ 2× размера WAV на диске), затем перевод в WAV;
#   -TwoPass     — без промежуточного файла: первый проход только ищет пик, второй пишет WAV (вдвое дольше).
# WAV больше 4 ГБ (≈ 6.7 ч) пишется в формате RF64 — его открывает Audacity.
param(
    [double]$Seconds = 150,
    [double]$Hours = 0,          # если задано, длина = Hours × 3600 с (вместо -Seconds)
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
    [switch]$KeyC,         # до мажор по etalon1: аккорды F → C → Am → G, тёплый бас, тета 5 Гц (без -Dark/-Calm)
    [switch]$Celestial,    # по эталону Celestial Spirit: ре минор Dm → Bb → C → Am, тёмный (верх до 1.1 кГц), широкое стерео, пульсация 1 Гц
    [int]$Chakra = 0,      # пресет чакры: 1 = муладхара (до мажор, как v9; см. sevenlights/CLAUDE.md)
    [double]$Tonic = 0,    # тоника (нота до) в Гц, например 396: вся высота сдвигается, строй перестаёт быть 432
    [string]$Segments = "",       # части с разной частотой по очереди, например "528,432,396" (432 = строй A = 432, другое — тоника)
    [double]$SegmentFade = 30,    # длина затухания/появления на стыке частей, с
    [int]$Threads = 0,     # число потоков (0 = все ядра)
    [switch]$TwoPass       # без промежуточного файла: два прохода рендера
)

Add-Type -TypeDefinition @"
using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading.Tasks;

public static class AmbientSynth
{
    const int SR = 44100;
    const double TAU = Math.PI * 2;
    const int Block = 10 * SR;        // блок рендера: 10 с

    // Тонкая настройка (задаётся из параметров скрипта)
    public static double PianoGain = 1.0, PianoMin = 3.5, PianoMax = 7.5;
    public static bool Bright = false;
    public static int Threads = 0;
    // Высота строя: A4 = 432 Гц; другое значение (через -Tonic) сдвигает все звуковысотные слои
    public static double A4 = 432.0;
    // Части трека: своя высота строя (A4) у каждой, стыки — затухание одной части поверх появления следующей
    public static double[] SegA4 = null;
    public static double SegFade = 30;
    // Настройки пресета -Celestial (по умолчанию выключены: прежние пресеты не меняются)
    public static int ChordSet = 0;              // 0 = до мажор, 1 = ре минор
    public static bool WidePads = false;         // голоса пэдов разведены по каналам: L и R почти независимы
    public static double LowPassHz = 0;          // срез верхов для пресета с аккордами (0 = 3500 Гц, как у до мажора)
    public static double PulseHz = 0, PulseDepth = 0;   // мягкая пульсация громкости (изохронный ритм)
    public static double BassDetune = 0;         // бас слева ниже, справа выше на эту долю (0.005 = ±0.5%): широкий бас, медленные биения
    static double FadeInSec = 10, FadeOutSec = 15;

    // ---------- План трека: все случайные события выбираются заранее, в том же порядке, что и раньше ----------

    class PadVoice
    {
        public bool chord;            // до мажор: голос аккорда с огибающей перехода
        public int k;                 // номер аккорда
        public long i0, i1;           // где звучит (для аккорда)
        public double fv, panL, panR, ph0, ampPeriod, ampPhase, briPeriod, briPhase, level;
    }
    class Star { public double f, period, ph, pan; }
    class Bowl { public long start; public int len; public double f0, vel, gl, gr; public double[] beat; }
    class WhaleCall { public long start; public int len; public double f0, arc, tilt, vel, gl, gr; public double[] samples; }
    class Note { public long start; public int len; public double f, vel, pan, top; }

    class Plan
    {
        public long n;
        public double seconds;
        public bool stars_on, bowls_on, whales_on, piano_on, binaural_on, dark, calm, keyC;
        public double[] bass; public double seg, xf, fundLvl, octLvl;
        public double briBase, briRange; public int harmonics;
        public List<PadVoice> pads = new List<PadVoice>();   // по возрастанию i0
        public List<Star> stars = new List<Star>();
        public List<Bowl> bowls = new List<Bowl>();
        public List<WhaleCall> calls = new List<WhaleCall>();
        public List<Note> notes = new List<Note>();
        public double carrier, beatHz, binLvl;
    }

    // Смена аккордов (до мажор): каждый аккорд 16 с, переход перекрёстным затуханием 6 с
    const double ChordSeg = 16.0, ChordXf = 6.0;
    static readonly double[][] Chords = {
        new double[] { -16, -12, -9, -5, -2 },   // Fmaj9: F3 A3 C4 E4 G4
        new double[] { -21, -14, -5, -2, 3 },    // C:     C3 G3 E4 G4 C5
        new double[] { -24, -17, -14, -9, -5 },  // Am7:   A2 E3 G3 C4 E4
        new double[] { -26, -19, -10, -5, -2 },  // G6:    G2 D3 B3 E4 G4
    };

    // Ре минор (по эталону Celestial Spirit: сильнейшие ноты A, Bb, C, D)
    static readonly double[][] ChordsDm = {
        new double[] { -19, -12, -9, -5, -4 },   // Dm9:    D3 A3 C4 E4 F4
        new double[] { -23, -16, -12, -7, -4 },  // Bbmaj7: Bb2 F3 A3 D4 F4
        new double[] { -21, -14, -7, -5, -2 },   // Cadd9:  C3 G3 D4 E4 G4
        new double[] { -24, -17, -14, -9, -5 },  // Am7:    A2 E3 G3 C4 E4
    };

    static double Note432(double s) { return A4 * Math.Pow(2, s / 12.0); }

    static Plan MakePlan(double seconds, int seed, bool stars_on, bool bowls_on, bool whales_on, bool piano_on, bool binaural_on, bool dark, bool calm, bool keyC, long nSamples = -1)
    {
        var p = new Plan();
        p.seconds = seconds; p.n = nSamples >= 0 ? nSamples : (long)(seconds * SR);
        p.stars_on = stars_on; p.bowls_on = bowls_on; p.whales_on = whales_on; p.piano_on = piano_on; p.binaural_on = binaural_on;
        p.dark = dark; p.calm = calm; p.keyC = keyC;
        long n = p.n;
        var rnd = new Random(seed);
        Func<double, double> note = Note432;

        // 1. Бас: медленная басовая линия (тёмный / спокойный / до мажор), полутоны от A1 = 54 Гц
        p.bass = keyC ? (ChordSet == 1 ? new double[] { 5, 1, 3, 0 } : new double[] { 8, 3, 0, 10 }) : calm ? new double[] { 11, 6 } : new double[] { -1, 1, 3, -2 };
        p.seg = keyC ? ChordSeg : calm ? 20.0 : 16.0; p.xf = keyC ? ChordXf : calm ? 7.0 : 5.0;
        p.fundLvl = keyC ? (ChordSet == 1 ? 0.30 : 0.45) : calm ? 0.35 : 0.40; p.octLvl = keyC ? (ChordSet == 1 ? 0.30 : 0.28) : calm ? 0.12 : 0.24;

        // 2. Пэды
        double[] pad = calm ? new double[] { -25, -18, -13, -9, -6, 1 }
                     : dark ? new double[] { -25, -18, -13, -11, -9, -6 } : new double[] { -24, -17, -12, -9, -5, -2 };
        p.briBase = (calm ? 0.20 : dark ? 0.15 : 0.30) + (Bright ? 0.05 : 0); p.briRange = calm ? 0.14 : dark ? 0.12 : 0.20;
        p.harmonics = calm ? 5 : dark ? 4 : 6;
        if (keyC)
        {
            for (int k = 0; k * ChordSeg < seconds; k++)
            {
                var table = ChordSet == 1 ? ChordsDm : Chords;
                var chord = table[k % table.Length];
                long i0 = (long)(k * ChordSeg * SR), i1 = Math.Min(n, (long)(((k + 1) * ChordSeg + ChordXf) * SR));
                foreach (double semi in chord)
                {
                    double f = note(semi);
                    double ampPeriod = 20 + rnd.NextDouble() * 20, ampPhase = rnd.NextDouble() * TAU;
                    double level = semi < -14 ? 0.06 : 0.07;
                    for (int v = -1; v <= 1; v++)
                    {
                        var pv = new PadVoice { chord = true, k = k, i0 = i0, i1 = i1, level = level, ampPeriod = ampPeriod, ampPhase = ampPhase };
                        pv.fv = f * Math.Pow(2, v * 5 / 1200.0);
                        pv.panL = Math.Sqrt(0.5 - v * 0.3); pv.panR = Math.Sqrt(0.5 + v * 0.3);
                        if (WidePads)
                        {
                            // Крайние голоса (−5 и +5 центов) — каждый только в своём канале, средний тише:
                            // каналы почти независимы, стерео очень широкое (как у эталона, корреляция L/R ≈ 0)
                            pv.panL = v < 0 ? 1 : v == 0 ? 0.35 : 0;
                            pv.panR = v > 0 ? 1 : v == 0 ? 0.35 : 0;
                        }
                        pv.ph0 = rnd.NextDouble() * TAU;
                        p.pads.Add(pv);
                    }
                }
            }
        }
        else foreach (double semi in pad)
        {
            double f = note(semi);
            double ampPeriod = 25 + rnd.NextDouble() * 30, ampPhase = rnd.NextDouble() * TAU;
            double briPeriod = 30 + rnd.NextDouble() * 40, briPhase = rnd.NextDouble() * TAU;
            double level = semi < -14 ? (dark ? 0.06 : 0.10) : 0.07;
            for (int v = -1; v <= 1; v++)
            {
                var pv = new PadVoice { i0 = 0, i1 = n, level = level, ampPeriod = ampPeriod, ampPhase = ampPhase, briPeriod = briPeriod, briPhase = briPhase };
                pv.fv = f * Math.Pow(2, v * 5 / 1200.0);   // ±5 центов — мягкий хорус
                pv.panL = Math.Sqrt(0.5 - v * 0.3); pv.panR = Math.Sqrt(0.5 + v * 0.3);
                pv.ph0 = rnd.NextDouble() * TAU;
                p.pads.Add(pv);
            }
        }

        // 3. Мерцающие "звёзды": A5, C6, E6
        double[] stars = { 12, 15, 19 };
        for (int k = 0; stars_on && k < stars.Length; k++)
        {
            var st = new Star { f = note(stars[k]) };
            st.period = 18 + rnd.NextDouble() * 20; st.ph = rnd.NextDouble() * TAU;
            st.pan = k % 2 == 0 ? 0.3 : 0.7;
            p.stars.Add(st);
        }

        // 4. Поющие чаши: A3, C4, E4 — удар мягкой колотушкой раз в 14–24 с
        double[] bowls = { -12, -9, -5 };
        double strike = 5.0;
        while (bowls_on && strike < seconds - 18)
        {
            var b = new Bowl();
            b.f0 = note(bowls[rnd.Next(bowls.Length)]);
            b.vel = 0.10 + rnd.NextDouble() * 0.04;
            double pan = 0.3 + rnd.NextDouble() * 0.4;
            b.gl = Math.Sqrt(1 - pan); b.gr = Math.Sqrt(pan);
            b.beat = new double[BowlRatio.Length];
            for (int q = 0; q < BowlRatio.Length; q++) b.beat[q] = 0.6 + rnd.NextDouble() * 1.8;
            b.start = (long)(strike * SR); b.len = (int)Math.Min(n - b.start, 30L * SR);
            p.bowls.Add(b);
            strike += 14 + rnd.NextDouble() * 10;
        }

        // 5. Далёкие киты: редкие фразы из 1–3 протяжных "стонов" раз в 22–38 с
        if (whales_on)
        {
            double phrase = 12.0;
            while (phrase < seconds - 20)
            {
                double pan = 0.25 + rnd.NextDouble() * 0.5;
                double gl = Math.Sqrt(1 - pan), gr = Math.Sqrt(pan);
                int calls = 1 + rnd.Next(3);
                double tc = phrase;
                for (int c = 0; c < calls; c++)
                {
                    var w = new WhaleCall { gl = gl, gr = gr };
                    double d = 2.5 + rnd.NextDouble() * 2.5;
                    w.f0 = 120 + rnd.NextDouble() * 120;
                    w.arc = -3 + rnd.NextDouble() * 8;     // подъём/спад в середине, полутона
                    w.tilt = -4 + rnd.NextDouble() * 6;    // общий уклон к концу, полутона
                    w.vel = 0.6 + rnd.NextDouble() * 0.4;
                    w.start = (long)(tc * SR); w.len = (int)Math.Min(n - w.start, (long)(d * SR));
                    p.calls.Add(w);
                    tc += d + 0.6 + rnd.NextDouble() * 1.2;
                }
                phrase = tc + 22 + rnd.NextDouble() * 16;
            }
        }

        // 6. "Фетровое" фортепиано: редкие ноты пентатоники, мелодия ходит маленькими шагами
        // светлый: A3 C4 D4 E4 G4 A4 C5 E5;  тёмный: Ab3 Bb3 C4 Eb4 F4 Ab4 Bb4 C5;  до мажор: C4 D4 E4 G4 A4 C5 D5 E5
        // ре минор: ре-минорная пентатоника A3 C4 D4 F4 G4 A4 C5 D5
        double[] scale = keyC ? (ChordSet == 1 ? new double[] { -12, -9, -7, -4, -2, 0, 3, 5 } : new double[] { -9, -7, -5, -2, 0, 3, 5, 7 })
                       : dark ? new double[] { -13, -11, -9, -6, -4, -1, 1, 3 } : new double[] { -12, -9, -7, -5, -2, 0, 3, 7 };
        double pianoTop = keyC ? (ChordSet == 1 ? 1500 : 4000) : calm ? (Bright ? 4000 : 3000) : dark ? 1500 : 5000;
        int pos = 4;
        double tn = 8.0;
        while (piano_on && tn < seconds - 12)
        {
            pos = Math.Max(0, Math.Min(scale.Length - 1, pos + rnd.Next(-2, 3)));
            double vel = PianoGain * (0.07 + rnd.NextDouble() * 0.03);
            double pan = 0.4 + rnd.NextDouble() * 0.2;
            AddNote(p, (long)(tn * SR), note(scale[pos]), vel, pan, pianoTop);
            if (rnd.NextDouble() < 0.25 && pos >= 3)
                AddNote(p, (long)((tn + 0.04) * SR), note(scale[pos - 3]), PianoGain * 0.05, 0.45, pianoTop);
            tn += PianoMin + rnd.NextDouble() * (PianoMax - PianoMin);
        }

        // 8. Бинауральные биения: светлый — альфа 10 Гц от A3 = 216 Гц; тёмный — альфа 10 Гц от Ab3;
        // спокойный и до мажор — тета 5 Гц от C4 ≈ 256.9 Гц
        bool soft = calm || keyC;
        p.carrier = soft ? note(keyC && ChordSet == 1 ? -7 : -9) : dark ? note(-13) : A4 / 2;
        p.beatHz = soft ? 5.0 : 10.0; p.binLvl = soft ? 0.025 : 0.035;
        return p;
    }

    static void AddNote(Plan p, long start, double f, double vel, double pan, double top)
    {
        // Нота звучит до 20 с и последние 2 с плавно уходит в ноль: обрыв ещё звучащей ноты давал щелчок
        p.notes.Add(new Note { start = start, len = (int)Math.Min(p.n - start, 20L * SR), f = f, vel = vel, pan = pan, top = top });
    }

    // Негармонические обертоны чаши (1 : 2.76 : 5.40 : 8.93), каждый раздвоен на 0.6–2.4 Гц — даёт "пульсацию"
    static readonly double[] BowlRatio = { 1.0, 2.76, 5.40, 8.93 };
    static readonly double[] BowlAmp = { 1.0, 0.45, 0.18, 0.07 };
    static readonly double[] BowlTau = { 11.0, 6.0, 3.2, 1.8 };

    // ---------- Синтез сухих слоёв (без состояния — считается параллельно по кускам блока) ----------

    static void Synth(Plan p, long g0, int cnt, double[] L, double[] R, int off,
                      List<PadVoice> pads, List<Bowl> bowls, List<Note> notes, double[] wl, double[] wr)
    {
        long g1 = g0 + cnt;

        // 1. Низкий дрон / басовая линия
        if (!p.dark && !p.keyC)
        {
            // A1 (54 Гц) и A2 (108 Гц), медленное "дыхание"
            for (int i = 0; i < cnt; i++)
            {
                double t = (double)(g0 + i) / SR;
                double breath = 0.8 + 0.2 * Math.Sin(TAU * t / 40.0);
                double s = breath * (0.30 * Math.Sin(TAU * (A4 / 8) * t) + 0.15 * Math.Sin(TAU * (A4 / 4) * t + 1.3));
                L[off + i] += s; R[off + i] += s;
            }
        }
        else
        {
            // Ноты сменяются плавным перекрёстным затуханием — без скольжения высоты
            double seg = p.seg, xf = p.xf;
            for (int i = 0; i < cnt; i++)
            {
                double t = (double)(g0 + i) / SR;
                double breath = 0.85 + 0.15 * Math.Sin(TAU * t / 12.0);   // "дыхание" ~12 с, как у эталона
                int j = (int)(t / seg);
                double s = 0, sR = 0;
                for (int q = j - 1; q <= j; q++)
                {
                    if (q < 0) continue;
                    double u = t - q * seg, env;
                    if (u < xf) env = 0.5 - 0.5 * Math.Cos(Math.PI * u / xf);
                    else if (u < seg) env = 1;
                    else if (u < seg + xf) env = 0.5 + 0.5 * Math.Cos(Math.PI * (u - seg) / xf);
                    else env = 0;
                    if (q == 0 && u < xf) env = 1;   // первая нота звучит сразу (общее появление трека и так плавное)
                    double f = A4 / 8 * Math.Pow(2, p.bass[q % p.bass.Length] / 12.0);
                    // При сдвиге строя вниз бас не уходит в суб-бас: нота ниже 50 Гц поднимается на октаву
                    if (A4 != 432.0) while (f < 50) f *= 2;
                    // Суб-бас умеренный: при 0.65 небольшие динамики/наушники хрипели ("как пластинка")
                    if (BassDetune > 0)
                    {
                        // Широкий бас: слева чуть ниже, справа чуть выше — медленные биения ~0.5 Гц, высота ровная
                        double fl = f * (1 - BassDetune), fr = f * (1 + BassDetune);
                        s += env * (p.fundLvl * Math.Sin(TAU * fl * t) + p.octLvl * Math.Sin(TAU * 2 * fl * t + 1.3));
                        sR += env * (p.fundLvl * Math.Sin(TAU * fr * t) + p.octLvl * Math.Sin(TAU * 2 * fr * t + 1.3));
                    }
                    else s += env * (p.fundLvl * Math.Sin(TAU * f * t) + p.octLvl * Math.Sin(TAU * 2 * f * t + 1.3));
                }
                s *= breath;
                if (BassDetune > 0) { sR *= breath; L[off + i] += s; R[off + i] += sR; }
                else { L[off + i] += s; R[off + i] += s; }
            }
        }

        // 2. Тёплые пэды, по 3 расстроенных голоса на ноту
        foreach (var v in pads)
        {
            long a0 = Math.Max(g0, v.i0), a1 = Math.Min(g1, v.i1);
            if (v.chord)
            {
                for (long g = a0; g < a1; g++)
                {
                    double t = (double)g / SR, u = t - v.k * ChordSeg, env;
                    if (u < ChordXf) env = v.k == 0 ? 1 : 0.5 - 0.5 * Math.Cos(Math.PI * u / ChordXf);
                    else if (u < ChordSeg) env = 1;
                    else env = 0.5 + 0.5 * Math.Cos(Math.PI * (u - ChordSeg) / ChordXf);
                    double a = 0.5 + 0.5 * Math.Sin(TAU * t / v.ampPeriod + v.ampPhase);
                    a = 0.4 + 0.6 * a * a;
                    double sum = 0, w = 1;
                    for (int h = 1; h <= 5; h++) { sum += w * Math.Sin(TAU * v.fv * h * t + v.ph0 * h); w *= 0.3; }
                    double s = v.level * env * a * sum;
                    int i = (int)(g - g0) + off;
                    L[i] += s * v.panL; R[i] += s * v.panR;
                }
            }
            else
            {
                for (long g = a0; g < a1; g++)
                {
                    double t = (double)g / SR;
                    double a = 0.5 + 0.5 * Math.Sin(TAU * t / v.ampPeriod + v.ampPhase);
                    a = 0.25 + 0.75 * a * a;
                    double bright = p.briBase + p.briRange * (0.5 + 0.5 * Math.Sin(TAU * t / v.briPeriod + v.briPhase));
                    double sum = 0, w = 1;
                    for (int h = 1; h <= p.harmonics; h++)
                    {
                        sum += w * Math.Sin(TAU * v.fv * h * t + v.ph0 * h);
                        w *= bright;
                    }
                    double s = v.level * a * sum;
                    int i = (int)(g - g0) + off;
                    L[i] += s * v.panL; R[i] += s * v.panR;
                }
            }
        }

        // 3. "Звёзды" — редкие тихие всплески, высота тона неизменна
        foreach (var st in p.stars)
        {
            for (int i = 0; i < cnt; i++)
            {
                double t = (double)(g0 + i) / SR;
                double env = Math.Max(0, Math.Sin(TAU * t / st.period + st.ph));
                env = env * env * env;
                double s = 0.018 * env * Math.Sin(TAU * st.f * t);
                L[off + i] += s * Math.Sqrt(1 - st.pan); R[off + i] += s * Math.Sqrt(st.pan);
            }
        }

        // 4. Поющие чаши
        foreach (var b in bowls)
        {
            long a0 = Math.Max(g0, b.start), a1 = Math.Min(g1, b.start + b.len);
            for (long g = a0; g < a1; g++)
            {
                double t = (double)(g - b.start) / SR;
                double attack = Math.Min(1.0, t / 0.008);
                double s = 0;
                for (int q = 0; q < BowlRatio.Length; q++)
                {
                    double f = b.f0 * BowlRatio[q];
                    s += BowlAmp[q] * Math.Exp(-t / BowlTau[q]) *
                         (Math.Sin(TAU * f * t) + Math.Sin(TAU * (f + b.beat[q]) * t)) * 0.5;
                }
                s *= b.vel * attack;
                int i = (int)(g - g0) + off;
                L[i] += s * b.gl; R[i] += s * b.gr;
            }
        }

        // 5. Киты (уже пропущены через "даль" — см. WhaleBlock)
        if (p.whales_on)
            for (int i = 0; i < cnt; i++) { L[off + i] += wl[off + i]; R[off + i] += wr[off + i]; }

        // 6. Фортепиано: чуть растянутые обертоны (как у настоящей струны), две струны на ноту, верха быстро гаснут
        foreach (var nt in notes)
        {
            long a0 = Math.Max(g0, nt.start), a1 = Math.Min(g1, nt.start + nt.len);
            if (a0 >= a1) continue;
            int len = nt.len, rel = 2 * SR;
            double gl = Math.Sqrt(1 - nt.pan), gr = Math.Sqrt(nt.pan);
            for (int h = 1; h <= 10; h++)
            {
                double fh = nt.f * h * Math.Sqrt(1 + 0.0004 * h * h);
                if (fh > nt.top) break;
                double amp = nt.vel * Math.Pow(h, -1.3) * Math.Exp(-(h - 1) * 0.35);
                double tauH = 5.0 / (1 + 0.6 * (h - 1));
                for (long g = a0; g < a1; g++)
                {
                    int j = (int)(g - nt.start);
                    double t = (double)j / SR;
                    double tail = j < len - rel ? 1.0 : 0.5 + 0.5 * Math.Cos(Math.PI * (j - (len - rel)) / rel);
                    double s = amp * tail * Math.Min(1.0, t / 0.012) * Math.Exp(-t / tauH) *
                               0.5 * (Math.Sin(TAU * fh * t) + Math.Sin(TAU * fh * 1.0007 * t));
                    int i = (int)(g - g0) + off;
                    L[i] += s * gl; R[i] += s * gr;
                }
            }
        }
    }

    // Один стон кита целиком: плавная дуга высоты тона (120–240 Гц) + обертоны с формантой ~450 Гц
    static double[] WhaleSamples(WhaleCall w)
    {
        var o = new double[w.len];
        double phase = 0;
        for (int j = 0; j < w.len; j++)
        {
            double x = (double)j / w.len;
            double semi = w.arc * Math.Sin(Math.PI * x) + w.tilt * x;
            double f = w.f0 * Math.Pow(2, semi / 12.0);
            phase += TAU * f / SR;
            double env = Math.Pow(Math.Sin(Math.PI * x), 1.5);
            double s = 0;
            for (int h = 1; h <= 8; h++)
            {
                double fh = f * h;
                double wgt = Math.Exp(-Math.Pow((fh - 450) / 250, 2)) + 0.35 / h;
                s += wgt * Math.Sin(phase * h);
            }
            s *= 0.05 * w.vel * env;
            o[j] = s;
        }
        return o;
    }

    // ---------- Обработка с состоянием (последовательно, состояние переносится между блоками) ----------

    // "Издалека": двухполюсный НЧ-фильтр (~700 Гц) и два затухающих подводных эха
    class Distant
    {
        double k = 1 - Math.Exp(-TAU * 700.0 / SR), a = 0, b = 0;
        int d1, d2; double[] hist = new double[1 << 17]; const int Mask = (1 << 17) - 1;
        public Distant(double echo1, double echo2) { d1 = (int)(echo1 * SR); d2 = (int)(echo2 * SR); }
        public void Process(double[] x, int cnt, long g0)
        {
            for (int i = 0; i < cnt; i++)
            {
                long g = g0 + i;
                a += k * (x[i] - a); b += k * (a - b);
                hist[g & Mask] = b;
                double y = b;
                if (g >= d1) y += 0.35 * hist[(g - d1) & Mask] + (g >= d2 ? 0.2 * hist[(g - d2) & Mask] : 0);
                x[i] = y;
            }
        }
    }

    // Длинная реверберация (Freeverb-подобная)
    class Reverb
    {
        static readonly int[] Combs = { 1557, 1617, 1491, 1422, 1277, 1356, 1188, 1116 };
        static readonly int[] Aps = { 556, 441, 341, 225 };
        const double feedback = 0.90, damp = 0.35, wet = 0.55, dry = 0.6;
        double[][] cb, ab; int[] ci, ai; double[] store;
        // Вход ревербератора без баса (ФВЧ ~400 Гц, 12 дБ/окт): низ остаётся сухим и одинаковым в обоих каналах,
        // иначе резонансы гребенчатых фильтров по-разному раскачивают басовые ноты слева и справа
        double hk = 1 - Math.Exp(-TAU * 400.0 / SR), h1 = 0, h2 = 0;
        public Reverb(int spread)
        {
            cb = new double[Combs.Length][]; ci = new int[Combs.Length]; store = new double[Combs.Length];
            for (int c = 0; c < Combs.Length; c++) cb[c] = new double[Combs[c] + spread];
            ab = new double[Aps.Length][]; ai = new int[Aps.Length];
            for (int c = 0; c < Aps.Length; c++) ab[c] = new double[Aps[c] + spread];
        }
        public void Process(double[] x, int cnt)
        {
            for (int i = 0; i < cnt; i++)
            {
                h1 += hk * (x[i] - h1); double y1 = x[i] - h1;
                h2 += hk * (y1 - h2); double inp = y1 - h2;
                double outp = 0;
                for (int c = 0; c < cb.Length; c++)
                {
                    double[] buf = cb[c]; int idx = ci[c];
                    double o = buf[idx];
                    store[c] = o * (1 - damp) + store[c] * damp;
                    buf[idx] = inp * 0.015 + store[c] * feedback;
                    ci[c] = (idx + 1) % buf.Length;
                    outp += o;
                }
                for (int c = 0; c < ab.Length; c++)
                {
                    double[] buf = ab[c]; int idx = ai[c];
                    double b = buf[idx];
                    buf[idx] = outp + b * 0.5;
                    outp = b - outp;
                    ai[c] = (idx + 1) % buf.Length;
                }
                x[i] = x[i] * dry + outp * wet * 8;
            }
        }
    }

    class LowPass
    {
        double k, a, b;
        public LowPass(double fc) { k = 1 - Math.Exp(-TAU * fc / SR); }
        public void Process(double[] x, int cnt) { for (int i = 0; i < cnt; i++) { a += k * (x[i] - a); b += k * (a - b); x[i] = b; } }
    }

    // ФВЧ 2-го порядка (два каскада по 6 дБ/окт)
    class HighPass
    {
        double k, a, b;
        public HighPass(double fc) { k = 1 - Math.Exp(-TAU * fc / SR); }
        public void Process(double[] x, int cnt)
        {
            for (int i = 0; i < cnt; i++) { a += k * (x[i] - a); double y = x[i] - a; b += k * (y - b); x[i] = y - b; }
        }
    }

    // ---------- Рендер блоками ----------

    // Выбор событий, звучащих в [g0, g1): список отсортирован по началу, длина событий не больше maxLen
    static List<T> Active<T>(List<T> all, Func<T, long> start, Func<T, long> end, long maxLen, long g0, long g1, ref int from)
    {
        while (from < all.Count && start(all[from]) + maxLen < g0) from++;
        var r = new List<T>();
        for (int q = from; q < all.Count && start(all[q]) < g1; q++)
            if (end(all[q]) > g0) r.Add(all[q]);
        return r;
    }

    // Проход по всему треку: sink получает готовые блоки (после обработки, огибающей и до нормализации). Возвращает пик.
    static double RenderPass(Plan p, Action<double[], double[], int> sink, string label)
    {
        long n = p.n;
        double[] L = new double[Block], R = new double[Block], wl = new double[Block], wr = new double[Block];
        var revL = new Reverb(0); var revR = new Reverb(23);
        var disL = new Distant(0.7, 1.5); var disR = new Distant(0.75, 1.45);
        LowPass lpL = null, lpR = null; HighPass hpL = null, hpR = null;
        // до мажор: тёплый бас без суб-баса, верх до ~3.5 кГц; спокойный: верх ~2.5 (3.5) кГц, всё ниже ~65 Гц убрано;
        // тёмный: срез верхов ~1100 Гц, как у эталона, где выше 1 кГц почти ничего нет
        if (p.keyC) { double lp = LowPassHz > 0 ? LowPassHz : 3500; lpL = new LowPass(lp); lpR = new LowPass(lp); hpL = new HighPass(45); hpR = new HighPass(45); }
        else if (p.calm) { double lp = Bright ? 3500 : 2500; lpL = new LowPass(lp); lpR = new LowPass(lp); hpL = new HighPass(65); hpR = new HighPass(65); }
        else if (p.dark) { lpL = new LowPass(1100); lpR = new LowPass(1100); }

        int threads = Threads > 0 ? Threads : Environment.ProcessorCount;
        int padFrom = 0, bowlFrom = 0, callFrom = 0, noteFrom = 0;
        long fadeIn = (long)(FadeInSec * SR), fadeOut = (long)(FadeOutSec * SR);
        double peak = 1e-9;
        var sw = Stopwatch.StartNew(); double lastLog = 0;

        for (long g0 = 0; g0 < n; g0 += Block)
        {
            int cnt = (int)Math.Min(Block, n - g0);
            long g1 = g0 + cnt;
            var pads = Active(p.pads, v => v.i0, v => v.i1, 25L * SR, g0, g1, ref padFrom);
            if (!p.keyC) pads = p.pads;
            var bowls = Active(p.bowls, b => b.start, b => b.start + b.len, 30L * SR, g0, g1, ref bowlFrom);
            var notes = Active(p.notes, x => x.start, x => x.start + x.len, 20L * SR, g0, g1, ref noteFrom);

            // Киты: сухой стон → "даль" (с состоянием), последовательно для каждого канала
            if (p.whales_on)
            {
                Array.Clear(wl, 0, cnt); Array.Clear(wr, 0, cnt);
                var calls = Active(p.calls, w => w.start, w => w.start + w.len, 6L * SR, g0, g1, ref callFrom);
                foreach (var w in calls)
                {
                    if (w.samples == null) w.samples = WhaleSamples(w);
                    long a0 = Math.Max(g0, w.start), a1 = Math.Min(g1, w.start + w.len);
                    for (long g = a0; g < a1; g++)
                    {
                        double s = w.samples[g - w.start];
                        wl[g - g0] += s * w.gl; wr[g - g0] += s * w.gr;
                    }
                    if (w.start + w.len <= g1) w.samples = null;   // стон закончился — память больше не нужна
                }
                disL.Process(wl, cnt, g0); disR.Process(wr, cnt, g0);
            }

            // Сухие слои — параллельно по кускам блока
            Array.Clear(L, 0, cnt); Array.Clear(R, 0, cnt);
            int parts = threads * 4, step = (cnt + parts - 1) / parts;
            Parallel.For(0, parts, new ParallelOptions { MaxDegreeOfParallelism = threads }, part =>
            {
                int off = part * step, c = Math.Min(step, cnt - off);
                if (c > 0) Synth(p, g0 + off, c, L, R, off, pads, bowls, notes, wl, wr);
            });

            // Реверберация, фильтры, бинауральные биения, огибающая — каждый канал в своём потоке
            double[] pk = new double[2];
            Parallel.For(0, 2, c =>
            {
                double[] x = c == 0 ? L : R;
                (c == 0 ? revL : revR).Process(x, cnt);
                var lp = c == 0 ? lpL : lpR; if (lp != null) lp.Process(x, cnt);
                var hp = c == 0 ? hpL : hpR; if (hp != null) hp.Process(x, cnt);
                // Мягкая пульсация громкости (изохронный ритм, слышен и в колонках)
                if (PulseDepth > 0)
                    for (int i = 0; i < cnt; i++) { double t = (double)(g0 + i) / SR; x[i] *= 1 - PulseDepth * (0.5 + 0.5 * Math.Sin(TAU * PulseHz * t)); }
                // Бинауральные биения (только в наушниках) — после реверберации, чтобы каналы не смешивались
                if (p.binaural_on)
                {
                    double f = c == 0 ? p.carrier : p.carrier + p.beatHz;
                    for (int i = 0; i < cnt; i++) { double t = (double)(g0 + i) / SR; x[i] += p.binLvl * Math.Sin(TAU * f * t); }
                }
                // Плавное появление 10 с и затухание 15 с
                double m = 0;
                for (int i = 0; i < cnt; i++)
                {
                    long g = g0 + i;
                    double gain = 1;
                    if (g < fadeIn) gain = Math.Pow((double)g / fadeIn, 2);
                    if (g > n - fadeOut) gain = Math.Pow((double)(n - g) / fadeOut, 2);
                    x[i] *= gain;
                    m = Math.Max(m, Math.Abs(x[i]));
                }
                pk[c] = m;
            });
            peak = Math.Max(peak, Math.Max(pk[0], pk[1]));

            if (sink != null) sink(L, R, cnt);

            double el = sw.Elapsed.TotalSeconds;
            if (el - lastLog >= 15 || g1 == n)
            {
                lastLog = el;
                double done = (double)g1 / n;
                Console.WriteLine(string.Format("  {0}: {1,5:F1}%  ({2} из {3}), прошло {4}, осталось ~{5}",
                    label, 100 * done, Hms(g1 / (double)SR), Hms(n / (double)SR), Hms(el), Hms(el / done - el)));
            }
        }
        return peak;
    }

    static string Hms(double s)
    {
        var ts = TimeSpan.FromSeconds(Math.Max(0, s));
        return string.Format("{0}:{1:D2}:{2:D2}", (int)ts.TotalHours, ts.Minutes, ts.Seconds);
    }

    // Заголовок WAV 16 бит стерео; больше 4 ГБ — RF64 (ds64 хранит 64-битные размеры)
    static void WriteHeader(BinaryWriter bw, long n)
    {
        long dataLen = n * 4;
        bool rf64 = 36 + dataLen > uint.MaxValue;
        bw.Write((rf64 ? "RF64" : "RIFF").ToCharArray());
        bw.Write(rf64 ? uint.MaxValue : (uint)(36 + dataLen));
        bw.Write("WAVE".ToCharArray());
        if (rf64)
        {
            bw.Write("ds64".ToCharArray()); bw.Write(28);
            bw.Write(72 + dataLen); bw.Write(dataLen); bw.Write(n); bw.Write(0);
        }
        bw.Write("fmt ".ToCharArray()); bw.Write(16); bw.Write((short)1); bw.Write((short)2);
        bw.Write(SR); bw.Write(SR * 4); bw.Write((short)4); bw.Write((short)16);
        bw.Write("data".ToCharArray()); bw.Write(rf64 ? uint.MaxValue : (uint)dataLen);
    }

    static short Pcm(double v, double norm) { return (short)Math.Round(Math.Max(-1, Math.Min(1, v * norm)) * 32767); }

    // Весь трек: одна часть (как раньше) или несколько частей с разной высотой строя (SegA4).
    // Стык частей: последние SegFade секунд части k (затухание) складываются с первыми SegFade секундами части k+1 (появление).
    static double RenderAll(double seconds, int seed, bool stars_on, bool bowls_on, bool whales_on, bool piano_on, bool binaural_on, bool dark, bool calm, bool keyC,
                            Action<double[], double[], int> sink, string label)
    {
        if (SegA4 == null || SegA4.Length < 2)
        {
            if (SegA4 != null) A4 = SegA4[0];
            FadeInSec = 10; FadeOutSec = 15;
            return RenderPass(MakePlan(seconds, seed, stars_on, bowls_on, whales_on, piano_on, binaural_on, dark, calm, keyC), sink, label);
        }
        int k = SegA4.Length;
        long N = (long)(seconds * SR), ov = (long)(SegFade * SR);
        long segN = (N + (k - 1) * ov) / k;
        if (segN < 2 * ov + SR) throw new Exception("Части слишком короткие для затухания " + SegFade + " с: увеличьте длину или уменьшите -SegmentFade");
        double[] outL = new double[Block], outR = new double[Block]; int outCnt = 0;
        double[] tailL = new double[ov], tailR = new double[ov], nextL = new double[ov], nextR = new double[ov];
        double peak = 1e-9;
        Action<double, double> emit = (l, r) =>
        {
            outL[outCnt] = l; outR[outCnt] = r; outCnt++;
            peak = Math.Max(peak, Math.Max(Math.Abs(l), Math.Abs(r)));
            if (outCnt == Block) { if (sink != null) sink(outL, outR, outCnt); outCnt = 0; }
        };
        for (int s = 0; s < k; s++)
        {
            long n = s < k - 1 ? segN : N + (k - 1) * ov - (k - 1) * segN;
            A4 = SegA4[s];
            FadeInSec = s == 0 ? 10 : SegFade;
            FadeOutSec = s == k - 1 ? 15 : SegFade;
            var p = MakePlan((double)n / SR, seed + s, stars_on, bowls_on, whales_on, piano_on, binaural_on, dark, calm, keyC, n);
            long j = 0;   // позиция внутри части
            bool first = s == 0, last = s == k - 1;
            RenderPass(p, (L, R, cnt) =>
            {
                for (int i = 0; i < cnt; i++, j++)
                {
                    if (!last && j >= n - ov) { nextL[j - (n - ov)] = L[i]; nextR[j - (n - ov)] = R[i]; }   // хвост — сложится со следующей частью
                    else if (!first && j < ov) emit(L[i] + tailL[j], R[i] + tailR[j]);                      // стык с хвостом предыдущей
                    else emit(L[i], R[i]);
                }
            }, string.Format("{0}, часть {1}/{2} (A4 = {3:F1} Гц)", label, s + 1, k, SegA4[s]));
            var t = tailL; tailL = nextL; nextL = t; t = tailR; tailR = nextR; nextR = t;
        }
        if (outCnt > 0 && sink != null) sink(outL, outR, outCnt);
        return peak;
    }

    public static void Render(string path, double seconds, int seed, bool stars_on, bool bowls_on, bool whales_on, bool piano_on, bool binaural_on, bool dark, bool calm, bool keyC, bool twoPass)
    {
        long n = (long)(seconds * SR);
        byte[] pcm = new byte[Block * 4];
        Func<Action<double[], double[], int>, string, double> pass = (sink, label) =>
            RenderAll(seconds, seed, stars_on, bowls_on, whales_on, piano_on, binaural_on, dark, calm, keyC, sink, label);

        using (var bw = new BinaryWriter(new FileStream(path, FileMode.Create, FileAccess.Write, FileShare.None, 1 << 20)))
        {
            WriteHeader(bw, n);
            double norm;
            if (twoPass)
            {
                double peak = pass(null, "проход 1/2 (поиск пика)");
                norm = 0.63 / peak;   // ≈ −4 дБ: запас, чтобы не перегружать динамики на низах
                pass((L, R, cnt) =>
                {
                    for (int i = 0; i < cnt; i++)
                    {
                        short l = Pcm(L[i], norm), r = Pcm(R[i], norm);
                        pcm[4 * i] = (byte)l; pcm[4 * i + 1] = (byte)(l >> 8); pcm[4 * i + 2] = (byte)r; pcm[4 * i + 3] = (byte)(r >> 8);
                    }
                    bw.Write(pcm, 0, cnt * 4);
                }, "проход 2/2 (запись)");
            }
            else
            {
                // Промежуточный файл: float32, L/R вперемешку
                string tmp = path + ".part.f32";
                float[] fb = new float[Block * 2]; byte[] raw = new byte[Block * 8];
                double peak;
                try
                {
                    using (var fs = new FileStream(tmp, FileMode.Create, FileAccess.Write, FileShare.None, 1 << 20))
                    {
                        peak = pass((L, R, cnt) =>
                        {
                            for (int i = 0; i < cnt; i++) { fb[2 * i] = (float)L[i]; fb[2 * i + 1] = (float)R[i]; }
                            Buffer.BlockCopy(fb, 0, raw, 0, cnt * 8);
                            fs.Write(raw, 0, cnt * 8);
                        }, "рендер");
                    }
                    norm = 0.63 / peak;   // ≈ −4 дБ: запас, чтобы не перегружать динамики на низах
                    Console.WriteLine("  нормализация и запись WAV...");
                    using (var fs = new FileStream(tmp, FileMode.Open, FileAccess.Read, FileShare.None, 1 << 20))
                    {
                        for (long g0 = 0; g0 < n; g0 += Block)
                        {
                            int cnt = (int)Math.Min(Block, n - g0), need = cnt * 8, got = 0;
                            while (got < need) { int r = fs.Read(raw, got, need - got); if (r <= 0) throw new IOException("промежуточный файл обрезан"); got += r; }
                            Buffer.BlockCopy(raw, 0, fb, 0, need);
                            for (int i = 0; i < cnt; i++)
                            {
                                short l = Pcm(fb[2 * i], norm), r = Pcm(fb[2 * i + 1], norm);
                                pcm[4 * i] = (byte)l; pcm[4 * i + 1] = (byte)(l >> 8); pcm[4 * i + 2] = (byte)r; pcm[4 * i + 3] = (byte)(r >> 8);
                            }
                            bw.Write(pcm, 0, cnt * 4);
                        }
                    }
                }
                finally { if (File.Exists(tmp)) File.Delete(tmp); }
            }
        }
    }
}
"@

if ($Hours -gt 0) { $Seconds = $Hours * 3600 }

# Пресеты чакр. Явно заданные параметры не перезаписываются.
if ($Chakra -eq 1) {
    # Муладхара: до мажор, тёплый бас без суб-баса, тета 5 Гц — звук v9
    $KeyC = $true
    if (-not $PSBoundParameters.ContainsKey('NoStars')) { $NoStars = $true }
    if (-not $PSBoundParameters.ContainsKey('NoBowls')) { $NoBowls = $true }
    if (-not $PSBoundParameters.ContainsKey('PianoGain')) { $PianoGain = 2.4 }
    if (-not $PSBoundParameters.ContainsKey('PianoMin')) { $PianoMin = 3 }
    if (-not $PSBoundParameters.ContainsKey('PianoMax')) { $PianoMax = 6 }
} elseif ($Chakra -ne 0) { throw "Пресет готов только для -Chakra 1 (муладхара)" }

# Пресет по эталону Celestial Spirit: ре минор, тёмный (верх до 1.4 кГц), широкое стерео и бас, пульсация 1 Гц, ноты раз в 5–9 с
$celestialSet = @{ ChordSet = 0; WidePads = $false; LowPassHz = 0; PulseHz = 0; PulseDepth = 0; BassDetune = 0 }
if ($Celestial) {
    $KeyC = $true
    $celestialSet = @{ ChordSet = 1; WidePads = $true; LowPassHz = 1400; PulseHz = 1.0; PulseDepth = 0.12; BassDetune = 0.005 }
    if (-not $PSBoundParameters.ContainsKey('NoStars')) { $NoStars = $true }
    if (-not $PSBoundParameters.ContainsKey('NoBowls')) { $NoBowls = $true }
    if (-not $PSBoundParameters.ContainsKey('PianoGain')) { $PianoGain = 3.0 }
    if (-not $PSBoundParameters.ContainsKey('PianoMin')) { $PianoMin = 5 }
    if (-not $PSBoundParameters.ContainsKey('PianoMax')) { $PianoMax = 9 }
}

# Частота -> высота строя A4. 432 = обычный строй A = 432 Гц.
# Другое значение = тоника: высота сдвигается так, чтобы до совпала с этой частотой
# (в ближайшей октаве к C4 = 256.9 Гц, сдвиг не больше ±6 полутонов).
function Get-A4([double]$hz) {
    if ($hz -eq 432) { "  432 Гц: строй A4 = 432 Гц, C4 = 256.87 Гц"; return 432.0 }
    $shift = 12 * [math]::Log($hz / (432 * [math]::Pow(2, -9 / 12)), 2)
    while ($shift -gt 6) { $shift -= 12 }
    while ($shift -le -6) { $shift += 12 }
    $r = 432 * [math]::Pow(2, $shift / 12)
    "  $hz Гц: тоника C4 = $([math]::Round($r * [math]::Pow(2, -9 / 12), 2)) Гц, сдвиг $([math]::Round($shift, 2)) полутона, A4 = $([math]::Round($r, 2)) Гц"
    return $r
}
$a4 = 432.0
$segA4 = $null
if ($Segments) {
    $hzList = $Segments -split '[,; ]+' | Where-Object { $_ } | ForEach-Object { [double]$_ }
    "Части ($($hzList.Count)), стык $SegmentFade с:"
    $list = foreach ($hz in $hzList) { if ($hz -le 0) { throw "Частота части должна быть больше 0: $hz" }; $res = Get-A4 $hz; Write-Host $res[0]; $res[-1] }
    $segA4 = [double[]]@($list)
} elseif ($Tonic -gt 0) {
    $res = Get-A4 $Tonic; $res[0..($res.Count - 2)]; $a4 = $res[-1]
}
$path = [IO.Path]::GetFullPath($Out, (Get-Location).Path)
$wavGb = $Seconds * 44100 * 4 / 1GB
"Длина: $([TimeSpan]::FromSeconds($Seconds).ToString('h\:mm\:ss')), WAV ≈ $([math]::Round($wavGb, 2)) ГБ" +
    $(if ($TwoPass) { ", два прохода" } else { ", промежуточный файл ≈ $([math]::Round(2 * $wavGb, 2)) ГБ" }) +
    $(if (36 + $Seconds * 44100 * 4 -gt [uint32]::MaxValue) { ", формат RF64 (больше 4 ГБ)" } else { "" })
$sw = [Diagnostics.Stopwatch]::StartNew()
[AmbientSynth]::PianoGain = $PianoGain
[AmbientSynth]::PianoMin = $PianoMin
[AmbientSynth]::PianoMax = $PianoMax
[AmbientSynth]::Bright = [bool]$Bright
[AmbientSynth]::Threads = $Threads
[AmbientSynth]::A4 = $a4
[AmbientSynth]::SegA4 = $segA4
[AmbientSynth]::SegFade = $SegmentFade
foreach ($k in $celestialSet.Keys) { [AmbientSynth]::$k = $celestialSet[$k] }
[AmbientSynth]::Render($path, $Seconds, $Seed, -not $NoStars, -not $NoBowls, -not $NoWhales, -not $NoPiano, -not $NoBinaural, [bool]($Dark -or $Calm), [bool]$Calm, [bool]$KeyC, [bool]$TwoPass)
"Готово: $path ($([TimeSpan]::FromSeconds($sw.Elapsed.TotalSeconds).ToString('h\:mm\:ss')))"
