# Title
CH008_SC003 CL002 Cut Motion Prompt

# ID
CH008_SC003_CL002_cut_motion_prompt

# Purpose
Bridge the wide tracking shot of the drifting vessel with the boarding action by capturing the green warriors' smooth approach toward the ship perimeter while maintaining continuity of the ship's drift path and environmental lighting.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
green skinned warriors approaching gray low profile vessel drifting southeast banners stem stern glowing devices prow medium shot Martian valley background smooth motion camera tracking drift path

# Negative Prompt
morphing faces extra limbs wrong skin color blue static image flickering text artifacts blurry details sudden jumps lighting shifts

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Green Warriors (approaching), Martians (elevated)
- look_continuity_policy: preserve keyframe lighting and grade
- intended_lighting_change: none
- composition_type: medium shot
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: open on warrior eyeline tracking ship
- dependency_policy: depends on CL001
- auto_advance_policy: smooth approach
- fallback_strategy: insert if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: cinematic sci-fi
- batch_role: 
- fix_of: 

# Continuity Notes
- Ship drift vector must match CL001 southeast trajectory.
- Warrior eyelines track ship movement across horizon without snapping.
- Background valley architecture remains consistent with keyframe grade.

# Repair Notes
- If warriors appear static, inject subtle motion tags for approach.
- If lighting shifts, revert to keyframe style profile immediately.
- Ensure no sudden jumps in ship position relative to camera frame.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
