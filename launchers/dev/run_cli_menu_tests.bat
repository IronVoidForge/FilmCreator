@echo off
setlocal
python -m pytest tests/test_pipeline_menu.py tests/test_production_pipeline.py tests/test_production_status.py tests/test_production_cleanup.py -q -p no:cacheprovider
endlocal
