@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0" || exit /b 1

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

start "FilmCreator Authoring Shell" cmd /k "cd /d %FILMCREATOR_ROOT% && echo Authoring shell ready. && echo. && echo LM Studio should be running in this phase. && echo ComfyUI should be closed if VRAM is tight. && echo. && echo Connectivity smoke test: && echo python -m orchestrator lmstudio-check && echo. && echo Pilot prompt-writer smoke test: && echo python -m orchestrator write-prompts pilot_scene --scene SC001 --clip CL001"

endlocal
