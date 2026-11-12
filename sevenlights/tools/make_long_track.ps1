# Растягивает один или несколько коротких треков на нужную длину БЕЗ заметных швов.
#
# Запуск:
#   pwsh -File make_long_track.ps1 -In track.mp3 -TrimStart 8 -TrimEnd 6 -Hours 3 -Out long.wav
#   pwsh -File make_long_track.ps1 -In a.mp3,b.mp3,c.mp3 -TrimStart 8 -TrimEnd 6 -Hours 3 -Out long.flac
#   pwsh -File make_long_track.ps1 -In track.mp3 -TrimStart 8 -TrimEnd 6 -Mode Crossfade -Fade 20 -Hours 3 -Out long.wav
#
# Режим Smart (по умолчанию) — подбор стыка по звуку:
#   Треки идут по кругу A → B → C → A. На каждом стыке программа ищет в конце одного трека и в начале следующего
#   две точки, где звучание совпадает (те же ноты, близкая фаза волны), и склеивает их коротким кроссфейдом
#   (0.5 с, если звук совпал; 3 или 8 с, если треки заметно разные). Для одного трека конец «замыкается» на его же начало.
# Режим Crossfade — классическое наложение конца на начало на -Fade секунд (по умолчанию 20 с), без поиска.
#
# Параметры
#   -In          один или несколько аудиофайлов (wav, mp3, flac, m4a...), порядок = порядок в круге
#   -Out         итоговый файл (.wav / .flac / .mp3), по умолчанию long.wav (3 ч WAV ≈ 1.9 ГБ)
#   -Hours       длина итога в часах (3)
#   -TrimStart / -TrimEnd   секунд срезать в начале/конце КАЖДОГО трека (нарастание и затухание; у треков нейросетей ~6–8 с)
#   -HighPass    срез баса ниже этой частоты, Гц (70). 0 — без среза. Сверхнизкий бас (30–60 Гц) звучит тревожно и хрипит на колонках
#   -Fade        длина стыка, с. Smart по умолчанию подбирает сама для каждого стыка: звук совпадает (сходство ≥ 0.8) — 0.5 с,
#                похоже (0.6–0.8) — 3 с, разная музыка — 8 с. Crossfade по умолчанию 20 с
#   -Search      как далеко от краёв искать точки стыка, с (30)
#   -FadeIn / -FadeOut   появление и затухание всего итога, с (10 и 15)
#   -Check       собрать ровно ОДИН круг (те же стыки, что в длинной версии) — для проверки авторских прав на YouTube
#                до сборки многочасового файла. -Hours игнорируется
#
# Нужны ffmpeg 4.4+ и ffprobe в PATH. Проверено в PowerShell 7 (pwsh); десятичная точка не зависит от локали.
# В Windows PowerShell 5.1 скрипт не проверялся: русские сообщения могут отображаться кракозябрами.
param(
    [Parameter(Mandatory)][string[]]$In,
    [string]$Out = "long.wav",
    [double]$Hours = 3,
    [ValidateSet('Smart', 'Crossfade')][string]$Mode = 'Smart',
    [double]$TrimStart = 0,
    [double]$TrimEnd = 0,
    [double]$HighPass = 70,
    [double]$Fade = 0,
    [double]$Search = 30,
    [double]$FadeIn = 10,
    [double]$FadeOut = 15,
    [switch]$Check
)

$ErrorActionPreference = 'Stop'
$inv = [Globalization.CultureInfo]::InvariantCulture
function F([double]$x) { $x.ToString('0.######', $inv) }
function T([double]$s) { [TimeSpan]::FromSeconds($s).ToString('h\:mm\:ss\.f') }

