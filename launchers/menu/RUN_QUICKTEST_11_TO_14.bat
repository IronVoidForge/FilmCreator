@echo off
setlocal EnableExtensions

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0.." || goto :fail
cd /d "%FILMCREATOR_ROOT%" || goto :fail

set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"
set "CHAPTERS=%~2"
if "%CHAPTERS%"=="" set "CHAPTERS=2-3"

python -m orchestrator run-quicktest-composite "%PROJECT_SLUG%" --composite 11_to_14 --chapters "%CHAPTERS%"
exit /b %ERRORLEVEL%

:fail
echo Failed to run quicktest composite 11 to 14.
exit /b 1
