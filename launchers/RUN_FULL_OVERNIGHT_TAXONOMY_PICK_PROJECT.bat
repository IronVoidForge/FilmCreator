@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "PROJECT_SLUG=%~1"
set "CHAPTERS=%~2"
set "NO_CLEAR=%~3"

call "%~dp0_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail_resolver
set "REPO_ROOT=%FILMCREATOR_ROOT%"

if "%PROJECT_SLUG%"=="" (
    call :pick_project
    if errorlevel 1 goto :picker_failed
)

if "%CHAPTERS%"=="" (
    call :pick_chapters
    if errorlevel 1 goto :picker_failed
)

if "%NO_CLEAR%"=="" (
    call :pick_clear_mode
    if errorlevel 1 goto :picker_failed
)

set "LOG_DIR=%REPO_ROOT%\logs\overnight"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set "STAMP=%%i"
set "LOG_FILE=%LOG_DIR%\%PROJECT_SLUG%_overnight_full_%STAMP%.log"
set "LATEST_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_full_latest.log"
set "TEMP_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_step.tmp"
set "TEMP_PS_SCRIPT=%LOG_DIR%\%PROJECT_SLUG%_overnight_temp.ps1"
set "TEMP_PY_SCRIPT=%LOG_DIR%\%PROJECT_SLUG%_overnight_temp.py"

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
echo.
echo SCOPE WARNING:
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
if /I "%NO_CLEAR%"=="NO_CLEAR" (
    echo CLEAR SKIPPED: NO_CLEAR flag detected
) else (
    echo WARNING: This will clear generated artifacts for %PROJECT_SLUG% and regenerate them.
    echo Preserved: source/raw book/project metadata.
    echo Cleared: chapter analysis, breakdowns, taxonomy, bibles, downstream prompt/quality artifacts.
)
echo.
echo ========================================

cd /d "%REPO_ROOT%"
if errorlevel 1 goto :fail

if /I NOT "%NO_CLEAR%"=="NO_CLEAR" (
    call :clear_artifacts
    if errorlevel 1 goto :end_with_error
)

call :lm_studio_check
if errorlevel 1 goto :end_with_error

call :analyze_book
if errorlevel 1 goto :end_with_error

call :run_step "03 Character taxonomy" "python -m orchestrator synthesize-character-taxonomy ""%PROJECT_SLUG%"" --force"
if errorlevel 1 goto :end_with_error

call :run_step "04 Identity refinement plan" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"""
if errorlevel 1 goto :end_with_error

call :run_step "05 Identity refinement apply" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"" --apply"
if errorlevel 1 goto :end_with_error

call :run_step "06 Character bibles" "python -m orchestrator synthesize-character-bibles ""%PROJECT_SLUG%"" --force"
if errorlevel 1 goto :end_with_error

call :run_step "07 Environment bibles" "python -m orchestrator synthesize-environment-bibles ""%PROJECT_SLUG%"" --force"
if errorlevel 1 goto :end_with_error

call :run_step "08 Visual fallbacks" "python -m orchestrator synthesize-visual-fallbacks ""%PROJECT_SLUG%"" --force"
if errorlevel 1 goto :end_with_error

if "%CHAPTERS%"=="" (
    call :run_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

if "%CHAPTERS%"=="" (
    call :run_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

if "%CHAPTERS%"=="" (
    call :run_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

if "%CHAPTERS%"=="" (
    call :run_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

if "%CHAPTERS%"=="" (
    call :run_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

if "%CHAPTERS%"=="" (
    call :run_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
) else (
    call :run_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    if errorlevel 1 goto :end_with_error
)

call :run_step "15 Quality grading" "python -m orchestrator grade-artifacts ""%PROJECT_SLUG%"""
if errorlevel 1 goto :end_with_error

echo.
echo ========================================
echo Overnight pipeline completed successfully.
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

:clear_artifacts
echo.
echo ----------------------------------------
echo START: 00 Clear generated artifacts
echo ----------------------------------------
>> "%LOG_FILE%" echo.
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LOG_FILE%" echo START: 00 Clear generated artifacts
>> "%LOG_FILE%" echo ----------------------------------------

