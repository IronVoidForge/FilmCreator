@echo off
setlocal EnableExtensions DisableDelayedExpansion

echo.
echo This launcher is archived and obsolete.
echo It used sentinel-file skipping and is not trustworthy for smart resume.
echo Use:
echo   python -m orchestrator.overnight_pipeline_resume_check princess_of_mars_test 2-3 --report
echo or:
echo   launchers\quicktest_phase\00_VALIDATE_RESUME_STATE.bat
echo.
exit /b 1

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
set "PROJECT_DIR=%FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%"

set "LOG_DIR=%FILMCREATOR_ROOT%\logs\quick_pipeline_test"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"
set "LOG_FILE=%LOG_DIR%\latest_quick_pipeline_resume_from_045.log"
if exist "%LOG_FILE%" del "%LOG_FILE%"

call :log ""
call :log "========================================"
call :log "FilmCreator Quick Pipeline Smart Resume"
call :log "========================================"
call :log "Project slug: %PROJECT_SLUG%"
call :log "Chapters: %CHAPTERS%"
call :log "Repo root: %FILMCREATOR_ROOT%"
call :log "Script dir: %SCRIPT_DIR%"
call :log "Log file: %LOG_FILE%"

call :run_or_skip "04.5 Visual fallback synthesis" "%PROJECT_DIR%\02_story_analysis\world\global\VISUAL_FALLBACKS.json" cmd python -m orchestrator synthesize-visual-fallbacks "%PROJECT_SLUG%" --force
if errorlevel 1 goto :fail
call :run_or_skip "05 Descriptor enrichment" "%PROJECT_DIR%\02_story_analysis\descriptors\DESCRIPTOR_INDEX.json" file "%SCRIPT_DIR%\05_run_descriptor_enrichment.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call :run_or_skip "06 Prompt preparation" "%PROJECT_DIR%\03_prompt_packages\prepared\PROMPT_PREPARATION_INDEX.json" file "%SCRIPT_DIR%\06_run_prompt_preparation.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call :run_or_skip "07 Quality grading" "%PROJECT_DIR%\02_story_analysis\grading\QUALITY_GRADE_INDEX.json" file "%SCRIPT_DIR%\07_run_quality_grading.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail

call :log ""
call :log "========================================"
call :log "Smart resume pipeline complete."
call :log "========================================"
goto :done

:run_or_skip
set "STEP_NAME=%~1"
set "SENTINEL=%~2"
set "MODE=%~3"
if exist "%SENTINEL%" (
 call :log ""
 call :log "SKIP: %STEP_NAME%"
 call :log "FOUND: %SENTINEL%"
 exit /b 0
)
if "%MODE%"=="file" (
 call :run_file_step "%STEP_NAME%" "%~4" "%~5" "%~6" "%~7" "%~8"
 exit /b %ERRORLEVEL%
)
if "%MODE%"=="cmd" (
 call :run_cmd_step "%STEP_NAME%" %4 %5 %6 %7 %8 %9
 exit /b %ERRORLEVEL%
)
call :log "FAILED: %STEP_NAME% unknown mode %MODE%"
exit /b 1

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
set "CMD_A1=%~2"
set "CMD_A2=%~3"
set "CMD_A3=%~4"
set "CMD_A4=%~5"
set "CMD_A5=%~6"
set "CMD_A6=%~7"
set "CMD_A7=%~8"
set "CMD_A8=%~9"
call :log ""
call :log "----------------------------------------"
call :log "START: %STEP_NAME%"
call :log "----------------------------------------"
powershell -NoProfile -ExecutionPolicy Bypass -Command "& { & '%CMD_A1%' '%CMD_A2%' '%CMD_A3%' '%CMD_A4%' '%CMD_A5%' '%CMD_A6%' '%CMD_A7%' '%CMD_A8%' 2>&1 | Tee-Object -FilePath '%LOG_FILE%' -Append; exit $LASTEXITCODE }"
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
call :log "Smart resume pipeline failed."
call :log "See log: %LOG_FILE%"
call :log "========================================"
popd >nul
echo.
echo Press any key to close this window.
pause >nul
exit /b 1

:fail_before_log
echo.
echo Smart resume pipeline failed before logging could start.
echo Press any key to close this window.
pause >nul
exit /b 1

:done
popd >nul
echo.
echo Press any key to close this window.
pause >nul
exit /b 0
