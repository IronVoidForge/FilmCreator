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
set /p CHAPTERS=Chapters filter [all]:

echo.
echo ========================================
echo FilmCreator Scene Bindings and Downstream Refresh
echo ========================================
echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher will run:
echo   1. scene binding synthesis
echo   2. shot package synthesis
echo   3. dialogue timeline synthesis
echo   4. descriptor enrichment
echo   5. prompt preparation
echo.
echo Character and environment bibles are NOT rerun.
echo.

set "CHAPTER_ARGS="
if not "%CHAPTERS%"=="" set "CHAPTER_ARGS=--chapters %CHAPTERS%"

echo.
echo [1/5] Running scene binding synthesis...
python -m orchestrator synthesize-scene-bindings %PROJECT_SLUG% --force %CHAPTER_ARGS%
if errorlevel 1 goto :fail

echo.
echo [2/5] Running shot package synthesis...
python -m orchestrator synthesize-shot-packages %PROJECT_SLUG% --force %CHAPTER_ARGS%
if errorlevel 1 goto :fail

echo.
echo [3/5] Running dialogue timeline synthesis...
python -m orchestrator synthesize-dialogue-timeline %PROJECT_SLUG% --force %CHAPTER_ARGS%
if errorlevel 1 goto :fail

echo.
echo [4/5] Running descriptor enrichment...
python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --force %CHAPTER_ARGS%
if errorlevel 1 goto :fail

echo.
echo [5/5] Running prompt preparation...
python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG% --force %CHAPTER_ARGS%
if errorlevel 1 goto :fail

echo.
echo Scene bindings and downstream refresh complete.
echo.
echo Suggested review files:
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\scene_bindings\SCENE_BINDING_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\contracts\shots\SHOT_PACKAGE_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\DESCRIPTOR_INDEX.md
echo   projects\%PROJECT_SLUG%\03_prompt_packages\prepared\PROMPT_PREPARATION_INDEX.md
goto :done

:fail
echo.
echo Scene bindings and downstream refresh failed.
pause
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
