# World Refinement Report

- project_slug: princess_of_mars_test
- generated_at_utc: 2026-04-26T18:37:22.789012+00:00
- candidate_count: 12
- comparison_count: 14
- decision_count: 12

## Decisions

- environment ['dead_sea_bottom', 'dead_sea_bottom_expanse', 'dead_sea_bottom_incubator', 'dead_sea_bottom_valley'] -> merge_into_existing (target=dead_sea_bottom, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: Variants identified as chapter suffixes or descriptive expansions of the same environment; high confidence in dead_sea_bottom as root.
- environment ['deserted_martian_city', 'deserted_martian_city_plaza'] -> keep_separate (target=, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: Taxonomy conflict: 'city' (large scale) vs 'plaza' (sub-location/part of city). Merging would violate spatial hierarchy and entity kind distinction.
- character ['bull_ape', 'bull_ape_mate'] -> flag_for_human_review (target=, new_id=, new_kind=, confidence=low, human_review=True)
  - reason: Taxonomy conflict: low taxonomy confidence
- character ['lorquas_ptomel', 'lorquas_ptomel_jed'] -> flag_for_human_review (target=, new_id=, new_kind=, confidence=low, human_review=True)
  - reason: Taxonomy conflict: low taxonomy confidence
- character ['martian_warrior', 'martian_warrior_leader'] -> keep_separate (target=, new_id=, new_kind=, confidence=low, human_review=True)
  - reason: Potential role-based distinction (leader vs warrior) cannot be resolved due to unknown taxonomy and low heuristic score; merging generic roles without high confidence violates guardrails.
- character ['sola', 'sola_s_mother'] -> keep_separate (target=, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: The candidate suggests merging a character with their mother based on a chapter suffix heuristic; however, they are distinct individuals (mother vs daughter) and must remain separate to avoid identity collision.
- character ['the_watch_dog', 'watch_dog'] -> flag_for_human_review (target=, new_id=, new_kind=, confidence=low, human_review=True)
  - reason: Taxonomy conflict: 'the_watch_dog' has unknown primary_type/confidence 0.0, while 'watch_dog' is identified as a creature. Cannot safely merge without verifying if they are the same entity type.
- environment ['arizona_mountain_cave', 'arizona_mountain_cave_ledge'] -> keep_separate (target=, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: The entities represent distinct spatial locations (a cave vs. a specific ledge within/of that cave); merging would violate spatial granularity and risk losing specific environmental context.
- environment ['green_martian_city', 'green_martian_city_complex'] -> merge_into_existing (target=green_martian_city, new_id=, new_kind=, confidence=medium, human_review=False)
  - reason: Identified as a chapter suffix/variant; both entities share the same entity_kind (city) and appear in the same chapter.
- environment ['martian_plaza', 'martian_plaza_city'] -> merge_into_existing (target=martian_plaza, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: High-confidence match based on chapter suffix/variant detection; both entities share the same entity_kind (plaza).
- environment ['martian_wilderness', 'martian_wilderness_corridor'] -> merge_into_existing (target=martian_wilderness, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: High confidence that 'martian_wilderness_corridor' is a variant/suffix of the primary environment 'martian_wilderness'.
- environment ['mossy_waste', 'mossy_waste_expanse'] -> merge_into_existing (target=mossy_waste, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: mossy_waste_expanse is a descriptive suffix variant of mossy_waste; both share identical entity kind and chapter context.
