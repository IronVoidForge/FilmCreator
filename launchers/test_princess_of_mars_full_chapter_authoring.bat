@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator"

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
python -c "from orchestrator.story_authoring import analyze_chapter, build_chapter_continuity, plan_scene, write_shared_prompts; from orchestrator.authoring import write_prompts; import json; project='princess_of_mars_test'; chapter='CH008_a_princess_of_mars_ch08.md'; analysis = analyze_chapter(project_slug=project, chapter=chapter); continuity = build_chapter_continuity(project_slug=project, analysis=analysis); scene_runs = []; [scene_runs.append({'scene_id': scene_id, 'planning': plan_scene(project_slug=project, scene_id=scene_id).to_dict(), 'clip_prompts': write_prompts(project_slug=project, scene_id=scene_id).to_dict()}) for scene_id in analysis.scene_ids]; shared = write_shared_prompts(project_slug=project).to_dict(); print(json.dumps({'analysis': analysis.to_dict(), 'continuity': continuity.to_dict(), 'scene_runs': scene_runs, 'shared_prompts': shared}, indent=2))"
if errorlevel 1 goto :fail

echo.
echo If this worked, inspect:
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\world\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\scene_breakdowns\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\beat_bundles\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\clip_plans\
echo   C:\FilmCreator\projects\princess_of_mars_test\03_prompt_packages\
echo   C:\FilmCreator\projects\princess_of_mars_test\02_story_analysis\logs\
pause
exit /b 0

:fail
echo.
echo Princess of Mars full chapter authoring cascade failed.
pause
exit /b 1
