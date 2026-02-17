@echo off
REM ============================================
REM SCHEDULATORE LASER - Avvio Backend
REM ============================================

echo.
echo ╔════════════════════════════════════════╗
echo ║   SCHEDULATORE LASER - BACKEND START   ║
echo ╚════════════════════════════════════════╝
echo.

REM Vai alla cartella app
cd /d "%~dp0..\app"

echo [*] Cartella corrente: %cd%
echo.

REM Controlla se Python è installato
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRORE] Python non trovato nel PATH
    echo [INFO] Installare Python 3.8+ e aggiungerlo al PATH
    pause
    exit /b 1
)

echo [OK] Python trovato
echo.

REM Controlla se requirements.txt esiste
if not exist "requirements.txt" (
    echo [ERRORE] requirements.txt non trovato
    pause
    exit /b 1
)

echo [*] Installazione dipendenze...
python -m pip install -q -r requirements.txt
if errorlevel 1 (
    echo [ERRORE] Installazione dipendenze fallita
    pause
    exit /b 1
)

echo [OK] Dipendenze installate
echo.

REM Avvia il backend
echo [*] Avvio Backend...
echo.
echo ╔════════════════════════════════════════╗
echo ║  Backend in esecuzione su:             ║
echo ║  http://localhost:5000                 ║
echo ║                                        ║
echo ║  Dashboard: frontend/dashboard.html    ║
echo ║  Caricamento: frontend/welcome.html    ║
echo ║                                        ║
echo ║  Premi CTRL+C per fermare              ║
echo ╚════════════════════════════════════════╝
echo.

python run.py

pause
