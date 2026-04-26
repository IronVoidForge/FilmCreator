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
echo Chapters: %CHAPTERS_DISPLAY%
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
echo CONSOLE OUTPUT:
echo - Compact summaries only.
echo - Full raw command output is written to the log files above.
echo ========================================

cd /d "%REPO_ROOT%"
if errorlevel 1 goto :fail

if /I "%MODE%"=="VALIDATE_ONLY" (
    echo.
    echo ========================================
    echo VALIDATE ONLY MODE
    echo ========================================
    echo Project: %PROJECT_SLUG%
    echo Chapters: %CHAPTERS_DISPLAY%
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

call :set_stage_flags

if /I "%MODE%"=="PLAN_ONLY" (
    call :print_plan
    exit /b 0
)

echo.
echo Resuming from stage: %RESUME_STAGE%
echo.
>> "%LOG_FILE%" echo Resuming from stage: %RESUME_STAGE%
>> "%LATEST_LOG%" echo Resuming from stage: %RESUME_STAGE%

if "%RUN_STORY_ANALYSIS%"=="1" (
    call :lm_studio_check
    if errorlevel 1 goto :end_with_error

    call :analyze_book
    if errorlevel 1 goto :end_with_error
)

if "%RUN_CHARACTER_TAXONOMY%"=="1" (
    call :run_step "03 Character taxonomy" "python -m orchestrator synthesize-character-taxonomy ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
)

if "%RUN_IDENTITY_REFINEMENT%"=="1" (
    call :run_step "04 Identity refinement plan" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"""
    if errorlevel 1 goto :end_with_error

    call :run_step "05 Identity refinement apply" "python -m orchestrator refine-identities ""%PROJECT_SLUG%"" --apply"
    if errorlevel 1 goto :end_with_error
)

if "%RUN_CHARACTER_BIBLES%"=="1" (
    call :run_step "06 Character bibles" "python -m orchestrator synthesize-character-bibles ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
)

if "%RUN_ENVIRONMENT_BIBLES%"=="1" (
    call :run_step "07 Environment bibles" "python -m orchestrator synthesize-environment-bibles ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
)

if "%RUN_VISUAL_FALLBACKS%"=="1" (
    call :run_step "08 Visual fallbacks" "python -m orchestrator synthesize-visual-fallbacks ""%PROJECT_SLUG%"" --force"
    if errorlevel 1 goto :end_with_error
)

if "%RUN_SCENE_CONTRACTS%"=="1" (
    if "%CHAPTERS%"=="" (
        call :run_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "09 Scene contracts" "python -m orchestrator synthesize-scene-contracts ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :end_with_error
)

if "%RUN_SCENE_BINDINGS%"=="1" (
    if "%CHAPTERS%"=="" (
        call :run_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "10 Scene bindings" "python -m orchestrator synthesize-scene-bindings ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :end_with_error
)

if "%RUN_SHOT_PACKAGES%"=="1" (
    if "%CHAPTERS%"=="" (
        call :run_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "11 Shot packages" "python -m orchestrator synthesize-shot-packages ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :end_with_error
)

if "%RUN_DIALOGUE_TIMELINE%"=="1" (
    if "%CHAPTERS%"=="" (
        call :run_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "12 Dialogue timeline" "python -m orchestrator synthesize-dialogue-timeline ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :end_with_error
)

if "%RUN_DESCRIPTOR_ENRICHMENT%"=="1" (
    if "%CHAPTERS%"=="" (
        call :run_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "13 Descriptor enrichment" "python -m orchestrator synthesize-descriptor-enrichment ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :end_with_error
)

if "%RUN_PROMPT_PREPARATION%"=="1" (
    if "%CHAPTERS%"=="" (
        call :run_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force"
    ) else (
        call :run_step "14 Prompt preparation" "python -m orchestrator synthesize-prompt-preparation ""%PROJECT_SLUG%"" --force --chapters ""%CHAPTERS%"""
    )
    if errorlevel 1 goto :end_with_error
)

