@echo off
setlocal EnableExtensions

set "BAT_VERSION=SIMPLE_BAT_CMDSTRING_V4_2026-04-26"

set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

set "CHAPTERS=%~2"
set "MODE=%~3"

if /I "%CHAPTERS%"=="PLAN_ONLY" (
    set "MODE=PLAN_ONLY"
    set "CHAPTERS="
)

if /I "%CHAPTERS%"=="VALIDATE_ONLY" (
    set "MODE=VALIDATE_ONLY"
    set "CHAPTERS="
)

if "%CHAPTERS%"=="" (
    set "CHAPTERS_DISPLAY=ALL"
) else (
    set "CHAPTERS_DISPLAY=%CHAPTERS%"
)

call "%~dp0_shared\resolve_filmcreator_root.bat" "%~dp0"
if errorlevel 1 (
    echo Failed to resolve FilmCreator root.
    pause
    exit /b 1
)

set "REPO_ROOT=%FILMCREATOR_ROOT%"
set "LOG_DIR=%REPO_ROOT%\logs\overnight"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set "STAMP=%%i"

set "LOG_FILE=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_%STAMP%.log"
set "LATEST_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_latest.log"
set "TEMP_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_step.tmp"

if exist "%LATEST_LOG%" del "%LATEST_LOG%" >nul 2>nul
if exist "%TEMP_LOG%" del "%TEMP_LOG%" >nul 2>nul

cd /d "%REPO_ROOT%"
if errorlevel 1 (
    echo Failed to change to repo root: %REPO_ROOT%
    pause
    exit /b 1
)

echo ============================================================
echo FilmCreator Overnight Resume Pipeline
echo BAT_VERSION: %BAT_VERSION%
echo Project:     %PROJECT_SLUG%
echo Chapters:    %CHAPTERS_DISPLAY%
echo Repo root:   %REPO_ROOT%
echo Log:         %LOG_FILE%
echo Latest:      %LATEST_LOG%
echo ============================================================
echo.

echo ============================================================>>"%LOG_FILE%"
echo FilmCreator Overnight Resume Pipeline>>"%LOG_FILE%"
echo BAT_VERSION: %BAT_VERSION%>>"%LOG_FILE%"
echo Project: %PROJECT_SLUG%>>"%LOG_FILE%"
echo Chapters: %CHAPTERS_DISPLAY%>>"%LOG_FILE%"
echo Repo root: %REPO_ROOT%>>"%LOG_FILE%"
echo Log file: %LOG_FILE%>>"%LOG_FILE%"
echo Latest log: %LATEST_LOG%>>"%LOG_FILE%"
echo ============================================================>>"%LOG_FILE%"

copy /y "%LOG_FILE%" "%LATEST_LOG%" >nul

if /I "%MODE%"=="VALIDATE_ONLY" (
    echo VALIDATE_ONLY
    python -m orchestrator.overnight_pipeline_resume_check "%PROJECT_SLUG%" "%CHAPTERS%" --report
    echo.
    echo Log: %LOG_FILE%
    pause
    exit /b 0
)

echo Detecting resume stage...
python -m orchestrator.overnight_pipeline_resume_check "%PROJECT_SLUG%" "%CHAPTERS%" > "%TEMP_LOG%" 2>&1
set "CHECK_EXIT=%ERRORLEVEL%"

type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"

if not "%CHECK_EXIT%"=="0" (
    echo ERROR: Resume detection failed. exit=%CHECK_EXIT%
    echo See log: %LOG_FILE%
    type "%TEMP_LOG%"
    pause
    exit /b %CHECK_EXIT%
)

set "RESUME_STAGE="
for /f "usebackq delims=" %%s in ("%TEMP_LOG%") do (
    if not defined RESUME_STAGE set "RESUME_STAGE=%%s"
)

if "%RESUME_STAGE%"=="" (
    echo ERROR: Resume detection produced no stage.
    echo See log: %LOG_FILE%
    pause
    exit /b 1
)

echo Detected: %RESUME_STAGE%
echo Detected: %RESUME_STAGE%>>"%LOG_FILE%"
echo Detected: %RESUME_STAGE%>>"%LATEST_LOG%"
echo.

if "%RESUME_STAGE%"=="complete" (
    echo Already complete.
    echo Log: %LOG_FILE%
    pause
    exit /b 0
)

set "START_LEVEL="
if "%RESUME_STAGE%"=="story_analysis" set "START_LEVEL=1"
if "%RESUME_STAGE%"=="character_taxonomy" set "START_LEVEL=3"
if "%RESUME_STAGE%"=="identity_refinement" set "START_LEVEL=4"
if "%RESUME_STAGE%"=="character_bibles" set "START_LEVEL=6"
if "%RESUME_STAGE%"=="environment_bibles" set "START_LEVEL=7"
if "%RESUME_STAGE%"=="visual_fallbacks" set "START_LEVEL=8"
if "%RESUME_STAGE%"=="scene_contracts" set "START_LEVEL=9"
if "%RESUME_STAGE%"=="scene_bindings" set "START_LEVEL=10"
if "%RESUME_STAGE%"=="shot_packages" set "START_LEVEL=11"
if "%RESUME_STAGE%"=="dialogue_timeline" set "START_LEVEL=12"
if "%RESUME_STAGE%"=="descriptor_enrichment" set "START_LEVEL=13"
if "%RESUME_STAGE%"=="prompt_preparation" set "START_LEVEL=14"
if "%RESUME_STAGE%"=="quality_grading" set "START_LEVEL=15"

if "%START_LEVEL%"=="" (
    echo ERROR: Unknown resume stage: %RESUME_STAGE%
    pause
    exit /b 1
)

if /I "%MODE%"=="PLAN_ONLY" (
    echo PLAN_ONLY
    echo BAT_VERSION: %BAT_VERSION%
    echo resume=%RESUME_STAGE% start_level=%START_LEVEL% project=%PROJECT_SLUG% chapters=%CHAPTERS_DISPLAY%
    echo.
    echo Step list:
    if %START_LEVEL% LEQ 1 echo 01 LM Studio check
    if %START_LEVEL% LEQ 2 echo 02 Story analysis
    if %START_LEVEL% LEQ 3 echo 03 Character taxonomy
    if %START_LEVEL% LEQ 4 echo 04 Identity refinement plan
    if %START_LEVEL% LEQ 5 echo 05 Identity refinement apply
    if %START_LEVEL% LEQ 6 echo 06 Character bibles
    if %START_LEVEL% LEQ 7 echo 07 Environment bibles
    if %START_LEVEL% LEQ 8 echo 08 Visual fallbacks
    if %START_LEVEL% LEQ 9 echo 09 Scene contracts
    if %START_LEVEL% LEQ 10 echo 10 Scene bindings
    if %START_LEVEL% LEQ 11 echo 11 Shot packages
    if %START_LEVEL% LEQ 12 echo 12 Dialogue timeline
    if %START_LEVEL% LEQ 13 echo 13 Descriptor enrichment
    if %START_LEVEL% LEQ 14 echo 14 Prompt preparation
    if %START_LEVEL% LEQ 15 echo 15 Quality grading
    echo.
    echo Log: %LOG_FILE%
    exit /b 0
)

echo Resume stage: %RESUME_STAGE%
echo Start level:  %START_LEVEL%
echo Resume stage: %RESUME_STAGE%>>"%LOG_FILE%"
echo Start level: %START_LEVEL%>>"%LOG_FILE%"
echo Resume stage: %RESUME_STAGE%>>"%LATEST_LOG%"
echo Start level: %START_LEVEL%>>"%LATEST_LOG%"
echo.

if %START_LEVEL% LEQ 1 (
    call :run_step "01 LM Studio check" "python -m orchestrator diagnostics-lmstudio"
    if errorlevel 1 goto :fail_run
)

REM Story analysis intentionally not included in this downstream resume runner.

if %START_LEVEL% LEQ 3 (
    call :run_step "03 Character taxonomy" "python -m orchestrator synthesize-character-taxonomy ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 4 (
    call :run_step "04 Identity refinement plan" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"""
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 5 (
    call :run_step "05 Identity refinement apply" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"" --apply"
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 6 (
    call :run_step "06 Character bibles" "python -m orchestrator synthesize-character-bibles ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 7 (
    call :run_step "07 Environment bibles" "python -m orchestrator synthesize-environment-bibles ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 8 (
    call :run_step "08 Visual fallbacks" "python -m orchestrator synthesize-visual-fallbacks ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 9 (
    if "%CHAPTERS%"=="" (
        call :run_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 10 (
    if "%CHAPTERS%"=="" (
        call :run_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 11 (
    if "%CHAPTERS%"=="" (
        call :run_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 12 (
    if "%CHAPTERS%"=="" (
        call :run_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 13 (
    if "%CHAPTERS%"=="" (
        call :run_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 14 (
    if "%CHAPTERS%"=="" (
        call :run_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :fail_run
)

if %START_LEVEL% LEQ 15 (
    call :run_step "15 Quality grading" "python -m orchestrator grade-artifacts ""%PROJECT_SLUG%"""
    if errorlevel 1 goto :fail_run
)

echo.
echo ============================================================
echo COMPLETE
echo Log:    %LOG_FILE%
echo Latest: %LATEST_LOG%
echo ============================================================
pause
exit /b 0

:run_step
set "STEP_NAME=%~1"
set "STEP_COMMAND=%~2"

echo.
echo ----------------------------------------
echo START: %STEP_NAME%
echo ----------------------------------------

echo.>>"%LOG_FILE%"
echo ---------------------------------------->>"%LOG_FILE%"
echo START: %STEP_NAME%>>"%LOG_FILE%"
echo COMMAND: %STEP_COMMAND%>>"%LOG_FILE%"
echo ---------------------------------------->>"%LOG_FILE%"

echo.>>"%LATEST_LOG%"
echo ---------------------------------------->>"%LATEST_LOG%"
echo START: %STEP_NAME%>>"%LATEST_LOG%"
echo COMMAND: %STEP_COMMAND%>>"%LATEST_LOG%"
echo ---------------------------------------->>"%LATEST_LOG%"

cmd /c %STEP_COMMAND% > "%TEMP_LOG%" 2>&1
set "STEP_EXIT=%ERRORLEVEL%"

type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"

if not "%STEP_EXIT%"=="0" (
    echo FAILED: %STEP_NAME% exit code %STEP_EXIT%
    echo See log: %LOG_FILE%
    echo Last output:
    type "%TEMP_LOG%"
    exit /b %STEP_EXIT%
)

findstr /R /C:"^\[[A-Za-z0-9_-][A-Za-z0-9_-]*\].*starting" "%TEMP_LOG%"
findstr /R /C:"^\[[A-Za-z0-9_-][A-Za-z0-9_-]*\].*finished" "%TEMP_LOG%"
findstr /I /C:"total_registry_entries" /C:"candidate_count" /C:"comparison_count" /C:"decision_count" /C:"applied_count" /C:"human_review_count" /C:"total_entries" /C:"total_chapters" /C:"total_events" /C:"total_scene_entries" /C:"total_shot_entries" /C:"total_scene_bindings" /C:"total_shot_bindings" /C:"synthesized_count" /C:"reused_count" /C:"review_queue_count" /C:"needs_review_count" /C:"unknown_count" /C:"total_records" "%TEMP_LOG%"

echo DONE: %STEP_NAME% exit code 0
exit /b 0

:fail_run
echo.
echo ============================================================
echo STOPPED
echo Log:    %LOG_FILE%
echo Latest: %LATEST_LOG%
echo ============================================================
pause
exit /b 1