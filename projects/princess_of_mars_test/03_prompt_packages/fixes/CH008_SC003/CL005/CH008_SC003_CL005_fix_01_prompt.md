# Title
CH008_SC003 CL005 Fix 01 Prompt

# ID
CH008_SC003_CL005_fix_01_prompt

# Purpose
Fix local details in close-up item removal shot while preserving Martians hand anatomy and ship interior continuity.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Martian green-skinned hands removing food containers from disabled ship deck, dead sailors lying stationary in background, ship interior dim lighting, specific items like water carboys being dumped, ornate Martian jewelry visible on wrist, smoke haze from burning ship distant, high detail texture on skin and metal.

# Negative Prompt
human hands, extra fingers, distorted anatomy, bright sunlight, motion blur, inconsistent lighting, floating objects, wrong skin tone, missing ornaments, blurry background, low resolution.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL005
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians hands, Dead Sailors
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: close-up
- continuity_mode: insert
- starting_keyframe_strategy: 
- dependency_policy: depends on CL004
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
- Track specific items removed (food containers, water carboys) for visual consistency with previous shots.
- Maintain Martian hand anatomy (green skin, distinct features) distinct from human hands.
- Keep background dead sailors stationary and consistent in pose.

# Repair Notes
- Ensure hands do not appear human or distorted during item removal action.
- Verify lighting matches the dim ship interior established in CL004.
- Correct any floating debris that does not match the drifting ship context.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
