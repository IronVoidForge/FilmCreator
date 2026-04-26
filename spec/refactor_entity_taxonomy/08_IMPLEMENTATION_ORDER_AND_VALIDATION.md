# 08 - Implementation Order And Validation

## Recommended order
1. Fallback safety patch
2. Chapter entity extraction
3. Character taxonomy stage
4. World refinement integration
5. Character bible integration
6. Fallback from taxonomy
7. Quality grading rerun routing

## After each phase
- `python -m compileall orchestrator`
- run targeted pytest only
- inspect JSON outputs on 3-5 spot checks

## Do not run full auto pipeline until phases 1-6 pass targeted tests.

## Final validation
Run quick pipeline auto logged on two books and compare outputs.
