@echo off
setlocal

call "%~dp0_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo Quick Pipeline Test: Shot Packages
echo ========================================
echo.
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"
set "CHAPTERS=%~2"
if "%CHAPTERS%"=="" set /p CHAPTERS=Chapters filter [2-3]:
if "%CHAPTERS%"=="" set "CHAPTERS=2-3"

echo.
echo Project slug: %PROJECT_SLUG%
echo Chapters: %CHAPTERS%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo Running shot package synthesis...
python -m orchestrator synthesize-shot-packages %PROJECT_SLUG% --chapters %CHAPTERS%
if errorlevel 1 goto :fail

echo.
echo Shot package synthesis complete.
goto :done

:fail
echo.
echo Shot package synthesis failed.
popd >nul
exit /b 1

:done
popd >nul
exit /b 0
