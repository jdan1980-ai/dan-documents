@echo off
echo Stopping bot on port 8000...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8000.*LISTENING"') do (
    echo Killing PID %%a
    taskkill /F /PID %%a >nul 2>&1
)
echo Done.
timeout /t 2 >nul
