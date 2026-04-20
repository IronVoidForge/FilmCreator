@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo FilmCreator Phase 7 Test Launcher
echo ========================================
echo.
set /p PROJECT_SLUG=Project slug [princess_of_mars_test]: 
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher will run:
echo   1. identity refinement plan
echo   2. pause for review
echo   3. identity refinement apply
echo   4. pause for review
echo   5. character bible synthesis
echo   6. pause for review
echo   7. forced character bible synthesis refresh
echo.
pause

echo.
echo [1/4] Building identity refinement plan...
python -m orchestrator refine-identities %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 1
echo Check this file before continuing:
echo   projects\%PROJECT_SLUG%\02_story_analysis\world\refinement\CHARACTER_MERGE_PLAN.json
echo.
pause

echo.
echo [2/4] Applying identity refinement merges...
python -m orchestrator refine-identities %PROJECT_SLUG% --apply
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 2
echo Check these files before continuing:
echo   projects\%PROJECT_SLUG%\02_story_analysis\world\refinement\CHARACTER_MERGE_PLAN.json
echo   projects\%PROJECT_SLUG%\02_story_analysis\world\refinement\CHARACTER_REGISTRY_GLOBAL_REFINED.json
echo.
pause

echo.
echo [3/4] Running character bible synthesis...
python -m orchestrator synthesize-character-bibles %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 3
echo Check these outputs before continuing:
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\characters\CHARACTER_BIBLE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\characters\review\CHARACTER_BIBLE_REVIEW_QUEUE.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\characters\CHAR_*.md
echo.
pause

echo.
echo [4/4] Running forced character bible synthesis refresh...
python -m orchestrator synthesize-character-bibles %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Final review checkpoint
echo Recommended files to inspect:
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\characters\CHARACTER_BIBLE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\characters\review\CHARACTER_BIBLE_REVIEW_QUEUE.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\bibles\characters\CHAR_john_carter.md
echo.
echo Phase 7 test launcher complete.
goto :done

:fail
echo.
echo Phase 7 test launcher failed.
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
