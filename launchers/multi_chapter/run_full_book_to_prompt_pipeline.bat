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
pause

echo.
echo [1/10] Checking LM Studio connectivity...
python -m orchestrator lmstudio-check
if errorlevel 1 goto :fail

echo.
echo [2/10] Running multi-chapter analysis from the manifest...
python -c "from orchestrator.book_authoring import analyze_book; import json; summary = analyze_book(project_slug='%PROJECT_SLUG%'); print(json.dumps(summary.to_dict(), indent=2))"
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 1
echo   projects\%PROJECT_SLUG%\02_story_analysis\story_summary\
echo   projects\%PROJECT_SLUG%\02_story_analysis\chapter_analysis\
echo   projects\%PROJECT_SLUG%\02_story_analysis\world\
pause

echo.
echo [3/10] Building identity refinement plan...
python -m orchestrator refine-identities %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 2
echo   projects\%PROJECT_SLUG%\02_story_analysis\world\refinement\CHARACTER_MERGE_PLAN.json
pause

echo.
echo [4/10] Applying identity refinement merges...
python -m orchestrator refine-identities %PROJECT_SLUG% --apply
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 3
echo   projects\%PROJECT_SLUG%\02_story_analysis\world\refinement\CHARACTER_REGISTRY_GLOBAL_REFINED.json
echo   projects\%PROJECT_SLUG%\02_story_analysis\world\refinement\ENVIRONMENT_REGISTRY_GLOBAL_REFINED.json
pause

echo.
echo [5/10] Running character bible synthesis...
python -m orchestrator synthesize-character-bibles %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 4
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\characters\CHARACTER_BIBLE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\characters\review\CHARACTER_BIBLE_REVIEW_QUEUE.md
pause

echo.
echo [6/10] Running environment bible synthesis...
python -m orchestrator synthesize-environment-bibles %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 5
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\environments\ENVIRONMENT_BIBLE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\environments\review\ENVIRONMENT_BIBLE_REVIEW_QUEUE.md
pause

echo.
echo [7/10] Running scene contract synthesis...
python -m orchestrator synthesize-scene-contracts %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 6
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\scenes\SCENE_CONTRACT_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\scenes\review\SCENE_CONTRACT_REVIEW_QUEUE.md
pause

echo.
echo [8/10] Running shot package synthesis...
python -m orchestrator synthesize-shot-packages %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 7
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\SHOT_PACKAGE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\review\SHOT_PACKAGE_REVIEW_QUEUE.md
pause

echo.
echo [9/10] Running dialogue timeline synthesis...
python -m orchestrator synthesize-dialogue-timeline %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 8
echo   projects\%PROJECT_SLUG%\02_story_analysis\timelines\chapters\CH001\CH001_DIALOGUE_TIMELINE.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\timelines\dialogue\DIALOGUE_TIMELINE_INDEX.md
pause

echo.
echo [10/10] Running descriptor enrichment and prompt preparation...
python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --force
if errorlevel 1 goto :fail
python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Final review checkpoint
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\DESCRIPTOR_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\review\PROMPT_PREPARATION_REVIEW_QUEUE.md
echo.
echo Full book-to-prompt pipeline complete.
goto :done

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
