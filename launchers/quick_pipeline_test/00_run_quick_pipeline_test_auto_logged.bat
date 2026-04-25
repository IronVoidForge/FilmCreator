@echo off
setlocal EnableExtensions DisableDelayedExpansion

set "SCRIPT_DIR=%~dp0"
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

call "%SCRIPT_DIR%\_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail_before_log

pushd "%FILMCREATOR_ROOT%" >nul
if errorlevel 1 goto :fail_before_log

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
set "STEP_OUTPUT=%LOG_DIR%\latest_step_output.tmp"
if exist "%LOG_FILE%" del "%LOG_FILE%"
if exist "%STEP_OUTPUT%" del "%STEP_OUTPUT%"

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
call :log "Script dir: %SCRIPT_DIR%"
call :log "Log file: %LOG_FILE%"
call :log ""

call :require_file "%SCRIPT_DIR%\00_clear_downstream_artifacts.bat"
if errorlevel 1 goto :fail
call :require_file "%SCRIPT_DIR%\01_run_scene_contracts.bat"
if errorlevel 1 goto :fail
call :require_file "%SCRIPT_DIR%\02_run_scene_bindings.bat"
if errorlevel 1 goto :fail
call :require_file "%SCRIPT_DIR%\03_run_shot_packages.bat"
if errorlevel 1 goto :fail
call :require_file "%SCRIPT_DIR%\04_run_dialogue_timeline.bat"
if errorlevel 1 goto :fail
call :require_file "%SCRIPT_DIR%\05_run_descriptor_enrichment.bat"
if errorlevel 1 goto :fail
call :require_file "%SCRIPT_DIR%\06_run_prompt_preparation.bat"
if errorlevel 1 goto :fail
call :require_file "%SCRIPT_DIR%\07_run_quality_grading.bat"
if errorlevel 1 goto :fail
if "%RUN_CHARACTER_BIBLES%"=="1" (
    call :require_file "%SCRIPT_DIR%\08_run_character_bibles.bat"
    if errorlevel 1 goto :fail
)
if "%RUN_ENVIRONMENT_BIBLES%"=="1" (
    call :require_file "%SCRIPT_DIR%\09_run_environment_bibles.bat"
    if errorlevel 1 goto :fail
)

call :begin_step "00 Clear downstream artifacts"
call "%SCRIPT_DIR%\00_clear_downstream_artifacts.bat" "%PROJECT_SLUG%" "%CHAPTERS%" "Y" > "%STEP_OUTPUT%" 2>&1
call :finish_step "00 Clear downstream artifacts"
if errorlevel 1 goto :fail

if "%RUN_CHARACTER_BIBLES%"=="1" (
    call :begin_step "08 Character bibles"
    call "%SCRIPT_DIR%\08_run_character_bibles.bat" "%PROJECT_SLUG%" "%CHARACTER_LIMIT%" > "%STEP_OUTPUT%" 2>&1
    call :finish_step "08 Character bibles"
    if errorlevel 1 goto :fail
) else (
    call :log "Skipping character bibles because RUN_CHARACTER_BIBLES=%RUN_CHARACTER_BIBLES%"
)

if "%RUN_ENVIRONMENT_BIBLES%"=="1" (
    call :begin_step "09 Environment bibles"
    call "%SCRIPT_DIR%\09_run_environment_bibles.bat" "%PROJECT_SLUG%" "%ENVIRONMENT_LIMIT%" > "%STEP_OUTPUT%" 2>&1
    call :finish_step "09 Environment bibles"
    if errorlevel 1 goto :fail
) else (
    call :log "Skipping environment bibles because RUN_ENVIRONMENT_BIBLES=%RUN_ENVIRONMENT_BIBLES%"
)

call :begin_step "01 Scene contracts"
call "%SCRIPT_DIR%\01_run_scene_contracts.bat" "%PROJECT_SLUG%" "%CHAPTERS%" > "%STEP_OUTPUT%" 2>&1
call :finish_step "01 Scene contracts"
if errorlevel 1 goto :fail

call :begin_step "02 Scene bindings"
call "%SCRIPT_DIR%\02_run_scene_bindings.bat" "%PROJECT_SLUG%" "%CHAPTERS%" > "%STEP_OUTPUT%" 2>&1
call :finish_step "02 Scene bindings"
if errorlevel 1 goto :fail

call :begin_step "03 Shot packages"
call "%SCRIPT_DIR%\03_run_shot_packages.bat" "%PROJECT_SLUG%" "%CHAPTERS%" > "%STEP_OUTPUT%" 2>&1
call :finish_step "03 Shot packages"
if errorlevel 1 goto :fail

call :begin_step "04 Dialogue timeline"
call "%SCRIPT_DIR%\04_run_dialogue_timeline.bat" "%PROJECT_SLUG%" "%CHAPTERS%" > "%STEP_OUTPUT%" 2>&1
call :finish_step "04 Dialogue timeline"
if errorlevel 1 goto :fail

call :begin_step "04.5 Visual fallback synthesis"
python -m orchestrator synthesize-visual-fallbacks "%PROJECT_SLUG%" --force > "%STEP_OUTPUT%" 2>&1
call :finish_step "04.5 Visual fallback synthesis"
if errorlevel 1 goto :fail

call :begin_step "05 Descriptor enrichment"
call "%SCRIPT_DIR%\05_run_descriptor_enrichment.bat" "%PROJECT_SLUG%" "%CHAPTERS%" > "%STEP_OUTPUT%" 2>&1
call :finish_step "05 Descriptor enrichment"
if errorlevel 1 goto :fail

call :begin_step "06 Prompt preparation"
call "%SCRIPT_DIR%\06_run_prompt_preparation.bat" "%PROJECT_SLUG%" "%CHAPTERS%" > "%STEP_OUTPUT%" 2>&1
call :finish_step "06 Prompt preparation"
if errorlevel 1 goto :fail

call :begin_step "07 Quality grading"
call "%SCRIPT_DIR%\07_run_quality_grading.bat" "%PROJECT_SLUG%" "%CHAPTERS%" > "%STEP_OUTPUT%" 2>&1
call :finish_step "07 Quality grading"
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

:require_file
if exist "%~1" exit /b 0
call :log "Missing required BAT file: %~1"
exit /b 1

:begin_step
set "STEP_NAME=%~1"
if exist "%STEP_OUTPUT%" del "%STEP_OUTPUT%"
call :log ""
call :log "----------------------------------------"
call :log "START: %STEP_NAME%"
call :log "----------------------------------------"
exit /b 0

:finish_step
set "STEP_NAME=%~1"
set "STEP_EXIT=%ERRORLEVEL%"
if exist "%STEP_OUTPUT%" (
    type "%STEP_OUTPUT%"
    type "%STEP_OUTPUT%" >> "%LOG_FILE%"
    del "%STEP_OUTPUT%"
) else (
    call :log "Warning: step output file was not created."
)
if not "%STEP_EXIT%"=="0" (
    call :log "FAILED: %STEP_NAME% with exit code %STEP_EXIT%"
    exit /b %STEP_EXIT%
)
call :log "DONE: %STEP_NAME%"
exit /b 0

:log
if "%~1"=="" (
    echo.
    >> "%LOG_FILE%" echo.
) else (
    echo %~1
    >> "%LOG_FILE%" echo %~1
)
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
