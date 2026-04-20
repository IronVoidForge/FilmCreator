@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo LM Studio connectivity smoke test
echo.
echo Make sure LM Studio is running and ComfyUI is closed if VRAM is tight.
echo.

python -m orchestrator lmstudio-check
if errorlevel 1 goto :fail

echo.
echo If this worked, you should see:
echo   - base_url
echo   - configured_model
echo   - resolved_model
echo   - one or more available_models
pause
exit /b 0

:fail
echo.
echo LM Studio connectivity test failed.
pause
exit /b 1
