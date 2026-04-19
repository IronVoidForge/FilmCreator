# Princess of Mars Test Project Tree

This file lists the current working project structure for `princess_of_mars_test`.
Logs, failures, caches, and other transient artifacts are intentionally omitted.

## Root

```text
PROJECT_STATUS.md
project_state.json
01_source/
02_story_analysis/
03_prompt_packages/
05_scenes/
```

## 01_source

```text
01_source/chapters/
  CH008_a_princess_of_mars_ch08.md
  CH009_a_princess_of_mars_ch09.md
  CH010_a_princess_of_mars_ch10.md

01_source/character_descriptions/
  airship_crews_clarification.md
  carter_clarification.md
  dejah_thoris_clarification.md
  earthly_woman_prisoner_clarification.md
  green_martian_female_ch008_clarification.md
  green_martian_females_clarification.md
  green_martian_warrior_ch008_clarification.md
  green_martian_warriors_clarification.md
  green_martians_clarification.md
  green_warriors_clarification.md
  human_woman_prisoner_clarification.md
  john_carter_clarification.md
  lorquas_ptomel_clarification.md
  martian_female_clarification.md
  martian_prisoner_clarification.md
  martian_warrior_clarification.md
  narrator_clarification.md
  narrator_observer_clarification.md
  prisoner_captive_clarification.md
  prisoner_clarification.md
  protagonist_ch008_clarification.md
  sola_ch008_clarification.md
  sola_clarification.md
  the_narrator_clarification.md
  woola_clarification.md
```

## 02_story_analysis

```text
02_story_analysis/README.md

02_story_analysis/story_summary/
  README.md
  project_summary.md

02_story_analysis/chapter_analysis/
  CH008_summary.md
  README.md

02_story_analysis/scene_breakdowns/
  README.md
  SC001.md
  SC002.md
  SC003.md
  SCENE_INDEX.md

02_story_analysis/beat_bundles/
  README.md
  SC001/BEAT_INDEX.md
  SC001/BT001.md
  SC001/BT002.md
  SC001/BT003.md

02_story_analysis/clip_plans/
  README.md
  SC001/SC001_clip_roster.md
  SC001/CL001.md
  SC001/CL002.md
  SC001/CL003.md
  SC001/CL004.md
  SC001/CL005.md
  SC001/CL006.md

02_story_analysis/character_breakdowns/
  README.md
  CHARACTER_INDEX.md
  carter.md
  green_martian_females.md
  green_martians.md
  prisoner.md

02_story_analysis/environment_breakdowns/
  README.md
  ENVIRONMENT_INDEX.md
  city_buildings.md
  disabled_airship.md
  open_plaza.md

02_story_analysis/authoring_tasks/
  README.md
  T001_chapter_intake_and_summary.md
  T002_character_extraction.md
  T003_environment_extraction.md
  T004_scene_decomposition.md
  T005_scene_breakdown_and_beats.md
  T006_clip_roster_and_clip_plans.md
  T007_shared_reference_prompt_writing.md
  T008_clip_prompt_writing.md
```

## 03_prompt_packages

