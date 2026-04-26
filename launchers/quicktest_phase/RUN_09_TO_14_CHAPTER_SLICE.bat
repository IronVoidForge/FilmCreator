@echo off
setlocal EnableExtensions
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"
set "CHAPTERS=%~2"
if "%CHAPTERS%"=="" set "CHAPTERS=2-3"

echo ============================================================
echo FilmCreator Quicktest Composite
echo Composite: 09 to 14 chapter slice
echo Project:   %PROJECT_SLUG%
echo Chapters:  %CHAPTERS%
echo ============================================================
echo.
call "%~dp0\09_SCENE_CONTRACTS_CHAPTERS.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call "%~dp0\10_SCENE_BINDINGS_CHAPTERS.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call "%~dp0\11_SHOT_PACKAGES_CHAPTERS.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call "%~dp0\12_DIALOGUE_TIMELINE_CHAPTERS.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call "%~dp0\13_DESCRIPTOR_ENRICHMENT_CHAPTERS.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
call "%~dp0\14_PROMPT_PREPARATION_CHAPTERS.bat" "%PROJECT_SLUG%" "%CHAPTERS%"
if errorlevel 1 goto :fail
echo COMPLETE
pause
exit /b 0
:fail
echo STOPPED
pause
exit /b 1
