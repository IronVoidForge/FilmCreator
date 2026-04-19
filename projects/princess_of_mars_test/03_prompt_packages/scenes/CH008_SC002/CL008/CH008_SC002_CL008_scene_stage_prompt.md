# Title
CH008_SC002 CL008 Scene Stage Prompt

# ID
CH008_SC002_CL008_scene_stage_prompt

# Purpose
Depict the fleet ships swinging broadside to maximize firepower and reposition, focusing on crew members moving to new firing positions and weapons being realigned within a damaged gray airship hull. Establish the transition from staggered formation to aligned broadside with visible rotation mechanism sway.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Medium shot of Martian Fleet Crews inside a damaged gray airship hull. Crew members huddled behind ship structures, shifting for cover while moving to new firing positions. Weapons elevated and realigned. Ship rotation mechanism visible with slight sway on damaged thrusters. Smoke density increasing from hull fires. Hull damage visible (scorched metal). Banners partially dissolved. Daylight transitioning to fire glow.

# Negative Prompt
No towing machinery, no intact hull sections remaining, no additional airships in frame, no human faces other than crew members, no green skin on Martians inconsistent with character index, no daylight without fire glow transition, no distorted weapons or rotation mechanism.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5.0
- required_refs: Ship rotation mechanism visible, crew realignment in progress, hull damage consistent with previous shots
- optional_refs: Window frame obstruction (if applicable to scene context), smoke density increasing
- visible_character_assets: Crew members moving to new firing positions; Green Martians operating weapons
- look_continuity_policy: parallel to wide shot for coverage
- intended_lighting_change: daylight transitioning to fire glow
- composition_type: Medium/POV
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: slight sway on damaged thrusters
- dependency_policy: parallel to wide shot for coverage
- auto_advance_policy: insert crew adjusting angles if movement erratic
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: match cut to rotation mechanism detail
- consistency_assist_method: 
- anatomy_repair_policy: apply repair policy for green skin and muscular build
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- beat_index: BT003

# Continuity Notes
- Ensure ship is swinging broadside to maximize firepower. Crew movement must align with new firing angles. Smoke density should increase from hull fires. Hull damage must be consistent with previous shots (scorched metal, banners dissolved). Rotation mechanism sway should be visible on damaged thrusters.

# Repair Notes
- If hull damage visibility is low, increase scorched metal coverage on ship structures. If green skin is distorted, apply repair policy for consistent muscular build and ornaments. If fire intensity is low, increase flame coverage on missile impact points.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
