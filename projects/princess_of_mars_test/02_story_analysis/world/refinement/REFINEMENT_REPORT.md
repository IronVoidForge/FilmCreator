# World Refinement Report

- project_slug: princess_of_mars_test
- generated_at_utc: 2026-04-21T20:08:09.010889+00:00
- candidate_count: 8
- comparison_count: 9
- decision_count: 8

## Decisions

- environment ['dead_sea_bottom', 'dead_sea_bottom_expanse', 'dead_sea_bottom_incubator'] -> flag_for_human_review (target=, new_id=, new_kind=, confidence=low, human_review=True)
  - reason: Decision subject ids did not match candidate ids.
- character ['chieftain', 'the_chieftain'] -> merge_into_existing (target=chieftain, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: alias overlap: 'the_chieftain' is a redundant variation of the canonical ID 'chieftain'
- character ['bull_ape', 'bull_ape_mate'] -> merge_into_existing (target=bull_ape, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: detected chapter suffix variant; bull_ape is the preferred canonical target
- character ['lorquas_ptomel', 'lorquas_ptomel_jed'] -> merge_into_existing (target=lorquas_ptomel, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: detected chapter suffix variant; merging secondary ID into primary canonical entity
- character ['martian_warrior', 'martian_warrior_leader'] -> merge_into_existing (target=martian_warrior, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: High confidence match based on chapter suffix/variant heuristic; martian_warrior is the dominant canonical entity.
- environment ['arizona_mountain_cave', 'arizona_mountain_cave_ledge'] -> merge_into_existing (target=arizona_mountain_cave, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: arizona_mountain_cave_ledge is identified as a chapter suffix/variant of the parent environment
- environment ['martian_plaza', 'martian_plaza_city'] -> merge_into_existing (target=martian_plaza, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: detected chapter suffix variant; martian_plaza is the preferred canonical target
- environment ['mossy_waste', 'mossy_waste_expanse'] -> merge_into_existing (target=mossy_waste, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: mossy_waste_expanse is a descriptive variant/suffix of mossy_waste; preferred target has higher rank score.
