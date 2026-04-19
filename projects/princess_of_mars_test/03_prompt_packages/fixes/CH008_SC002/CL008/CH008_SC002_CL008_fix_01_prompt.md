# Title
CH008_SC002 CL008 Fix 01 Prompt

# ID
CH008_SC002_CL008_fix_01_prompt

# Purpose
Correct focus from salvage/towing to crew realignment and broadside firing on a damaged ship. Maintain continuity with battle state (smoke, fire damage). Ensure Martians operate weapons while Narrator observes from window POV context.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Medium shot of damaged gray warship swinging broadside across valley, crew members shifting to new firing positions, weapons elevated and realigned, hull scorched with visible thruster sway, smoke trails rising, daylight mixed with fire illumination, distant hills beyond horizon, city buildings in background.

# Negative Prompt
No undamaged ships visible, no towing equipment deployed, no modern elements, no excessive smoke obscuring the ship entirely, no green Martian anatomy errors, no floating debris unrelated to battle, no sudden movement breaking continuity.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5.0
- required_refs: Damaged ship hull, crew realignment positions
- optional_refs: Window frame
- visible_character_assets: Crew members on ship
- look_continuity_policy: Maintain battle damage state
- intended_lighting_change: Fire glow mixed with daylight
- composition_type: Medium shot
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: slight sway on damaged thrusters
- dependency_policy: parallel to wide shot for coverage
- auto_advance_policy: none
- fallback_strategy: insert crew adjusting angles if movement erratic
- consistency_assist_policy: maintain weapon alignment
- consistency_assist_method: 
- anatomy_repair_policy: correct green Martian features
- consistency_targets: 
- style_profile: cinematic_compositional
- batch_role: fix_01
- fix_of: 

# Continuity Notes
- Focus on crew movement and weapon alignment, not salvage operations.
- Ship is damaged but maneuverable (thruster sway).
- Maintain battle damage state (scorched hull, smoke).
- Ensure visibility of firing positions despite smoke.
- Window frame context consistent with observer POV from previous beats.

# Repair Notes
- Correct the focus from towing/salvage to active engagement/realignment.
- Ensure ship rotation mechanism or thruster sway is visible.
- Avoid anatomy errors on Martian figures operating equipment.
- Maintain continuity with previous beats regarding fire intensity and damage.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
