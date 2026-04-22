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
echo Resume Latest Dev Slice Run
echo ========================================
echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This launcher resumes the latest matching `dev_slice_downstream` run.
echo If no interrupted run exists, it will start a fresh one with the saved config.
echo.

python -m orchestrator summarize-downstream-run %PROJECT_SLUG% --pipeline-key dev_slice_downstream
if errorlevel 1 goto :fail

echo.
echo Resuming latest dev slice run...
python -m orchestrator run-downstream-pipeline %PROJECT_SLUG% --pipeline-key dev_slice_downstream --shot-variant primary_keyframe --shot-variant alternate_angle --shot-variant consistency_repair
if errorlevel 1 goto :fail

echo.
echo Latest dev slice run complete.
goto :done

:fail
echo.
echo Latest dev slice run failed.
pause
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
