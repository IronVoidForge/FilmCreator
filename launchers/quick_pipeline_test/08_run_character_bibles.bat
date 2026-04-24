@echo off
setlocal

call "%~dp0_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo Quick Pipeline Test: Character Bibles
echo ========================================
echo.
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"
set "LIMIT=%~2"
if "%LIMIT%"=="" set /p LIMIT=Character limit [3]:
if "%LIMIT%"=="" set "LIMIT=3"

echo.
echo Project slug: %PROJECT_SLUG%
echo Character limit: %LIMIT%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo Running character bible synthesis for a small slice...
python -m orchestrator synthesize-character-bibles %PROJECT_SLUG% --limit %LIMIT%
if errorlevel 1 goto :fail

echo.
echo Character bible synthesis complete.
goto :done

:fail
echo.
echo Character bible synthesis failed.
popd >nul
exit /b 1

:done
popd >nul
exit /b 0
