@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Pilot scene LM Studio authoring smoke test
echo.
echo This test checks LM Studio connectivity first, then rewrites the canonical
echo scene-stage, keyframe, still-fix, and cut-motion prompt packages for SC001 CL001.
echo ComfyUI should be closed during this test if VRAM is tight.
echo.

echo [1/2] Checking LM Studio connectivity...
python -m orchestrator lmstudio-check
if errorlevel 1 goto :fail

echo.
echo [2/2] Writing pilot prompt packages...
python -m orchestrator write-prompts pilot_scene --scene SC001 --clip CL001
if errorlevel 1 goto :fail

echo.
echo If this worked, inspect these files:
echo   %FILMCREATOR_ROOT%\projects\pilot_scene\03_prompt_packages\scenes\SC001\CL001\SC001_CL001_scene_stage_prompt.md
echo   %FILMCREATOR_ROOT%\projects\pilot_scene\03_prompt_packages\keyframes\SC001\CL001\SC001_CL001_keyframe_prompt.md
echo   %FILMCREATOR_ROOT%\projects\pilot_scene\03_prompt_packages\fixes\SC001\CL001\SC001_CL001_fix_01_prompt.md
echo   %FILMCREATOR_ROOT%\projects\pilot_scene\03_prompt_packages\cut_motion\SC001\CL001\SC001_CL001_cut_motion_prompt.md
echo.
echo What to look for:
echo   1. Each file should still have the canonical heading schema.
echo   2. Purpose, Positive Prompt, Negative Prompt, Continuity Notes, and Repair Notes should contain fresh non-placeholder text.
echo   3. The workflow types should remain canonical for each stage.
echo   4. clip_state.json should point at these prompt packages under the inputs section.
pause
exit /b 0

:fail
echo.
echo Pilot scene LM Studio prompt-writer test failed.
pause
exit /b 1
