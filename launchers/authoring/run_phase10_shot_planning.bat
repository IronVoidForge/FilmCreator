@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo FilmCreator Phase 10 Shot Planning Launcher
echo ========================================
echo.
set /p PROJECT_SLUG=Project slug [princess_of_mars_test]: 
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher will run:
echo   1. shot package synthesis
echo   2. pause for review
echo   3. forced shot package synthesis refresh
echo.
pause

echo.
echo [1/2] Running shot package synthesis...
python -m orchestrator synthesize-shot-packages %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 1
echo Check these outputs before continuing:
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\SHOT_PACKAGE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\SHOT_PACKAGE_REVIEW_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\review\SHOT_PACKAGE_REVIEW_QUEUE.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\CH*\CH*_SC*\SH*.md
echo.
pause

echo.
echo [2/2] Running forced shot package synthesis refresh...
python -m orchestrator synthesize-shot-packages %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Final review checkpoint
echo Recommended files to inspect:
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\SHOT_PACKAGE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\SHOT_PACKAGE_REVIEW_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\scenes\CH024\CH024_SC001.md
echo.
echo Phase 10 shot planning launcher complete.
goto :done

:fail
echo.
echo Phase 10 shot planning launcher failed.
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
