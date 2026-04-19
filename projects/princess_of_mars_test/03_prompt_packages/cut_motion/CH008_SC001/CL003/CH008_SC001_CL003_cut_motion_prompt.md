# Title
CH008_SC001 CL003 Cut Motion Prompt

# ID
CH008_SC001_CL003_cut_motion_prompt

# Purpose
Capture the sudden retreat order reaction upon entering open ground. Focus on observer emotional shift from anticipation to urgency while maintaining keyframe lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Static observer face reacting to overhead command signal, sudden stop on motion, emotional shift visible in eyes, medium close up composition, open valley terrain background, preserved lighting grade, subtle camera shake indicating urgency.

# Negative Prompt
morphing face, extra limbs, flickering signal, wrong color palette, blurry text, distorted background, inconsistent lighting, static image, low resolution

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Carter face_reaction, implied_command_signal_source
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_close_up_reaction
- continuity_mode: cutaway
- starting_keyframe_strategy: static_on_carter_face_with_command_signal_visible_above
- dependency_policy: independent_can_follow_any_previous_clip
- auto_advance_policy: 
- fallback_strategy: cut_to_wide_halt_if_reaction_misread
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve keyframe lighting and grade by default. Focus on visible motion, camera behavior, and environment change. Ensure command signal remains visible above terrain.

# Repair Notes
- Ensure observer face consistency with previous clip. Maintain signal visibility without distortion. Correct any anatomy drift during emotional shift.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