```text
03_prompt_packages/characters/
  airship_crews/airship_crews_ref_prompt.md
  captive_ch001/captive_ch001_ref_prompt.md
  carter/carter_ref_prompt.md
  dejah_thoris/dejah_thoris_ref_prompt.md
  earthly_woman_prisoner/earthly_woman_prisoner_ref_prompt.md
  green_martian_females/green_martian_females_ref_prompt.md
  green_martian_warriors/green_martian_warriors_ref_prompt.md
  green_martians/green_martians_ref_prompt.md
  green_warriors/green_warriors_ref_prompt.md
  human_woman_prisoner/human_woman_prisoner_ref_prompt.md
  john_carter/john_carter_ref_prompt.md
  lorquas_ptomel/lorquas_ptomel_ref_prompt.md
  martian_prisoner/martian_prisoner_ref_prompt.md
  narrator/narrator_ref_prompt.md
  narrator_ch001/narrator_ch001_ref_prompt.md
  narrator_observer/narrator_observer_ref_prompt.md
  prisoner/prisoner_ref_prompt.md
  prisoner_captive/prisoner_captive_ref_prompt.md
  sola/sola_ref_prompt.md
  the_narrator/the_narrator_ref_prompt.md
  woola/woola_ref_prompt.md
  woola_ch001/woola_ch001_ref_prompt.md

03_prompt_packages/environments/
  airship/airship_ref_prompt.md
  building_interior/building_interior_ref_prompt.md
  building_interiors/building_interiors_ref_prompt.md
  building_roofs/building_roofs_ref_prompt.md
  building_windows_upper_floor/building_windows_upper_floor_ref_prompt.md
  buildings/buildings_ref_prompt.md
  city/city_ref_prompt.md
  city_buildings/city_buildings_ref_prompt.md
  city_plaza_exterior/city_plaza_exterior_ref_prompt.md
  deserted_city_buildings/deserted_city_buildings_ref_prompt.md
  disabled_airship/disabled_airship_ref_prompt.md
  disabled_martian_ship/disabled_martian_ship_ref_prompt.md
  hills/hills_ref_prompt.md
  martian_valley_hills/martian_valley_hills_ref_prompt.md
  open_ground_hill/open_ground_hill_ref_prompt.md
  open_plaza/open_plaza_ref_prompt.md
  plaza_encounter_space/plaza_encounter_space_ref_prompt.md
  plaza_return/plaza_return_ref_prompt.md
  plaza_street_level/plaza_street_level_ref_prompt.md
  rooftops/rooftops_ref_prompt.md
  upper_floor_window/upper_floor_window_ref_prompt.md
  valley/valley_ref_prompt.md
  valley_battlefield/valley_battlefield_ref_prompt.md
  valley_hills_vista/valley_hills_vista_ref_prompt.md
  window_upper_floor/window_upper_floor_ref_prompt.md

03_prompt_packages/scenes/
  SC001/CL001/SC001_CL001_scene_stage_prompt.md
  SC001/CL002/SC001_CL002_scene_stage_prompt.md
  SC001/CL003/SC001_CL003_scene_stage_prompt.md
  SC001/CL004/SC001_CL004_scene_stage_prompt.md
  SC001/CL005/SC001_CL005_scene_stage_prompt.md
  SC001/CL006/SC001_CL006_scene_stage_prompt.md

03_prompt_packages/keyframes/
  SC001/CL001/SC001_CL001_keyframe_prompt.md
  SC001/CL002/SC001_CL002_keyframe_prompt.md
  SC001/CL003/SC001_CL003_keyframe_prompt.md
  SC001/CL004/SC001_CL004_keyframe_prompt.md
  SC001/CL005/SC001_CL005_keyframe_prompt.md
  SC001/CL006/SC001_CL006_keyframe_prompt.md

03_prompt_packages/fixes/
  SC001/CL001/SC001_CL001_fix_01_prompt.md
  SC001/CL002/SC001_CL002_fix_01_prompt.md
  SC001/CL003/SC001_CL003_fix_01_prompt.md
  SC001/CL004/SC001_CL004_fix_01_prompt.md
  SC001/CL005/SC001_CL005_fix_01_prompt.md
  SC001/CL006/SC001_CL006_fix_01_prompt.md

03_prompt_packages/cut_motion/
  SC001/CL001/SC001_CL001_cut_motion_prompt.md
  SC001/CL002/SC001_CL002_cut_motion_prompt.md
  SC001/CL003/SC001_CL003_cut_motion_prompt.md
  SC001/CL004/SC001_CL004_cut_motion_prompt.md
  SC001/CL005/SC001_CL005_cut_motion_prompt.md
  SC001/CL006/SC001_CL006_cut_motion_prompt.md
```

## 05_scenes

```text
05_scenes/SC001/scene_state.json
05_scenes/SC001/clips/CL001/clip_state.json
05_scenes/SC001/clips/CL002/clip_state.json
05_scenes/SC001/clips/CL003/clip_state.json
05_scenes/SC001/clips/CL004/clip_state.json
05_scenes/SC001/clips/CL005/clip_state.json
05_scenes/SC001/clips/CL006/clip_state.json
05_scenes/SC002/scene_state.json
05_scenes/SC003/scene_state.json
05_scenes/SC004/scene_state.json
05_scenes/SC005/scene_state.json
05_scenes/SC006/scene_state.json
05_scenes/SC007/scene_state.json
05_scenes/SC008/scene_state.json
```

## Notes

- Generated logs under `02_story_analysis/logs/` and `03_prompt_packages/logs/` are intentionally excluded.
- Historical stale prompt-package folders such as `narrator_ch001` and `woola_ch001` are still present until we regenerate or retire them.
