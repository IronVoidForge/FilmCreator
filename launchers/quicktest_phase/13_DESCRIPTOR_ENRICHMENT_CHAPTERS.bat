@echo off
setlocal EnableExtensions
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"
set "CHAPTERS=%~2"
if "%CHAPTERS%"=="" set "CHAPTERS=2-3"
call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0"
if errorlevel 1 exit /b 1
cd /d "%FILMCREATOR_ROOT%"
echo COMMAND: python -m orchestrator synthesize-descriptor-enrichment "%PROJECT_SLUG%" --force --chapters "%CHAPTERS%"
python -m orchestrator synthesize-descriptor-enrichment "%PROJECT_SLUG%" --force --chapters "%CHAPTERS%"
pause
