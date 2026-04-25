@echo off
setlocal

cd /d C:\FilmCreator_MC

set PROJECT=princess_of_mars_test
set CHAPTERS=2-3

echo ============================================================
echo FilmCreator - Environment Prompt Prep Only
echo Project:  %PROJECT%
echo Chapters: %CHAPTERS%
echo ============================================================
echo.
echo This prepares environment reference prompt packages only.
echo It does NOT run ComfyUI.
echo It does NOT generate images.
echo.

echo [1/3] Refreshing environment bibles for selected chapters...
python -m orchestrator synthesize-environment-bibles %PROJECT% --chapters %CHAPTERS% --force
if errorlevel 1 goto fail

echo.
echo [2/3] Enriching descriptors for selected chapters...
python -m orchestrator synthesize-descriptor-enrichment %PROJECT% --chapters %CHAPTERS% --force
if errorlevel 1 goto fail

echo.
echo [3/3] Preparing prompt packages for selected chapter environments...
python -m orchestrator synthesize-prompt-preparation %PROJECT% --chapters %CHAPTERS% --force
if errorlevel 1 goto fail

echo.
echo Done. Environment prompts are here:
echo projects\%PROJECT%\03_prompt_packages\prepared\environments
echo.
pause
exit /b 0

:fail
echo.
echo ERROR: Environment prompt prep failed.
pause
exit /b 1
