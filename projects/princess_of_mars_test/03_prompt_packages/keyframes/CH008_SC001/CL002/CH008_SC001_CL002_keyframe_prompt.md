# Title
CH008_SC001 CL002 Keyframe Prompt

# ID
CH008_SC001_CL002_keyframe_prompt

# Purpose
Establish John Carter's perspective watching twenty large gray air craft descend toward city building from upper floor window, capturing the pivotal arrival moment with valley and hills beyond maintaining geographical continuity.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
wide establishing shot, long low gray-painted vessels descending from upper sky toward city building facade, twenty air craft visible with strange banners on prows, valley below and hills beyond framing edges, daylight illuminating scene, figures crowding forward decks, cinematic lighting, high fidelity still, smoke from fire visible in background, missile impact flames spurt, open ground plaza below, distant horizon maintaining continuity.

# Negative Prompt
blur, distortion, extra limbs, missing characters, wrong character count, human protagonist, bright interior lighting, overexposed, low resolution, cartoonish, 3d render, plastic skin, bad anatomy, mismatched lighting, static pose, lack of motion, crowded composition, out of focus, burning, flames, fire, naval vessels, airships (wrong type), wrong vessel appearance

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md air_craft_descending_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown, CL001_wide_establishing_first
- visible_character_assets: none_vessel_focus
- look_continuity_policy: dependent_on_CL001_wide_establishing_first
- intended_lighting_change: exterior_daylight_maintained
- composition_type: wide_establishing_shot
- continuity_mode: insert
- starting_keyframe_strategy: first_craft_visible_in_distance
- dependency_policy: none
- auto_advance_policy: none
- fallback_strategy: cut_to_wide_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: reference_alignment
- anatomy_repair_policy: strict
- consistency_targets: vessel_count, banner_appearance, valley_hills_continuity
- style_profile: cinematic_warfare_era
- batch_role: interval_frame
- fix_of: CL001_wide_establishing_first

# Continuity Notes
- Maintain air craft appearance consistency (long low gray-painted vessels with strange banners).
- Ensure valley and hills background maintains geographical continuity from preceding clip.
- Keep vessel count at twenty visible throughout keyframe sequence.
- Capture descent trajectory from upper sky to lower city level.
- Avoid showing character details or command signals in this establishing shot.

# Repair Notes
- Correct any vessel appearance inconsistencies that don't match gray-painted long low design.
- Ensure banner and device placement on prows matches scene breakdown specifications.
- Fix lighting mismatches from preceding clip to maintain exterior daylight continuity.
- Verify valley and hills background maintains geographical consistency.
- Adjust vessel count if wrong number appears in composition.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
