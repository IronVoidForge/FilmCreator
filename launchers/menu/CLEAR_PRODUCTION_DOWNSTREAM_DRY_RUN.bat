@echo off
setlocal EnableExtensions

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0.." || goto :fail
cd /d "%FILMCREATOR_ROOT%" || goto :fail

set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

python -m orchestrator clear-production "%PROJECT_SLUG%" --scope downstream_only
exit /b %ERRORLEVEL%

:fail
echo Failed to plan downstream cleanup.
exit /b 1
