@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail
set "PROJECT_SLUG=princess_of_mars_test"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    pause
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Retrying failed chapters from latest resilient book run...
python -m orchestrator.cli retry-failed-chapters %PROJECT_SLUG%
if errorlevel 1 goto :fail

echo.
echo Failed-chapter retry complete.
pause
exit /b 0

:fail
echo.
echo Failed-chapter retry failed.
pause
exit /b 1
