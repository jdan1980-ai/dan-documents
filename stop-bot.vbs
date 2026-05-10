' Silent stop — no console window
Set sh = CreateObject("WScript.Shell")
sh.Run "cmd /c for /f ""tokens=5"" %a in ('netstat -ano ^| findstr "":8000.*LISTENING""') do taskkill /F /PID %a", 0, True
sh.Popup "Bot stopped.", 2, "YouTube Analytics", 64
