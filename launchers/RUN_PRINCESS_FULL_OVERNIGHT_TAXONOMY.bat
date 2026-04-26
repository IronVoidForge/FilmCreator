@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

set "CHAPTERS=%~2"
if "%CHAPTERS%"=="" set "CHAPTERS=2-3"

set "NO_CLEAR=%~3"

call "%~dp0_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail_resolver
set "REPO_ROOT=%FILMCREATOR_ROOT%"

set "LOG_DIR=%REPO_ROOT%\logs\overnight"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set "STAMP=%%i"
set "LOG_FILE=%LOG_DIR%\%PROJECT_SLUG%_overnight_full_%STAMP%.log"
set "LATEST_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_full_latest.log"
set "TEMP_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_step.tmp"

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
    call :run_step "00 Clear generated artifacts" "powershell -NoProfile -ExecutionPolicy Bypass -Command ""$paths = @('projects\%PROJECT_SLUG%\02_story_analysis\chapter_analysis', 'projects\%PROJECT_SLUG%\02_story_analysis\character_breakdowns', 'projects\%PROJECT_SLUG%\02_story_analysis\environment_breakdowns', 'projects\%PROJECT_SLUG%\02_story_analysis\world\chapters', 'projects\%PROJECT_SLUG%\02_story_analysis\taxonomy', 'projects\%PROJECT_SLUG%\02_story_analysis\bibles', 'projects\%PROJECT_SLUG%\02_story_analysis\contracts', 'projects\%PROJECT_SLUG%\02_story_analysis\timelines', 'projects\%PROJECT_SLUG%\02_story_analysis\descriptors', 'projects\%PROJECT_SLUG%\02_story_analysis\grading', 'projects\%PROJECT_SLUG%\02_story_analysis\quality', 'projects\%PROJECT_SLUG%\02_story_analysis\dialogue_enrichment', 'projects\%PROJECT_SLUG%\02_story_analysis\world\refinement', 'projects\%PROJECT_SLUG%\02_story_analysis\world\global\VISUAL_FALLBACKS.json', 'projects\%PROJECT_SLUG%\03_prompt_packages', 'projects\%PROJECT_SLUG%\04_references', 'projects\%PROJECT_SLUG%\05_scenes', 'projects\%PROJECT_SLUG%\06_reviews', 'projects\%PROJECT_SLUG%\07_finals'); foreach ($p in $paths) { if (Test-Path $p) { Write-Host \""Removing: $p\""; Remove-Item -Path $p -Recurse -Force -ErrorAction Stop } else { Write-Host \""Not found (skipping): $p\"" } }; Write-Host \""Clear completed successfully\"""""
)

call :run_step "01 LM Studio connectivity check" "python -c ""from json import dumps; from orchestrator.settings import load_runtime_settings; from orchestrator.lmstudio_client import LMStudioClient; settings=load_runtime_settings(); client=LMStudioClient(settings); print(dumps(client.check().to_dict(), indent=2))"""
call :run_step "02 Multi-chapter analysis / chapter summaries / breakdowns" "python -c ""from orchestrator.book_authoring import analyze_book; import json; summary = analyze_book(project_slug='%PROJECT_SLUG%'); print(json.dumps(summary.to_dict(), indent=2))"""
call :run_step "03 Character taxonomy" "python -m orchestrator synthesize-character-taxonomy ""%PROJECT_SLUG%"" --force"
call :run_step "04 Identity refinement plan" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"""
call :run_step "05 Identity refinement apply" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"" --apply"
call :run_step "06 Character bibles" "python -m orchestrator synthesize-character-bibles ""%PROJECT_SLUG%"" --force"
call :run_step "07 Environment bibles" "python -m orchestrator synthesize-environment-bibles ""%PROJECT_SLUG%"" --force"
call :run_step "08 Visual fallbacks" "python -m orchestrator synthesize-visual-fallbacks ""%PROJECT_SLUG%"" --force"

if "%CHAPTERS%"=="" (
    call :run_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force"
) else (
    call :run_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

if "%CHAPTERS%"=="" (
    call :run_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force"
) else (
    call :run_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

if "%CHAPTERS%"=="" (
    call :run_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force"
) else (
    call :run_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

if "%CHAPTERS%"=="" (
    call :run_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force"
) else (
    call :run_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

if "%CHAPTERS%"=="" (
    call :run_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force"
) else (
    call :run_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

if "%CHAPTERS%"=="" (
    call :run_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force"
) else (
    call :run_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

call :run_step "15 Quality grading" "python -m orchestrator grade-artifacts ""%PROJECT_SLUG%"""

echo.
echo ========================================
echo Overnight pipeline completed successfully.
echo Log file: %LOG_FILE%
echo Latest log: %LATEST_LOG%
echo ========================================
exit /b 0

:run_step
set "STEP_NAME=%~1"
set "CMD_LINE=%~2"

echo.
echo ----------------------------------------
echo START: !STEP_NAME!
echo ----------------------------------------
>> "%LOG_FILE%" echo.
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LOG_FILE%" echo START: !STEP_NAME!
>> "%LOG_FILE%" echo ----------------------------------------

cmd /c "!CMD_LINE!" > "%TEMP_LOG%" 2>&1
set "EXIT_CODE=%ERRORLEVEL%"

type "%TEMP_LOG%"
type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"
del "%TEMP_LOG%" >nul 2>nul

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

:fail_resolver
echo Failed to resolve FilmCreator root
exit /b 1
