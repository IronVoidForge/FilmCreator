# Title
CH008_SC001 CL002 Keyframe Prompt

# ID
CH008_SC001_CL002_keyframe_prompt

# Purpose
Establish green-skinned warrior formation along city boundary line, beginning coordinated retreat toward eastern sector, maintaining continuity with preceding wide establishing shot.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
medium group shot, green-skinned warriors in ornate armor positioned along city boundary line, coordinated movement toward eastern horizon, dust kicked up by retreating troops visible, daylight illuminating scene, upper floor window frame visible in foreground for context, cinematic lighting, high fidelity still, smoke from fire visible in background.

# Negative Prompt
blur, distortion, extra limbs, missing characters, wrong character count, human protagonist, bright interior lighting, overexposed, low resolution, cartoonish, 3d render, plastic skin, bad anatomy, mismatched lighting, static pose, lack of motion, crowded composition, out of focus, burning, flames, fire, naval vessels, airships (wrong type), wrong vessel appearance.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md martian_retreat_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown, CL001_wide_establishing_first
- visible_character_assets: green_martian_warriors
- look_continuity_policy: dependent_on_CL001_wide_establishing_first
- intended_lighting_change: exterior_daylight_maintained
- composition_type: medium_group_shot
- continuity_mode: cutaway
- starting_keyframe_strategy: martians_at_city_perimeter
- dependency_policy: none
- auto_advance_policy: none
- fallback_strategy: cut_to_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: reference_alignment
- anatomy_repair_policy: strict
- consistency_targets: formation_spacing, dust_continuity, city_boundary_reference
- style_profile: cinematic_warfare_era
- batch_role: interval_frame
- fix_of: CL001_wide_establishing_first

# Continuity Notes
- Maintain green-skinned warrior appearance consistency (green skin, ornate armor). Ensure city boundary background maintains geographical continuity from preceding clip. Keep formation spacing consistent with retreat motion. Capture dust kicked up by retreating troops. Avoid showing character details or command signals in this establishing shot.

# Repair Notes
- Correct any green-skinned warrior appearance inconsistencies that don't match green skin/ornate armor design. Ensure city boundary and horizon matches scene breakdown specifications. Fix lighting mismatches from preceding clip to maintain exterior daylight continuity. Verify dust continuity with retreating troops. Adjust formation spacing if wrong number appears in composition.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
