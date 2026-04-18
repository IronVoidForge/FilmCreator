# Title
SC001 CL006 Fix 01 Prompt

# ID
SC001_CL006_fix_01_prompt

# Purpose
Corrective still-generation prompt for stage still_fix that preserves composition and look while fixing local issues using approved base image_1 and secondary reference image_2.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
human male protagonist standing at dark wood window with metal accents, observing gray airships approaching deserted city, daylight sunlight reflecting off ship devices, smoke and flame from burning vessel visible in distance, polished stone tiles floor, profile to camera three-quarter angle, hands on window sill, green Martian warrior attire, military strategy tone, action-oriented atmosphere, cinematic lighting, high detail

# Negative Prompt
blurry, distorted, extra fingers, floating limbs, wrong anatomy, inconsistent lighting, dark shadows where daylight expected, extra objects, text, watermark, signature, low resolution, bad hands, missing window frame, wrong floor material, mismatched attire colors

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL006
- duration_seconds: 5
- required_refs: image_1
- optional_refs: image_2
- visible_character_assets: human male protagonist, green Martian warrior
- look_continuity_policy: preserve composition and lighting
- intended_lighting_change: daylight morning to midday
- composition_type: medium profile shot
- continuity_mode: window frame consistent
- starting_keyframe_strategy: approved still base
- dependency_policy: two_ref_klein_distilled
- auto_advance_policy: manual_review
- fallback_strategy: re_generate_with_refs
- consistency_assist_policy: enabled
- consistency_assist_method: local_fix
- anatomy_repair_policy: strict
- consistency_targets: window_wiper, floor_tiles, attire
- style_profile: barsoom_action
- batch_role: fix_01
- fix_of: still_base_artifacts

# Continuity Notes
- Window wiper position must remain unchanged for continuity
- Lighting shifts from soft morning to brighter midday throughout scene
- narrator maintains consistent distance from window frame
- Floor material remains consistent polished stone tiles

# Repair Notes
- Fix any distorted hands or fingers on the window sill
- Correct facial expression artifacts in close-up shots
- Ensure background airships match fleet formation consistency
- Remove extra limbs or floating objects near window frame

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
