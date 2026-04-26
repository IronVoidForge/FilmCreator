@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"

set "MODE=%~2"

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0.." || goto :fail_resolver
set "REPO_ROOT=%FILMCREATOR_ROOT%"
set "PROJECT_DIR=%REPO_ROOT%\projects\%PROJECT_SLUG%"

echo ========================================
echo Clear downstream artifacts for refinement testing
echo ========================================
echo Project slug: %PROJECT_SLUG%
echo Project dir: %PROJECT_DIR%
echo Mode: %MODE%
echo.
echo PRESERVED:
echo - 01_source
echo - 02_story_analysis\chapter_analysis
echo - 02_story_analysis\character_breakdowns
echo - 02_story_analysis\environment_breakdowns
echo - 02_story_analysis\world\chapters
echo - reference assets / approved references
echo.
echo WILL DELETE IF PRESENT:
echo - 02_story_analysis\taxonomy
echo - 02_story_analysis\world\refinement
echo - 02_story_analysis\world\global\VISUAL_FALLBACKS.json
echo - 02_story_analysis\bibles
echo - 02_story_analysis\contracts
echo - 02_story_analysis\timelines
echo - 02_story_analysis\descriptors
echo - 02_story_analysis\grading
echo - 03_prompt_packages\prepared
echo ========================================
echo.

if not exist "%PROJECT_DIR%" (
    echo Project directory not found: %PROJECT_DIR%
    exit /b 1
)

if /I "%MODE%"=="DRY_RUN" (
    echo DRY RUN ONLY. No files will be deleted.
    call :show_target "02_story_analysis\taxonomy"
    call :show_target "02_story_analysis\world\refinement"
    call :show_file_target "02_story_analysis\world\global\VISUAL_FALLBACKS.json"
    call :show_target "02_story_analysis\bibles"
    call :show_target "02_story_analysis\contracts"
    call :show_target "02_story_analysis\timelines"
    call :show_target "02_story_analysis\descriptors"
    call :show_target "02_story_analysis\grading"
    call :show_target "03_prompt_packages\prepared"
    echo.
    echo DRY RUN complete.
    pause
    exit /b 0
)

set /p CONFIRM=Type DELETE to clear downstream artifacts for %PROJECT_SLUG%: 
if /I not "%CONFIRM%"=="DELETE" (
    echo Cancelled.
    pause
    exit /b 0
)

call :delete_dir "02_story_analysis\taxonomy"
call :delete_dir "02_story_analysis\world\refinement"
call :delete_file "02_story_analysis\world\global\VISUAL_FALLBACKS.json"
call :delete_dir "02_story_analysis\bibles"
call :delete_dir "02_story_analysis\contracts"
call :delete_dir "02_story_analysis\timelines"
call :delete_dir "02_story_analysis\descriptors"
call :delete_dir "02_story_analysis\grading"
call :delete_dir "03_prompt_packages\prepared"
echo.
echo ----------------------------------------
echo Verifying downstream cleanup...
echo ----------------------------------------

set "VERIFY_FAILED=0"

call :verify_missing_dir "02_story_analysis\taxonomy"
call :verify_missing_dir "02_story_analysis\world\refinement"
call :verify_missing_file "02_story_analysis\world\global\VISUAL_FALLBACKS.json"
call :verify_missing_dir "02_story_analysis\bibles"
call :verify_missing_dir "02_story_analysis\contracts"
call :verify_missing_dir "02_story_analysis\timelines"
call :verify_missing_dir "02_story_analysis\descriptors"
call :verify_missing_dir "02_story_analysis\grading"
call :verify_missing_dir "03_prompt_packages\prepared"

if not "%VERIFY_FAILED%"=="0" (
    echo.
    echo ERROR: Cleanup verification failed. Some downstream artifacts still exist.
    echo Do not run resume until these are removed.
    pause
    exit /b 1
)
echo.
echo Cleanup complete.
echo Preserved chapter summaries and source story analysis.
pause
exit /b 0

:show_target
set "REL=%~1"
set "ABS=%PROJECT_DIR%\%REL%"
if exist "%ABS%" (
    echo EXISTS DIR: %ABS%
) else (
    echo missing dir: %ABS%
)
exit /b 0

:show_file_target
set "REL=%~1"
set "ABS=%PROJECT_DIR%\%REL%"
if exist "%ABS%" (
    echo EXISTS FILE: %ABS%
) else (
    echo missing file: %ABS%
)
exit /b 0

:delete_dir
set "REL=%~1"
set "ABS=%PROJECT_DIR%\%REL%"
if exist "%ABS%" (
    echo Deleting directory: %ABS%
    rmdir /s /q "%ABS%"
) else (
    echo Skipping missing directory: %ABS%
)
exit /b 0

:delete_file
set "REL=%~1"
set "ABS=%PROJECT_DIR%\%REL%"
if exist "%ABS%" (
    echo Deleting file: %ABS%
    del /f /q "%ABS%"
) else (
    echo Skipping missing file: %ABS%
)
exit /b 0
:verify_missing_dir
set "REL=%~1"
set "ABS=%PROJECT_DIR%\%REL%"
if exist "%ABS%" (
    echo STILL EXISTS DIR: %ABS%
    set "VERIFY_FAILED=1"
) else (
    echo removed dir: %ABS%
)
exit /b 0

:verify_missing_file
set "REL=%~1"
set "ABS=%PROJECT_DIR%\%REL%"
if exist "%ABS%" (
    echo STILL EXISTS FILE: %ABS%
    set "VERIFY_FAILED=1"
) else (
    echo removed file: %ABS%
)
exit /b 0
:fail_resolver
echo Failed to resolve FilmCreator root.
exit /b 1
