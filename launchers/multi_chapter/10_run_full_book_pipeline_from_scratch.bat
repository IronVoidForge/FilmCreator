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
echo   7. scene binding synthesis
echo   8. shot package synthesis
echo   9. dialogue timeline synthesis
echo  10. descriptor enrichment
echo  11. prompt preparation
echo.

echo.
echo [1/11] Checking LM Studio connectivity...
set "STEP_LABEL=LM Studio connectivity"
call :step_begin
python -c "from json import dumps; from orchestrator.settings import load_runtime_settings; from orchestrator.lmstudio_client import LMStudioClient; settings=load_runtime_settings(); client=LMStudioClient(settings); print(dumps(client.check().to_dict(), indent=2))"
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail

echo.
echo [2/11] Running multi-chapter analysis from the manifest...
set "STEP_LABEL=Multi-chapter analysis"
call :step_begin
python -c "from orchestrator.book_authoring import analyze_book; import json; summary = analyze_book(project_slug='%PROJECT_SLUG%'); print(json.dumps(summary.to_dict(), indent=2))"
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail

echo.
echo [3/11] Building identity refinement plan...
set "STEP_LABEL=Identity refinement plan"
call :step_begin
python -m orchestrator refine-identities %PROJECT_SLUG%
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail

echo.
echo [4/11] Applying identity refinement merges...
set "STEP_LABEL=Identity refinement apply"
call :step_begin
python -m orchestrator refine-identities %PROJECT_SLUG% --apply
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail

echo.
echo [5/11] Running character bible synthesis...
set "STEP_LABEL=Character bible synthesis"
call :step_begin
python -m orchestrator synthesize-character-bibles %PROJECT_SLUG% --force
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail

echo.
echo [6/11] Running environment bible synthesis...
set "STEP_LABEL=Environment bible synthesis"
call :step_begin
python -m orchestrator synthesize-environment-bibles %PROJECT_SLUG% --force
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail

echo.
echo [7/11] Running scene contract synthesis...
set "STEP_LABEL=Scene contract synthesis"
call :step_begin
python -m orchestrator synthesize-scene-contracts %PROJECT_SLUG% --force
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail

echo.
echo [8/11] Running scene binding synthesis...
set "STEP_LABEL=Scene binding synthesis"
call :step_begin
python -m orchestrator synthesize-scene-bindings %PROJECT_SLUG% --force
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail

echo.
echo [9/11] Running shot package synthesis...
set "STEP_LABEL=Shot package synthesis"
call :step_begin
python -m orchestrator synthesize-shot-packages %PROJECT_SLUG% --force
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail

echo.
echo [10/11] Running dialogue timeline synthesis...
set "STEP_LABEL=Dialogue timeline synthesis"
call :step_begin
python -m orchestrator synthesize-dialogue-timeline %PROJECT_SLUG% --force
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail

echo.
echo [11/11] Running descriptor enrichment and prompt preparation...
set "STEP_LABEL=Descriptor enrichment"
call :step_begin
python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --force
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail
set "STEP_LABEL=Prompt preparation"
call :step_begin
python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG% --force
if errorlevel 1 goto :fail
call :step_end
if errorlevel 1 goto :fail

echo.
echo Final review checkpoint
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\DESCRIPTOR_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\review\PROMPT_PREPARATION_REVIEW_QUEUE.md
echo.
echo Full book-to-prompt pipeline complete.
goto :done

:step_begin
setlocal EnableExtensions EnableDelayedExpansion
for /f %%I in ('powershell -NoProfile -Command "[DateTime]::UtcNow.ToString(\"o\")"') do set "STEP_START=%%I"
echo [timing] !STEP_LABEL! starting...
endlocal & set "STEP_START=%STEP_START%" & exit /b 0

:step_end
setlocal EnableExtensions EnableDelayedExpansion
for /f %%I in ('powershell -NoProfile -Command "[DateTime]::UtcNow.ToString(\"o\")"') do set "STEP_END=%%I"
for /f %%I in ('powershell -NoProfile -Command "$s=[datetime]::Parse(\"%STEP_START%\"); $e=[datetime]::Parse(\"%STEP_END%\"); [math]::Round(($e-$s).TotalSeconds,1)"') do set "STEP_SECONDS=%%I"
echo [timing] !STEP_LABEL!: !STEP_SECONDS!s
endlocal & exit /b 0

:fail
echo.
echo Full book-to-prompt pipeline failed.
pause
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
