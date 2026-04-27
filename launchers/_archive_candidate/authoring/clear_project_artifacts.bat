@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo FilmCreator Project Artifact Reset
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
echo This will remove generated artifacts for:
echo   %PROJECT_ROOT%
echo.
echo The following folders and files will be deleted if present:
echo   02_story_analysis
echo   03_prompt_packages
echo   04_references
echo   05_scenes
echo   06_reviews
echo   07_finals
echo   logs
echo   project_state.json
echo   PROJECT_STATUS.md
echo   PROJECT_TREE.md
echo.
set /p CONFIRM=Type DELETE to continue:
if /I not "%CONFIRM%"=="DELETE" (
    echo Aborted.
    goto :done
)

echo.
echo Removing project artifacts...
powershell -NoProfile -Command ^
    "$root = '%PROJECT_ROOT%';" ^
    "$targets = @(" ^
    "    (Join-Path $root '02_story_analysis')," ^
    "    (Join-Path $root '03_prompt_packages')," ^
    "    (Join-Path $root '04_references')," ^
    "    (Join-Path $root '05_scenes')," ^
    "    (Join-Path $root '06_reviews')," ^
    "    (Join-Path $root '07_finals')," ^
    "    (Join-Path $root 'logs')," ^
    "    (Join-Path $root 'project_state.json')," ^
    "    (Join-Path $root 'PROJECT_STATUS.md')," ^
    "    (Join-Path $root 'PROJECT_TREE.md')" ^
    ");" ^
    "foreach ($target in $targets) { if (Test-Path -LiteralPath $target) { Remove-Item -LiteralPath $target -Recurse -Force -ErrorAction SilentlyContinue } }"

echo.
echo Reset complete.
echo You can now rerun the generation pipeline from the start.

:done
popd >nul
pause
exit /b 0

:fail
popd >nul
pause
exit /b 1
