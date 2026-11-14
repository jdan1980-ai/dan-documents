# Готовое видео для YouTube из петли + длинного звука + оверлея — без CapCut (то же, что make_video.py).
#
#   pwsh -File make_video.ps1 -Loop loop.mp4 -Audio album_3h.flac -Overlay overlay_intro_welcome.png -Out C:\SevenLightsUpload\video.mp4
#
# Петля один раз перекодируется в «склеиваемый» вид, интро (2 круга петли) — с оверлеем, остальное склеивается
# без перекодирования. Долгая часть — только кодирование звука в AAC (несколько минут на 3 часа).
# Нужен ffmpeg/ffprobe в PATH. Пока работает ffmpeg, ничего не печатайте в окно.
param(
    [Parameter(Mandatory)][string]$Loop,
    [Parameter(Mandatory)][string]$Audio,
    [string]$Overlay = '',
    [Parameter(Mandatory)][string]$Out,
    [int]$Crf = 20
)
$ErrorActionPreference = 'Stop'
$inv = [Globalization.CultureInfo]::InvariantCulture
$fps = 30
function Dur([string]$p) { [double]::Parse((& ffprobe -v error -show_entries format=duration -of csv=p=0 $p | Select-Object -First 1).Trim(), $inv) }
function Ff { & ffmpeg -y -loglevel error @args; if ($LASTEXITCODE -ne 0) { throw "ffmpeg завершился с ошибкой" } }

foreach ($f in @($Loop, $Audio) + $(if ($Overlay) { @($Overlay) } else { @() })) {
    if (-not (Test-Path -LiteralPath $f)) { throw "Не найден файл: $f (папка: $((Get-Location).Path))" }
}
$sw = [Diagnostics.Stopwatch]::StartNew()
$audioDur = Dur $Audio
$frames = [math]::Max(1, [math]::Round((Dur $Loop) * $fps))
$tmp = Join-Path ([IO.Path]::GetTempPath()) ("makevideo_" + [Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $tmp | Out-Null
try {
    $enc = @('-c:v', 'libx264', '-preset', 'medium', '-crf', "$Crf", '-pix_fmt', 'yuv420p', '-r', "$fps",
        '-g', "$frames", '-keyint_min', "$frames", '-sc_threshold', '0', '-profile:v', 'high', '-level', '4.1',
        '-video_track_timescale', '15360', '-an')
    $loopReady = Join-Path $tmp 'loop.mp4'
    "1/3 Петля…"
    Ff -i $Loop -vf "scale=1920:1080,setsar=1,fps=$fps" -frames:v "$frames" @enc $loopReady

    $parts = @()
    $introLoops = 0
    if ($Overlay) {
        $introLoops = [math]::Max(1, [math]::Ceiling(11 * $fps / $frames))
        $n = $introLoops * $frames
        $intro = Join-Path $tmp 'intro.mp4'
        $flt = "[0:v]scale=1920:1080,setsar=1,fps=$fps[bg];[1:v]format=rgba,fade=t=in:st=2:d=1.5:alpha=1,fade=t=out:st=8.5:d=2:alpha=1[o];[bg][o]overlay=0:0:eof_action=pass[v]"
        "2/3 Интро с оверлеем…"
        Ff -stream_loop ($introLoops - 1) -i $loopReady -loop 1 -t (($n / $fps).ToString($inv)) -i $Overlay -filter_complex $flt -map '[v]' -frames:v "$n" @enc $intro
        $parts += $intro
    }
    $introDur = $introLoops * $frames / $fps
    $reps = [math]::Max(0, [math]::Ceiling(($audioDur - $introDur) / ($frames / $fps)))
    $list = Join-Path $tmp 'list.txt'
    $lines = @($parts | ForEach-Object { "file '$($_ -replace '\\', '/')'" })
    $lines += @(1..$reps | ForEach-Object { "file '$($loopReady -replace '\\', '/')'" })
    [IO.File]::WriteAllLines($list, $lines)

    "3/3 Склейка видео и кодирование звука (несколько минут)…"
    $outDir = Split-Path -Parent ([IO.Path]::GetFullPath($Out))
    if ($outDir -and -not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }
    Ff -f concat -safe 0 -i $list -i $Audio -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -t ($audioDur.ToString('0.000', $inv)) -movflags +faststart $Out
}
finally { Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue }
$d = Dur $Out
"Готово: $Out — {0:N2} ч, {1:N2} ГБ, за {2:N0} мин" -f ($d / 3600), ((Get-Item $Out).Length / 1GB), $sw.Elapsed.TotalMinutes
