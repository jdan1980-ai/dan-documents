@echo off
title YouTube Analytics Bot
color 0A
cd /d C:\Users\jdan1\projects\dan-documents
call venv\Scripts\activate.bat
cls
echo.
echo  ===========================================================
echo                YouTube Analytics Bot
echo  ===========================================================
echo.
echo    URL:     http://127.0.0.1:8000
echo    Stop:    close this window or run "Stop Bot"
echo    Status:  starting...
echo.
echo  -----------------------------------------------------------
echo.
start "" http://127.0.0.1:8000
uvicorn app.main:app --host 127.0.0.1 --port 8000
