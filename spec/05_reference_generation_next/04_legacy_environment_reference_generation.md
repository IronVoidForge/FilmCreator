# 2.2 Environment Reference Generation

## Goal

Generate reusable environment references at the project scope so clip work can compose from approved environments instead of rebuilding them ad hoc.

## Inputs

- Environment breakdown in `02_story_analysis/environment_breakdowns/`
- Environment prompt in `03_prompt_packages/environments/<env_id>/`
- Workflow ID `still.t2i.klein.distilled`

## Outputs

- Candidate outputs routed to the project environment reference area
- Approved environment refs promoted into `04_references/environments/<env_id>/`
- Review copies mirrored into `06_reviews/selected/`

## Acceptance

- Scene and clip work can consume a stable approved environment ref by state reference.
- Environment generation remains project-scoped unless a future feature intentionally overrides that rule.
