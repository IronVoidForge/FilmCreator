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
echo It will resume the latest interrupted matching run automatically if one exists.
echo Shot prompt prep stays trimmed to the current reduced shot variant set.
echo.

echo.
echo Running resumable downstream pipeline...
python -m orchestrator run-downstream-pipeline %PROJECT_SLUG% --chapters %CHAPTERS% --start-phase scene_contracts --pipeline-key dev_slice_downstream --shot-variant primary_keyframe --shot-variant alternate_angle --shot-variant consistency_repair
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
