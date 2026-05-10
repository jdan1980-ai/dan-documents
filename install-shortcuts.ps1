$desktop = [Environment]::GetFolderPath('Desktop')
$proj = 'C:\Users\jdan1\projects\dan-documents'
$ws = New-Object -ComObject WScript.Shell

$start = $ws.CreateShortcut("$desktop\Start Bot.lnk")
$start.TargetPath = "$proj\start-bot.bat"
$start.WorkingDirectory = $proj
$start.IconLocation = "$env:SystemRoot\System32\SHELL32.dll,137"
$start.Description = "Start YouTube Analytics Bot"
$start.Save()

$stop = $ws.CreateShortcut("$desktop\Stop Bot.lnk")
$stop.TargetPath = "wscript.exe"
$stop.Arguments = "`"$proj\stop-bot.vbs`""
$stop.WorkingDirectory = $proj
$stop.IconLocation = "$env:SystemRoot\System32\SHELL32.dll,131"
$stop.Description = "Stop YouTube Analytics Bot"
$stop.Save()

$open = $ws.CreateShortcut("$desktop\Open Bot.lnk")
$open.TargetPath = "http://127.0.0.1:8000"
$open.IconLocation = "$env:SystemRoot\System32\SHELL32.dll,14"
$open.Description = "Open Bot in Browser"
$open.Save()

Write-Host "Installed 3 shortcuts on Desktop:" -ForegroundColor Green
Write-Host "  - Start Bot     (green play icon)"
Write-Host "  - Stop Bot      (red stop icon)"
Write-Host "  - Open Bot      (browser icon)"
