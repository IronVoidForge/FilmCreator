@echo off
setlocal

call "%~dp0..\..\_shared\resolve_filmcreator_root.bat" "%~dp0" || exit /b 1
set "COMFY_URL=http://127.0.0.1:8190/system_stats"
set "BATCH_MANIFEST=projects/pilot_scene/05_scenes/SC001/clips/CL001/logs/RUN_0001.json"
set "REF_ENV=projects/pilot_scene/05_scenes/SC001/clips/CL001/inputs/smoke_env.png"
set "REF_CHAR=projects/pilot_scene/05_scenes/SC001/clips/CL001/inputs/smoke_char.png"
set "FILMCREATOR_COMFY_BASE_URL=http://127.0.0.1:8190"
set "FILMCREATOR_COMFY_INPUT_DIR=%FILMCREATOR_ROOT%\.comfy_clean\input"
set "FILMCREATOR_COMFY_OUTPUT_DIR=%FILMCREATOR_ROOT%\.comfy_clean\output"

if not exist "%FILMCREATOR_ROOT%\%BATCH_MANIFEST%" (
    echo Missing batch manifest: %FILMCREATOR_ROOT%\%BATCH_MANIFEST%
    exit /b 1
)

if not exist "%FILMCREATOR_ROOT%\%REF_ENV%" (
    echo Missing environment ref: %FILMCREATOR_ROOT%\%REF_ENV%
    exit /b 1
)

if not exist "%FILMCREATOR_ROOT%\%REF_CHAR%" (
    echo Missing character ref: %FILMCREATOR_ROOT%\%REF_CHAR%
    exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -Command "try { $null = Invoke-WebRequest -UseBasicParsing '%COMFY_URL%' -TimeoutSec 3; exit 0 } catch { exit 1 }"
if not "%ERRORLEVEL%"=="0" (
    echo Clean ComfyUI is not reachable on 127.0.0.1:8190.
    echo Run launchers\render\clean_8190\start_render_terminals_clean_8190.bat first, then retry this file.
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"
python -m orchestrator run-batch %BATCH_MANIFEST% --ref "image_1=%REF_ENV%" --ref "image_2=%REF_CHAR%" --seed-base 3000 --execute

echo.
echo Review the batch manifest and generated stills under the pilot_scene project folders.
pause
endlocal
