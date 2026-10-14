<#
Seven Lights — build one sleep video from Flow Music fragments.

  1. Shuffles the fragments (never the same one twice in a row) and chains
     them with crossfades until the target length is reached.
  2. Mixes a quiet sine tone at the chosen frequency under the music.
  3. Normalises loudness, fades in and out.
  4. Renders the video: the image with a slow zoom for -VisualMinutes,
     a fade to black, then black screen to the end. -BlackOnly skips the image.

Examples:
  # 3-hour video, root chakra, 396 Hz
  .\build-video.ps1 -Fragments D:\flow\root -Hz 396 -Image D:\img\root.png -Hours 3 -Name root-chakra-3h

  # 8-hour black screen version
  .\build-video.ps1 -Fragments D:\flow\aura -Hz 528 -Hours 8 -BlackOnly -Name aura-8h
#>
param(
    [Parameter(Mandatory)] [string]$Fragments,   # folder with .mp3 / .wav / .m4a / .flac
    [Parameter(Mandatory)] [double]$Hz,          # tone frequency, e.g. 396
    [string]$Image,                              # still image for the opening (not needed with -BlackOnly)
    [double]$Hours = 3,
    [double]$VisualMinutes = 10,
    [switch]$BlackOnly,
    [double]$CrossfadeSec = 20,
    [double]$ToneDb = -24,                       # tone level relative to full scale before loudnorm
    [string]$Name = 'seven-lights-video',
    [string]$OutDir = (Join-Path $PSScriptRoot 'out')
)
$ErrorActionPreference = 'Stop'

function Find-Tool([string]$exe) {
    $cmd = Get-Command $exe -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    $hit = Get-ChildItem "$env:LOCALAPPDATA\Microsoft\WinGet\Packages" -Recurse -Filter $exe -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($hit) { return $hit.FullName }
    throw "$exe not found. Install it: winget install --id Gyan.FFmpeg -e"
}
$ffmpeg = Find-Tool 'ffmpeg.exe'
$ffprobe = Find-Tool 'ffprobe.exe'

if (-not $BlackOnly -and -not $Image) { throw 'Pass -Image or use -BlackOnly.' }
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$work = Join-Path $OutDir "$Name-work"
New-Item -ItemType Directory -Force -Path $work | Out-Null

# ---------- 1. Playlist ----------
$files = Get-ChildItem $Fragments -File | Where-Object { $_.Extension -match '^\.(mp3|wav|m4a|flac|ogg)$' }
if ($files.Count -lt 2) { throw "Need at least 2 audio fragments in $Fragments" }

$durations = @{}
foreach ($f in $files) {
    $durations[$f.FullName] = [double](& $ffprobe -v error -show_entries format=duration -of csv=p=0 $f.FullName)
}
$target = $Hours * 3600
$playlist = New-Object System.Collections.Generic.List[string]
$total = 0.0
$last = $null
while ($total -lt $target + $CrossfadeSec) {
    $pool = $files | Where-Object { $_.FullName -ne $last } | Get-Random -Count ([Math]::Min(1000, $files.Count))
    foreach ($f in $pool) {
        if ($f.FullName -eq $last) { continue }
        $playlist.Add($f.FullName); $last = $f.FullName
        $total += $durations[$f.FullName] - $CrossfadeSec
        if ($total -ge $target + $CrossfadeSec) { break }
    }
}
Write-Host ("Fragments: {0} files, playlist: {1} segments" -f $files.Count, $playlist.Count)

# ---------- 2. Chain with crossfades (in batches to keep filter graphs small) ----------
function Join-WithCrossfade([string[]]$inputs, [string]$out) {
    $args = @('-y', '-v', 'error')
    foreach ($i in $inputs) { $args += @('-i', $i) }
    $chain = ''
    $prev = '[0:a]'
    for ($k = 1; $k -lt $inputs.Count; $k++) {
        $lbl = if ($k -eq $inputs.Count - 1) { '[out]' } else { "[x$k]" }
        $chain += "$prev[$($k):a]acrossfade=d=$($CrossfadeSec):c1=tri:c2=tri$lbl;"
        $prev = $lbl
    }
    $args += @('-filter_complex', $chain.TrimEnd(';'), '-map', '[out]', '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s16le', $out)
    & $ffmpeg @args
    if ($LASTEXITCODE) { throw "ffmpeg crossfade failed for $out" }
}

