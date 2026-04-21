@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    pause
    exit /b 1
)

pushd "%FILMCREATOR_ROOT%" >nul

set "DEFAULT_SLUG=princess_of_mars_test"
set /p PROJECT_SLUG=Project slug [%DEFAULT_SLUG%]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=%DEFAULT_SLUG%"

echo.
echo ========================================
echo FilmCreator Quality Rerun Queue
echo ========================================
echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher will:
echo   1. preview the grading rerun queue
echo   2. ask for confirmation before executing any reruns
echo   3. run the queued family reruns only if you type RUN
echo.

echo.
python -m orchestrator rerun-quality-artifacts %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
set /p EXECUTE=Type RUN to execute the queued reruns, or press Enter to stop:
if /I not "%EXECUTE%"=="RUN" goto :done

echo.
echo Running queued reruns...
python -m orchestrator rerun-quality-artifacts %PROJECT_SLUG% --execute
if errorlevel 1 goto :fail

echo.
echo Reruns complete.
echo   projects\%PROJECT_SLUG%\02_story_analysis\grading\QUALITY_GRADE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\grading\review\QUALITY_RERUN_QUEUE.md
echo.
goto :done

:fail
echo.
echo Quality rerun queue launcher failed.
pause
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
