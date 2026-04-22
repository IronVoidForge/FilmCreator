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
echo FilmCreator Dialogue Enrichment
echo ========================================
echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher will run:
echo   1. dialogue enrichment pass
echo.

echo.
echo [1/1] Running dialogue enrichment...
python -m orchestrator synthesize-dialogue-enrichment %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Dialogue enrichment complete.
echo   projects\%PROJECT_SLUG%\02_story_analysis\dialogue_enrichment\DIALOGUE_ENRICHMENT_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\dialogue_enrichment\review\DIALOGUE_ENRICHMENT_REVIEW_QUEUE.md
goto :done

:fail
echo.
echo Dialogue enrichment failed.
pause
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
