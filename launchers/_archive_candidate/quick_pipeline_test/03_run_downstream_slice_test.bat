@echo off
setlocal

call "%~dp0_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo Quick Pipeline Test: Downstream Slice
echo ========================================
echo.
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo Running downstream slice for chapters 2-3...
python -m orchestrator run-downstream-pipeline %PROJECT_SLUG% --chapters 2-3 --start-phase scene_contracts --pipeline-key dev_slice_downstream --shot-variant primary_keyframe --shot-variant alternate_angle --shot-variant consistency_repair
if errorlevel 1 goto :fail

echo.
echo Downstream slice test complete.
goto :done

:fail
echo.
echo Downstream slice test failed.
popd >nul
exit /b 1

:done
popd >nul
exit /b 0
