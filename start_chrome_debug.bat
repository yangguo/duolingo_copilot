@echo off
REM Helper script to start Chrome with remote debugging enabled (Windows)
REM This allows the Duolingo Copilot to connect to your existing browser session

set PORT=%1
if "%PORT%"=="" set PORT=9222

echo Starting Chrome with remote debugging on port %PORT%...
echo.
echo After Chrome starts:
echo 1. Log in to Duolingo manually
echo 2. In another terminal, run:
echo    python duolingo_copilot.py --cdp-url http://localhost:%PORT% --skip-login
echo.

REM Try to find and start Chrome
if exist "%ProgramFiles%\Google\Chrome\Application\chrome.exe" (
    start "" "%ProgramFiles%\Google\Chrome\Application\chrome.exe" --remote-debugging-port=%PORT%
    exit /b 0
)

if exist "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe" (
    start "" "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe" --remote-debugging-port=%PORT%
    exit /b 0
)

if exist "%LocalAppData%\Google\Chrome\Application\chrome.exe" (
    start "" "%LocalAppData%\Google\Chrome\Application\chrome.exe" --remote-debugging-port=%PORT%
    exit /b 0
)

echo Chrome not found. Please install Google Chrome or run it manually with:
echo chrome.exe --remote-debugging-port=%PORT%
exit /b 1
