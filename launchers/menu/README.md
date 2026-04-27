# Menu and Operator Wrappers

These wrappers call the new tested Python operator commands rather than duplicating pipeline logic in BAT files.

## Launchers

- `RUN_PIPELINE_MENU.bat`
  - opens the interactive operator menu
- `PLAN_TRUSTED_RESUME.bat`
  - shows the trusted overnight resume plan without executing it
- `RUN_TRUSTED_RESUME.bat`
  - runs the trusted overnight resume path
- `RUN_QUICKTEST_11_TO_14.bat`
  - runs the tested quicktest composite from shot packages through prompt preparation
- `CLEAR_PRODUCTION_DOWNSTREAM_DRY_RUN.bat`
  - creates a dry-run cleanup plan for downstream artifacts

## Defaults

- `PROJECT_SLUG = princess_of_mars_test`
- quicktest wrappers default to `CHAPTERS = 2-3`

## Notes

- These wrappers are intentionally thin.
- The Python commands they call are covered by the focused test suite in:
  - `launchers/dev/run_cli_menu_tests.bat`
