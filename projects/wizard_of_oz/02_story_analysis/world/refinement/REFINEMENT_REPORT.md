# World Refinement Report

- project_slug: wizard_of_oz
- generated_at_utc: 2026-04-27T12:50:57.518646+00:00
- candidate_count: 3
- comparison_count: 4
- decision_count: 3

## Decisions

- environment ['yellow_brick_road', 'yellow_brick_road_pathway', 'yellow_brick_road_transit'] -> flag_for_human_review (target=, new_id=, new_kind=, confidence=low, human_review=True)
  - reason: Decision subject ids did not match candidate ids.
- character ['farmer', 'farmer_woman_family'] -> keep_separate (target=, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: taxonomy primary_type conflict: individual vs group (guardrail violation for merge)
- character ['oz', 'oz_the_wizard'] -> merge_into_existing (target=oz, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: High confidence match; oz_the_wizard is a descriptive variant of the canonical entity oz.
