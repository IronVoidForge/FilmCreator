@echo off
setlocal EnableExtensions EnableDelayedExpansion

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
if errorlevel 1 goto :fail_resolver

set "REPO_ROOT=%FILMCREATOR_ROOT%"
set "LOG_DIR=%REPO_ROOT%\logs\overnight"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set "STAMP=%%i"

set "LOG_FILE=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_%STAMP%.log"
set "LATEST_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_latest.log"
set "TEMP_LOG=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_step.tmp"
set "STEP_LIST=%LOG_DIR%\%PROJECT_SLUG%_overnight_resume_steps_%STAMP%.tsv"

if exist "%LATEST_LOG%" del "%LATEST_LOG%" >nul 2>nul
if exist "%TEMP_LOG%" del "%TEMP_LOG%" >nul 2>nul
if exist "%STEP_LIST%" del "%STEP_LIST%" >nul 2>nul

cd /d "%REPO_ROOT%"
if errorlevel 1 goto :fail_cd

echo ========================================
echo FilmCreator Overnight Resume Pipeline
echo ========================================
echo Project:  %PROJECT_SLUG%
echo Chapters: %CHAPTERS_DISPLAY%
echo Log:      %LOG_FILE%
echo Latest:   %LATEST_LOG%
echo ========================================
echo.

>> "%LOG_FILE%" echo ========================================
>> "%LOG_FILE%" echo FilmCreator Overnight Resume Pipeline
>> "%LOG_FILE%" echo ========================================
>> "%LOG_FILE%" echo Project: %PROJECT_SLUG%
>> "%LOG_FILE%" echo Chapters: %CHAPTERS_DISPLAY%
>> "%LOG_FILE%" echo Repo root: %REPO_ROOT%
>> "%LOG_FILE%" echo Log file: %LOG_FILE%
>> "%LOG_FILE%" echo Latest log: %LATEST_LOG%

>> "%LATEST_LOG%" echo ========================================
>> "%LATEST_LOG%" echo FilmCreator Overnight Resume Pipeline
>> "%LATEST_LOG%" echo ========================================
>> "%LATEST_LOG%" echo Project: %PROJECT_SLUG%
>> "%LATEST_LOG%" echo Chapters: %CHAPTERS_DISPLAY%
>> "%LATEST_LOG%" echo Repo root: %REPO_ROOT%
>> "%LATEST_LOG%" echo Log file: %LOG_FILE%
>> "%LATEST_LOG%" echo Latest log: %LATEST_LOG%

if /I "%MODE%"=="VALIDATE_ONLY" (
    echo VALIDATE_ONLY
    python -m orchestrator.overnight_pipeline_resume_check "%PROJECT_SLUG%" "%CHAPTERS%" --report
    echo.
    echo Log: %LOG_FILE%
    pause
    exit /b 0
)

call :detect_resume_stage
if errorlevel 1 goto :end_with_error

if "%RESUME_STAGE%"=="complete" (
    echo Already complete.
    echo Log: %LOG_FILE%
    pause
    exit /b 0
)

call :build_step_list
if errorlevel 1 goto :end_with_error

if /I "%MODE%"=="PLAN_ONLY" (
    call :print_plan
    exit /b 0
)

echo Resume stage: %RESUME_STAGE%
echo.

>> "%LOG_FILE%" echo Resume stage: %RESUME_STAGE%
>> "%LATEST_LOG%" echo Resume stage: %RESUME_STAGE%

for /f "usebackq tokens=1* delims=	" %%A in ("%STEP_LIST%") do (
    call :run_step "%%~A" "%%~B"
    if errorlevel 1 goto :end_with_error
)

echo.
echo ========================================
echo COMPLETE
echo Log:    %LOG_FILE%
echo Latest: %LATEST_LOG%
echo ========================================
pause
exit /b 0


:detect_resume_stage
echo Detecting resume stage...
python -m orchestrator.overnight_pipeline_resume_check "%PROJECT_SLUG%" "%CHAPTERS%" > "%TEMP_LOG%" 2>&1
set "CHECK_EXIT=%ERRORLEVEL%"

type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"

if not "%CHECK_EXIT%"=="0" (
    echo Resume detection failed.
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-Content '%TEMP_LOG%' -Tail 25"
    exit /b %CHECK_EXIT%
)

for /f "usebackq delims=" %%s in ("%TEMP_LOG%") do (
    set "RESUME_STAGE=%%s"
    goto :got_resume_stage
)

