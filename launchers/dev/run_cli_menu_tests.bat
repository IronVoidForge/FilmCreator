@echo off
setlocal
python -m pytest tests/test_pipeline_menu.py tests/test_production_pipeline.py tests/test_production_status.py -q
endlocal
