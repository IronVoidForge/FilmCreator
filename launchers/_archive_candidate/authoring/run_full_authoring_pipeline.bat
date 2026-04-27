@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo FilmCreator Full Authoring Pipeline
echo ========================================
echo.
set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher will run the implemented pipeline in dependency order:
echo   1. identity refinement plan
echo   2. identity refinement apply
echo   3. character bible synthesis
echo   4. environment bible synthesis
echo   5. scene contract synthesis
echo   6. shot package synthesis
echo   7. dialogue timeline synthesis
echo   8. descriptor enrichment
echo   9. prompt preparation
echo.
pause

echo.
echo [1/9] Building identity refinement plan...
python -m orchestrator refine-identities %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 1
echo   projects\%PROJECT_SLUG%\02_story_analysis\world\refinement\CHARACTER_MERGE_PLAN.json
pause

echo.
echo [2/9] Applying identity refinement merges...
python -m orchestrator refine-identities %PROJECT_SLUG% --apply
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 2
echo   projects\%PROJECT_SLUG%\02_story_analysis\world\refinement\CHARACTER_REGISTRY_GLOBAL_REFINED.json
echo   projects\%PROJECT_SLUG%\02_story_analysis\world\refinement\CHARACTER_DIRECTORY_REFINED.json
pause

echo.
echo [3/9] Running character bible synthesis...
python -m orchestrator synthesize-character-bibles %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 3
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\characters\CHARACTER_BIBLE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\characters\review\CHARACTER_BIBLE_REVIEW_QUEUE.md
pause

echo.
echo [4/9] Running environment bible synthesis...
python -m orchestrator synthesize-environment-bibles %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 4
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\environments\ENVIRONMENT_BIBLE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\environments\review\ENVIRONMENT_BIBLE_REVIEW_QUEUE.md
pause

echo.
echo [5/9] Running scene contract synthesis...
python -m orchestrator synthesize-scene-contracts %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 5
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\scenes\SCENE_CONTRACT_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\scenes\review\SCENE_CONTRACT_REVIEW_QUEUE.md
pause

echo.
echo [6/9] Running shot package synthesis...
python -m orchestrator synthesize-shot-packages %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 6
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\SHOT_PACKAGE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\review\SHOT_PACKAGE_REVIEW_QUEUE.md
pause

echo.
echo [7/9] Running dialogue timeline synthesis...
python -m orchestrator synthesize-dialogue-timeline %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 7
echo   projects\%PROJECT_SLUG%\02_story_analysis\timelines\chapters\CH001\CH001_DIALOGUE_TIMELINE.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\timelines\dialogue\DIALOGUE_TIMELINE_INDEX.md
pause

echo.
echo [8/9] Running descriptor enrichment...
python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 8
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\DESCRIPTOR_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\DESCRIPTOR_REVIEW_QUEUE.md
pause

echo.
echo [9/9] Running prompt preparation...
python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Final review checkpoint
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\review\PROMPT_PREPARATION_REVIEW_QUEUE.md
echo.
echo Full authoring pipeline complete.
goto :done

:fail
echo.
echo Full authoring pipeline failed.
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