foreach ($tool in 'ffmpeg', 'ffprobe') {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) { throw "Не найден ${tool}: установите ffmpeg и добавьте его в PATH" }
}
$autoFade = ($Mode -eq 'Smart' -and $Fade -le 0)
if ($Fade -le 0) { $Fade = if ($Mode -eq 'Smart') { 8 } else { 20 } }   # в авто-режиме Fade — максимум длины стыка
if ($Fade -gt 60) { throw "-Fade должен быть не больше 60 секунд" }

# При запуске через `pwsh -File ... -In a.wav,b.wav` список приходит одной строкой «a.wav,b.wav»: разбираем по запятым
$names = @($In | ForEach-Object { $_ -split ',' } | Where-Object { $_.Trim() } | ForEach-Object { $_.Trim() })
$missing = @($names | Where-Object { -not (Test-Path -LiteralPath $_) })
if ($missing.Count) {
    Write-Host "Не найдены файлы (папка: $((Get-Location).Path)):" -ForegroundColor Red
    $missing | ForEach-Object { Write-Host "  $_" -ForegroundColor Red }
    Write-Host "Аудиофайлы в этой папке:" -ForegroundColor Yellow
    Get-ChildItem -File | Where-Object { $_.Extension -match '^\.(mp3|wav|flac|m4a|ogg)$' } | ForEach-Object { Write-Host "  $($_.Name)" }
    exit 1
}
$files = @($names | ForEach-Object { (Resolve-Path -LiteralPath $_).Path })
$n = $files.Count
$len = @()
foreach ($f in $files) {
    $d = [double]::Parse((& ffprobe -v error -show_entries format=duration -of csv=p=0 $f | Select-Object -First 1).Trim(), $inv)
    $l = $d - $TrimStart - $TrimEnd
    if ($l -lt 2.5 * $Fade + 5) { throw "Трек '$f' после обрезки ($([math]::Round($l,1)) с) слишком короткий для стыка $Fade с" }
    $len += $l
}
$total = $Hours * 3600

# Срез баса: два каскада по 2 полюса = 24 дБ/окт
$hpf = if ($HighPass -gt 0) { "highpass=f=$(F $HighPass):poles=2,highpass=f=$(F $HighPass):poles=2," } else { '' }

