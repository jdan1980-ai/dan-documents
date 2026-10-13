# Seven Lights — channel banner (2560x1440) and avatar (800x800).
# Run: pwsh -File brand.ps1   (writes files next to this script)
Add-Type -AssemblyName System.Drawing

$outDir = $PSScriptRoot
$colors = @('#E53935', '#FB8C00', '#FDD835', '#43A047', '#1E88E5', '#5C6BF0', '#8E24AA')

function New-Canvas([int]$w, [int]$h) {
    $bmp = New-Object System.Drawing.Bitmap $w, $h
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.SmoothingMode = 'AntiAlias'
    $g.TextRenderingHint = 'AntiAliasGridFit'
    $g.Clear([System.Drawing.ColorTranslator]::FromHtml('#05060B'))
    return $bmp, $g
}

# Soft radial glow: centre colour fading to transparent.
function Add-Glow($g, [float]$cx, [float]$cy, [float]$r, [System.Drawing.Color]$color, [int]$alpha) {
    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $path.AddEllipse($cx - $r, $cy - $r, 2 * $r, 2 * $r)
    $brush = New-Object System.Drawing.Drawing2D.PathGradientBrush $path
    $brush.CenterColor = [System.Drawing.Color]::FromArgb($alpha, $color)
    $brush.SurroundColors = @([System.Drawing.Color]::FromArgb(0, $color))
    $g.FillPath($brush, $path)
    $brush.Dispose(); $path.Dispose()
}

function Add-Orb($g, [float]$cx, [float]$cy, [float]$core, [string]$hex) {
    $c = [System.Drawing.ColorTranslator]::FromHtml($hex)
    Add-Glow $g $cx $cy ($core * 7) $c 46
    Add-Glow $g $cx $cy ($core * 3.2) $c 120
    Add-Glow $g $cx $cy ($core * 1.5) $c 235
    Add-Glow $g $cx $cy ($core * 0.7) ([System.Drawing.Color]::White) 215
}

# Text with manual letter spacing, centred on $cx.
function Add-SpacedText($g, [string]$text, $font, $brush, [float]$cx, [float]$y, [float]$tracking) {
    $fmt = [System.Drawing.StringFormat]::GenericTypographic
    $fmt.FormatFlags = $fmt.FormatFlags -bor [System.Drawing.StringFormatFlags]::MeasureTrailingSpaces
    $widths = foreach ($ch in $text.ToCharArray()) { $g.MeasureString([string]$ch, $font, 9999, $fmt).Width }
    $total = ($widths | Measure-Object -Sum).Sum + $tracking * ($text.Length - 1)
    $x = $cx - $total / 2
    for ($i = 0; $i -lt $text.Length; $i++) {
        $g.DrawString([string]$text[$i], $font, $brush, $x, $y, $fmt)
        $x += $widths[$i] + $tracking
    }
}

# ---------- Banner 2560x1440 (safe area for all devices: centre 1546x423) ----------
$bmp, $g = New-Canvas 2560 1440
Add-Glow $g 1280 720 1500 ([System.Drawing.ColorTranslator]::FromHtml('#1B1F4A')) 150
Add-Glow $g 1280 720 700 ([System.Drawing.ColorTranslator]::FromHtml('#2A1E5C')) 70

$spacing = 150
$x0 = 1280 - 3 * $spacing
for ($i = 0; $i -lt 7; $i++) { Add-Orb $g ($x0 + $i * $spacing) 600 15 $colors[$i] }

$white = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(245, 240, 240, 248))
$soft = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(190, 190, 195, 220))
$titleFont = New-Object System.Drawing.Font 'Segoe UI Light', 96, ([System.Drawing.FontStyle]::Regular), ([System.Drawing.GraphicsUnit]::Pixel)
$subFont = New-Object System.Drawing.Font 'Segoe UI', 34, ([System.Drawing.FontStyle]::Regular), ([System.Drawing.GraphicsUnit]::Pixel)
Add-SpacedText $g 'SEVEN LIGHTS' $titleFont $white 1280 668 34
Add-SpacedText $g 'CHAKRA HEALING MUSIC FOR SLEEP' $subFont $soft 1280 812 14

$jpg = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$ep = New-Object System.Drawing.Imaging.EncoderParameters 1
$ep.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality), 95L
$bmp.Save((Join-Path $outDir 'SevenLights_banner_2560x1440.jpg'), $jpg, $ep)

# Preview with the safe area outlined (not for upload).
$pen = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(140, 255, 255, 255)), 3
$pen.DashStyle = 'Dash'
$g.DrawRectangle($pen, 507, 508, 1546, 423)
$small = New-Object System.Drawing.Bitmap $bmp, 1280, 720
$small.Save((Join-Path $outDir 'SevenLights_banner_safe-area_preview.png'), [System.Drawing.Imaging.ImageFormat]::Png)
$small.Dispose(); $g.Dispose(); $bmp.Dispose()

# ---------- Avatar 800x800 (YouTube crops it to a circle) ----------
$bmp, $g = New-Canvas 800 800
Add-Glow $g 400 400 520 ([System.Drawing.ColorTranslator]::FromHtml('#1B1F4A')) 170
$ring = 205
for ($i = 0; $i -lt 7; $i++) {
    $a = (-90 + $i * 360 / 7) * [Math]::PI / 180
    Add-Orb $g (400 + $ring * [Math]::Cos($a)) (400 + $ring * [Math]::Sin($a)) 21 $colors[$i]
}
$bmp.Save((Join-Path $outDir 'SevenLights_avatar_800.png'), [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose(); $bmp.Dispose()

Get-ChildItem $outDir -Filter 'SevenLights_*' | Select-Object Name, Length
