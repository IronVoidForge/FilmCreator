@echo off
setlocal

call "%~dp0_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo Quick Pipeline Test: Generate Environment References
echo ========================================
echo.
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"
set "LIMIT=%~2"
if "%LIMIT%"=="" set "LIMIT=2"

echo.
echo Project slug: %PROJECT_SLUG%
echo Limit: %LIMIT%
echo Variant: establishing_wide
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo Running environment reference generation for a small validation slice...
python -m orchestrator generate-environment-references %PROJECT_SLUG% --variant establishing_wide --limit %LIMIT% --test-slice --execute
if errorlevel 1 goto :fail

echo.
echo Environment reference generation complete.
goto :done

:fail
echo.
echo Environment reference generation failed.
popd >nul
exit /b 1

:done
popd >nul
exit /b 0
