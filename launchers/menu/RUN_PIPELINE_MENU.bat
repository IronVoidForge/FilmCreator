@echo off
setlocal EnableExtensions

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0.." || goto :fail
cd /d "%FILMCREATOR_ROOT%" || goto :fail

set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"
set "CHAPTERS=%~2"
set "MODE=%~3"
if "%MODE%"=="" set "MODE=resume"

if "%CHAPTERS%"=="" (
    python -m orchestrator menu "%PROJECT_SLUG%" --mode "%MODE%"
) else (
    python -m orchestrator menu "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --mode "%MODE%"
)
exit /b %ERRORLEVEL%

:fail
echo Failed to launch pipeline menu.
exit /b 1
