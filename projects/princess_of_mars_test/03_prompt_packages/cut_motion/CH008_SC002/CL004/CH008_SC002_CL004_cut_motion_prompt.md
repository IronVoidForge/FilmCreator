# Title
CH008_SC002 CL004 Cut Motion Prompt

# ID
CH008_SC002_CL004_cut_motion_prompt

# Purpose
Establish unmanned ship as new opportunity through medium shots of vulnerability, transitioning camera from wide valley view to focused ship perspective while preserving daylight illumination and keyframe grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
camera zooms in from wide valley view to medium ship perspective, green warriors at window frames observe unmanned vessel, hull remains intact but vulnerable, boarding equipment appears near deck edge, daylight illumination preserved, smoke rises from damaged ships nearby, scene shifts from battle tension to salvage opportunity, martians begin positioning for boarding action

# Negative Prompt
crew visible on deck, extra limbs, flickering lights, distorted ship structure, sudden lighting changes, wrong number of airships, blurry focus, morphing characters, excessive fire before intended moment, dark shadows overriding daylight grade, unstable camera movement

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL004
- duration_seconds: 5.0
- required_refs: Ship hull intact but vulnerable, no crew visible on deck, boarding equipment being prepared
- optional_refs: Window frame
- visible_character_assets: Martians at windows observing unmanned ship, Narrator noting opportunity
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: None
- composition_type: Wide/Medium
- continuity_mode: cutaway
- starting_keyframe_strategy: zoom_in
- dependency_policy: linear_sequence
- auto_advance_policy: standard
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: enabled
- consistency_assist_method: frame_reference
- anatomy_repair_policy: strict
- consistency_targets: ship structure, character count, lighting grade
- style_profile: cinematic_warfare
- batch_role: interval
- fix_of: BT004

# Continuity Notes
- Ship must remain unmanned with no visible crew activity on deck throughout motion sequence.
- Green warriors positioned at building windows observing the vessel without entering frame excessively.
- Daylight illumination must be maintained consistent with approved keyframe lighting and grade.
- Camera movement follows zoom_in strategy from wide valley view to medium ship perspective.
- Loot items not yet visible in this beat, focus remains on ship vulnerability and boarding preparation.

# Repair Notes
- If ship structure distorts during zoom, revert to stable hull geometry reference.
- Ensure lighting does not shift to fire illumination prematurely; salvage ritual begins after loot collection.
- Correct any extra limbs or morphing characters on green warriors by enforcing anatomy repair policy.
- Maintain continuity of window frame obstruction in foreground if visible in composition.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
