@echo off
setlocal

call "%~dp0..\..\_shared\resolve_filmcreator_root.bat" "%~dp0" || exit /b 1

cd /d "%FILMCREATOR_ROOT%"

echo Running Chapter IX authoring checkpoint...
python -m orchestrator authoring-checkpoint princess_of_mars_test --chapter CH009_a_princess_of_mars_ch09.md
pause
