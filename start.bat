@echo off
setlocal ENABLEDELAYEDEXPANSION

REM Change to script directory
cd /d "%~dp0"

REM Python executable (fallback to "python" if py not available)
where py >nul 2>&1
if %ERRORLEVEL%==0 (
  set "PY=py -3"
) else (
  set "PY=python"
)

REM Create venv if missing
if not exist "venv\Scripts\python.exe" (
  echo Creating virtual environment...
  %PY% -m venv venv
)

REM Upgrade pip and install requirements
call "%~dp0venv\Scripts\python.exe" -m pip install --upgrade pip >nul
if exist requirements.txt (
  echo Installing dependencies from requirements.txt...
  call "%~dp0venv\Scripts\python.exe" -m pip install -r requirements.txt
)

REM Run the app
call "%~dp0venv\Scripts\python.exe" run.py %*

endlocal
