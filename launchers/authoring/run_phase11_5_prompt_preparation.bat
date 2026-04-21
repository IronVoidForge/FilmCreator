@echo off
setlocal enabledelayedexpansion

echo ========================================
echo FilmCreator Phase 11.5 Prompt Preparation Launcher
echo ========================================
echo.

set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

for %%I in ("%~dp0..\..") do set "FILMCREATOR_ROOT=%%~fI"

echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher will run:
echo   1. prompt preparation synthesis
echo   2. pause for review
echo   3. forced prompt preparation refresh
echo.
pause

echo [1/2] Running prompt preparation synthesis...
python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 1
echo Check these outputs before continuing:
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_REVIEW_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\review\PROMPT_PREPARATION_REVIEW_QUEUE.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\characters\*
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\environments\*
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\shots\*
echo.
pause

echo [2/2] Running forced prompt preparation refresh...
python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Final review checkpoint
echo Recommended files to inspect:
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_REVIEW_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\review\PROMPT_PREPARATION_REVIEW_QUEUE.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\characters\john_carter\front_view_prompt.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\shots\CH010\CH010_SC001\SH001\primary_keyframe_prompt.md
echo.
echo Phase 11.5 prompt preparation launcher complete.
goto :end

:fail
echo.
echo Phase 11.5 prompt preparation launcher failed.
pause

:end
endlocal
