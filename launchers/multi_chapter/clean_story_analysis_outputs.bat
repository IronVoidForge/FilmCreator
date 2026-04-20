@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :root_not_found
cd /d "%FILMCREATOR_ROOT%"

set "DEFAULT_SLUG=princess_of_mars_test"
set /p PROJECT_SLUG=Project slug [%DEFAULT_SLUG%]: 
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=%DEFAULT_SLUG%"

set "TARGET=%FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%\02_story_analysis"

echo.
echo Repo root: %FILMCREATOR_ROOT%
echo Project slug: %PROJECT_SLUG%
echo Target: %TARGET%
echo.

if not exist "%FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%" (
    echo Project folder not found: %FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%
    pause
    exit /b 1
)

if exist "%TARGET%" (
    echo Removing generated story analysis outputs...
    powershell -NoProfile -Command "$target = '%TARGET%'; if (Test-Path -LiteralPath $target) { $items = Get-ChildItem -LiteralPath $target -Force -Recurse -ErrorAction SilentlyContinue | Sort-Object FullName -Descending; foreach ($item in $items) { try { Remove-Item -LiteralPath $item.FullName -Force -ErrorAction Stop } catch { } }; try { Remove-Item -LiteralPath $target -Force -Recurse -ErrorAction Stop } catch { } }"
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
