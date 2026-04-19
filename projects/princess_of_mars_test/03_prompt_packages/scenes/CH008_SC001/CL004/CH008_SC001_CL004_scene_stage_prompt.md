# Title
CH008_SC001 CL004 Scene Stage Prompt

# ID
CH008_SC001_CL004_scene_stage_prompt

# Purpose
Establish the visual staging for the airship arrival observation from the window (CL004). This shot captures the full procession of gray airships entering the valley view as observed by the narrator, following the dissolution of the Martians. It serves as a wide-angle reframe of the same moment initiated by BT003's reaction close-up, ensuring continuity with the scene breakdown where Martians melt into buildings within three minutes.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Interior window POV, Narrator observing from elevated position, Martians dissolving into mist below within room space, twenty gray airships sailing toward valley center, banners on stem/stern visible, glowing devices on prow clearly seen, red sky lighting, high stakes warfare atmosphere, detailed armor and weaponry, wide angle composition.

# Negative Prompt
deformed limbs, extra fingers, static shot, blurry text, low resolution, blue sky, green sky, inconsistent character count, wrong facial expressions, motion blur artifacts, distorted architecture, missing command signal source, incorrect color palette for Mars environment, marching through city plaza, solid martian presence without dissolve.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Narrator window_position, Martians dissolving_state, Airships entering_valley
- look_continuity_policy: wide_entering_observation
- intended_lighting_change: red sky lighting
- composition_type: wide_window_view
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
- Capture the continuity rules for this stage. Martians dissolve into mist within three minutes before disappearing from room space. Character placement consistency is critical (Narrator at window). The airship entry must be synchronized across the wide frame with banners and glowing devices visible. Environmental context shifts from built architecture to natural valley terrain as ships enter.

# Repair Notes
- Address potential issues like motion blur consistency during airship entry, ensuring character deformation does not occur during the dissolve, verifying that the "open ground" environment is distinct from "city plaza" in terms of lighting and texture. Ensure the command signal source is visible or implied correctly for continuity with CL003.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
