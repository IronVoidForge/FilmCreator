@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo Quick Pipeline Test: Clear Downstream Artifacts
echo ========================================
echo.
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.
echo This clears downstream artifacts only and preserves upstream chapter summaries.
echo Press any key to continue.
pause

call "%FILMCREATOR_ROOT%\launchers\multi_chapter\01_reset_downstream_artifacts.bat" %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo Downstream artifact clear complete.
goto :done

:fail
echo.
echo Downstream artifact clear failed.
popd >nul
exit /b 1

:done
popd >nul
exit /b 0
