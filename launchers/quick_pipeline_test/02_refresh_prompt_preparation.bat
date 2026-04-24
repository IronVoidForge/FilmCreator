@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo Quick Pipeline Test: Prompt Refresh
echo ========================================
echo.
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo Running prompt preparation refresh...
python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG% --force
if errorlevel 1 goto :fail

echo.
echo Prompt preparation refresh complete.
goto :done

:fail
echo.
echo Prompt refresh failed.
popd >nul
exit /b 1

:done
popd >nul
exit /b 0