:got_resume_stage
if "%RESUME_STAGE%"=="" (
    echo Resume detection produced no stage.
    exit /b 1
)

echo Detected: %RESUME_STAGE%
echo.
>> "%LOG_FILE%" echo Detected: %RESUME_STAGE%
>> "%LATEST_LOG%" echo Detected: %RESUME_STAGE%
exit /b 0


:build_step_list
if exist "%STEP_LIST%" del "%STEP_LIST%" >nul 2>nul

if "%RESUME_STAGE%"=="story_analysis" goto :add_story_analysis
if "%RESUME_STAGE%"=="character_taxonomy" goto :add_character_taxonomy
if "%RESUME_STAGE%"=="identity_refinement" goto :add_identity_refinement
if "%RESUME_STAGE%"=="character_bibles" goto :add_character_bibles
if "%RESUME_STAGE%"=="environment_bibles" goto :add_environment_bibles
if "%RESUME_STAGE%"=="visual_fallbacks" goto :add_visual_fallbacks
if "%RESUME_STAGE%"=="scene_contracts" goto :add_scene_contracts
if "%RESUME_STAGE%"=="scene_bindings" goto :add_scene_bindings
if "%RESUME_STAGE%"=="shot_packages" goto :add_shot_packages
if "%RESUME_STAGE%"=="dialogue_timeline" goto :add_dialogue_timeline
if "%RESUME_STAGE%"=="descriptor_enrichment" goto :add_descriptor_enrichment
if "%RESUME_STAGE%"=="prompt_preparation" goto :add_prompt_preparation
if "%RESUME_STAGE%"=="quality_grading" goto :add_quality_grading

echo Unknown resume stage: %RESUME_STAGE%
exit /b 1

:add_story_analysis
call :append_step "01 LM Studio check" "python -m orchestrator diagnostics-lmstudio"
call :append_step "02 Story analysis" "__ANALYZE_BOOK__"

:add_character_taxonomy
call :append_step "03 Character taxonomy" "python -m orchestrator synthesize-character-taxonomy ""%PROJECT_SLUG%"" --force"

:add_identity_refinement
call :append_step "04 Identity refinement plan" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"""
call :append_step "05 Identity refinement apply" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"" --apply"

:add_character_bibles
call :append_step "06 Character bibles" "python -m orchestrator synthesize-character-bibles ""%PROJECT_SLUG%"" --force"

:add_environment_bibles
call :append_step "07 Environment bibles" "python -m orchestrator synthesize-environment-bibles ""%PROJECT_SLUG%"" --force"

:add_visual_fallbacks
call :append_step "08 Visual fallbacks" "python -m orchestrator synthesize-visual-fallbacks ""%PROJECT_SLUG%"" --force"

:add_scene_contracts
if "%CHAPTERS%"=="" (
    call :append_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force"
) else (
    call :append_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

:add_scene_bindings
if "%CHAPTERS%"=="" (
    call :append_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force"
) else (
    call :append_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

:add_shot_packages
if "%CHAPTERS%"=="" (
    call :append_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force"
) else (
    call :append_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

:add_dialogue_timeline
if "%CHAPTERS%"=="" (
    call :append_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force"
) else (
    call :append_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

:add_descriptor_enrichment
if "%CHAPTERS%"=="" (
    call :append_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force"
) else (
    call :append_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

:add_prompt_preparation
if "%CHAPTERS%"=="" (
    call :append_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force"
) else (
    call :append_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
)

:add_quality_grading
call :append_step "15 Quality grading" "python -m orchestrator grade-artifacts ""%PROJECT_SLUG%"""

exit /b 0


:append_step
>> "%STEP_LIST%" echo %~1	%~2
exit /b 0


:print_plan
echo PLAN_ONLY | resume=%RESUME_STAGE% | project=%PROJECT_SLUG% | chapters=%CHAPTERS_DISPLAY%
for /f "usebackq tokens=1* delims=	" %%A in ("%STEP_LIST%") do echo %%~A
echo Log: %LOG_FILE%
exit /b 0


:run_step
set "STEP_NAME=%~1"
set "STEP_COMMAND=%~2"

echo.
echo ----------------------------------------
echo START: %STEP_NAME%
echo ----------------------------------------

>> "%LOG_FILE%" echo.
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LOG_FILE%" echo START: %STEP_NAME%
>> "%LOG_FILE%" echo COMMAND: %STEP_COMMAND%
>> "%LOG_FILE%" echo ----------------------------------------

