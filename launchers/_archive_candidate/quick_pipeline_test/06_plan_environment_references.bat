@echo off
setlocal

call "%~dp0_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo Quick Pipeline Test: Plan Environment References
echo ========================================
echo.
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo Running environment reference planning for a small validation slice...
python -m orchestrator plan-environment-references %PROJECT_SLUG% --limit 2
if errorlevel 1 goto :fail

echo.
echo Environment reference planning complete.
goto :done

:fail
echo.
echo Environment reference planning failed.
popd >nul
exit /b 1

:done
popd >nul
exit /b 0
