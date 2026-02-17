@echo off
REM ============================================
REM SCHEDULATORE LASER - Test Connessione
REM ============================================

echo.
echo ╔════════════════════════════════════════╗
echo ║   SCHEDULATORE LASER - TEST SISTEMA    ║
echo ╚════════════════════════════════════════╝
echo.

REM Test 1: Backend locale
echo [TEST 1] Verifica Backend locale...
curl -s http://localhost:5000/api/health >nul 2>&1
if errorlevel 1 (
    echo ❌ Backend NON raggiungibile su localhost:5000
    echo [FIX] Eseguire START_BACKEND.bat
) else (
    echo ✅ Backend raggiungibile su localhost:5000
)

echo.

REM Test 2: Python installato
echo [TEST 2] Verifica Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python NON installato
    echo [FIX] Installare Python 3.8+ da python.org
) else (
    for /f "tokens=*" %%i in ('python --version 2^>^&1') do (
        echo ✅ %%i
    )
)

echo.

REM Test 3: Cartelle upload
echo [TEST 3] Verifica cartelle upload...
if exist "..\app\uploads\pdfs" (
    echo ✅ Cartella uploads/pdfs esistente
) else (
    echo ❌ Cartella uploads/pdfs NON esiste
)

if exist "..\app\uploads\drawings" (
    echo ✅ Cartella uploads/drawings esistente
) else (
    echo ❌ Cartella uploads/drawings NON esiste
)

echo.

REM Test 4: File dipendenze
echo [TEST 4] Verifica dipendenze Python...
if exist "..\app\requirements.txt" (
    echo ✅ requirements.txt trovato
) else (
    echo ❌ requirements.txt NON trovato
)

echo.

REM Test 5: File Frontend
echo [TEST 5] Verifica file frontend...
if exist "welcome.html" (
    echo ✅ welcome.html trovato
) else (
    echo ❌ welcome.html NON trovato
)

if exist "scheduler.html" (
    echo ✅ scheduler.html trovato
) else (
    echo ❌ scheduler.html NON trovato
)

echo.
echo ╔════════════════════════════════════════╗
echo ║      TEST COMPLETATO                   ║
echo ╚════════════════════════════════════════╝
echo.

pause
