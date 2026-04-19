# Title
CH008_SC001 CL004 Cut Motion Prompt

# ID
CH008_SC001_CL004_cut_motion_prompt

# Purpose
Establish sudden halt and reverse movement of procession on open ground.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide shot green-clad warriors halting abruptly on valley floor. Camera holds steady then pans slightly to follow reverse movement toward city skyline. Warriors execute synchronized turn in place. Dust kicks up from boots during pivot. Lighting remains consistent with previous keyframe daylight high contrast. Background shows distant hills and approaching airship fleet silhouette.

# Negative Prompt
morphing faces extra limbs sudden zoom darkening or brightening exposure floating objects incorrect marching direction blurry text distorted anatomy static image low resolution color bleeding glitchy transitions.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: protagonist rear_position, green-clad warriors central_column
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide_halt_reverse
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: 
- dependency_policy: 
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Preserve keyframe lighting and grade by default. Focus on visible motion, camera behavior, and environment change. Ensure procession direction reverses smoothly without snapping. Maintain character count consistency.

# Repair Notes
- If reverse movement is too slow, increase pivot speed. If lighting shifts, force continuity with previous frame. If anatomy distorts during turn, apply repair policy.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
