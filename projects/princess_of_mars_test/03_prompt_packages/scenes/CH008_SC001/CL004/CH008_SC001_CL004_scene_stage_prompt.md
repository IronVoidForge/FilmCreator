# Title
CH008_SC001 CL004 Scene Stage Prompt

# ID
CH008_SC001_CL004_scene_stage_prompt

# Purpose
Establish the visual staging for the retreat order clip (CL004). This shot captures the full procession halting and reversing direction upon entering open ground, reacting to the command signal. It serves as a wide-angle reframe of the same moment initiated by CL003's reaction close-up.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green Martians in formation marching through city plaza into open valley, Carter positioned at rear of procession, gray-painted airships visible on hill crest in distance, sudden halt motion followed by coordinated reverse movement toward city boundary, wide angle composition, high stakes warfare atmosphere, red sky lighting, detailed armor and weaponry.

# Negative Prompt
deformed limbs, extra fingers, static shot, blurry text, low resolution, blue sky, green sky, inconsistent character count, wrong facial expressions, motion blur artifacts, distorted architecture, missing command signal source, incorrect color palette for Mars environment.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Carter rear_position, Warriors central_column, implied_commanders_elevated
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide_halt_reverse
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static_opening_with_full_procession_visible_before_movement_change
- dependency_policy: dependent_on_CL003_reaction_clip_first
- auto_advance_policy: 
- fallback_strategy: cut_to_high_angle_command_source_if_needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Capture the continuity rules for this stage. Procession movement must transition smoothly from city plaza to open ground. Character placement consistency is critical (Carter at rear). The halt and reverse motion must be synchronized across the wide frame. Environmental context shifts from built architecture to natural valley terrain.

# Repair Notes
- Address potential issues like motion blur consistency during rapid pivot, ensuring character deformation does not occur during the reverse movement, verifying that the "open ground" environment is distinct from "city plaza" in terms of lighting and texture. Ensure the command signal source is visible or implied correctly for continuity with CL003.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
