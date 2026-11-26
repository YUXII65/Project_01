@echo off
cd /d "%~dp0"

echo == 1. where python ==
where python
echo.

echo == 2. python -V ==
python -V
echo.

echo == 3. sys.executable of that python ==
python -c "import sys; print(sys.executable)"
echo.

if exist ".venv\Scripts\python.exe" goto havevenv
echo == 4. creating .venv ==
python -m venv .venv
if errorlevel 1 echo venv create FAILED
echo.

:havevenv
echo == 5. venv python -V ==
".venv\Scripts\python.exe" -V
echo.

echo == 6. sys.executable of venv python ==
".venv\Scripts\python.exe" -c "import sys; print(sys.executable)"
echo.

echo == 7. run v3_who_runs.py with venv python, cwd = project root ==
".venv\Scripts\python.exe" "v3_who_runs.py"
echo.
echo exit code = %ERRORLEVEL%
echo.
pause
