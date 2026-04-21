@echo off
setlocal enabledelayedexpansion

echo ========================================
echo FilmCreator Phase 11.7 Descriptor Enrichment Launcher
echo ========================================
echo.
set /p PROJECT_SLUG=Project slug [princess_of_mars_test]:
if "%PROJECT_SLUG%"=="" set PROJECT_SLUG=princess_of_mars_test
echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: C:\FilmCreator_MC
echo.
echo This launcher will run:
echo   1. descriptor enrichment synthesis
echo   2. pause for review
echo   3. forced descriptor enrichment refresh
echo.
pause

echo [1/2] Running descriptor enrichment synthesis...
python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --no-llm
echo.
echo Review checkpoint 1
echo Check these outputs before continuing:
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\DESCRIPTOR_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\DESCRIPTOR_REVIEW_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\review\DESCRIPTOR_REVIEW_QUEUE.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\characters\*.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\environments\*.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\scenes\*.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\shots\*\*\*.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\key_items\*.md
pause

echo [2/2] Running forced descriptor enrichment refresh...
python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --force
echo.
echo Final review checkpoint
echo Recommended files to inspect:
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\DESCRIPTOR_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\DESCRIPTOR_REVIEW_INDEX.md
echo   projects\%PROJECT_SLUG%\02_story_analysis\descriptors\review\DESCRIPTOR_REVIEW_QUEUE.md
echo.
echo Phase 11.7 descriptor enrichment launcher complete.
pause
