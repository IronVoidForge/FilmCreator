# Title
CH008_SC002 CL001 Cut Motion Prompt

# ID
CH008_SC002_CL001_cut_motion_prompt

# Purpose
Maintain static elevated perspective from building window, focus on minimal warrior movement and firing mechanics, preserve keyframe lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green warriors positioned in building windows, weapons loaded and ready, slight weapon adjustment before discharge, smoke begins to rise from impact points below, static camera hold, downward line of sight to valley floor, urban Martian architecture background.

# Negative Prompt
Camera movement, zooming, panning, lighting changes, grade shifts, blurry details, distorted anatomy, extra characters, flying objects not related to scene.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Scene breakdown for building window positioning
- visible_character_assets: Green Warriors, Weapons
- look_continuity_policy: Preserve keyframe lighting and grade
- intended_lighting_change: None
- composition_type: Wide shot from building window looking down at valley floor
- continuity_mode: Static elevated perspective with minimal camera movement
- starting_keyframe_strategy: Open on warriors positioned in windows, weapons visible and loaded
- dependency_policy: No hard dependencies; can stand alone as opening beat
- auto_advance_policy: None
- fallback_strategy: Use reframe_same_moment if timing adjustment needed
- consistency_assist_policy: None
- consistency_assist_method: None
- anatomy_repair_policy: None
- consistency_targets: Window height, Eyeline angle, Target area
- style_profile: Martian city aesthetic
- batch_role: Opening conflict establishment
- fix_of: None

# Continuity Notes
- Preserve keyframe lighting and grade by default. Focus on visible motion (weapon adjustment, smoke rise) and camera behavior (static hold). Environment change is minimal (valley floor reaction).

# Repair Notes
- Ensure warrior anatomy remains consistent with green-skinned warriors. Verify weapon discharge timing matches interval beats.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
