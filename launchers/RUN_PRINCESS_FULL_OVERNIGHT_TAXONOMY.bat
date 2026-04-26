@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

set "CHAPTERS=%~2"
if "%CHAPTERS%"=="" set "CHAPTERS=2-3"

set "REPO_ROOT=C:\FilmCreator_MC"
set "LOG_DIR=%REPO_ROOT%\logs\overnight"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set "STAMP=%%i"
set "LOG_FILE=%LOG_DIR%\%PROJECT_SLUG%_overnight_full_%STAMP%.log"
set "LATEST_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_full_latest.log"

if exist "%LATEST_LOG%" del "%LATEST_LOG%"

echo ========================================
echo FilmCreator Overnight Full Pipeline
echo ========================================
echo Project slug: %PROJECT_SLUG%
echo Chapters: %CHAPTERS%
echo Repo root: %REPO_ROOT%
echo Log file: %LOG_FILE%
echo Latest log: %LATEST_LOG%
echo ========================================

cd /d "%REPO_ROOT%"
if errorlevel 1 goto :fail

call :run "00 Multi-chapter analysis / chapter summaries / breakdowns" python -c "from orchestrator.book_authoring import analyze_book; analyze_book('%PROJECT_SLUG%')"
call :run "01 Character taxonomy" python -m orchestrator synthesize-character-taxonomy "%PROJECT_SLUG%" --force
call :run "02 Identity refinement plan" python -m orchestrator refine-identities "%PROJECT_SLUG%"
call :run "03 Identity refinement apply" python -m orchestrator refine-identities "%PROJECT_SLUG%" --apply
call :run "04 Character bibles" python -m orchestrator synthesize-character-bibles "%PROJECT_SLUG%" --force
call :run "05 Environment bibles" python -m orchestrator synthesize-environment-bibles "%PROJECT_SLUG%" --force
call :run "06 Visual fallbacks" python -m orchestrator synthesize-visual-fallbacks "%PROJECT_SLUG%" --force
call :run "07 Scene contracts" python -m orchestrator synthesize-scene-contracts "%PROJECT_SLUG%" --force --chapters "%CHAPTERS%"
call :run "08 Scene bindings" python -m orchestrator synthesize-scene-bindings "%PROJECT_SLUG%" --force --chapters "%CHAPTERS%"
call :run "09 Shot packages" python -m orchestrator synthesize-shot-packages "%PROJECT_SLUG%" --force --chapters "%CHAPTERS%"
call :run "10 Dialogue timeline" python -m orchestrator synthesize-dialogue-timeline "%PROJECT_SLUG%" --force --chapters "%CHAPTERS%"
call :run "11 Descriptor enrichment" python -m orchestrator synthesize-descriptor-enrichment "%PROJECT_SLUG%" --force --chapters "%CHAPTERS%"
call :run "12 Prompt preparation" python -m orchestrator synthesize-prompt-preparation "%PROJECT_SLUG%" --force --chapters "%CHAPTERS%"
call :run "13 Quality grading" python -m orchestrator grade-artifacts "%PROJECT_SLUG%"

echo.
echo ========================================
echo Overnight pipeline completed successfully.
echo Log file: %LOG_FILE%
echo Latest log: %LATEST_LOG%
echo ========================================
exit /b 0

:run
set "STEP_NAME=%~1"
shift /1

echo.
echo ----------------------------------------
echo START: !STEP_NAME!
echo ----------------------------------------
>> "%LOG_FILE%" echo.
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LOG_FILE%" echo START: !STEP_NAME!
>> "%LOG_FILE%" echo ----------------------------------------

powershell -NoProfile -ExecutionPolicy Bypass -Command "& { & %* 2>&1 | Tee-Object -FilePath '%LOG_FILE%' -Append | Tee-Object -FilePath '%LATEST_LOG%' -Append; exit $LASTEXITCODE }"

set "EXIT_CODE=%ERRORLEVEL%"

echo.
echo DONE: !STEP_NAME! exit code !EXIT_CODE!
>> "%LOG_FILE%" echo DONE: !STEP_NAME! exit code !EXIT_CODE!
>> "%LATEST_LOG%" echo DONE: !STEP_NAME! exit code !EXIT_CODE!

if not "!EXIT_CODE!"=="0" goto :stepfail
exit /b 0

:stepfail
echo.
echo ========================================
echo FAILED: !STEP_NAME! with exit code !EXIT_CODE!
echo Log file: %LOG_FILE%
echo Latest log: %LATEST_LOG%
echo ========================================
exit /b !EXIT_CODE!

:fail
echo Failed to enter repo root: %REPO_ROOT%
exit /b 1
