@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
set "PROJECT_SLUG=%~1"
if not defined PROJECT_SLUG set "PROJECT_SLUG=princess_of_mars_test"
set "CHAPTERS=%~2"
if not defined CHAPTERS set "CHAPTERS=2-3"
cd /d "%SCRIPT_DIR%..\.."
python -m orchestrator synthesize-visual-fallbacks "%PROJECT_SLUG%" --force || goto :fail
call "%SCRIPT_DIR%\05_run_descriptor_enrichment.bat" "%PROJECT_SLUG%" "%CHAPTERS%" || goto :fail
call "%SCRIPT_DIR%\06_run_prompt_preparation.bat" "%PROJECT_SLUG%" "%CHAPTERS%" || goto :fail
call "%SCRIPT_DIR%\07_run_quality_grading.bat" "%PROJECT_SLUG%" "%CHAPTERS%" || goto :fail
echo Resume pipeline complete.
exit /b 0
:fail
echo Resume pipeline failed.
exit /b 1
