@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Princess of Mars chapter analysis pass
echo.
echo This runs the chapter-scoped analysis pass only:
echo   - chapter summary
echo   - character extraction
echo   - environment extraction
echo   - scene decomposition
echo LM Studio should be running.
echo ComfyUI should be closed during this test if VRAM is tight.
echo.

echo [1/2] Checking LM Studio connectivity...
python -m orchestrator lmstudio-check
if errorlevel 1 goto :fail

echo.
echo [2/2] Running chapter analysis...
python -m orchestrator analyze-chapter princess_of_mars_test --chapter CH001_a_princess_of_mars_ch08.md
if errorlevel 1 goto :fail

echo.
echo If this worked, inspect:
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\story_summary\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\chapter_analysis\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\character_breakdowns\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\environment_breakdowns\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\scene_breakdowns\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\logs\
pause
exit /b 0

:fail
echo.
echo Princess of Mars chapter analysis pass failed.
pause
exit /b 1
