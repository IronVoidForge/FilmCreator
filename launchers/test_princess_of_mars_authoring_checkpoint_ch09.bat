@echo off
setlocal

cd /d C:\FilmCreator

echo Running Chapter IX authoring checkpoint...
python -m orchestrator authoring-checkpoint princess_of_mars_test --chapter CH009_a_princess_of_mars_ch09.md
pause
