@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Princess of Mars shared prompt pass
echo.
echo This runs the shared-reference prompt pass only:
echo   - character shared prompts
echo   - environment shared prompts
echo LM Studio should be running.
echo Run chapter analysis first so the analysis files exist.
echo.

echo [1/2] Checking LM Studio connectivity...
python -m orchestrator lmstudio-check
if errorlevel 1 goto :fail

echo.
echo [2/2] Writing shared prompts...
python -m orchestrator write-shared-prompts princess_of_mars_test
if errorlevel 1 goto :fail

echo.
echo If this worked, inspect:
echo   C:\FilmCreator\projects\princess_of_mars_test\03_prompt_packages\characters\
echo   C:\FilmCreator\projects\princess_of_mars_test\03_prompt_packages\environments\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\logs\
pause
exit /b 0

:fail
echo.
echo Princess of Mars shared prompt pass failed.
pause
exit /b 1
