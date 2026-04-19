# Title
CH008_SC001 CL002 Keyframe Prompt

# ID
CH008_SC001_CL002_keyframe_prompt

# Purpose
Establish the human protagonist positioned at the rear of a ceremonial procession moving forward through the city plaza toward open ground, capturing the visual anticipation and formation geometry before the sudden retreat order occurs.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
medium tracking shot, rear view of human protagonist walking in formation, green-clad warriors marching ahead in central column, spacious doorways and plazas visible on left and right, city architecture framing edges, open ground horizon approaching in distance, synchronized steps, anticipation atmosphere, cinematic lighting, high fidelity still, alien terrain valley entrance, procession artifacts at head, forward progression motion blur minimal, detailed textures on garments and weapons, atmospheric haze near horizon.

# Negative Prompt
blur, distortion, extra limbs, missing characters, wrong character count, airships, naval vessels, fire, flames, burning, retreat order, halt, reverse movement, dark shadows, overexposed, low resolution, cartoonish, 3d render, plastic skin, bad anatomy, mismatched lighting, static pose, lack of motion, crowded composition, out of focus.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md processions_return_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: human protagonist rear_position, green-clad warriors central_column visible
- look_continuity_policy: dependent_on_CL001_wide_establishing_first
- intended_lighting_change: none
- composition_type: medium_tracking
- continuity_mode: insert
- starting_keyframe_strategy: follow_human_protagonist_position_from_rear_of_procession
- dependency_policy: dependent_on_CL001_wide_establishing_first
- auto_advance_policy: none
- fallback_strategy: cut_to_medium_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: reference_alignment
- anatomy_repair_policy: strict
- consistency_targets: character_count, limb_placement, formation_geometry
- style_profile: cinematic_warfare_era
- batch_role: interval_frame
- fix_of: CL001_wide_establishing_first

# Continuity Notes
- Maintain forward progression motion logic with synchronized steps.
- Ensure location transition from built environment to natural terrain begins subtly.
- Keep human protagonist visible at rear while green-clad warriors occupy central column.
- Capture anticipation building among onlookers and procession members.
- Avoid showing command signals or retreat order in this keyframe.

# Repair Notes
- Correct any motion blur that obscures character details.
- Ensure formation geometry matches previous wide establishing shot.
- Fix lighting mismatches from preceding clip to maintain continuity.
- Verify character count remains consistent with procession scale.
- Adjust anatomy if limbs appear distorted during tracking movement.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
