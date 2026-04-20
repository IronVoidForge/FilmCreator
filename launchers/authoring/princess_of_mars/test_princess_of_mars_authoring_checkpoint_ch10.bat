@echo off
setlocal

call "%~dp0..\..\_shared\resolve_filmcreator_root.bat" "%~dp0" || exit /b 1

cd /d "%FILMCREATOR_ROOT%"

echo Running Chapter X authoring checkpoint...
python -m orchestrator authoring-checkpoint princess_of_mars_test --chapter CH010_a_princess_of_mars_ch10.md
pause
