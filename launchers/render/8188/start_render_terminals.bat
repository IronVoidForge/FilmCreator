@echo off
setlocal

call "%~dp0..\..\_shared\resolve_filmcreator_root.bat" "%~dp0" || exit /b 1
set "COMFY_URL=http://127.0.0.1:8188/system_stats"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

call "%~dp0start_comfyui_8188.bat"

echo Waiting briefly for ComfyUI to answer on 8188...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ready=$false; for($i=0; $i -lt 20; $i++){ try { $null = Invoke-WebRequest -UseBasicParsing '%COMFY_URL%' -TimeoutSec 2; $ready=$true; break } catch { Start-Sleep -Seconds 1 } }; if($ready){ exit 0 } else { exit 1 }"
if not "%ERRORLEVEL%"=="0" (
    echo ComfyUI did not become reachable on 127.0.0.1:8188 within the wait window.
    echo Check the ComfyUI terminal and try again.
    exit /b 1
)

start "FilmCreator Render Shell" cmd /k "cd /d %FILMCREATOR_ROOT% && echo ComfyUI render phase shell ready. && echo. && echo Current pilot batch command: && echo python -m orchestrator run-batch projects/pilot_scene/05_scenes/SC001/clips/CL001/logs/RUN_0001.json --ref image_1=projects/pilot_scene/05_scenes/SC001/clips/CL001/inputs/smoke_env.png --ref image_2=projects/pilot_scene/05_scenes/SC001/clips/CL001/inputs/smoke_char.png --seed-base 3000 --execute && echo. && echo ComfyUI is expected to stay open during render execution."

endlocal
