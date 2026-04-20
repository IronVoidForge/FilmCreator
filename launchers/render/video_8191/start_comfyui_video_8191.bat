@echo off
setlocal

call "%~dp0..\..\_shared\resolve_filmcreator_root.bat" "%~dp0" || exit /b 1

set "COMFY_ROOT=C:\ComfyUI\resources\ComfyUI"
set "COMFY_BASE=C:\ComfyUIInstall"
set "COMFY_PYTHON=C:\ComfyUIInstall\.venv\Scripts\python.exe"
set "COMFY_FRONTEND=C:\ComfyUI\resources\ComfyUI\web_custom_versions\desktop_app"
set "COMFY_URL=http://127.0.0.1:8191/system_stats"
set "VIDEO_ROOT=%FILMCREATOR_ROOT%\.comfy_video"
set "VIDEO_USER=%VIDEO_ROOT%\user"
set "VIDEO_INPUT=%VIDEO_ROOT%\input"
set "VIDEO_OUTPUT=%VIDEO_ROOT%\output"

powershell -NoProfile -ExecutionPolicy Bypass -Command "try { $null = Invoke-WebRequest -UseBasicParsing '%COMFY_URL%' -TimeoutSec 3; exit 0 } catch { exit 1 }"
if "%ERRORLEVEL%"=="0" (
    echo Video ComfyUI is already reachable on 127.0.0.1:8191.
    echo No new video server was started.
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

if not exist "%VIDEO_ROOT%" mkdir "%VIDEO_ROOT%"
if not exist "%VIDEO_USER%" mkdir "%VIDEO_USER%"
if not exist "%VIDEO_INPUT%" mkdir "%VIDEO_INPUT%"
if not exist "%VIDEO_OUTPUT%" mkdir "%VIDEO_OUTPUT%"

echo Starting video ComfyUI on 127.0.0.1:8191 with the required Wan video custom nodes...
start "ComfyUI Video 8191" cmd /k "cd /d %COMFY_ROOT% && %COMFY_PYTHON% .\main.py --base-directory %COMFY_BASE% --user-directory %VIDEO_USER% --input-directory %VIDEO_INPUT% --output-directory %VIDEO_OUTPUT% --front-end-root %COMFY_FRONTEND% --listen 127.0.0.1 --port 8191 --disable-auto-launch --disable-all-custom-nodes --whitelist-custom-nodes comfyui-longlook comfyui-videohelpersuite comfyui-impact-pack scale-image-to-total-pixels-advanced gguf"

:end
endlocal
