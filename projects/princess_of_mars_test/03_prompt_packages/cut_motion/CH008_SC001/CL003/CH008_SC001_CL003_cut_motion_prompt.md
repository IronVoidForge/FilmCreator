# Title
CH008_SC001 CL003 Cut Motion Prompt

# ID
CH008_SC001_CL003_cut_motion_prompt

# Purpose
Capture the arrival of enemy airships from the valley view. Focus on camera tracking motion and ship entry while maintaining keyframe lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Static hold then track twenty gray airships entering from horizon moving toward camera and valley center, banners on stem and stern visible, glowing devices on prow clearly seen, sky environment established, wide shot exterior valley view from window composition, subtle camera movement indicating forward motion across sky plane.

# Negative Prompt
morphing ships, extra limbs, flickering signal, wrong color palette, blurry text, distorted background, inconsistent lighting, static image, low resolution, human faces in ship, wrong banners, missing glowing devices.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: twenty_gray_airships_sailing_toward_valley, banners_on_ships, glowing_devices_on_ships
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide_shot_exterior_valley_view_from_window
- continuity_mode: insert
- starting_keyframe_strategy: static_clear_valley_view_no_ships_visible_yet
- dependency_policy: follows_CL002_directly
- auto_advance_policy: none
- fallback_strategy: cut_to_pov_tracking_ships_if_scale_issue
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve keyframe lighting and grade by default. Focus on visible motion, camera behavior, and environment change. Ensure airships enter frame from horizon moving toward camera/valley center. Maintain banner and device visibility without distortion.

# Repair Notes
- Ensure ship consistency with previous clip. Maintain banner/device visibility without distortion. Correct any anatomy drift during entry sequence.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
