@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "SEARCH_DIR=%SCRIPT_DIR%"
set "REPO_ROOT="

:find_root
if exist "%SEARCH_DIR%projects" if exist "%SEARCH_DIR%orchestrator" (
    set "REPO_ROOT=%SEARCH_DIR%"
    goto found_root
)
for %%I in ("%SEARCH_DIR%..") do set "PARENT_DIR=%%~fI\"
if /I "%PARENT_DIR%"=="%SEARCH_DIR%" goto root_not_found
set "SEARCH_DIR=%PARENT_DIR%"
goto find_root

:found_root
cd /d "%REPO_ROOT%"

set "DEFAULT_SLUG=princess_of_mars_test"
set /p PROJECT_SLUG=Project slug [%DEFAULT_SLUG%]: 
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=%DEFAULT_SLUG%"

set "TARGET=projects\%PROJECT_SLUG%\02_story_analysis"

echo.
echo Repo root: %REPO_ROOT%
echo Project slug: %PROJECT_SLUG%
echo Target: %TARGET%
echo.

if not exist "projects\%PROJECT_SLUG%" (
    echo Project folder not found: projects\%PROJECT_SLUG%
    pause
    exit /b 1
)

if exist "%TARGET%" (
    echo Removing generated story analysis outputs...
    rmdir /s /q "%TARGET%"
) else (
    echo Nothing to remove. Target does not exist yet.
)

mkdir "%TARGET%" >nul 2>nul

echo.
echo Done. Fresh analysis directory ready:
echo   %TARGET%
pause
exit /b 0

:root_not_found
echo Could not locate repo root from launcher path.
echo Expected to find both a 'projects' folder and an 'orchestrator' folder in some parent directory.
pause
exit /b 1
