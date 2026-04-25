@echo off
setlocal EnableExtensions

call "%~dp0_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail_before_log

pushd "%FILMCREATOR_ROOT%" >nul

set "PROJECT_SLUG=%~1"
if not defined PROJECT_SLUG set "PROJECT_SLUG=princess_of_mars_test"
set "CHAPTERS=%~2"
if not defined CHAPTERS set "CHAPTERS=2-3"
set "CHARACTER_LIMIT=%~3"
if not defined CHARACTER_LIMIT set "CHARACTER_LIMIT=3"
set "ENVIRONMENT_LIMIT=%~4"
if not defined ENVIRONMENT_LIMIT set "ENVIRONMENT_LIMIT=3"
set "RUN_CHARACTER_BIBLES=%~5"
if not defined RUN_CHARACTER_BIBLES set "RUN_CHARACTER_BIBLES=1"
set "RUN_ENVIRONMENT_BIBLES=%~6"
if not defined RUN_ENVIRONMENT_BIBLES set "RUN_ENVIRONMENT_BIBLES=1"

set "LOG_DIR=%FILMCREATOR_ROOT%\logs\quick_pipeline_test"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"
set "LOG_FILE=%LOG_DIR%\latest_quick_pipeline_auto.log"
if exist "%LOG_FILE%" del "%LOG_FILE%"

call :log ""
call :log "========================================"
call :log "FilmCreator Quick Pipeline Test Auto Logged"
call :log "========================================"
call :log ""
call :log "Project slug: %PROJECT_SLUG%"
call :log "Chapters: %CHAPTERS%"
call :log "Character bible limit: %CHARACTER_LIMIT%"
call :log "Environment bible limit: %ENVIRONMENT_LIMIT%"
call :log "Include character bibles: %RUN_CHARACTER_BIBLES%"
call :log "Include environment bibles: %RUN_ENVIRONMENT_BIBLES%"
call :log "Repo root: %FILMCREATOR_ROOT%"
call :log "Log file: %LOG_FILE%"
call :log ""

call :run_step "00 Clear downstream artifacts" call "%~dp000_clear_downstream_artifacts.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

if "%RUN_CHARACTER_BIBLES%"=="1" (
    call :run_step "08 Character bibles" call "%~dp008_run_character_bibles.bat" %PROJECT_SLUG% %CHARACTER_LIMIT%
    if errorlevel 1 goto :fail
) else (
    call :log "Skipping character bibles because RUN_CHARACTER_BIBLES=%RUN_CHARACTER_BIBLES%"
)

if "%RUN_ENVIRONMENT_BIBLES%"=="1" (
    call :run_step "09 Environment bibles" call "%~dp009_run_environment_bibles.bat" %PROJECT_SLUG% %ENVIRONMENT_LIMIT%
    if errorlevel 1 goto :fail
) else (
    call :log "Skipping environment bibles because RUN_ENVIRONMENT_BIBLES=%RUN_ENVIRONMENT_BIBLES%"
)

call :run_step "01 Scene contracts" call "%~dp001_run_scene_contracts.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call :run_step "02 Scene bindings" call "%~dp002_run_scene_bindings.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call :run_step "03 Shot packages" call "%~dp003_run_shot_packages.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call :run_step "04 Dialogue timeline" call "%~dp004_run_dialogue_timeline.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call :run_step "04.5 Visual fallback synthesis" python -m orchestrator synthesize-visual-fallbacks %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

call :run_step "05 Descriptor enrichment" call "%~dp005_run_descriptor_enrichment.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call :run_step "06 Prompt preparation" call "%~dp006_run_prompt_preparation.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call :run_step "07 Quality grading" call "%~dp007_run_quality_grading.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call :log ""
call :log "========================================"
call :log "Quick pipeline test complete."
call :log "========================================"
call :log ""
call :log "Verify expected outputs:"
call :log "- projects\%PROJECT_SLUG%\02_story_analysis\world\global\VISUAL_FALLBACKS.json"
call :log "- projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_INDEX.json"
call :log "- projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_REVIEW_INDEX.json"
call :log "- projects\%PROJECT_SLUG%\02_story_analysis\grading\QUALITY_GRADE_INDEX.json"
call :log "- projects\%PROJECT_SLUG%\02_story_analysis\grading\review\QUALITY_RERUN_QUEUE.json"
call :log ""

goto :done

:run_step
set "STEP_NAME=%~1"
shift /1
call :log ""
call :log "----------------------------------------"
call :log "START: %STEP_NAME%"
call :log "----------------------------------------"
call :log "Command: %*"
%* 2>&1 | powershell -NoProfile -Command "$input | Tee-Object -FilePath '%LOG_FILE%' -Append"
set "STEP_EXIT=%ERRORLEVEL%"
if not "%STEP_EXIT%"=="0" (
    call :log "FAILED: %STEP_NAME% with exit code %STEP_EXIT%"
    exit /b %STEP_EXIT%
)
call :log "DONE: %STEP_NAME%"
exit /b 0

:log
set "LOG_MESSAGE=%~1"
echo %LOG_MESSAGE%
>> "%LOG_FILE%" echo %LOG_MESSAGE%
exit /b 0

:fail
call :log ""
call :log "========================================"
call :log "Quick pipeline test failed."
call :log "See log: %LOG_FILE%"
call :log "========================================"
call :log ""
popd >nul
echo.
echo Press any key to close this window.
pause >nul
exit /b 1

:fail_before_log
echo.
echo Quick pipeline test failed before logging could start.
echo Press any key to close this window.
pause >nul
exit /b 1

:done
popd >nul
echo.
echo Press any key to close this window.
pause >nul
exit /b 0
