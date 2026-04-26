@echo off
setlocal EnableExtensions

set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

set "CHAPTERS=%~2"
if "%CHAPTERS%"=="" set "CHAPTERS=2-3"

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0"
if errorlevel 1 (
    echo Failed to resolve FilmCreator root.
    pause
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"
if errorlevel 1 (
    echo Failed to change to repo root: %FILMCREATOR_ROOT%
    pause
    exit /b 1
)

echo ============================================================
echo FilmCreator Quicktest Phase
echo Phase:    00 Validate resume state
echo Project:  %PROJECT_SLUG%
echo Chapters: %CHAPTERS%
echo Repo:     %FILMCREATOR_ROOT%
echo ============================================================
echo.
echo NOTE: This validation is chapter-aware when CHAPTERS is supplied.
echo NOTE: Default CHAPTERS is 2-3. Override with arg 2.
echo.
echo COMMAND: python -m orchestrator.overnight_pipeline_resume_check "%PROJECT_SLUG%" "%CHAPTERS%" --report
echo.

python -m orchestrator.overnight_pipeline_resume_check "%PROJECT_SLUG%" "%CHAPTERS%" --report
set "EXIT_CODE=%ERRORLEVEL%"

echo.
echo Exit code: %EXIT_CODE%
pause
exit /b %EXIT_CODE%
