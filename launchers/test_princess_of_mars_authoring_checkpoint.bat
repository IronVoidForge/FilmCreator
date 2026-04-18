@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Princess of Mars authoring checkpoint
echo.
echo This runs the first pre-SQL authoring checkpoint against the pasted Chapter VIII source.
echo LM Studio should be running.
echo ComfyUI should be closed during this test if VRAM is tight.
echo.

echo [1/2] Checking LM Studio connectivity...
python -m orchestrator lmstudio-check
if errorlevel 1 goto :fail

echo.
echo [2/2] Running the authoring checkpoint...
python -m orchestrator authoring-checkpoint princess_of_mars_test --chapter CH001_a_princess_of_mars_ch08.md --scene SC001
if errorlevel 1 goto :fail

echo.
echo If this worked, inspect these outputs:
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\story_summary\project_summary.md
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\chapter_analysis\CH001_summary.md
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\character_breakdowns\CHARACTER_INDEX.md
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\environment_breakdowns\ENVIRONMENT_INDEX.md
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\scene_breakdowns\SCENE_INDEX.md
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\scene_breakdowns\SC001.md
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\beat_bundles\SC001\BEAT_INDEX.md
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\clip_plans\SC001\SC001_clip_roster.md
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\clip_plans\SC001\CL001.md
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\logs\
echo   C:\FilmCreator\projects\princess_of_mars_test\03_prompt_packages\characters\
echo   C:\FilmCreator\projects\princess_of_mars_test\03_prompt_packages\environments\
echo   C:\FilmCreator\projects\princess_of_mars_test\03_prompt_packages\keyframes\SC001\
echo.
echo What to look for:
echo   1. The analysis files should contain fresh non-placeholder text.
echo   2. Any underdescribed characters should be listed in the JSON output under manual_character_description_requests.
echo   3. If a character is flagged, a manual paste target should exist under:
echo      C:\FilmCreator\projects\princess_of_mars_test\01_source\character_descriptions\
echo   4. SC001 should now have beat bundles, a clip roster, and clip plans such as CL001 and CL002.
echo   5. Shared character/environment prompt packages and clip-local prompt packages should now exist.
echo   6. The logs folder should now contain one raw LM Studio exchange file per authoring task.
echo   7. The checkpoint should have reached those outputs through multiple single-purpose LM Studio calls rather than one monolithic generation.
pause
exit /b 0

:fail
echo.
echo Princess of Mars authoring checkpoint failed.
pause
exit /b 1
