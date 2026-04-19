# Title
CH008_SC001 CL002 Keyframe Prompt

# ID
CH008_SC001_CL002_keyframe_prompt

# Purpose
Establish the group of green-clad warriors pausing at building entrances upon retreat order, capturing the transition from procession to interior entry in a deserted city setting.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
medium shot, group clusters of green-clad warriors standing at doorway thresholds, eyelines directed inward toward dark interiors, deserted buildings with open doorways visible, exterior daylight illuminating figures, synchronized entry motion beginning, tactical retreat atmosphere, cinematic lighting, high fidelity still, valley city architecture framing edges, dark shadows swallowing figures, detailed textures on garments and weapons.

# Negative Prompt
blur, distortion, extra limbs, missing characters, wrong character count, airships, naval vessels, fire, flames, burning, human protagonist, halt, reverse movement, bright interior lighting, overexposed, low resolution, cartoonish, 3d render, plastic skin, bad anatomy, mismatched lighting, static pose, lack of motion, crowded composition, out of focus.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md building_entry_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown, CL001_wide_establishing_first
- visible_character_assets: green-clad warriors doorway_clusters
- look_continuity_policy: dependent_on_CL001_wide_establishing_first
- intended_lighting_change: exterior_daylight_to_interior_darkness
- composition_type: medium_shot_entry
- continuity_mode: insert
- starting_keyframe_strategy: group_pause_at_doorway_thresholds
- dependency_policy: dependent_on_CL001_wide_establishing_first
- auto_advance_policy: none
- fallback_strategy: cut_to_medium_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: reference_alignment
- anatomy_repair_policy: strict
- consistency_targets: character_count, limb_placement, entry_geometry
- style_profile: cinematic_warfare_era
- batch_role: interval_frame
- fix_of: CL001_wide_establishing_first

# Continuity Notes
- Maintain retreat order execution logic with synchronized entry motion.
- Ensure location transition from built environment to interior darkness begins subtly.
- Keep green-clad warriors visible at doorway thresholds while interiors remain dark.
- Capture urgency building among procession members entering buildings.
- Avoid showing command signals or airship battle in this keyframe.

# Repair Notes
- Correct any motion blur that obscures character details during entry.
- Ensure interior darkness matches building interiors from scene breakdown.
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
