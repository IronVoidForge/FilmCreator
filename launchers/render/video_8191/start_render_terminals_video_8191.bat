@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator"
set "COMFY_URL=http://127.0.0.1:8191/system_stats"
set "VIDEO_INPUT=C:\FilmCreator\.comfy_video\input"
set "VIDEO_OUTPUT=C:\FilmCreator\.comfy_video\output"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

call "%~dp0start_comfyui_video_8191.bat"

echo Waiting for video ComfyUI to answer on 8191...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ready=$false; for($i=0; $i -lt 90; $i++){ try { $null = Invoke-WebRequest -UseBasicParsing '%COMFY_URL%' -TimeoutSec 2; $ready=$true; break } catch { Start-Sleep -Seconds 1 } }; if($ready){ exit 0 } else { exit 1 }"
if not "%ERRORLEVEL%"=="0" (
    echo Video ComfyUI did not become reachable on 127.0.0.1:8191 within the wait window.
    echo Check the video ComfyUI terminal and try again.
    exit /b 1
)

start "FilmCreator Video Render Shell" cmd /k "cd /d %FILMCREATOR_ROOT% && set FILMCREATOR_COMFY_BASE_URL=http://127.0.0.1:8191 && set FILMCREATOR_COMFY_INPUT_DIR=%VIDEO_INPUT% && set FILMCREATOR_COMFY_OUTPUT_DIR=%VIDEO_OUTPUT% && set FILMCREATOR_COMFY_TIMEOUT_SECONDS=7200 && echo Video render shell ready. && echo FILMCREATOR_COMFY_BASE_URL=%FILMCREATOR_COMFY_BASE_URL% && echo FILMCREATOR_COMFY_INPUT_DIR=%FILMCREATOR_COMFY_INPUT_DIR% && echo FILMCREATOR_COMFY_OUTPUT_DIR=%FILMCREATOR_COMFY_OUTPUT_DIR% && echo FILMCREATOR_COMFY_TIMEOUT_SECONDS=%FILMCREATOR_COMFY_TIMEOUT_SECONDS% && echo. && echo Current pilot short-cut motion commands: && echo python -m orchestrator plan-batch pilot_scene cut_motion --scene SC001 --clip CL001 --seed 5000 && echo python -m orchestrator run-batch ^<manifest_path^> --seed-base 6000 --execute"

endlocal
