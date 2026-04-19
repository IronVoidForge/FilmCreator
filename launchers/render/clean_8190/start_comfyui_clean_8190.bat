@echo off
setlocal

set "COMFY_ROOT=C:\ComfyUI\resources\ComfyUI"
set "COMFY_BASE=C:\ComfyUIInstall"
set "COMFY_PYTHON=C:\ComfyUIInstall\.venv\Scripts\python.exe"
set "COMFY_FRONTEND=C:\ComfyUI\resources\ComfyUI\web_custom_versions\desktop_app"
set "COMFY_URL=http://127.0.0.1:8190/system_stats"
set "CLEAN_ROOT=C:\FilmCreator\.comfy_clean"
set "CLEAN_USER=%CLEAN_ROOT%\user"
set "CLEAN_INPUT=%CLEAN_ROOT%\input"
set "CLEAN_OUTPUT=%CLEAN_ROOT%\output"

powershell -NoProfile -ExecutionPolicy Bypass -Command "try { $null = Invoke-WebRequest -UseBasicParsing '%COMFY_URL%' -TimeoutSec 3; exit 0 } catch { exit 1 }"
if "%ERRORLEVEL%"=="0" (
    echo Clean ComfyUI is already reachable on 127.0.0.1:8190.
    echo No new clean server was started.
    goto :end
)

if not exist "%COMFY_PYTHON%" (
    echo Missing Python executable: %COMFY_PYTHON%
    exit /b 1
)

if not exist "%COMFY_ROOT%\main.py" (
    echo Missing ComfyUI main.py under: %COMFY_ROOT%
    exit /b 1
)

if not exist "%COMFY_FRONTEND%\index.html" (
    echo Missing frontend folder: %COMFY_FRONTEND%
    exit /b 1
)

if not exist "%CLEAN_ROOT%" mkdir "%CLEAN_ROOT%"
if not exist "%CLEAN_USER%" mkdir "%CLEAN_USER%"
if not exist "%CLEAN_INPUT%" mkdir "%CLEAN_INPUT%"
if not exist "%CLEAN_OUTPUT%" mkdir "%CLEAN_OUTPUT%"

echo Starting clean ComfyUI on 127.0.0.1:8190 with custom nodes disabled...
start "ComfyUI Clean 8190" cmd /k "cd /d %COMFY_ROOT% && %COMFY_PYTHON% .\main.py --base-directory %COMFY_BASE% --user-directory %CLEAN_USER% --input-directory %CLEAN_INPUT% --output-directory %CLEAN_OUTPUT% --front-end-root %COMFY_FRONTEND% --listen 127.0.0.1 --port 8190 --disable-auto-launch --disable-all-custom-nodes"

:end
endlocal
