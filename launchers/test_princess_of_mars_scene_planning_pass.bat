@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Princess of Mars scene planning pass
echo.
echo This runs the scene-scoped planning pass only:
echo   - scene beat mapping
echo   - clip roster generation
echo   - clip plan generation
echo LM Studio should be running.
echo Run the chapter analysis pass first so SC001 exists.
echo.

echo [1/2] Checking LM Studio connectivity...
python -m orchestrator lmstudio-check
if errorlevel 1 goto :fail

echo.
echo [2/2] Running scene planning...
python -m orchestrator plan-scene princess_of_mars_test --scene CH008_SC001
if errorlevel 1 goto :fail

echo.
echo If this worked, inspect:
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\beat_bundles\CH008_SC001\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\clip_plans\CH008_SC001\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\logs\
pause
exit /b 0

:fail
echo.
echo Princess of Mars scene planning pass failed.
pause
exit /b 1
