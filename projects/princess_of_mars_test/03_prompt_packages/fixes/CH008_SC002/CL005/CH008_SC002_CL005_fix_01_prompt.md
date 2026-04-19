# Title
CH008_SC002 CL005 Fix 01 Prompt

# ID
CH008_SC002_CL005_fix_01_prompt

# Purpose
Generate corrective still for Clip CL005 Beat BT005 (Boarding Action) preserving composition and look while fixing local issues. Ensure green-skinned warriors transition smoothly from building windows to gray vessel deck without breaking scene continuity or introducing extra crew members. Maintain daylight mixed with fire glow consistency as salvage phase begins.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
green-skinned warriors boarding gray vessel from window, daylight mixed with fire glow on hull, wide shot perspective from building, boarding equipment visible on deck, loot collection starting, smooth movement trajectory, cinematic lighting, detailed textures, desert city background, floating craft in air space, tactical boarding sequence, no crew resistance visible.

# Negative Prompt
distorted limbs, extra crew members, static composition, missing boarding gear, wrong lighting, blurry movement, dark shadows, human figures on deck, damaged hull inconsistent, poor anatomy, low resolution, overexposed fire, underexposed window view, floating debris, incorrect vessel shape.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL005
- duration_seconds: 5.0
- required_refs: Ship deck accessible, boarding equipment deployed, no crew resistance visible.
- optional_refs: Window frame.
- visible_character_assets: green-skinned warriors transitioning from windows to ship deck; human observer watching boarding action.
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide shot of boarding from window perspective, Medium shot of green figures on ship deck.
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: track_forward
- dependency_policy: linear_sequence
- auto_advance_policy: 
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain reblock_same_scene continuity ensuring green-skinned warriors move from windows to deck without teleportation.
- Preserve context of twenty gray vessels in scene while focusing on single unmanned craft for boarding sequence.
- Ensure lighting shifts from daylight to fire illumination are consistent with salvage phase progression.
- Keep visible character assets aligned with observer perspective at window frame.

# Repair Notes
- Fix anatomy distortion during movement from window to deck trajectory.
- Ensure boarding equipment is clearly visible on vessel deck without adding extra crew members.
- Correct fire glow intensity on hull to match salvage ritual solemnity.
- Maintain window frame obstruction in foreground for perspective consistency.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