>> "%LATEST_LOG%" echo.
>> "%LATEST_LOG%" echo ----------------------------------------
>> "%LATEST_LOG%" echo START: %STEP_NAME%
>> "%LATEST_LOG%" echo COMMAND: %STEP_COMMAND%
>> "%LATEST_LOG%" echo ----------------------------------------

if "%STEP_COMMAND%"=="__ANALYZE_BOOK__" (
    call :execute_analysis
) else (
    call :execute_command "%STEP_COMMAND%"
)
set "STEP_EXIT=%ERRORLEVEL%"

type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"

if not "%STEP_EXIT%"=="0" (
    echo FAILED: %STEP_NAME% exit code %STEP_EXIT%
    echo Last 30 log lines:
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-Content '%TEMP_LOG%' -Tail 30"
    exit /b %STEP_EXIT%
)

call :print_progress_lines "%TEMP_LOG%"
call :print_counts "%TEMP_LOG%"

echo DONE: %STEP_NAME% exit code 0
exit /b 0


:execute_analysis
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$cmd = 'from orchestrator.book_authoring import analyze_book; import json; summary = analyze_book(project_slug=''%PROJECT_SLUG%''); print(json.dumps(summary.to_dict(), indent=2))';" ^
  "python -c $cmd > '%TEMP_LOG%' 2>&1;" ^
  "exit $LASTEXITCODE"
exit /b %ERRORLEVEL%


:execute_command
set "COMMAND_TO_RUN=%~1"
cmd /c %COMMAND_TO_RUN% > "%TEMP_LOG%" 2>&1
exit /b %ERRORLEVEL%


:print_progress_lines
set "PROGRESS_SOURCE=%~1"

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$p='%PROGRESS_SOURCE%';" ^
  "if (!(Test-Path $p)) { exit 0 };" ^
  "$lines = Get-Content $p;" ^
  "$progress = $lines | Where-Object {" ^
  "  ($_ -match '^\[[A-Za-z0-9_-]+\]') -and" ^
  "  ($_ -match 'starting|finished|synthesized|reused|failed|error|warning')" ^
  "};" ^
  "$progress | Select-Object -Last 120 | ForEach-Object { Write-Host $_ }"

exit /b 0


:print_counts
set "COUNT_SOURCE=%~1"

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$p='%COUNT_SOURCE%';" ^
  "if (!(Test-Path $p)) { exit 0 };" ^
  "$raw=Get-Content $p -Raw;" ^
  "$i=$raw.IndexOf('{');" ^
  "if ($i -lt 0) { exit 0 };" ^
  "$j=$raw.Substring($i).Trim();" ^
  "try { $o=$j | ConvertFrom-Json -ErrorAction Stop } catch { exit 0 };" ^
  "$a=@();" ^
  "foreach($k in 'status','total_registry_entries','candidate_count','comparison_count','decision_count','applied_count','human_review_count','total_entries','total_chapters','total_events','total_scene_entries','total_shot_entries','total_scene_bindings','total_shot_bindings','synthesized_count','reused_count','stale_locked_count','review_queue_count','needs_review_count','unknown_count','total_records'){" ^
  "  if($o.PSObject.Properties.Name -contains $k){ $a += ($k + '=' + $o.$k) }" ^
  "}" ^
  "if($o.PSObject.Properties.Name -contains 'written_files'){ $a += ('files=' + @($o.written_files).Count) }" ^
  "if($o.PSObject.Properties.Name -contains 'warnings'){ $a += ('warnings=' + @($o.warnings).Count) }" ^
  "if($o.PSObject.Properties.Name -contains 'family_summaries'){" ^
  "  $fs=@($o.family_summaries);" ^
  "  $nonzero=$fs | Where-Object { $_.count -gt 0 } | ForEach-Object { $_.family + '=' + $_.count + '/rerun=' + $_.rerun_count };" ^
  "  if($nonzero){ $a += ('families=' + ($nonzero -join ', ')) }" ^
  "}" ^
  "if($a.Count -gt 0){ Write-Host ('SUMMARY: ' + ($a -join ' | ')) }"

exit /b 0


:end_with_error
echo.
echo ========================================
echo STOPPED
echo Log:    %LOG_FILE%
echo Latest: %LATEST_LOG%
echo ========================================
pause
exit /b 1


:fail_resolver
echo Failed to resolve FilmCreator root.
pause
exit /b 1


:fail_cd
echo Failed to change to repo root: %REPO_ROOT%
pause
exit /b 1