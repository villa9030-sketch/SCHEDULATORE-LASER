@echo off
REM ============================================
REM SCHEDULATORE LASER - Trova IP Server
REM ============================================

echo.
echo ╔════════════════════════════════════════╗
echo ║   SCHEDULATORE LASER - INFORMAZIONI IP ║
echo ╚════════════════════════════════════════╝
echo.

echo [INFO] Configurazione di rete locale:
echo.

REM Mostra gli indirizzi IP
ipconfig /all

echo.
echo ╔════════════════════════════════════════╗
echo ║   ISTRUZIONI PER ACCESSO DA REMOTO     ║
echo ╚════════════════════════════════════════╝
echo.

echo [1] Trovare l'indirizzo IPv4 della scheda di rete attiva
echo     (di solito inizia con 192.168.x.x o 10.x.x.x)
echo.

echo [2] Su altre postazioni, aprire il browser e digitare:
echo     http://^[IPv4_DEL_SERVER^]:5000
echo.

echo [ESEMPIO]
echo Questo computer ha IP: 192.168.1.100
echo Da remoto digitare: http://192.168.1.100:5000
echo.

echo [TEST VELOCE]
echo Digitare il comando (sostituire con vostro IP):
echo     ping 192.168.1.100
echo.

pause
