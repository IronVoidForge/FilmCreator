@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "SEARCH_DIR=%~1"
if not defined SEARCH_DIR set "SEARCH_DIR=%~dp0"
if not "!SEARCH_DIR:~-1!"=="\" set "SEARCH_DIR=!SEARCH_DIR!\"

:find_root
if exist "!SEARCH_DIR!projects\" if exist "!SEARCH_DIR!orchestrator\" (
    endlocal & set "FILMCREATOR_ROOT=%SEARCH_DIR:~0,-1%" & exit /b 0
)

for %%I in ("!SEARCH_DIR!..") do set "PARENT_DIR=%%~fI\"
if /I "!PARENT_DIR!"=="!SEARCH_DIR!" (
    endlocal & exit /b 1
)

set "SEARCH_DIR=!PARENT_DIR!"
goto :find_root
