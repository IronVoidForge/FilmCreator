@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

start "FilmCreator Authoring Shell" cmd /k "cd /d %FILMCREATOR_ROOT% && echo Authoring shell ready. && echo. && echo LM Studio should be running for future authoring integration tests. && echo ComfyUI should be closed in this phase if VRAM is tight. && echo. && echo Current local planning command: && echo python -m orchestrator plan-batch pilot_scene keyframe --scene SC001 --clip CL001 --batch-size 4 --seed 1000"

endlocal
