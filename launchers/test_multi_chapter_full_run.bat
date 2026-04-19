@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator_MC"
set "PROJECT_SLUG=princess_of_mars_test"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    pause
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Checking LM Studio connectivity...
python -m orchestrator lmstudio-check
if errorlevel 1 goto :fail

echo.
echo Running multi-chapter analysis from manifest...
python -c "from orchestrator.book_authoring import analyze_book; import json; summary = analyze_book(project_slug='%PROJECT_SLUG%'); print(json.dumps(summary.to_dict(), indent=2))"
if errorlevel 1 goto :fail

echo.
echo Multi-chapter analysis complete.
pause
exit /b 0

:fail
echo.
echo Multi-chapter analysis failed.
pause
exit /b 1