if "%RUN_QUALITY_GRADING%"=="1" (
    call :run_step "15 Quality grading" "python -m orchestrator grade-artifacts ""%PROJECT_SLUG%"""
    if errorlevel 1 goto :end_with_error
)

echo.
echo ========================================
echo Overnight resume pipeline completed successfully.
echo Log file: %LOG_FILE%
echo Latest log: %LATEST_LOG%
echo ========================================
pause
exit /b 0


:detect_resume_stage
echo.
echo ----------------------------------------
echo Detecting resume stage...
echo ----------------------------------------

>> "%LOG_FILE%" echo ----------------------------------------
>> "%LOG_FILE%" echo Detecting resume stage...
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LATEST_LOG%" echo ----------------------------------------
>> "%LATEST_LOG%" echo Detecting resume stage...
>> "%LATEST_LOG%" echo ----------------------------------------

python -m orchestrator.overnight_pipeline_resume_check "%PROJECT_SLUG%" "%CHAPTERS%" > "%TEMP_LOG%" 2>&1
set "CHECK_EXIT=%ERRORLEVEL%"

type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"

if not "%CHECK_EXIT%"=="0" (
    echo Resume detection failed. See log for details.
    exit /b %CHECK_EXIT%
)

for /f "usebackq delims=" %%s in ("%TEMP_LOG%") do (
    set "RESUME_STAGE=%%s"
    goto :got_resume_stage
)

:got_resume_stage
if "%RESUME_STAGE%"=="" (
    echo Resume stage detection produced no output.
    exit /b 1
)

echo Detected stage: %RESUME_STAGE%
>> "%LOG_FILE%" echo Detected stage: %RESUME_STAGE%
>> "%LATEST_LOG%" echo Detected stage: %RESUME_STAGE%
exit /b 0


:set_stage_flags
set "RUN_STORY_ANALYSIS=0"
set "RUN_CHARACTER_TAXONOMY=0"
set "RUN_IDENTITY_REFINEMENT=0"
set "RUN_CHARACTER_BIBLES=0"
set "RUN_ENVIRONMENT_BIBLES=0"
set "RUN_VISUAL_FALLBACKS=0"
set "RUN_SCENE_CONTRACTS=0"
set "RUN_SCENE_BINDINGS=0"
set "RUN_SHOT_PACKAGES=0"
set "RUN_DIALOGUE_TIMELINE=0"
set "RUN_DESCRIPTOR_ENRICHMENT=0"
set "RUN_PROMPT_PREPARATION=0"
set "RUN_QUALITY_GRADING=0"

