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

echo.
echo ========================================
echo Character Descriptor Spot Check
echo ========================================
echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher reruns a small validation set of character descriptors:
echo   - john_carter
echo   - dejah_thoris
echo   - lorquas_ptomel
echo   - chieftain
echo   - bull_ape
echo   - woola
echo.
echo It is meant for quick quality inspection before a larger rerun.
echo.

python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --force --entity-type character --entity-id john_carter --entity-id dejah_thoris --entity-id lorquas_ptomel --entity-id chieftain --entity-id bull_ape --entity-id woola
if errorlevel 1 goto :fail

echo.
echo Character descriptor spot check complete.
echo.
echo Suggested review files:
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\characters\john_carter.json
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\characters\dejah_thoris.json
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\characters\lorquas_ptomel.json
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\characters\chieftain.json
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\characters\bull_ape.json
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\characters\woola.json
goto :done

:fail
echo.
echo Character descriptor spot check failed.
pause
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
