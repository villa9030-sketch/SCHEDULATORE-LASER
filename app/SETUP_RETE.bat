@echo off
REM ============================================
REM SCHEDULATORE LASER - Setup Rete Multi-Postazione
REM ============================================

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║   SCHEDULATORE LASER - SETUP RETE MULTI-POSTAZIONE        ║
echo ║   Questo script ti aiuta a configurare l'accesso remoto    ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

echo [STEP 1] Verifica Backend
echo ──────────────────────────────────────────────────────────
echo Assicurati che START_BACKEND.bat sia in esecuzione
echo su questo computer.
echo.
pause

echo [STEP 2] Trova IP Server
echo ──────────────────────────────────────────────────────────
ipconfig | findstr "IPv4"
echo.
echo 👆 Annota l'indirizzo IPv4 della scheda di rete attiva
echo   (solitamente inizia con 192.168 o 10.0)
echo.

set /p ServerIP="Inserisci IP Server (es: 192.168.1.100): "

echo.
echo [STEP 3] Test Connessione
echo ──────────────────────────────────────────────────────────
echo Testiamo la connessione al server...
echo.

ping -n 1 %ServerIP% >nul 2>&1
if errorlevel 1 (
    echo ❌ ERRORE: IP non raggiungibile
    echo   Verificare che:
    echo   1. IP sia corretto
    echo   2. Server sia acceso
    echo   3. Firewall permetta la connessione
    echo.
    pause
    exit /b 1
) else (
    echo ✅ IP raggiungibile!
)

echo.
echo [STEP 4] Test Backend
echo ──────────────────────────────────────────────────────────
curl -s http://%ServerIP%:5000/api/health >nul 2>&1
if errorlevel 1 (
    echo ❌ ERRORE: Backend non raggiungibile
    echo   Verificare che:
    echo   1. START_BACKEND.bat sia in esecuzione
    echo   2. Porta 5000 sia aperta nel firewall
    echo.
    pause
    exit /b 1
) else (
    echo ✅ Backend raggiungibile!
)

echo.
echo [STEP 5] Genera URL di Accesso
echo ──────────────────────────────────────────────────────────
echo.
echo URL PER QUESTA POSTAZIONE:
echo.
echo http://%ServerIP%:5000/frontend/welcome.html
echo.
echo COPIA L'URL SOPRA E INCOLLALO NEL BROWSER
echo.

echo [STEP 6] Salva Configurazione
echo ──────────────────────────────────────────────────────────
setlocal enabledelayedexpansion
set SETUP_FILE="%USERPROFILE%\Desktop\Schedulatore_Setup.txt"

(
    echo Server IP: %ServerIP%
    echo Creato: %date% %time%
    echo.
    echo URL di Accesso:
    echo http://%ServerIP%:5000/frontend/welcome.html
    echo.
    echo Informazioni Aggiuntive:
    echo - Backend deve rimanere in esecuzione
    echo - Collegare da stessa rete WiFi/Ethernet
    echo - Tutte le postazioni vedono gli stessi dati
    echo - Auto-refresh dashboard ogni 30 secondi
) > %SETUP_FILE%

echo ✅ Configurazione salvata: %SETUP_FILE%
echo.

echo ╔════════════════════════════════════════════════════════════╗
echo ║   SETUP COMPLETATO!                                        ║
echo ║                                                            ║
echo ║   URL SCHEDULATORE:                                        ║
echo ║   http://%ServerIP%:5000/frontend/welcome.html            ║
echo ║                                                            ║
echo ║   PROSSIMI PASSI:                                          ║
echo ║   1. Apri browser su questa postazione                     ║
echo ║   2. Copia/incolla l'URL sopra                             ║
echo ║   3. Usa lo scheduler                                      ║
echo ║   4. Da altre postazioni, usa lo stesso URL                ║
echo ║                                                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

pause
