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
echo Quick Pipeline Test: Generate Environment References
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
echo Variant: establishing_wide
echo Prompt variants: raw, environment_clean, environment_readability, environment_polish
echo Repo root: %FILMCREATOR_ROOT%
echo ComfyUI base URL: %FILMCREATOR_COMFY_BASE_URL%
echo ComfyUI input dir: %FILMCREATOR_COMFY_INPUT_DIR%
echo ComfyUI output dir: %FILMCREATOR_COMFY_OUTPUT_DIR%
echo.
echo Running environment reference generation for a small validation slice...
echo.
echo [1/4] prompt-variant=raw
python -m orchestrator generate-environment-references %PROJECT_SLUG% --chapters %CHAPTERS% --variant establishing_wide --limit %LIMIT% --test-slice --execute --prompt-variant raw
if errorlevel 1 goto :fail
echo.
echo [2/4] prompt-variant=environment_clean
python -m orchestrator generate-environment-references %PROJECT_SLUG% --chapters %CHAPTERS% --variant establishing_wide --limit %LIMIT% --test-slice --execute --prompt-variant environment_clean
if errorlevel 1 goto :fail
echo.
echo [3/4] prompt-variant=environment_readability
python -m orchestrator generate-environment-references %PROJECT_SLUG% --chapters %CHAPTERS% --variant establishing_wide --limit %LIMIT% --test-slice --execute --prompt-variant environment_readability
if errorlevel 1 goto :fail
echo.
echo [4/4] prompt-variant=environment_polish
python -m orchestrator generate-environment-references %PROJECT_SLUG% --chapters %CHAPTERS% --variant establishing_wide --limit %LIMIT% --test-slice --execute --prompt-variant environment_polish
if errorlevel 1 goto :fail

echo.
echo Environment reference generation complete.
echo Exit code: 0
set "EXIT_CODE=0"
goto :finish

:fail
echo.
echo Environment reference generation failed.
echo Exit code: 1
set "EXIT_CODE=1"
goto :finish

:finish
echo.
pause
popd >nul
exit /b %EXIT_CODE%
