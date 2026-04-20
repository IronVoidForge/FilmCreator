@echo off
setlocal

call "%~dp0..\..\_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail
set "PROJECT_SLUG=pilot_scene"
set "SCENE_ID=SC001"
set "CLIP_ID=CL001"
set "STAGE=still_fix"
set "FIX_DIR_REL=projects\pilot_scene\05_scenes\SC001\clips\CL001\stills\fixes"
set "CLIP_STATE_REL=projects\pilot_scene\05_scenes\SC001\clips\CL001\clip_state.json"

if not exist "%FILMCREATOR_ROOT%" (
    call :die Missing FilmCreator root: %FILMCREATOR_ROOT%
)

if not exist "%FILMCREATOR_ROOT%\%CLIP_STATE_REL%" (
    call :die Missing clip state: %FILMCREATOR_ROOT%\%CLIP_STATE_REL%
)

for /f "usebackq delims=" %%I in (`powershell -NoProfile -ExecutionPolicy Bypass -Command "$clipState = Get-Content '%FILMCREATOR_ROOT%\%CLIP_STATE_REL%' -Raw | ConvertFrom-Json; $clipState.latest_runs.still_fix"`) do set "MANIFEST_REL=%%I"
if not defined MANIFEST_REL (
    call :die No latest still-fix manifest was found in clip state.
)

if not exist "%FILMCREATOR_ROOT%\%MANIFEST_REL%" (
    call :die Missing still-fix manifest: %FILMCREATOR_ROOT%\%MANIFEST_REL%
)

echo Opening the still-fix folder for review...
start "" "%FILMCREATOR_ROOT%\%FIX_DIR_REL%"
echo.

cd /d "%FILMCREATOR_ROOT%"
python -m orchestrator interactive-review-and-promote %PROJECT_SLUG% %SCENE_ID% %CLIP_ID% %STAGE% "%MANIFEST_REL%" approved_still_fix --index 1
if errorlevel 1 (
    echo.
    call :die Interactive still-fix review failed.
)

echo.
echo Selected review copy should now exist under:
echo   %FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%\06_reviews\selected\
echo.
echo If approved_still_fix and current_continuity_source are populated, the still-fix review handoff worked.
pause
exit /b 0

:die
echo %*
echo.
pause
exit /b 1
