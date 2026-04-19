@echo off
setlocal

set DEFAULT_SLUG=princess_of_mars_test
set /p PROJECT_SLUG=Project slug [%DEFAULT_SLUG%]: 
if "%PROJECT_SLUG%"=="" set PROJECT_SLUG=%DEFAULT_SLUG%

call clean_story_analysis_outputs.bat

echo.
echo Starting multi-chapter analysis...
echo.

python -c "from orchestrator.book_authoring import analyze_book; analyze_book(project_slug='%PROJECT_SLUG%')"

echo.
echo Run complete.
pause
