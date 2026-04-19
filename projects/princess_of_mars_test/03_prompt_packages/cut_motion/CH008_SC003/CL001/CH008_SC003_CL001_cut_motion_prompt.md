# Title
CH008_SC003 CL001 Cut Motion Prompt

# ID
CH008_SC003_CL001_cut_motion_prompt

# Purpose
Establish ship trajectory and unmanned state via smooth tracking follow drift path, preserving lighting and grade continuity for wide shot composition.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
wide tracking shot of gray low-profile vessel drifting southeast on water surface, banners visible on stem and stern, glowing devices on prow, distant green warriors observing from elevated positions, open valley background, consistent cinematic lighting, smooth camera movement following ship drift vector, unmanned state, no crew visible, urban Martian architecture environment.

# Negative Prompt
static camera, human crew inside vessel, distorted ship hull, sudden camera jumps, inconsistent color palette, bright daylight mismatch, close-up of interior, wrong weather conditions, static lighting change, floating debris without wind effect.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Green Warriors (distant), Martians (elevated observation)
- look_continuity_policy: preserve lighting and grade by default
- intended_lighting_change: none
- composition_type: wide tracking shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on ship drift vector from distance
- dependency_policy: none
- auto_advance_policy: 
- fallback_strategy: insert if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: Martian City Urban Architecture
- batch_role: cut_motion
- fix_of: 

# Continuity Notes
- Capture ship trajectory consistency from south position to southeast drift vector.
- Maintain unmanned state throughout clip duration.
- Ensure distant green warriors remain elevated and do not enter frame abruptly.
- Preserve cinematic lighting and grade consistent with approved keyframe.
- Avoid sudden shifts in camera angle or focal length during tracking motion.

# Repair Notes
- If ship shape distorts, revert to low-profile vessel geometry.
- If crew becomes visible inside hull, mask interior details to maintain unmanned state.
- If lighting flickers, stabilize exposure and color temperature to match scene baseline.
- If motion is jerky, smooth camera tracking path along drift vector.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
