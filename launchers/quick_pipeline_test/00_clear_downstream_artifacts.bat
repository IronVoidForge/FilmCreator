@echo off
setlocal

call "%~dp0_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo Quick Pipeline Test: Clear Downstream Artifacts
echo ========================================
echo.
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"
set "AUTO_CONFIRM=%~3"

echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This clears downstream artifacts only and preserves chapter summaries and bibles.
if /I not "%AUTO_CONFIRM%"=="Y" (
    echo Press any key to continue.
    pause
) else (
    echo Auto-confirm enabled. Continuing without pause.
)

set "PROJECT_ROOT=%FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%"
if not exist "%PROJECT_ROOT%" (
    echo Project folder not found: %PROJECT_ROOT%
    goto :fail
)

echo.
echo Removing downstream artifacts...
powershell -NoProfile -Command ^
    "$root = '%PROJECT_ROOT%';" ^
    "$targets = @(" ^
    "    (Join-Path $root '02_story_analysis\contracts')," ^
    "    (Join-Path $root '02_story_analysis\timelines')," ^
    "    (Join-Path $root '02_story_analysis\descriptors')," ^
    "    (Join-Path $root '02_story_analysis\grading')," ^
    "    (Join-Path $root '02_story_analysis\dialogue_enrichment')," ^
    "    (Join-Path $root '02_story_analysis\world\refinement')," ^
    "    (Join-Path $root '03_prompt_packages')," ^
    "    (Join-Path $root '04_references')," ^
    "    (Join-Path $root '05_scenes')," ^
    "    (Join-Path $root '06_reviews')," ^
    "    (Join-Path $root '07_finals')," ^
    "    (Join-Path $root 'logs')" ^
    ");" ^
    "foreach ($target in $targets) { if (Test-Path -LiteralPath $target) { Remove-Item -LiteralPath $target -Recurse -Force -ErrorAction SilentlyContinue } }"

echo.
echo Downstream artifact clear complete.
goto :done

:fail
echo.
echo Downstream artifact clear failed.
popd >nul
exit /b 1

:done
popd >nul
exit /b 0
