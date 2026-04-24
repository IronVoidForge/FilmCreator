@echo off
setlocal

call "%~dp0_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo Quick Pipeline Test: Generate Character References
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
echo Variant: bust_portrait
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo Running character reference generation for a small validation slice...
python -m orchestrator generate-character-references %PROJECT_SLUG% --variant bust_portrait --limit %LIMIT% --test-slice --execute
if errorlevel 1 goto :fail

echo.
echo Character reference generation complete.
goto :done

:fail
echo.
echo Character reference generation failed.
popd >nul
exit /b 1

:done
popd >nul
exit /b 0
