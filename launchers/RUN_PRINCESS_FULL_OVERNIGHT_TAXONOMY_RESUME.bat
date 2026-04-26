@echo off
setlocal EnableExtensions

set "BAT_VERSION=PS_WRAPPER_QUIET_V1_2026-04-26"

set "SCRIPT_DIR=%~dp0"
set "PS_SCRIPT=%SCRIPT_DIR%RUN_PRINCESS_FULL_OVERNIGHT_TAXONOMY_RESUME.ps1"

if not exist "%PS_SCRIPT%" (
    echo ERROR: Missing PowerShell runner:
    echo %PS_SCRIPT%
    pause
    exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%PS_SCRIPT%" %*
set "EXIT_CODE=%ERRORLEVEL%"

pause
exit /b %EXIT_CODE%