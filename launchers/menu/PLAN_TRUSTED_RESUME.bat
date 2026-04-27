@echo off
setlocal EnableExtensions

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0.." || goto :fail
cd /d "%FILMCREATOR_ROOT%" || goto :fail

set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"
set "CHAPTERS=%~2"

if "%CHAPTERS%"=="" (
    python -m orchestrator run-production "%PROJECT_SLUG%" --mode resume --plan-only
) else (
    python -m orchestrator run-production "%PROJECT_SLUG%" --mode resume --chapters "%CHAPTERS%" --plan-only
)
exit /b %ERRORLEVEL%

:fail
echo Failed to plan trusted resume run.
exit /b 1