$batch = 20
$parts = @()
for ($b = 0; $b -lt $playlist.Count; $b += $batch) {
    $slice = $playlist[$b..([Math]::Min($b + $batch, $playlist.Count) - 1)]
    $part = Join-Path $work ("part{0:D3}.wav" -f $parts.Count)
    if ($slice.Count -eq 1) {
        & $ffmpeg -y -v error -i $slice[0] -ar 48000 -ac 2 -c:a pcm_s16le $part
    } else {
        Join-WithCrossfade $slice $part
    }
    $parts += $part
}
$music = Join-Path $work 'music.wav'
if ($parts.Count -eq 1) { Copy-Item $parts[0] $music -Force } else { Join-WithCrossfade $parts $music }

# ---------- 3. Tone, length, loudness, fades ----------
$fadeOutStart = $target - 120
$audio = Join-Path $OutDir "$Name.m4a"
& $ffmpeg -y -v error -i $music -f lavfi -i "sine=frequency=$($Hz):sample_rate=48000" `
    -filter_complex "[1:a]volume=$($ToneDb)dB,aformat=channel_layouts=stereo[t];[0:a][t]amix=inputs=2:duration=first:normalize=0,atrim=0:$target,loudnorm=I=-20:TP=-2:LRA=11,afade=t=in:d=30,afade=t=out:st=$($fadeOutStart):d=120[a]" `
    -map '[a]' -c:a aac -b:a 192k $audio
if ($LASTEXITCODE) { throw 'ffmpeg audio mix failed' }

# ---------- 4. Video ----------
$fps = 24
$video = Join-Path $OutDir "$Name.mp4"
if ($BlackOnly) {
    & $ffmpeg -y -v error -f lavfi -i "color=c=black:s=1920x1080:r=$fps" -i $audio -t $target `
        -c:v libx264 -preset veryfast -tune stillimage -crf 30 -pix_fmt yuv420p -c:a copy -shortest $video
} else {
    $visual = [Math]::Min($VisualMinutes * 60, $target)
    $frames = [int]($visual * $fps)
    $opening = Join-Path $work 'opening.mp4'
    $black = Join-Path $work 'black.mp4'
    # Slow zoom from 100% to ~108% over the opening, then 15 s fade to black.
    & $ffmpeg -y -v error -loop 1 -framerate $fps -i $Image -t $visual `
        -vf "scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,zoompan=z='1+0.08*on/$frames':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=$fps,fade=t=in:d=5,fade=t=out:st=$($visual - 15):d=15,format=yuv420p" `
        -c:v libx264 -preset medium -crf 20 $opening
    if ($LASTEXITCODE) { throw 'ffmpeg opening failed' }
    $rest = $target - $visual
    $list = Join-Path $work 'video.txt'
    if ($rest -gt 1) {
        & $ffmpeg -y -v error -f lavfi -i "color=c=black:s=1920x1080:r=$fps" -t $rest `
            -c:v libx264 -preset veryfast -tune stillimage -crf 30 -pix_fmt yuv420p $black
        "file '$($opening -replace "'", "'\''")'`nfile '$($black -replace "'", "'\''")'" | Set-Content -Encoding ascii $list
    } else {
        "file '$($opening -replace "'", "'\''")'" | Set-Content -Encoding ascii $list
    }
    & $ffmpeg -y -v error -f concat -safe 0 -i $list -i $audio -map 0:v -map 1:a -c copy -shortest $video
}
if ($LASTEXITCODE) { throw 'ffmpeg video failed' }

$dur = [double](& $ffprobe -v error -show_entries format=duration -of csv=p=0 $video)
Write-Host ("Done: {0}  ({1:N1} min, {2:N0} MB)" -f $video, ($dur / 60), ((Get-Item $video).Length / 1MB))
Write-Host "Working files are in $work — delete that folder once you are happy with the result."
