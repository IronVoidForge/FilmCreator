@echo off
setlocal

call "%~dp0_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

set "PROJECT_SLUG=%~1"
if not defined PROJECT_SLUG set "PROJECT_SLUG=princess_of_mars_test"
set "CHAPTERS=%~2"
if not defined CHAPTERS set "CHAPTERS=2-3"
set "CHARACTER_LIMIT=%~3"
if not defined CHARACTER_LIMIT set "CHARACTER_LIMIT=3"
set "ENVIRONMENT_LIMIT=%~4"
if not defined ENVIRONMENT_LIMIT set "ENVIRONMENT_LIMIT=3"
set "RUN_CHARACTER_BIBLES=%~5"
if not defined RUN_CHARACTER_BIBLES set "RUN_CHARACTER_BIBLES=0"
set "RUN_ENVIRONMENT_BIBLES=%~6"
if not defined RUN_ENVIRONMENT_BIBLES set "RUN_ENVIRONMENT_BIBLES=0"

echo.
echo ========================================
echo FilmCreator Quick Pipeline Test (Auto)
echo ========================================
echo.
echo Project slug: %PROJECT_SLUG%
echo Chapters: %CHAPTERS%
echo Character bible limit: %CHARACTER_LIMIT%
echo Environment bible limit: %ENVIRONMENT_LIMIT%
echo Include character bibles: %RUN_CHARACTER_BIBLES%
echo Include environment bibles: %RUN_ENVIRONMENT_BIBLES%
echo Repo root: %FILMCREATOR_ROOT%
echo.

call "%~dp000_clear_downstream_artifacts.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

if "%RUN_CHARACTER_BIBLES%"=="1" (
    call "%~dp008_run_character_bibles.bat" %PROJECT_SLUG% %CHARACTER_LIMIT%
    if errorlevel 1 goto :fail
)

if "%RUN_ENVIRONMENT_BIBLES%"=="1" (
    call "%~dp009_run_environment_bibles.bat" %PROJECT_SLUG% %ENVIRONMENT_LIMIT%
    if errorlevel 1 goto :fail
)

call "%~dp001_run_scene_contracts.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call "%~dp002_run_scene_bindings.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call "%~dp003_run_shot_packages.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call "%~dp004_run_dialogue_timeline.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call "%~dp005_run_descriptor_enrichment.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call "%~dp006_run_prompt_preparation.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

call "%~dp007_run_quality_grading.bat" %PROJECT_SLUG% %CHAPTERS%
if errorlevel 1 goto :fail

echo.
echo Quick pipeline test complete.
popd >nul
exit /b 0

:fail
echo.
echo Quick pipeline test failed.
popd >nul
exit /b 1
