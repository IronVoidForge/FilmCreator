# Title
CH008_SC002 CL005 Fix 01 Prompt

# ID
CH008_SC002_CL005_fix_01_prompt

# Purpose
Generate corrective still for Clip CL005 Beat BT002 (Fleet Returns Fire) preserving composition and look while fixing local issues. Ensure Martian Fleet Crews transition smoothly from damaged ship structures to firing positions without breaking scene continuity or introducing extra crew members. Maintain daylight mixed with fire glow consistency as counter-battery phase begins.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Martian Fleet Crews firing from damaged ships, daylight mixed with fire glow on hull, close-up perspective on weapon muzzle flash, return fire arcs visible, debris falling, smooth movement trajectory, cinematic lighting, detailed textures, scorched hull background, gray vessel structures, tactical counter-battery sequence, no crew resistance visible.

# Negative Prompt
distorted limbs, extra crew members, static composition, missing firing gear, wrong lighting, blurry movement, dark shadows, human figures on deck, damaged hull inconsistent, poor anatomy, low resolution, overexposed fire, underexposed ship view, floating debris, incorrect vessel shape, boarding action.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL005
- duration_seconds: 5.0
- required_refs: Ship deck accessible, firing equipment deployed, no crew resistance visible.
- optional_refs: Window frame.
- visible_character_assets: Martian Fleet Crews transitioning from ship structures to firing positions; human observer watching counter-battery action.
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Close-up of weapon muzzle flash, Medium shot of crew firing from damaged ships.
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
- Maintain reblock_same_scene continuity ensuring Martian Fleet Crews move from ship structures to firing positions without teleportation.
- Preserve context of twenty gray vessels in scene while focusing on single damaged craft for counter-battery sequence.
- Ensure lighting shifts from daylight to fire illumination are consistent with salvage phase progression.
- Keep visible character assets aligned with observer perspective at window frame.

# Repair Notes
- Fix anatomy distortion during movement from ship structures to firing positions trajectory.
- Ensure firing equipment is clearly visible on vessel deck without adding extra crew members.
- Correct fire glow intensity on hull to match counter-battery ritual solemnity.
- Maintain window frame obstruction in foreground for perspective consistency.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
