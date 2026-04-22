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
set "DEFAULT_CHAPTERS=1-6"
set /p CHAPTERS=Chapters filter [%DEFAULT_CHAPTERS%]:
if "%CHAPTERS%"=="" set "CHAPTERS=%DEFAULT_CHAPTERS%"

echo.
echo ========================================
echo FilmCreator Dev Slice Downstream Pipeline
echo ========================================
echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo Chapters: %CHAPTERS%
echo.
echo This launcher will run:
echo   1. scene contract synthesis
echo   2. scene binding synthesis
echo   3. shot package synthesis
echo   4. dialogue timeline synthesis
echo   5. descriptor enrichment
echo   6. prompt preparation
echo.
echo It assumes chapter summaries, character bibles, and environment bibles already exist.
echo Shot prompt prep stays trimmed to the current reduced shot variant set.
echo.

echo.
echo [1/6] Running scene contract synthesis...
python -m orchestrator synthesize-scene-contracts %PROJECT_SLUG% --force --chapters %CHAPTERS%
if errorlevel 1 goto :fail

echo.
echo [2/6] Running scene binding synthesis...
python -m orchestrator synthesize-scene-bindings %PROJECT_SLUG% --force --chapters %CHAPTERS%
if errorlevel 1 goto :fail

echo.
echo [3/6] Running shot package synthesis...
python -m orchestrator synthesize-shot-packages %PROJECT_SLUG% --force --chapters %CHAPTERS%
if errorlevel 1 goto :fail

echo.
echo [4/6] Running dialogue timeline synthesis...
python -m orchestrator synthesize-dialogue-timeline %PROJECT_SLUG% --force --chapters %CHAPTERS%
if errorlevel 1 goto :fail

echo.
echo [5/6] Running descriptor enrichment...
python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --force --chapters %CHAPTERS%
if errorlevel 1 goto :fail

echo.
echo [6/6] Running prompt preparation...
python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG% --force --chapters %CHAPTERS%
if errorlevel 1 goto :fail

echo.
echo Dev slice downstream pipeline complete.
goto :done

:fail
echo.
echo Dev slice downstream pipeline failed.
pause
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
