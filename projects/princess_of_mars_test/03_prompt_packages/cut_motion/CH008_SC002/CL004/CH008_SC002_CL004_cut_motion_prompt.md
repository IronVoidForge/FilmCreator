# Title
CH008_SC002 CL004 Cut Motion Prompt

# ID
CH008_SC002_CL004_cut_motion_prompt

# Purpose
Fill in the stage intent for CL004 cut motion generation, focusing on deck crew firing operations during the enemy ship's swing arc while maintaining continuity with the approved opening frame and keyframe lighting.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
gray low-profile vessel deck crew firing operations weapons active ship swinging broadside smoke trails banners showing flame damage static medium shot slight pan following crew actions valley battle zone aerial space

# Negative Prompt
deformed hands extra fingers missing weapons still image no ship movement wrong color palette blurry details distorted anatomy floating objects inconsistent lighting

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md - Enemy Fleet Return Fire & Swing beat bundle
- optional_refs: Deck crew close-ups coverage families
- visible_character_assets: Enemy Fleet (crew on deck), Weapons active during swing
- look_continuity_policy: Soft dependency on CL003; can follow ship swing arc
- intended_lighting_change: Preserve keyframe lighting and grade by default
- composition_type: Medium shot of crew positioned on deck for firing
- continuity_mode: Close-up action detail work on deck crew operations
- starting_keyframe_strategy: Open on crew already in firing positions, weapons active
- dependency_policy: Soft dependency on CL003; can follow ship swing arc
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
- Capture the continuity rules for this stage. Ensure bullet drops at explosion points maintain timing and placement consistency. Track banner dissolving in flame for progressive damage tracking. Verify ship swing arc completion from broadside position. Maintain lighting stability with previous clip (CL003) to support soft dependency policy.

# Repair Notes
- Capture any repair or corrective guidance for this stage. Focus on anatomy consistency between crew members and ship structure. Ensure motion smoothness during the swing arc without jitter. Correct any lighting shifts that deviate from the approved keyframe grade. Maintain weapon activation state throughout the clip duration.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
