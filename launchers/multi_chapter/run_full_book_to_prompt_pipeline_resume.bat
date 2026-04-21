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
echo FilmCreator Full Book-to-Prompt Resume Pipeline
echo ========================================
echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher will run:
echo   1. LM Studio connectivity check
echo   2. retry any recorded failed chapters
echo   3. resume book analysis from the last partial chapter
echo   4. identity refinement plan
echo   5. identity refinement apply
echo   6. character bible synthesis
echo   7. environment bible synthesis
echo   8. scene contract synthesis
echo   9. shot package synthesis
echo  10. dialogue timeline synthesis
echo  11. descriptor enrichment
echo  12. prompt preparation
echo.

echo.
echo [1/12] Checking LM Studio connectivity...
python -c "from json import dumps; from orchestrator.settings import load_runtime_settings; from orchestrator.lmstudio_client import LMStudioClient; settings=load_runtime_settings(); client=LMStudioClient(settings); print(dumps(client.check().to_dict(), indent=2))"
if errorlevel 1 goto :fail

echo.
echo [2/12] Retrying recorded failed chapters and resuming book analysis...
python -m orchestrator.resume_book_analysis %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo [3/12] Building identity refinement plan...
python -m orchestrator refine-identities %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo [4/12] Applying identity refinement merges...
python -m orchestrator refine-identities %PROJECT_SLUG% --apply
if errorlevel 1 goto :fail

echo.
echo [5/12] Running character bible synthesis...
python -m orchestrator synthesize-character-bibles %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo [6/12] Running environment bible synthesis...
python -m orchestrator synthesize-environment-bibles %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo [7/12] Running scene contract synthesis...
python -m orchestrator synthesize-scene-contracts %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo [8/12] Running shot package synthesis...
python -m orchestrator synthesize-shot-packages %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo [9/12] Running dialogue timeline synthesis...
python -m orchestrator synthesize-dialogue-timeline %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo [10/12] Running descriptor enrichment...
python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo [11/12] Running prompt preparation...
python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Final review checkpoint
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\DESCRIPTOR_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\review\PROMPT_PREPARATION_REVIEW_QUEUE.md
echo.
echo Full book-to-prompt resume pipeline complete.
goto :done

:fail
echo.
echo Full book-to-prompt resume pipeline failed.
pause
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
