@echo off
cd /d C:\FilmCreator

echo Running Phase B1 identity + environment resolution...

python -c "from orchestrator.world_registry import run_phase_b1_resolution; import json; print(json.dumps(run_phase_b1_resolution('princess_of_mars_test'), indent=2))"

pause
