# Растягивает короткий трек (или несколько) на нужную длину БЕСШОВНО: конец плавно перетекает в начало.
#
# Запуск:
#   pwsh -File make_long_track.ps1 -In track.wav -Hours 3 -Out long.wav
#   pwsh -File make_long_track.ps1 -In a.wav,b.wav,c.wav -Hours 3 -Fade 20 -Out long.wav
#   pwsh -File make_long_track.ps1 -In track.mp3 -TrimStart 4 -TrimEnd 6 -Hours 3 -Out long.wav
#
# Как это работает.
#   Берутся треки по кругу: A → B → C → A. На каждом стыке последние -Fade секунд одного трека затухают поверх
#   первых -Fade секунд следующего (равномощное смешивание, высота тона не меняется). Круг замыкается так,
#   что последний звук круга — это ровно то, что в треке звучало перед его началом, и круг можно повторять
#   сколько угодно: шва нет не только в смысле «нет щелчка», но и по самому звуку (стык — тот же кроссфейд).
#   Для одного трека круг короче трека на -Fade секунд.
#
# Параметры
#   -In          один или несколько аудиофайлов (wav, mp3, flac, m4a...)
#   -Out         итоговый файл (по умолчанию long.wav). WAV 3 часа стерео 44.1 кГц ≈ 1.9 ГБ
#   -Hours       длина итога в часах (по умолчанию 3)
#   -Fade        длина кроссфейда в секундах, 1–60 (по умолчанию 15; для медленного амбиента 15–30)
#   -TrimStart   сколько секунд срезать в начале каждого трека (если трек начинается с тишины/нарастания)
#   -TrimEnd     сколько секунд срезать в конце каждого трека (если трек заканчивается затуханием)
#   -FadeIn / -FadeOut  плавное появление и затухание всего итога, секунды (10 и 15)
#
# Нужны ffmpeg и ffprobe в PATH. Работает в PowerShell 7 и в Windows PowerShell 5.1 (десятичная точка не зависит от локали).
param(
    [Parameter(Mandatory)][string[]]$In,
    [string]$Out = "long.wav",
    [double]$Hours = 3,
    [double]$Fade = 15,
    [double]$TrimStart = 0,
    [double]$TrimEnd = 0,
    [double]$FadeIn = 10,
    [double]$FadeOut = 15
)

$ErrorActionPreference = 'Stop'
$inv = [Globalization.CultureInfo]::InvariantCulture
function F([double]$x) { $x.ToString('0.######', $inv) }

foreach ($tool in 'ffmpeg', 'ffprobe') {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) { throw "Не найден ${tool}: установите ffmpeg и добавьте его в PATH" }
}
if ($Fade -lt 1 -or $Fade -gt 60) { throw "-Fade должен быть от 1 до 60 секунд" }

# Длины треков после обрезки
# При запуске через `pwsh -File ... -In a.wav,b.wav` список приходит одной строкой «a.wav,b.wav»: разбираем по запятым
$files = @($In | ForEach-Object { $_ -split ',' } | Where-Object { $_.Trim() } | ForEach-Object { (Resolve-Path $_.Trim()).Path })
$len = @()
foreach ($f in $files) {
    $d = [double]::Parse((& ffprobe -v error -show_entries format=duration -of csv=p=0 $f | Select-Object -First 1).Trim(), $inv)
    $l = $d - $TrimStart - $TrimEnd
    if ($l -lt 2.5 * $Fade) { throw "Трек '$f' после обрезки ($([math]::Round($l,1)) с) короче 2.5 × Fade ($([math]::Round(2.5*$Fade,1)) с): уменьшите -Fade или -TrimStart/-TrimEnd" }
    $len += $l
}
$n = $files.Count
$unit = ($len | Measure-Object -Sum).Sum - $n * $Fade       # длина круга
$chainEnd = ($len | Measure-Object -Sum).Sum - ($n - 1) * $Fade   # длина цепочки A~B~...~N до замыкания
$total = $Hours * 3600
"Треков: $n, длина круга: $([TimeSpan]::FromSeconds($unit).ToString('h\:mm\:ss')), повторов круга: $([math]::Round($total / $unit, 1)), итог: $([TimeSpan]::FromSeconds($total).ToString('h\:mm\:ss'))"
if ($unit -lt 600) { Write-Warning "Круг короче 10 минут: на $Hours ч он повторится $([math]::Round($total / $unit)) раз, слушатель заметит повторы. Добавьте ещё треки (-In a.wav,b.wav,...)" }

# Фильтр: все входы приводятся к одному формату, обрезаются, склеиваются кроссфейдами; первый трек подаётся ещё раз в конец
$inputs = @($files) + @($files[0])
$lens = @($len) + @($len[0])
$sb = New-Object Text.StringBuilder
for ($i = 0; $i -lt $inputs.Count; $i++) {
    [void]$sb.AppendLine("[${i}:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,atrim=start=$(F $TrimStart):end=$(F ($TrimStart + $lens[$i])),asetpts=PTS-STARTPTS[c$i];")
}
$prev = 'c0'
for ($i = 1; $i -lt $inputs.Count; $i++) {
    [void]$sb.AppendLine("[$prev][c$i]acrossfade=d=$(F $Fade):c1=qsin:c2=qsin[x$i];")
    $prev = "x$i"
}
[void]$sb.AppendLine("[$prev]atrim=start=$(F $Fade):end=$(F $chainEnd),asetpts=PTS-STARTPTS[unit]")

$tmp = Join-Path ([IO.Path]::GetTempPath()) ("longtrack_" + [Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $tmp | Out-Null
try {
    $script = Join-Path $tmp 'filter.txt'
    [IO.File]::WriteAllText($script, $sb.ToString(), (New-Object Text.UTF8Encoding($false)))
    $unitWav = Join-Path $tmp 'unit.wav'
    $args1 = @('-y', '-loglevel', 'error')
    foreach ($f in $inputs) { $args1 += @('-i', $f) }
    $args1 += @('-filter_complex_script', $script, '-map', '[unit]', '-c:a', 'pcm_f32le', $unitWav)
    & ffmpeg @args1
    if ($LASTEXITCODE -ne 0) { throw "ffmpeg не смог собрать круг" }

    # Повтор круга на нужную длину + плавное появление и затухание всего итога
    $outPath = [IO.Path]::GetFullPath($Out, (Get-Location).Path)
    $af = "afade=t=in:d=$(F $FadeIn),afade=t=out:st=$(F ($total - $FadeOut)):d=$(F $FadeOut)"
    $args2 = @('-y', '-loglevel', 'error', '-stream_loop', '-1', '-i', $unitWav, '-t', (F $total), '-af', $af)
    if ($outPath -match '\.wav$') { $args2 += @('-c:a', 'pcm_s16le') }
    elseif ($outPath -match '\.flac$') { $args2 += @('-c:a', 'flac') }
    elseif ($outPath -match '\.mp3$') { $args2 += @('-c:a', 'libmp3lame', '-b:a', '320k') }
    $args2 += @($outPath)
    & ffmpeg @args2
    if ($LASTEXITCODE -ne 0) { throw "ffmpeg не смог повторить круг" }
    "Готово: $outPath ($([math]::Round((Get-Item $outPath).Length / 1MB)) МБ)"
    "Круг повторяется каждые $([TimeSpan]::FromSeconds($unit).ToString('h\:mm\:ss'))"
}
finally { Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue }
