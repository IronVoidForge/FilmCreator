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
call :log "Script dir: %SCRIPT_DIR%"
call :log "Log file: %LOG_FILE%"

call :run_file_step "00 Clear downstream artifacts" "%SCRIPT_DIR%\00_clear_downstream_artifacts.bat" "%PROJECT_SLUG%" "%CHAPTERS%" "Y"
if errorlevel 1 goto :fail
if "%RUN_CHARACTER_BIBLES%"=="1" call :run_file_step "08 Character bibles" "%SCRIPT_DIR%\08_run_character_bibles.bat" "%PROJECT_SLUG%" "%CHARACTER_LIMIT%"
if errorlevel 1 goto :fail
if "%RUN_ENVIRONMENT_BIBLES%"=="1" call :run_file_step "09 Environment bibles" "%SCRIPT_DIR%\09_run_environment_bibles.bat" "%PROJECT_SLUG%" "%ENVIRONMENT_LIMIT%"
if errorlevel 1 goto :fail
call :run_file_step "01 Scene contracts" "%SCRIPT_DIR%\01_run_scene_contracts.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call :run_file_step "02 Scene bindings" "%SCRIPT_DIR%\02_run_scene_bindings.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call :run_file_step "03 Shot packages" "%SCRIPT_DIR%\03_run_shot_packages.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call :run_file_step "04 Dialogue timeline" "%SCRIPT_DIR%\04_run_dialogue_timeline.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call :run_cmd_step "04.5 Visual fallback synthesis" python -m orchestrator synthesize-visual-fallbacks "%PROJECT_SLUG%" --force
if errorlevel 1 goto :fail
call :run_file_step "05 Descriptor enrichment" "%SCRIPT_DIR%\05_run_descriptor_enrichment.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call :run_file_step "06 Prompt preparation" "%SCRIPT_DIR%\06_run_prompt_preparation.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call :run_file_step "07 Quality grading" "%SCRIPT_DIR%\07_run_quality_grading.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail

call :log ""
call :log "========================================"
call :log "Quick pipeline test complete."
call :log "========================================"
goto :done

:run_file_step
set "STEP_NAME=%~1"
set "STEP_FILE=%~2"
set "A1=%~3"
set "A2=%~4"
set "A3=%~5"
set "A4=%~6"
call :log ""
call :log "----------------------------------------"
call :log "START: %STEP_NAME%"
call :log "----------------------------------------"
powershell -NoProfile -ExecutionPolicy Bypass -Command "& { & '%STEP_FILE%' '%A1%' '%A2%' '%A3%' '%A4%' 2>&1 | Tee-Object -FilePath '%LOG_FILE%' -Append; exit $LASTEXITCODE }"
set "RC=%ERRORLEVEL%"
if not "%RC%"=="0" (
 call :log "FAILED: %STEP_NAME% with exit code %RC%"
 exit /b %RC%
)
call :log "DONE: %STEP_NAME%"
exit /b 0

:run_cmd_step
set "STEP_NAME=%~1"
shift
call :log ""
call :log "----------------------------------------"
call :log "START: %STEP_NAME%"
call :log "----------------------------------------"
powershell -NoProfile -ExecutionPolicy Bypass -Command "& { cmd /c \"%*\" 2>&1 | Tee-Object -FilePath '%LOG_FILE%' -Append; exit $LASTEXITCODE }"
set "RC=%ERRORLEVEL%"
if not "%RC%"=="0" (
 call :log "FAILED: %STEP_NAME% with exit code %RC%"
 exit /b %RC%
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
