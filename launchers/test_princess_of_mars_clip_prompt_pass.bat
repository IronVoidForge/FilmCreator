@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Princess of Mars clip prompt pass
echo.
echo This runs the clip-local prompt pass only for CH008_SC001:
echo   - scene-stage prompt
echo   - keyframe prompt
echo   - still-fix prompt
echo   - cut-motion prompt
echo LM Studio should be running.
echo Run scene planning first so CH008_SC001 clip plans exist.
echo.

echo [1/2] Checking LM Studio connectivity...
python -m orchestrator lmstudio-check
if errorlevel 1 goto :fail

echo.
echo [2/2] Writing clip-local prompts...
python -m orchestrator write-prompts princess_of_mars_test --scene CH008_SC001
if errorlevel 1 goto :fail

echo.
echo If this worked, inspect:
echo   C:\FilmCreator\projects\princess_of_mars_test\03_prompt_packages\scenes\CH008_SC001\
echo   C:\FilmCreator\projects\princess_of_mars_test\03_prompt_packages\keyframes\CH008_SC001\
echo   C:\FilmCreator\projects\princess_of_mars_test\03_prompt_packages\fixes\CH008_SC001\
echo   C:\FilmCreator\projects\princess_of_mars_test\03_prompt_packages\cut_motion\CH008_SC001\
pause
exit /b 0

:fail
echo.
echo Princess of Mars clip prompt pass failed.
pause
exit /b 1
