@echo off
setlocal

call "%~dp0_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

call "%~dp0_shared\start_clean_comfyui_8190.bat"
if errorlevel 1 goto :fail
set "FILMCREATOR_COMFY_BASE_URL=http://127.0.0.1:8190"
set "FILMCREATOR_COMFY_INPUT_DIR=%FILMCREATOR_ROOT%\.comfy_clean\input"
set "FILMCREATOR_COMFY_OUTPUT_DIR=%FILMCREATOR_ROOT%\.comfy_clean\output"

echo.
echo ========================================
echo Quick Pipeline Test: Generate Character References
echo ========================================
echo.
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"
set "LIMIT=%~2"
if "%LIMIT%"=="" set "LIMIT=2"
set "CHAPTERS=%~3"
if "%CHAPTERS%"=="" set "CHAPTERS=2-3"

echo.
echo Project slug: %PROJECT_SLUG%
echo Chapters: %CHAPTERS%
echo Limit: %LIMIT%
echo Variant: bust_portrait
echo Prompt variants: raw, character_clean, character_readability, character_polish
echo Repo root: %FILMCREATOR_ROOT%
echo ComfyUI base URL: %FILMCREATOR_COMFY_BASE_URL%
echo ComfyUI input dir: %FILMCREATOR_COMFY_INPUT_DIR%
echo ComfyUI output dir: %FILMCREATOR_COMFY_OUTPUT_DIR%
echo.
echo Running character reference generation for a small validation slice...
echo.
echo [1/4] prompt-variant=raw
python -m orchestrator generate-character-references %PROJECT_SLUG% --chapters %CHAPTERS% --variant bust_portrait --limit %LIMIT% --test-slice --execute --prompt-variant raw
if errorlevel 1 goto :fail
echo.
echo [2/4] prompt-variant=character_clean
python -m orchestrator generate-character-references %PROJECT_SLUG% --chapters %CHAPTERS% --variant bust_portrait --limit %LIMIT% --test-slice --execute --prompt-variant character_clean
if errorlevel 1 goto :fail
echo.
echo [3/4] prompt-variant=character_readability
python -m orchestrator generate-character-references %PROJECT_SLUG% --chapters %CHAPTERS% --variant bust_portrait --limit %LIMIT% --test-slice --execute --prompt-variant character_readability
if errorlevel 1 goto :fail
echo.
echo [4/4] prompt-variant=character_polish
python -m orchestrator generate-character-references %PROJECT_SLUG% --chapters %CHAPTERS% --variant bust_portrait --limit %LIMIT% --test-slice --execute --prompt-variant character_polish
if errorlevel 1 goto :fail

echo.
echo Character reference generation complete.
echo Exit code: 0
set "EXIT_CODE=0"
goto :finish

:fail
echo.
echo Character reference generation failed.
echo Exit code: 1
set "EXIT_CODE=1"
goto :finish

:finish
echo.
pause
popd >nul
exit /b %EXIT_CODE%
