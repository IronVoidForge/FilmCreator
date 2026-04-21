@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

pushd "%FILMCREATOR_ROOT%" >nul

set "DEFAULT_SLUG=princess_of_mars_test"
set /p PROJECT_SLUG=Project slug [%DEFAULT_SLUG%]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=%DEFAULT_SLUG%"

echo.
echo ========================================
echo FilmCreator Full Book-to-Prompt Pipeline
echo ========================================
echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher will run:
echo   1. multi-chapter book analysis and chapter summaries
echo   2. identity refinement plan
echo   3. identity refinement apply
echo   4. character bible synthesis
echo   5. environment bible synthesis
echo   6. scene contract synthesis
echo   7. shot package synthesis
echo   8. dialogue timeline synthesis
echo   9. descriptor enrichment
echo  10. prompt preparation
echo.

echo.
echo [1/10] Checking LM Studio connectivity...
call :run_step "LM Studio connectivity" python -m orchestrator lmstudio-check
if errorlevel 1 goto :fail

echo.
echo [2/10] Running multi-chapter analysis from the manifest...
call :run_step "Multi-chapter analysis" python -c "from orchestrator.book_authoring import analyze_book; import json; summary = analyze_book(project_slug='%PROJECT_SLUG%'); print(json.dumps(summary.to_dict(), indent=2))"
if errorlevel 1 goto :fail

echo.
echo [3/10] Building identity refinement plan...
call :run_step "Identity refinement plan" python -m orchestrator refine-identities %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo [4/10] Applying identity refinement merges...
call :run_step "Identity refinement apply" python -m orchestrator refine-identities %PROJECT_SLUG% --apply
if errorlevel 1 goto :fail

echo.
echo [5/10] Running character bible synthesis...
call :run_step "Character bible synthesis" python -m orchestrator synthesize-character-bibles %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo [6/10] Running environment bible synthesis...
call :run_step "Environment bible synthesis" python -m orchestrator synthesize-environment-bibles %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo [7/10] Running scene contract synthesis...
call :run_step "Scene contract synthesis" python -m orchestrator synthesize-scene-contracts %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo [8/10] Running shot package synthesis...
call :run_step "Shot package synthesis" python -m orchestrator synthesize-shot-packages %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo [9/10] Running dialogue timeline synthesis...
call :run_step "Dialogue timeline synthesis" python -m orchestrator synthesize-dialogue-timeline %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo [10/10] Running descriptor enrichment and prompt preparation...
call :run_step "Descriptor enrichment" python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --force
if errorlevel 1 goto :fail
call :run_step "Prompt preparation" python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Final review checkpoint
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\DESCRIPTOR_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\review\PROMPT_PREPARATION_REVIEW_QUEUE.md
echo.
echo Full book-to-prompt pipeline complete.
goto :done

:run_step
setlocal EnableExtensions EnableDelayedExpansion
set "STEP_LABEL=%~1"
shift
set "STEP_CMD=%*"
echo [timing] !STEP_LABEL! starting...
powershell -NoProfile -Command "$sw=[Diagnostics.Stopwatch]::StartNew(); & cmd /c %STEP_CMD%; $code=$LASTEXITCODE; $sw.Stop(); Write-Host ('[timing] %STEP_LABEL%: {0:n1}s' -f $sw.Elapsed.TotalSeconds); exit $code"
endlocal & exit /b %errorlevel%

:fail
echo.
echo Full book-to-prompt pipeline failed.
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
