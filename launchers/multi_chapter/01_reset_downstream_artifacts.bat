@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo FilmCreator Downstream Artifact Reset
echo ========================================
echo.
set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

set "PROJECT_ROOT=%FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%"
if not exist "%PROJECT_ROOT%" (
    echo Project folder not found: %PROJECT_ROOT%
    goto :fail
)

echo.
echo This will remove downstream artifacts for:
echo   %PROJECT_ROOT%
echo.
echo The following folders will be deleted if present:
echo   02_story_analysis\bibles
echo   02_story_analysis\contracts
echo   02_story_analysis\timelines
echo   02_story_analysis\descriptors
echo   02_story_analysis\grading
echo   02_story_analysis\dialogue_enrichment
echo   02_story_analysis\world\refinement
echo   03_prompt_packages
echo   04_references
echo   05_scenes
echo   06_reviews
echo   07_finals
echo   logs
echo.
echo Story analysis, chapter summaries, and chapter-level breakdowns are preserved.
echo.
set /p CONFIRM=Type DELETE to continue:
if /I not "%CONFIRM%"=="DELETE" (
    echo Aborted.
    goto :done
)

echo.
echo Removing downstream artifacts...
powershell -NoProfile -Command ^
    "$root = '%PROJECT_ROOT%';" ^
    "$targets = @(" ^
    "    (Join-Path $root '02_story_analysis\bibles')," ^
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
echo Downstream reset complete.
echo You can now rerun the pipeline from character bibles onward.

:done
popd >nul
pause
exit /b 0

:fail
popd >nul
pause
exit /b 1
