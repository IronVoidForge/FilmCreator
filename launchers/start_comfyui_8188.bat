@echo off
setlocal

set "COMFY_ROOT=C:\ComfyUI\resources\ComfyUI"
set "COMFY_BASE=C:\ComfyUIInstall"
set "COMFY_PYTHON=C:\ComfyUIInstall\.venv\Scripts\python.exe"
set "COMFY_FRONTEND=C:\ComfyUI\resources\ComfyUI\web_custom_versions\desktop_app"
set "COMFY_URL=http://127.0.0.1:8188/system_stats"

powershell -NoProfile -ExecutionPolicy Bypass -Command "try { $null = Invoke-WebRequest -UseBasicParsing '%COMFY_URL%' -TimeoutSec 3; exit 0 } catch { exit 1 }"
if "%ERRORLEVEL%"=="0" (
    echo ComfyUI is already reachable on 127.0.0.1:8188.
    echo No new server was started.
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

echo Starting ComfyUI on 127.0.0.1:8188...
start "ComfyUI 8188" cmd /k "cd /d %COMFY_ROOT% && %COMFY_PYTHON% .\main.py --base-directory %COMFY_BASE% --front-end-root %COMFY_FRONTEND% --listen 127.0.0.1 --port 8188 --disable-auto-launch --log-stdout"

:end
endlocal
