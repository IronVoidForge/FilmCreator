# Title
SC001 CL001 Cut Motion Prompt

# ID
SC001_CL001_cut_motion_prompt

# Purpose
Fill in the stage intent for cut motion generation between keyframes.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide establishing shot transitions to medium tracking forward movement. Narrator walks through deserted city streets with procession garments intact. Woola follows close behind at heel. Camera tracks subject smoothly into building entrance interior depth. Lighting remains consistent with exterior sunlight gleaming on surroundings. Environment shifts from open valley view to corridor space.

# Negative Prompt
morphing artifacts, flickering lighting, wrong anatomy, extra characters, sudden crowd appearance, incorrect camera angle, distorted background, inconsistent grade, blurry motion, static frame, low resolution

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, Scene SC001 breakdown
- optional_refs: Procession garment details, plaza distance markers
- visible_character_assets: narrator, woola
- look_continuity_policy: preserve_keyframe_lighting
- intended_lighting_change: none
- composition_type: wide_establishing_to_medium_tracking
- continuity_mode: cut
- starting_keyframe_strategy: establish_exterior_city_context_first
- dependency_policy: none_standalone_opening_shot
- auto_advance_policy: standard
- fallback_strategy: use_static_wide_if_tracking_unavailable
- consistency_assist_policy: enabled
- consistency_assist_method: interval_frames
- anatomy_repair_policy: enabled
- consistency_targets: narrator_position, woola_position
- style_profile: epic_narrative
- batch_role: opening_sequence
- fix_of: none

# Continuity Notes
- Preserve keyframe lighting and grade by default.
- Focus on visible motion, camera behavior, and environment change.
- Ensure narrator moves forward smoothly into interior.
- Maintain procession garment integrity throughout transition.
- Keep Woola close behind at heel throughout transition.

# Repair Notes
- Fix any morphing artifacts during wide-to-medium transition.
- Ensure lighting consistency between exterior and interior entrance.
- Correct anatomy if narrator or Woola distort during movement.
- Maintain environment state (deserted streets) without introducing new crowds prematurely.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
