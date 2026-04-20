# World Refinement Report

- project_slug: princess_of_mars_test
- generated_at_utc: 2026-04-20T04:45:13.924060+00:00
- candidate_count: 4
- comparison_count: 5
- decision_count: 4

## Decisions

- character ['narrator', 'narrator_ch003', 'narrator_i'] -> merge_into_existing (target=narrator, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: normalized identity roots match; chapter suffix variants detected; preferred target narrator has highest rank score (38)
- character ['bull_ape', 'bull_ape_mate'] -> keep_separate (target=, new_id=, new_kind=, confidence=medium, human_review=False)
  - reason: Both entities are singular individuals with no competing canonical aliases detected; low heuristic score (14) suggests keeping separate despite preferred target ranking
- character ['lorquas_ptomel', 'lorquas_ptomel_jed'] -> merge_into_existing (target=lorquas_ptomel, new_id=, new_kind=, confidence=high, human_review=False)
  - reason: chapter suffix variant merged to preferred canonical ID with higher rank score (113 vs 51)
- environment ['plaza', 'plaza_destination'] -> merge_into_existing (target=plaza, new_id=, new_kind=, confidence=medium, human_review=False)
  - reason: Merging into preferred target plaza with higher canonical rank score (82 vs 35) and more chapter mentions
