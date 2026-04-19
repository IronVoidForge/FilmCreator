@echo off
setlocal

set DEFAULT_SLUG=princess_of_mars_test
set /p PROJECT_SLUG=Project slug [%DEFAULT_SLUG%]: 
if "%PROJECT_SLUG%"=="" set PROJECT_SLUG=%DEFAULT_SLUG%

set TARGET=projects\%PROJECT_SLUG%\02_story_analysis

echo.
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
echo.
echo Source files under 01_source were not changed.
pause
