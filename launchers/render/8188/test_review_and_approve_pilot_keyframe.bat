@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator"
set "PROJECT_SLUG=pilot_scene"
set "SCENE_ID=SC001"
set "CLIP_ID=CL001"
set "STAGE=keyframe"
set "KEYFRAME_DIR_REL=projects\pilot_scene\05_scenes\SC001\clips\CL001\stills\keyframes"
set "CLIP_STATE_REL=projects\pilot_scene\05_scenes\SC001\clips\CL001\clip_state.json"

if not exist "%FILMCREATOR_ROOT%" (
    call :die Missing FilmCreator root: %FILMCREATOR_ROOT%
)

if not exist "%FILMCREATOR_ROOT%\%CLIP_STATE_REL%" (
    call :die Missing clip state: %FILMCREATOR_ROOT%\%CLIP_STATE_REL%
)

for /f "usebackq delims=" %%I in (`powershell -NoProfile -ExecutionPolicy Bypass -Command "$clipState = Get-Content '%FILMCREATOR_ROOT%\%CLIP_STATE_REL%' -Raw | ConvertFrom-Json; $clipState.latest_runs.keyframe"`) do set "MANIFEST_REL=%%I"
if not defined MANIFEST_REL (
    call :die No latest keyframe manifest was found in clip state.
)

if not exist "%FILMCREATOR_ROOT%\%MANIFEST_REL%" (
    call :die Missing keyframe manifest: %FILMCREATOR_ROOT%\%MANIFEST_REL%
)

echo Opening the keyframe folder for review...
start "" "%FILMCREATOR_ROOT%\%KEYFRAME_DIR_REL%"
echo.

cd /d "%FILMCREATOR_ROOT%"
python -m orchestrator interactive-review-and-promote %PROJECT_SLUG% %SCENE_ID% %CLIP_ID% %STAGE% "%MANIFEST_REL%" approved_keyframe --index 1
if errorlevel 1 (
    echo.
    call :die Interactive keyframe review failed.
)

echo.
echo Selected review copy should now exist under:
echo   %FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%\06_reviews\selected\
echo.
echo If approved_keyframe and current_continuity_source are populated, the review-and-approval handoff worked.
pause
exit /b 0

:die
echo %*
echo.
pause
exit /b 1
