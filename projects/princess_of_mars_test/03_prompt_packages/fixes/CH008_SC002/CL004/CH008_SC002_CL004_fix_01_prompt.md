# Title
CH008_SC002 CL004 Fix 01 Prompt

# ID
CH008_SC002_CL004_fix_01_prompt

# Purpose
Fill in the stage intent here. Corrective still-generation for deck crew firing operations during enemy ship swing. Preserve composition and look while fixing local issues. Assume image_1 is approved still base and image_2 is secondary reference when needed.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Gray low-profile vessel deck crew firing smoke trails banners dissolving in flame ship swinging broadside glowing devices on prow valley battle zone background medium shot of crew positioned on deck for firing open on crew already in firing positions weapons active during swing

# Negative Prompt
blurry distorted anatomy extra limbs text watermark low resolution inconsistent lighting wrong perspective floating elements missing details

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: Deck crew close-ups coverage families
- visible_character_assets: Enemy Fleet (crew on deck)
- look_continuity_policy: Soft dependency on CL003
- intended_lighting_change: None
- composition_type: Medium shot of crew positioned on deck for firing
- continuity_mode: Close-up action detail work on deck crew operations
- starting_keyframe_strategy: Open on crew already in firing positions, weapons active
- dependency_policy: Soft dependency on CL003; can follow ship swing arc
- auto_advance_policy: None
- fallback_strategy: Use insert if need to emphasize crew action timing
- consistency_assist_policy: None
- consistency_assist_method: None
- anatomy_repair_policy: Preserve composition and look while fixing local issues
- consistency_targets: Ship swing arc completion, bullet drops at explosion points
- style_profile: Klein Distilled
- batch_role: still_fix
- fix_of: CL004

# Continuity Notes
- Capture the continuity rules for this stage. Ship swings 360 degrees from broadside, crew firing active during swing, smoke trails visible from firing points, banners showing flame damage at contact points, valley battle zone background consistent with previous shots.

# Repair Notes
- Capture any repair or corrective guidance for this stage. Fix local issues while preserving look. Ensure ship movement arc is smooth and crew actions are synchronized with swing timing. Maintain lighting consistency with approved still base image_1.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
