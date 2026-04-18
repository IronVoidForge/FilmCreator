@echo off
setlocal

cd /d C:\FilmCreator

echo Running Chapter X authoring checkpoint...
python -m orchestrator authoring-checkpoint princess_of_mars_test --chapter CH010_a_princess_of_mars_ch10.md
pause
