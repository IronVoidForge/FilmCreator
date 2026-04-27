@echo off
setlocal
python -m pytest tests/test_pipeline_menu.py tests/test_production_pipeline.py tests/test_production_status.py tests/test_production_cleanup.py tests/test_production_run_state.py tests/test_cli_menu_commands.py tests/test_phase_range.py -q -p no:cacheprovider
endlocal