if "%RESUME_STAGE%"=="story_analysis" (
    set "RUN_STORY_ANALYSIS=1"
    set "RUN_CHARACTER_TAXONOMY=1"
    set "RUN_IDENTITY_REFINEMENT=1"
    set "RUN_CHARACTER_BIBLES=1"
    set "RUN_ENVIRONMENT_BIBLES=1"
    set "RUN_VISUAL_FALLBACKS=1"
    set "RUN_SCENE_CONTRACTS=1"
    set "RUN_SCENE_BINDINGS=1"
    set "RUN_SHOT_PACKAGES=1"
    set "RUN_DIALOGUE_TIMELINE=1"
    set "RUN_DESCRIPTOR_ENRICHMENT=1"
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="character_taxonomy" (
    set "RUN_CHARACTER_TAXONOMY=1"
    set "RUN_IDENTITY_REFINEMENT=1"
    set "RUN_CHARACTER_BIBLES=1"
    set "RUN_ENVIRONMENT_BIBLES=1"
    set "RUN_VISUAL_FALLBACKS=1"
    set "RUN_SCENE_CONTRACTS=1"
    set "RUN_SCENE_BINDINGS=1"
    set "RUN_SHOT_PACKAGES=1"
    set "RUN_DIALOGUE_TIMELINE=1"
    set "RUN_DESCRIPTOR_ENRICHMENT=1"
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="identity_refinement" (
    set "RUN_IDENTITY_REFINEMENT=1"
    set "RUN_CHARACTER_BIBLES=1"
    set "RUN_ENVIRONMENT_BIBLES=1"
    set "RUN_VISUAL_FALLBACKS=1"
    set "RUN_SCENE_CONTRACTS=1"
    set "RUN_SCENE_BINDINGS=1"
    set "RUN_SHOT_PACKAGES=1"
    set "RUN_DIALOGUE_TIMELINE=1"
    set "RUN_DESCRIPTOR_ENRICHMENT=1"
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="character_bibles" (
    set "RUN_CHARACTER_BIBLES=1"
    set "RUN_ENVIRONMENT_BIBLES=1"
    set "RUN_VISUAL_FALLBACKS=1"
    set "RUN_SCENE_CONTRACTS=1"
    set "RUN_SCENE_BINDINGS=1"
    set "RUN_SHOT_PACKAGES=1"
    set "RUN_DIALOGUE_TIMELINE=1"
    set "RUN_DESCRIPTOR_ENRICHMENT=1"
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="environment_bibles" (
    set "RUN_ENVIRONMENT_BIBLES=1"
    set "RUN_VISUAL_FALLBACKS=1"
    set "RUN_SCENE_CONTRACTS=1"
    set "RUN_SCENE_BINDINGS=1"
    set "RUN_SHOT_PACKAGES=1"
    set "RUN_DIALOGUE_TIMELINE=1"
    set "RUN_DESCRIPTOR_ENRICHMENT=1"
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="visual_fallbacks" (
    set "RUN_VISUAL_FALLBACKS=1"
    set "RUN_SCENE_CONTRACTS=1"
    set "RUN_SCENE_BINDINGS=1"
    set "RUN_SHOT_PACKAGES=1"
    set "RUN_DIALOGUE_TIMELINE=1"
    set "RUN_DESCRIPTOR_ENRICHMENT=1"
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="scene_contracts" (
    set "RUN_SCENE_CONTRACTS=1"
    set "RUN_SCENE_BINDINGS=1"
    set "RUN_SHOT_PACKAGES=1"
    set "RUN_DIALOGUE_TIMELINE=1"
    set "RUN_DESCRIPTOR_ENRICHMENT=1"
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="scene_bindings" (
    set "RUN_SCENE_BINDINGS=1"
    set "RUN_SHOT_PACKAGES=1"
    set "RUN_DIALOGUE_TIMELINE=1"
    set "RUN_DESCRIPTOR_ENRICHMENT=1"
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="shot_packages" (
    set "RUN_SHOT_PACKAGES=1"
    set "RUN_DIALOGUE_TIMELINE=1"
    set "RUN_DESCRIPTOR_ENRICHMENT=1"
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="dialogue_timeline" (
    set "RUN_DIALOGUE_TIMELINE=1"
    set "RUN_DESCRIPTOR_ENRICHMENT=1"
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="descriptor_enrichment" (
    set "RUN_DESCRIPTOR_ENRICHMENT=1"
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="prompt_preparation" (
    set "RUN_PROMPT_PREPARATION=1"
    set "RUN_QUALITY_GRADING=1"
)

if "%RESUME_STAGE%"=="quality_grading" (
    set "RUN_QUALITY_GRADING=1"
)

if "%RUN_STORY_ANALYSIS%%RUN_CHARACTER_TAXONOMY%%RUN_IDENTITY_REFINEMENT%%RUN_CHARACTER_BIBLES%%RUN_ENVIRONMENT_BIBLES%%RUN_VISUAL_FALLBACKS%%RUN_SCENE_CONTRACTS%%RUN_SCENE_BINDINGS%%RUN_SHOT_PACKAGES%%RUN_DIALOGUE_TIMELINE%%RUN_DESCRIPTOR_ENRICHMENT%%RUN_PROMPT_PREPARATION%%RUN_QUALITY_GRADING%"=="0000000000000" (
    echo Unknown or unsupported resume stage: %RESUME_STAGE%
    exit /b 1
)

exit /b 0


:print_plan
echo.
echo ========================================
echo PLAN ONLY MODE
echo Resume stage: %RESUME_STAGE%
echo Project: %PROJECT_SLUG%
echo Chapters: %CHAPTERS_DISPLAY%
echo ========================================
if "%RUN_STORY_ANALYSIS%"=="1" echo 01 LM Studio connectivity check
if "%RUN_STORY_ANALYSIS%"=="1" echo 02 Multi-chapter analysis / chapter summaries / breakdowns
if "%RUN_CHARACTER_TAXONOMY%"=="1" echo 03 Character taxonomy
if "%RUN_IDENTITY_REFINEMENT%"=="1" echo 04 Identity refinement plan
if "%RUN_IDENTITY_REFINEMENT%"=="1" echo 05 Identity refinement apply
if "%RUN_CHARACTER_BIBLES%"=="1" echo 06 Character bibles
if "%RUN_ENVIRONMENT_BIBLES%"=="1" echo 07 Environment bibles
if "%RUN_VISUAL_FALLBACKS%"=="1" echo 08 Visual fallbacks
if "%RUN_SCENE_CONTRACTS%"=="1" echo 09 Scene contracts
if "%RUN_SCENE_BINDINGS%"=="1" echo 10 Scene bindings
if "%RUN_SHOT_PACKAGES%"=="1" echo 11 Shot packages
if "%RUN_DIALOGUE_TIMELINE%"=="1" echo 12 Dialogue timeline
if "%RUN_DESCRIPTOR_ENRICHMENT%"=="1" echo 13 Descriptor enrichment
if "%RUN_PROMPT_PREPARATION%"=="1" echo 14 Prompt preparation
if "%RUN_QUALITY_GRADING%"=="1" echo 15 Quality grading
echo ========================================
exit /b 0


:lm_studio_check
echo.
echo ----------------------------------------
echo START: 01 LM Studio connectivity check
echo ----------------------------------------

>> "%LOG_FILE%" echo ----------------------------------------
>> "%LOG_FILE%" echo START: 01 LM Studio connectivity check
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LATEST_LOG%" echo ----------------------------------------
>> "%LATEST_LOG%" echo START: 01 LM Studio connectivity check
>> "%LATEST_LOG%" echo ----------------------------------------

python -m orchestrator diagnostics-lmstudio > "%TEMP_LOG%" 2>&1
set "STEP_EXIT=%ERRORLEVEL%"

type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"

if not "%STEP_EXIT%"=="0" (
    echo FAILED: 01 LM Studio connectivity check exit code %STEP_EXIT%
    exit /b %STEP_EXIT%
)

echo DONE: 01 LM Studio connectivity check
exit /b 0


:analyze_book
echo.
echo ----------------------------------------
echo START: 02 Multi-chapter analysis / chapter summaries / breakdowns
echo Full output is being written to log.
echo ----------------------------------------

>> "%LOG_FILE%" echo ----------------------------------------
>> "%LOG_FILE%" echo START: 02 Multi-chapter analysis / chapter summaries / breakdowns
>> "%LOG_FILE%" echo ----------------------------------------
>> "%LATEST_LOG%" echo ----------------------------------------
>> "%LATEST_LOG%" echo START: 02 Multi-chapter analysis / chapter summaries / breakdowns
>> "%LATEST_LOG%" echo ----------------------------------------

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$ErrorActionPreference='Stop';" ^
  "$cmd = 'from orchestrator.book_authoring import analyze_book; import json; summary = analyze_book(project_slug=''%PROJECT_SLUG%''); print(json.dumps(summary.to_dict(), indent=2))';" ^
  "python -c $cmd 2>&1 | Tee-Object -FilePath '%TEMP_LOG%' | ForEach-Object { if ($_ -match '^\[authoring\]|completed_chapters|failed_chapters|error|ERROR|Traceback') { $_ } };" ^
  "exit $LASTEXITCODE"

set "STEP_EXIT=%ERRORLEVEL%"

type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"

if not "%STEP_EXIT%"=="0" (
    echo FAILED: 02 Multi-chapter analysis exit code %STEP_EXIT%
    exit /b %STEP_EXIT%
)

call :print_json_summary "%TEMP_LOG%"
echo DONE: 02 Multi-chapter analysis
exit /b 0


:run_step
set "STEP_NAME=%~1"
set "STEP_COMMAND=%~2"

echo.
echo ----------------------------------------
echo START: %STEP_NAME%
echo COMMAND: %STEP_COMMAND%
echo Full raw output is being written to log.
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

cmd /c %STEP_COMMAND% > "%TEMP_LOG%" 2>&1
set "STEP_EXIT=%ERRORLEVEL%"

type "%TEMP_LOG%" >> "%LOG_FILE%"
type "%TEMP_LOG%" >> "%LATEST_LOG%"

if not "%STEP_EXIT%"=="0" (
    echo FAILED: %STEP_NAME% exit code %STEP_EXIT%
    echo Last 40 lines:
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-Content '%TEMP_LOG%' -Tail 40"
    exit /b %STEP_EXIT%
)

call :print_json_summary "%TEMP_LOG%"

echo DONE: %STEP_NAME% exit code %STEP_EXIT%
exit /b 0


:print_json_summary
set "SUMMARY_SOURCE=%~1"

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$path='%SUMMARY_SOURCE%';" ^
  "if (!(Test-Path $path)) { exit 0 };" ^
  "$raw = Get-Content $path -Raw;" ^
  "$jsonStart = $raw.IndexOf('{');" ^
  "if ($jsonStart -lt 0) {" ^
  "  $lines = $raw -split \"`r?`n\" | Where-Object { $_ -match '^\[|total_|synthesized|reused|warning|error|DONE|FAILED' } | Select-Object -Last 25;" ^
  "  if ($lines) { $lines | ForEach-Object { '  ' + $_ } }" ^
  "  exit 0;" ^
  "}" ^
  "$jsonText = $raw.Substring($jsonStart).Trim();" ^
  "try { $obj = $jsonText | ConvertFrom-Json -ErrorAction Stop } catch {" ^
  "  $lines = $raw -split \"`r?`n\" | Where-Object { $_ -match '^\[|total_|synthesized|reused|warning|error|DONE|FAILED' } | Select-Object -Last 25;" ^
  "  if ($lines) { $lines | ForEach-Object { '  ' + $_ } }" ^
  "  exit 0;" ^
  "};" ^
  "Write-Host 'SUMMARY:';" ^
  "$keys = @('status','project_slug','total_registry_entries','candidate_count','comparison_count','decision_count','applied_count','human_review_count','total_entries','total_chapters','total_events','total_scene_entries','total_shot_entries','total_scene_bindings','total_shot_bindings','synthesized_count','reused_count','stale_locked_count','review_queue_count','needs_review_count','unknown_count');" ^
  "foreach ($k in $keys) {" ^
  "  if ($obj.PSObject.Properties.Name -contains $k) { Write-Host ('  ' + $k + ': ' + $obj.$k) }" ^
  "}" ^
  "if ($obj.warnings) {" ^
  "  $count = @($obj.warnings).Count;" ^
  "  Write-Host ('  warnings: ' + $count);" ^
  "  @($obj.warnings | Select-Object -First 5) | ForEach-Object { Write-Host ('    - ' + $_) }" ^
  "}" ^
  "if ($obj.written_files) {" ^
  "  $count = @($obj.written_files).Count;" ^
  "  Write-Host ('  written_files: ' + $count);" ^
  "  @($obj.written_files | Select-Object -First 5) | ForEach-Object { Write-Host ('    - ' + $_) };" ^
  "  if ($count -gt 5) { Write-Host ('    ... +' + ($count - 5) + ' more') }" ^
  "}"

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


:fail_resolver
echo Failed to resolve FilmCreator root.
pause
exit /b 1


:fail
echo Failed to change to repo root: %REPO_ROOT%
pause
exit /b 1