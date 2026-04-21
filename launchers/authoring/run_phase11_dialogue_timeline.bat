@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo FilmCreator Phase 11 Dialogue Timeline Launcher
echo ========================================
echo.
set /p PROJECT_SLUG=Project slug [princess_of_mars_test]: 
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher will run:
echo   1. dialogue timeline synthesis
echo   2. pause for review
echo   3. forced dialogue timeline synthesis refresh
echo.
pause

echo.
echo [1/2] Running dialogue timeline synthesis...
python -m orchestrator synthesize-dialogue-timeline %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo Review checkpoint 1
echo Check these outputs before continuing:
echo   projects\%PROJECT_SLUG%\02_story_analysis\timelines\dialogue_timeline.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\timelines\edit_timeline.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\timelines\review\DIALOGUE_TIMELINE_REVIEW_QUEUE.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\timelines\chapters\CH*\CH*_DIALOGUE_TIMELINE.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\CH*\CH*_SC*\SH*\DIALOGUE.md
echo.
pause

echo.
echo [2/2] Running forced dialogue timeline synthesis refresh...
python -m orchestrator synthesize-dialogue-timeline %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Final review checkpoint
echo Recommended files to inspect:
echo   projects\%PROJECT_SLUG%\02_story_analysis\timelines\dialogue_timeline.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\timelines\edit_timeline.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\timelines\review\DIALOGUE_TIMELINE_REVIEW_QUEUE.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\CH024\CH024_SC001\SH001\DIALOGUE.md
echo.
echo Phase 11 dialogue timeline launcher complete.
goto :done

:fail
echo.
echo Phase 11 dialogue timeline launcher failed.
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
