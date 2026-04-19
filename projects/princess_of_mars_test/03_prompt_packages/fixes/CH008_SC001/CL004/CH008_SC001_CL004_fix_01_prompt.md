# Title
CH008_SC001 CL004 Fix 01 Prompt

# ID
CH008_SC001_CL004_fix_01_prompt

# Purpose
Generate a corrected still for CL004 that captures the abrupt halt and reverse movement of the procession in open ground, ensuring the command signal is visible and maintaining continuity with the retreat order beat. Preserve the wide composition and lighting while fixing local generation issues.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
wide angle view green-clad warriors marching formation stopping suddenly open terrain valley floor main observer standing rear of column high vantage point commander issuing order visible above horizon urban structures bordering left and right sides tense mood anticipation turning to fear atmospheric lighting consistent with previous clips

# Negative Prompt
blurry distorted anatomy wrong movement direction missing characters inconsistent lighting text artifacts low resolution noise flickering incorrect color palette

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Carter rear_position, Warriors central_column, implied_commanders_elevated
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide_halt_reverse
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static_opening_with_full_procession_visible_before_movement_change
- dependency_policy: dependent_on_CL003_reaction_clip_first
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
- Procession must halt abruptly upon entering open ground.
- Command signal source must be visible from elevated position.
- Maintain formation integrity before reverse movement begins.
- Ensure city architecture frames the left and right sides of the shot.

# Repair Notes
- Correct any anatomy distortions in warrior figures or protagonist.
- Fix movement artifacts that suggest incorrect direction (ensure halt is clear).
- Preserve lighting consistency with previous clips (BT002 reaction).
- Verify command signal visibility matches elevated position description.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