$tmp = Join-Path ([IO.Path]::GetTempPath()) ("longtrack_" + [Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $tmp | Out-Null
try {
    $sb = New-Object Text.StringBuilder
    $report = @()

    if ($Mode -eq 'Crossfade') {
        # Классика: A ~ B ~ ... ~ A с кроссфейдом -Fade секунд, круг вырезается так, чтобы конец снова перетекал в начало
        $unit = ($len | Measure-Object -Sum).Sum - $n * $Fade
        $chainEnd = ($len | Measure-Object -Sum).Sum - ($n - 1) * $Fade
        $inputs = @($files) + @($files[0]); $lens = @($len) + @($len[0])
        for ($i = 0; $i -lt $inputs.Count; $i++) {
            [void]$sb.AppendLine("[${i}:a]${hpf}aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,atrim=start=$(F $TrimStart):end=$(F ($TrimStart + $lens[$i])),asetpts=PTS-STARTPTS[c$i];")
        }
        $prev = 'c0'
        for ($i = 1; $i -lt $inputs.Count; $i++) {
            [void]$sb.AppendLine("[$prev][c$i]acrossfade=d=$(F $Fade):c1=qsin:c2=qsin[x$i];")
            $prev = "x$i"
        }
        [void]$sb.AppendLine("[$prev]atrim=start=$(F $Fade):end=$(F $chainEnd),asetpts=PTS-STARTPTS[unit]")
        $ffInputs = $inputs
    }
    else {
        # Smart: сначала ищем точки стыка (на 8 кГц, моно), потом собираем
        $cs = @'
using System;
using System.IO;
using System.Collections.Generic;
public static class Splice
{
    const int SR = 8000;
    const double Ctx = 2.0, Win = 0.5, Fine = 0.4, Shift = 0.03;
    static void Fft(double[] re, double[] im)
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
    static float[] Load(string path)
    {
        byte[] b = File.ReadAllBytes(path);
        float[] x = new float[b.Length / 4];
        Buffer.BlockCopy(b, 0, x, 0, x.Length * 4);
        return x;
    }
    // Описание звука перед моментом t: лог-спектры 4 окон по 0.5 с (0–1 кГц), без среднего и нормированные
    static double[] Feature(float[] x, double t)
    {
        int n = (int)(Win * SR), N = 4096, bins = (int)(1000.0 / ((double)SR / N));
        double[] f = new double[bins * (int)(Ctx / Win)];
        double[] re = new double[N], im = new double[N];
        for (int k = 0; k < (int)(Ctx / Win); k++)
        {
            int e = (int)((t - k * Win) * SR);
            Array.Clear(re, 0, N); Array.Clear(im, 0, N);
            for (int i = 0; i < n; i++) re[i] = x[e - n + i] * (0.5 - 0.5 * Math.Cos(2 * Math.PI * i / (n - 1)));
            Fft(re, im);
            for (int i = 0; i < bins; i++) f[k * bins + i] = Math.Log(Math.Sqrt(re[i] * re[i] + im[i] * im[i]) + 1e-4);
        }
        double mean = 0; for (int i = 0; i < f.Length; i++) mean += f[i]; mean /= f.Length;
        double nrm = 0; for (int i = 0; i < f.Length; i++) { f[i] -= mean; nrm += f[i] * f[i]; }
        nrm = Math.Sqrt(nrm) + 1e-12; for (int i = 0; i < f.Length; i++) f[i] /= nrm;
        return f;
    }
    // Возвращает {e, s, корреляция волны, сходство контекста}: конец петли в треке A на e секунде -> продолжение трека B с s секунды
    public static double[] Find(string fileA, string fileB, double eMin, double eMax, double sMin, double sMax)
    {
        float[] xa = Load(fileA), xb = Load(fileB);
        double step = 0.1;
        List<double> te = new List<double>(), ts = new List<double>();
        for (double t = eMin; t <= eMax && t * SR < xa.Length; t += step) te.Add(t);
        for (double t = sMin; t <= sMax && t * SR < xb.Length; t += step) ts.Add(t);
        double[][] fe = new double[te.Count][], fs = new double[ts.Count][];
        for (int i = 0; i < te.Count; i++) fe[i] = Feature(xa, te[i]);
        for (int i = 0; i < ts.Count; i++) fs[i] = Feature(xb, ts[i]);
        // Топ-60 пар по сходству контекста
        List<double[]> top = new List<double[]>();
        double minTop = -2;
        for (int i = 0; i < te.Count; i++)
            for (int j = 0; j < ts.Count; j++)
            {
                double s = 0; double[] a = fe[i], b = fs[j];
                for (int k = 0; k < a.Length; k++) s += a[k] * b[k];
                if (top.Count < 60 || s > minTop)
                {
                    top.Add(new double[] { s, i, j });
                    if (top.Count > 60)
                    {
                        top.Sort(delegate (double[] p, double[] q) { return q[0].CompareTo(p[0]); });
                        top.RemoveRange(60, top.Count - 60);
                        minTop = top[top.Count - 1][0];
                    }
                }
            }
        // Точная подгонка фазы: сдвиг ±30 мс, окно 0.4 с
        int nf = (int)(Fine * SR), sh = (int)(Shift * SR);
        double[] best = null;
        foreach (double[] c in top)
        {
            double e = te[(int)c[1]], s0 = ts[(int)c[2]];
            int ie = (int)(e * SR);
            if (ie - nf < 0 || ie > xa.Length) continue;
            double ee = 0; for (int i = 0; i < nf; i++) ee += (double)xa[ie - nf + i] * xa[ie - nf + i];
            for (int d = -sh; d <= sh; d++)
            {
                int i0 = (int)(s0 * SR) + d;
                if (i0 - nf < 0 || i0 > xb.Length) continue;
                double dot = 0, ss = 0;
                for (int i = 0; i < nf; i++) { double v = xb[i0 - nf + i]; dot += xa[ie - nf + i] * v; ss += v * v; }
                double corr = dot / Math.Sqrt(ee * ss + 1e-12);
                if (best == null || corr > best[2]) best = new double[] { e, (double)i0 / SR, corr, c[0] };
            }
        }
        return best;
    }
}
'@
        Add-Type -TypeDefinition $cs
        # Каждый трек: срез баса, 8 кГц моно, сырой float32
        $raws = @()
        for ($i = 0; $i -lt $n; $i++) {
            $raw = Join-Path $tmp "an$i.f32"
            & ffmpeg -v error -y -i $files[$i] -af "${hpf}lowpass=f=1500" -f f32le -ac 1 -ar 8000 $raw
            if ($LASTEXITCODE -ne 0) { throw "ffmpeg не смог прочитать '$($files[$i])'" }
            $raws += $raw
        }
        # Стыки: j = конец трека j -> начало трека (j+1) % n
        $e = @(); $s = @(); $score = @()
        for ($j = 0; $j -lt $n; $j++) {
            $k = ($j + 1) % $n
            $eMax = $TrimStart + $len[$j]; $eMin = [math]::Max($TrimStart + 5, $eMax - $Search)
            $sMin = $TrimStart + [math]::Max(2.0, $Fade) + 0.1; $sMax = [math]::Min($TrimStart + $Search, $TrimStart + $len[$k] - 5)
            $best = [Splice]::Find($raws[$j], $raws[$k], $eMin, $eMax, $sMin, $sMax)
            if ($null -eq $best) { throw "Не удалось подобрать стык трека $($j+1) -> $($k+1)" }
            $e += $best[0]; $s += $best[1]; $score += , @($best[2], $best[3])
        }
        # Find вернул начало в СЛЕДУЮЩЕМ треке (стык j -> j+1): переставляем, чтобы $s[i] было началом трека i
        # (исправлено 12.11.2026: раньше начало трека j+1 применялось к треку j, и подобранная по волне точка стыка не совпадала)
        $s = @(for ($i = 0; $i -lt $n; $i++) { $s[($i - 1 + $n) % $n] })
        # Длина стыка для каждого шва: авто (по сходству звука) или заданная
        $cj = @()
        for ($j = 0; $j -lt $n; $j++) {
            if ($autoFade) { $cj += $(if ($score[$j][1] -ge 0.8) { 0.5 } elseif ($score[$j][1] -ge 0.6) { 3.0 } else { 8.0 }) } else { $cj += $Fade }
        }
        # Круг: тела треков [s_i, e_i - c_i], стыки = конец трека i с «предысторией» начала трека i+1
        $unit = 0.0
        for ($i = 0; $i -lt $n; $i++) { $unit += $e[$i] - $s[$i] }
        for ($i = 0; $i -lt $n; $i++) {
            $cEnd = $cj[$i]; $cStart = $cj[($i - 1 + $n) % $n]   # стык после этого трека и стык перед ним
            [void]$sb.AppendLine("[${i}:a]${hpf}aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,asplit=3[b$i][t$i][g$i];")
            [void]$sb.AppendLine("[b$i]atrim=start=$(F $s[$i]):end=$(F ($e[$i] - $cEnd)),asetpts=PTS-STARTPTS[body$i];")
            [void]$sb.AppendLine("[t$i]atrim=start=$(F ($e[$i] - $cEnd)):end=$(F $e[$i]),asetpts=PTS-STARTPTS[tail$i];")
            [void]$sb.AppendLine("[g$i]atrim=start=$(F ($s[$i] - $cStart)):end=$(F $s[$i]),asetpts=PTS-STARTPTS[ghost$i];")
        }
        $parts = @()
        for ($i = 0; $i -lt $n; $i++) {
            $k = ($i + 1) % $n
            $curve = if ($score[$i][0] -ge 0.6) { 'tri' } else { 'qsin' }   # линейный кроссфейд для похожих волн, равномощный для разных
            [void]$sb.AppendLine("[tail$i]afade=t=out:d=$(F $cj[$i]):curve=$curve[to$i];")
            [void]$sb.AppendLine("[ghost$k]afade=t=in:d=$(F $cj[$i]):curve=$curve[gi$i];")
            [void]$sb.AppendLine("[to$i][gi$i]amix=inputs=2:duration=longest:normalize=0[join$i];")
            $parts += "[body$i][join$i]"
        }
        [void]$sb.AppendLine(($parts -join '') + "concat=n=$(2 * $n):v=0:a=1[unit]")
        $ffInputs = $files
        $pos = 0.0
        for ($i = 0; $i -lt $n; $i++) {
            $pos += $e[$i] - $s[$i]
            $report += ("  Шов {0}: конец «{1}» {2} -> начало «{3}» {4}; волна {5:N2}, контекст {6:N2}; стык {7} с; в круге на {8}" -f ($i + 1), [IO.Path]::GetFileName($files[$i]), (T $e[$i]), [IO.Path]::GetFileName($files[($i + 1) % $n]), (T $s[($i + 1) % $n]), $score[$i][0], $score[$i][1], (F $cj[$i]), (T $pos))
        }
    }

    if ($Check) { $total = $unit }   # один круг для проверки (Content ID), длинный файл не нужен
    "Режим: $Mode; треков: $n; длина круга: $(T $unit); повторов круга: $([math]::Round($total / $unit, 1)); итог: $(T $total); срез баса: $(if ($HighPass -gt 0) { "$HighPass Гц" } else { 'нет' })"
    $report
    if ($unit -lt 600) { Write-Warning "Круг короче 10 минут: он повторится $([math]::Round($total / $unit)) раз, повторы будут слышны. Добавьте ещё треки (-In a.mp3,b.mp3,...)" }

    # Фильтр передаётся прямо в команде, одной строкой: -filter_complex_script устарел с ffmpeg 7 и в новых версиях может не работать
    $filter = ($sb.ToString() -replace "`r?`n", '')
    $unitWav = Join-Path $tmp 'unit.wav'
    $args1 = @('-y', '-loglevel', 'error')
    foreach ($f in $ffInputs) { $args1 += @('-i', $f) }
    $args1 += @('-filter_complex', $filter, '-map', '[unit]', '-c:a', 'pcm_f32le', $unitWav)
    & ffmpeg @args1
    if ($LASTEXITCODE -ne 0) { throw "ffmpeg не смог собрать круг (нужен ffmpeg 4.4 или новее)" }

    # Повтор круга на нужную длину + плавное появление и затухание всего итога
    $outPath = if ([IO.Path]::IsPathRooted($Out)) { $Out } else { Join-Path (Get-Location).Path $Out }
    $af = "afade=t=in:d=$(F $FadeIn),afade=t=out:st=$(F ($total - $FadeOut)):d=$(F $FadeOut)"
    $args2 = @('-y', '-loglevel', 'error', '-stream_loop', '-1', '-i', $unitWav, '-t', (F $total), '-af', $af)
    if ($outPath -match '\.wav$') { $args2 += @('-c:a', 'pcm_s16le') }
    elseif ($outPath -match '\.flac$') { $args2 += @('-c:a', 'flac') }
    elseif ($outPath -match '\.mp3$') { $args2 += @('-c:a', 'libmp3lame', '-b:a', '320k') }
    $args2 += @($outPath)
    & ffmpeg @args2
    if ($LASTEXITCODE -ne 0) { throw "ffmpeg не смог повторить круг" }
    "Готово: $outPath ($([math]::Round((Get-Item $outPath).Length / 1MB)) МБ)"
}
finally { Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue }
