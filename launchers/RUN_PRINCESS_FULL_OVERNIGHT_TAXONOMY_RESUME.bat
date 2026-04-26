@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

set "CHAPTERS=%~2"
if "%CHAPTERS%"=="" set "CHAPTERS=2-3"

set "MODE=%~3"

call "%~dp0_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail_resolver
set "REPO_ROOT=%FILMCREATOR_ROOT%"

set "LOG_DIR=%REPO_ROOT%\logs\overnight"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set "STAMP=%%i"
set "LOG_FILE=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_%STAMP%.log"
set "LATEST_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_latest.log"
set "TEMP_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_step.tmp"
set "TEMP_PY_SCRIPT=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_temp.py"

if exist "%LATEST_LOG%" del "%LATEST_LOG%"

echo ========================================
echo FilmCreator Overnight Resume Pipeline
echo ========================================
echo Project slug: %PROJECT_SLUG%
echo Chapters: %CHAPTERS%
echo Repo root: %REPO_ROOT%
echo Log file: %LOG_FILE%
echo Latest log: %LATEST_LOG%
echo ========================================
echo.
echo RESUME MODE:
echo Resume mode is non-destructive and will not clear artifacts.
echo The pipeline will detect completed stages and resume from the first incomplete stage.
echo.
echo SCOPE:
if "%CHAPTERS%"=="" (
    echo This run is whole-project downstream:
    echo - chapter-aware downstream commands will run without --chapters filters
) else (
    echo This run is mixed-scope:
    echo - analysis, taxonomy, identity refinement, bibles, environment bibles, visual fallbacks run on the whole project
    echo - scene contracts, scene bindings, shot packages, dialogue timeline, descriptor enrichment, and prompt preparation run only on chapters %CHAPTERS%
    echo - quality grading runs on all available artifacts
)
echo.
echo ========================================

cd /d "%REPO_ROOT%"
if errorlevel 1 goto :fail

if /I "%MODE%"=="VALIDATE_ONLY" (
    echo.
    echo ========================================
    echo VALIDATE ONLY MODE
    echo ========================================
    echo Project: %PROJECT_SLUG%
    echo Chapters: %CHAPTERS%
    echo.
    python -m orchestrator.overnight_pipeline_resume_check "%PROJECT_SLUG%" "%CHAPTERS%" --report
    echo.
    echo ========================================
    pause
    exit /b 0
)

call :detect_resume_stage
if errorlevel 1 goto :end_with_error

if "%RESUME_STAGE%"=="complete" (
    echo.
    echo ========================================
    echo All pipeline stages are already complete.
    echo No work needed.
    echo ========================================
    pause
    exit /b 0
)

echo.
echo Resuming from stage: %RESUME_STAGE%
echo.
>> "%LOG_FILE%" echo Resuming from stage: %RESUME_STAGE%
>> "%LATEST_LOG%" echo Resuming from stage: %RESUME_STAGE%

if "%RESUME_STAGE%"=="story_analysis" goto :stage_story_analysis
if "%RESUME_STAGE%"=="character_taxonomy" goto :stage_character_taxonomy
if "%RESUME_STAGE%"=="identity_refinement" goto :stage_identity_refinement
if "%RESUME_STAGE%"=="character_bibles" goto :stage_character_bibles
if "%RESUME_STAGE%"=="environment_bibles" goto :stage_environment_bibles
if "%RESUME_STAGE%"=="visual_fallbacks" goto :stage_visual_fallbacks
if "%RESUME_STAGE%"=="scene_contracts" goto :stage_scene_contracts
if "%RESUME_STAGE%"=="scene_bindings" goto :stage_scene_bindings
if "%RESUME_STAGE%"=="shot_packages" goto :stage_shot_packages
if "%RESUME_STAGE%"=="dialogue_timeline" goto :stage_dialogue_timeline
if "%RESUME_STAGE%"=="descriptor_enrichment" goto :stage_descriptor_enrichment
if "%RESUME_STAGE%"=="prompt_preparation" goto :stage_prompt_preparation
if "%RESUME_STAGE%"=="quality_grading" goto :stage_quality_grading

echo Unknown resume stage: %RESUME_STAGE%
goto :end_with_error

:stage_story_analysis
call :lm_studio_check
if errorlevel 1 goto :end_with_error

call :analyze_book
if errorlevel 1 goto :end_with_error

:stage_character_taxonomy
call :run_step "03 Character taxonomy" "python -m orchestrator synthesize-character-taxonomy ""%PROJECT_SLUG%"" --force"
if errorlevel 1 goto :end_with_error

:stage_identity_refinement
call :run_step "04 Identity refinement plan" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"""
if errorlevel 1 goto :end_with_error

call :run_step "05 Identity refinement apply" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"" --apply"
if errorlevel 1 goto :end_with_error

:stage_character_bibles
call :run_step "06 Character bibles" "python -m orchestrator synthesize-character-bibles ""%PROJECT_SLUG%"" --force"
if errorlevel 1 goto :end_with_error

:stage_environment_bibles
call :run_step "07 Environment bibles" "python -m orchestrator synthesize-environment-bibles ""%PROJECT_SLUG%"" --force"
if errorlevel 1 goto :end_with_error

:stage_visual_fallbacks
call :run_step "08 Visual fallbacks" "python -m orchestrator synthesize-visual-fallbacks ""%PROJECT_SLUG%"" --force"
if errorlevel 1 goto :end_with_error

:stage_scene_contracts
if "%CHAPTERS%"=="" (
    call :run_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

:stage_scene_bindings
if "%CHAPTERS%"=="" (
    call :run_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

:stage_shot_packages
if "%CHAPTERS%"=="" (
    call :run_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

:stage_dialogue_timeline
if "%CHAPTERS%"=="" (
    call :run_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

:stage_descriptor_enrichment
if "%CHAPTERS%"=="" (
    call :run_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

:stage_prompt_preparation
if "%CHAPTERS%"=="" (
    call :run_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

:stage_quality_grading
call :run_step "15 Quality grading" "python -m orchestrator grade-artifacts ""%PROJECT_SLUG%"""
if errorlevel 1 goto :end_with_error

echo.
echo ========================================
echo Overnight resume pipeline completed successfully.
echo Log file: %LOG_FILE%
echo Latest log: %LATEST_LOG%
echo ========================================
pause
exit /b 0

:end_with_error
echo.
echo ========================================
echo Pipeline stopped due to error
echo Log file: %LOG_FILE%
echo Latest log: %LATEST_LOG%
echo ========================================
pause
exit /b 1

:detect_resume_stage
echo.
echo ----------------------------------------
echo Detecting resume stage...
echo ----------------------------------------
>> "%LOG_FILE%" echo.
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LOG_FILE%" echo Detecting resume stage...
>> "%LOG_FILE%" echo ----------------------------------------

cd /d "%REPO_ROOT%"
python -m orchestrator.overnight_pipeline_resume_check "%PROJECT_SLUG%" "%CHAPTERS%" > "%TEMP_LOG%" 2>&1
set "EXIT_CODE=%ERRORLEVEL%"

if not "!EXIT_CODE!"=="0" (
    type "%TEMP_LOG%"
    type "%TEMP_LOG%" >> "%LOG_FILE%"
    type "%TEMP_LOG%" >> "%LATEST_LOG%"
    del "%TEMP_LOG%" >nul 2>nul
    echo Failed to detect resume stage
    exit /b 1
)

set /p RESUME_STAGE=<"%TEMP_LOG%"
del "%TEMP_LOG%" >nul 2>nul

echo Detected stage: %RESUME_STAGE%
>> "%LOG_FILE%" echo Detected stage: %RESUME_STAGE%
>> "%LATEST_LOG%" echo Detected stage: %RESUME_STAGE%

exit /b 0

:lm_studio_check
echo.
echo ----------------------------------------
echo START: 01 LM Studio connectivity check
echo ----------------------------------------
>> "%LOG_FILE%" echo.
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LOG_FILE%" echo START: 01 LM Studio connectivity check
>> "%LOG_FILE%" echo ----------------------------------------

echo import sys > "%TEMP_PY_SCRIPT%"
echo sys.path.insert(0, '.') >> "%TEMP_PY_SCRIPT%"
echo from json import dumps >> "%TEMP_PY_SCRIPT%"
echo from orchestrator.settings import load_runtime_settings >> "%TEMP_PY_SCRIPT%"
echo from orchestrator.lmstudio_client import LMStudioClient >> "%TEMP_PY_SCRIPT%"
echo settings = load_runtime_settings() >> "%TEMP_PY_SCRIPT%"
echo client = LMStudioClient(settings) >> "%TEMP_PY_SCRIPT%"
echo print(dumps(client.check().to_dict(), indent=2)) >> "%TEMP_PY_SCRIPT%"

cd /d "%REPO_ROOT%"
python "%TEMP_PY_SCRIPT%" > "%TEMP_LOG%" 2>&1
set "EXIT_CODE=%ERRORLEVEL%"

type "%TEMP_LOG%"
type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"
del "%TEMP_LOG%" >nul 2>nul
del "%TEMP_PY_SCRIPT%" >nul 2>nul

echo.
echo DONE: 01 LM Studio connectivity check exit code !EXIT_CODE!
>> "%LOG_FILE%" echo DONE: 01 LM Studio connectivity check exit code !EXIT_CODE!
>> "%LATEST_LOG%" echo DONE: 01 LM Studio connectivity check exit code !EXIT_CODE!

if not "!EXIT_CODE!"=="0" goto :stepfail_lm
exit /b 0

:analyze_book
echo.
echo ----------------------------------------
echo START: 02 Multi-chapter analysis / chapter summaries / breakdowns
echo ----------------------------------------
>> "%LOG_FILE%" echo.
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LOG_FILE%" echo START: 02 Multi-chapter analysis / chapter summaries / breakdowns
>> "%LOG_FILE%" echo ----------------------------------------

echo import sys > "%TEMP_PY_SCRIPT%"
echo sys.path.insert(0, '.') >> "%TEMP_PY_SCRIPT%"
echo from orchestrator.book_authoring import analyze_book >> "%TEMP_PY_SCRIPT%"
echo import json >> "%TEMP_PY_SCRIPT%"
echo summary = analyze_book(project_slug='%PROJECT_SLUG%') >> "%TEMP_PY_SCRIPT%"
echo print(json.dumps(summary.to_dict(), indent=2)) >> "%TEMP_PY_SCRIPT%"

cd /d "%REPO_ROOT%"
python "%TEMP_PY_SCRIPT%" > "%TEMP_LOG%" 2>&1
set "EXIT_CODE=%ERRORLEVEL%"

type "%TEMP_LOG%"
type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"
del "%TEMP_LOG%" >nul 2>nul
del "%TEMP_PY_SCRIPT%" >nul 2>nul

echo.
echo DONE: 02 Multi-chapter analysis / chapter summaries / breakdowns exit code !EXIT_CODE!
>> "%LOG_FILE%" echo DONE: 02 Multi-chapter analysis / chapter summaries / breakdowns exit code !EXIT_CODE!
>> "%LATEST_LOG%" echo DONE: 02 Multi-chapter analysis / chapter summaries / breakdowns exit code !EXIT_CODE!

if not "!EXIT_CODE!"=="0" goto :stepfail_analyze
exit /b 0

:run_step
set "STEP_NAME=%~1"
set "CMD_LINE=%~2"

echo.
echo ----------------------------------------
echo START: !STEP_NAME!
echo COMMAND: !CMD_LINE!
echo ----------------------------------------
>> "%LOG_FILE%" echo.
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LOG_FILE%" echo START: !STEP_NAME!
>> "%LOG_FILE%" echo COMMAND: !CMD_LINE!
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LATEST_LOG%" echo.
>> "%LATEST_LOG%" echo ----------------------------------------
>> "%LATEST_LOG%" echo START: !STEP_NAME!
>> "%LATEST_LOG%" echo COMMAND: !CMD_LINE!
>> "%LATEST_LOG%" echo ----------------------------------------

set "TEMP_STEP_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_step.tmp"
if exist "%TEMP_STEP_LOG%" del "%TEMP_STEP_LOG%" >nul 2>nul

cmd /d /s /c "!CMD_LINE!" > "%TEMP_STEP_LOG%" 2>&1
set "EXIT_CODE=!ERRORLEVEL!"

type "%TEMP_STEP_LOG%"
type "%TEMP_STEP_LOG%" >> "%LOG_FILE%"
type "%TEMP_STEP_LOG%" >> "%LATEST_LOG%"
del "%TEMP_STEP_LOG%" >nul 2>nul

echo.
echo DONE: !STEP_NAME! exit code !EXIT_CODE!
>> "%LOG_FILE%" echo DONE: !STEP_NAME! exit code !EXIT_CODE!
>> "%LATEST_LOG%" echo DONE: !STEP_NAME! exit code !EXIT_CODE!

if not "!EXIT_CODE!"=="0" goto :stepfail
exit /b 0

:stepfail_lm
set "STEP_NAME=01 LM Studio connectivity check"
goto :stepfail_common

:stepfail_analyze
set "STEP_NAME=02 Multi-chapter analysis / chapter summaries / breakdowns"
goto :stepfail_common

:stepfail
:stepfail_common
echo.
echo ========================================
echo FAILED: !STEP_NAME! with exit code !EXIT_CODE!
echo Log file: %LOG_FILE%
echo Latest log: %LATEST_LOG%
echo ========================================
>> "%LOG_FILE%" echo FAILED: !STEP_NAME! with exit code !EXIT_CODE!
>> "%LATEST_LOG%" echo FAILED: !STEP_NAME! with exit code !EXIT_CODE!
exit /b !EXIT_CODE!

:fail
echo Failed to enter repo root: %REPO_ROOT%
exit /b 1

:fail_resolver
echo Failed to resolve FilmCreator root
exit /b 1
