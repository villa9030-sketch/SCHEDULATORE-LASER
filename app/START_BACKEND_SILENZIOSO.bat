@echo off
REM Avvia il backend Flask in background silenziosamente
title Backend Flask - SCHEDULATORE LASER
cd /d "%~dp0"
start "" .venv\Scripts\python.exe -m backend.app
exit
