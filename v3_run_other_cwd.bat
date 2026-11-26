@echo off
echo cwd at start: %CD%
cd /d "%USERPROFILE%"
echo cwd now      : %CD%
echo.

echo == run v3_who_runs.py from a different cwd ==
python "E:\Code\Project_01\v3_who_runs.py"
echo.
echo exit code = %ERRORLEVEL%
echo.
pause
