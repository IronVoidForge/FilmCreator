@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail

cd /d "%FILMCREATOR_ROOT%"

echo Running Phase B1 identity + environment resolution...

python -c "from orchestrator.world_registry import run_phase_b1_resolution; import json; print(json.dumps(run_phase_b1_resolution('princess_of_mars_test'), indent=2))"

pause

exit /b 0

:fail
echo.
echo Phase B1 resolution failed.
pause
