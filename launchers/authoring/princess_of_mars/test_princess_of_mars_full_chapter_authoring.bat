@echo off
setlocal

call "%~dp0..\..\_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Princess of Mars full chapter authoring cascade
echo.
echo This runs the chapter-wide authoring cascade with Phase B identity and continuity outputs:
echo   - chapter analysis
echo   - canonical character/environment registry generation
echo   - chapter continuity state generation
echo   - scene planning for every scene in the chapter
echo   - shot prompt writing for every planned scene
echo   - shared character/environment prompt writing
echo LM Studio should be running.
echo ComfyUI should be closed during this test if VRAM is tight.
echo.

echo [1/2] Checking LM Studio connectivity...
python -m orchestrator lmstudio-check
if errorlevel 1 goto :fail

echo.
echo [2/2] Running full chapter authoring cascade...
python -m orchestrator.chapter_authoring_runner
if errorlevel 1 goto :fail

echo.
echo If this worked, inspect:
echo   %FILMCREATOR_ROOT%\projects\princess_of_mars_test\02_story_analysis\world\
echo   %FILMCREATOR_ROOT%\projects\princess_of_mars_test\02_story_analysis\scene_breakdowns\
echo   %FILMCREATOR_ROOT%\projects\princess_of_mars_test\02_story_analysis\beat_bundles\
echo   %FILMCREATOR_ROOT%\projects\princess_of_mars_test\02_story_analysis\clip_plans\
echo   %FILMCREATOR_ROOT%\projects\princess_of_mars_test\03_prompt_packages\
echo   %FILMCREATOR_ROOT%\projects\princess_of_mars_test\02_story_analysis\logs\
pause
exit /b 0

:fail
echo.
echo Princess of Mars full chapter authoring cascade failed.
pause
exit /b 1
