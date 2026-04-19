# Title
CH008_SC002 CL001 Scene Stage Prompt

# ID
CH008_SC002_CL001_scene_stage_prompt

# Purpose
Depict the engagement between Green Warriors on city buildings and Air Fleet in valley, establishing scale of threat through window perspective.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Window frame foreground obstruction, upper floor balcony background, twenty gray airships entering from distance across valley, daylight lighting, Green Warriors positioned on ridge/upper floors firing volley, banners fluttering in wind, smoke from previous impacts visible on valley floor.

# Negative Prompt
crew visible on ship hull before damage sequence, significant damage to ships before intended beat, proper nouns, model render artifacts, John Carter face visible (unless specified), Sola/Woola visible.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL001
- duration_seconds: 5.0
- required_refs: Window frame, twenty gray airships, valley floor
- optional_refs: Martians
- visible_character_assets: Green Warriors
- look_continuity_policy: static_hold
- intended_lighting_change: daylight
- composition_type: POV/Wide
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
- dependency_policy: linear_sequence
- auto_advance_policy: none
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: none
- consistency_assist_method: none
- anatomy_repair_policy: none
- consistency_targets: none
- style_profile: authoring.scene_stage
- batch_role: planning
- fix_of: none

# Continuity Notes
- Ship count must remain twenty until damage sequence.
- No crew visible on ship hull during this beat.
- Daylight lighting consistent with valley setting.
- Warriors firing from upper floors/windows.

# Repair Notes
- Ensure no significant damage to ships before intended beat.
- Verify window frame obstruction remains intact in foreground.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