echo $paths = @( > "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\chapter_analysis', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\character_breakdowns', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\environment_breakdowns', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\world\chapters', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\taxonomy', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\bibles', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\contracts', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\timelines', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\descriptors', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\grading', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\quality', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\dialogue_enrichment', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\world\refinement', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\02_story_analysis\world\global\VISUAL_FALLBACKS.json', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\03_prompt_packages', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\03_reference_assets', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\05_scenes', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\06_reviews', >> "%TEMP_PS_SCRIPT%"
echo   'projects\%PROJECT_SLUG%\07_finals' >> "%TEMP_PS_SCRIPT%"
echo ^) >> "%TEMP_PS_SCRIPT%"
echo foreach ($p in $paths) { >> "%TEMP_PS_SCRIPT%"
echo   if (Test-Path $p) { >> "%TEMP_PS_SCRIPT%"
echo     Write-Host "Removing: $p" >> "%TEMP_PS_SCRIPT%"
echo     Remove-Item -Path $p -Recurse -Force -ErrorAction Stop >> "%TEMP_PS_SCRIPT%"
echo   } else { >> "%TEMP_PS_SCRIPT%"
echo     Write-Host "Not found (skipping): $p" >> "%TEMP_PS_SCRIPT%"
echo   } >> "%TEMP_PS_SCRIPT%"
echo } >> "%TEMP_PS_SCRIPT%"
echo Write-Host "Clear completed successfully" >> "%TEMP_PS_SCRIPT%"

powershell -NoProfile -ExecutionPolicy Bypass -File "%TEMP_PS_SCRIPT%" > "%TEMP_LOG%" 2>&1
set "EXIT_CODE=%ERRORLEVEL%"

type "%TEMP_LOG%"
type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"
del "%TEMP_LOG%" >nul 2>nul
del "%TEMP_PS_SCRIPT%" >nul 2>nul

echo.
echo DONE: 00 Clear generated artifacts exit code !EXIT_CODE!
>> "%LOG_FILE%" echo DONE: 00 Clear generated artifacts exit code !EXIT_CODE!
>> "%LATEST_LOG%" echo DONE: 00 Clear generated artifacts exit code !EXIT_CODE!

if not "!EXIT_CODE!"=="0" goto :stepfail_clear
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

set "TEMP_STEP_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_full_step.tmp"
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

:stepfail_clear
set "STEP_NAME=00 Clear generated artifacts"
goto :stepfail_common

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

:pick_project
echo.
echo ========================================
echo Select FilmCreator project
echo ========================================
set /a PROJECT_COUNT=0
for /f "delims=" %%P in ('dir /b /ad "%REPO_ROOT%\projects" 2^>nul') do (
    set /a PROJECT_COUNT+=1
    set "PROJECT_!PROJECT_COUNT!=%%P"
    echo !PROJECT_COUNT!. %%P
)
if "%PROJECT_COUNT%"=="0" (
    echo No project folders were found under:
    echo   %REPO_ROOT%\projects
    exit /b 1
)
echo.
set /p PROJECT_CHOICE=Project number:
if "%PROJECT_CHOICE%"=="" (
    echo No project selected.
    exit /b 1
)
for %%N in (%PROJECT_CHOICE%) do set "PROJECT_SLUG=!PROJECT_%%N!"
if "%PROJECT_SLUG%"=="" (
    echo Invalid project selection: %PROJECT_CHOICE%
    exit /b 1
)
echo Selected project: %PROJECT_SLUG%
exit /b 0

:pick_chapters
echo.
echo Chapter selector examples: 1-999, 1-3, CH001-CH003, 4, 7, 12
set /p CHAPTERS=Chapters [1-999]:
if "%CHAPTERS%"=="" set "CHAPTERS=1-999"
exit /b 0

:pick_clear_mode
echo.
echo Existing generated artifacts will be preserved by default.
set /p CLEAR_CONFIRM=Clear and regenerate artifacts first? Type Y to clear [N]:
if /I "%CLEAR_CONFIRM%"=="Y" (
    set "NO_CLEAR="
) else (
    set "NO_CLEAR=NO_CLEAR"
)
exit /b 0

:picker_failed
echo.
echo Project/chapter selection failed.
pause
exit /b 1
