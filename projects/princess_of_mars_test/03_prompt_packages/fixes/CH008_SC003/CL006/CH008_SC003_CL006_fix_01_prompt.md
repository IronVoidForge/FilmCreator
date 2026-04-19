# Title
CH008_SC003 CL006 Fix 01 Prompt

# ID
CH008_SC003_CL006_fix_01_prompt

# Purpose
Generate corrective still for CL006 medium shot showing prisoner discovery after haul operation. Preserve composition and look while fixing local issues like anatomy distortion or background drift. Maintain emotional shift from curiosity to concern and discovery as per BT003 beat documentation. Ensure visual continuity with Green Warriors gathering around the Human Female Prisoner on the plain surface with southern building in background.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Green warriors gathering around slender human female prisoner on plain surface, building south of position visible in background daylight, smoke from fire aftermath, missile impact flames context, warrior green skin ornaments spears, prisoner light reddish copper skin coal black hair waving caught loosely into strange coiffure naked except for highly wrought ornaments cheeks crimson lips ruby, medium shot composition, emotional shift from curiosity to concern and discovery, action oriented awe inspiring tense combat sequences style

# Negative Prompt
distorted anatomy, wrong skin tones, extra limbs, blurry faces, modern clothing, valley background instead of plain, excessive motion blur, bright sunlight without smoke context, wrong hair color, wrong building location, distorted ornaments, low resolution, text, watermark

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL006
- duration_seconds: 5
- required_refs: CH008_SC003_BT003.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: green_warriors_gathering_around_prisoner, prisoner_stationary_discovered_state, building_south_of_position_in_background
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_shot
- continuity_mode: medium_shows_prisoner_discovery
- starting_keyframe_strategy: focus_on_warriors_gathering_around_prisoner_with_building_south_of_position_in_background
- dependency_policy: dependent_on_previous_tracking_shot_following_haul_operation_completion
- auto_advance_policy: 
- fallback_strategy: insert_close_up_if_medium_shots_fails_to_show_emotional_shift_from_curiosity_to_concern
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: action_oriented_awe_inspiring_tense_combat_sequences
- batch_role: 
- fix_of: still_fix

# Continuity Notes
- Maintain character consistency for Green Warriors and Human Female Prisoner across frames.
- Preserve environment continuity of plain surface and southern building background.
- Ensure emotional tone reflects discovery and concern rather than curiosity alone.

# Repair Notes
- Fix local anatomy distortions while preserving warrior formation.
- Correct lighting mismatches to match fire aftermath context.
- Align background building position to match continuity source.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
