# Title
CH008_SC005 CL002 Fix 01 Prompt

# ID
CH008_SC005_CL002_fix_01_prompt

# Purpose
Preserve medium two shot over-the-shoulder composition from Carter's perspective while fixing local quality issues in approved base frame. Maintain daylight with smoke and fire effects continuity. Ensure character placement matches approved reference without altering spatial context established in CL001.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Human male shoulder profile in foreground left, slender female companion approaching diagonally from background right, exterior corridor entrance threshold, daylight illumination with smoke haze and distant fire glow, open ground plaza beyond city buildings, valley floor visible in background, hills beyond horizon, medium two shot framing, over-the-shoulder perspective, urgent movement atmosphere, crimson cheeks on approaching figure, coal black hair caught loosely into strange coiffure, green skin warriors firing from upper floors windows, gray painted air craft drifting southeast, open plains and distant hills environment

# Negative Prompt
close up shot, wide establishing shot, interior room setting, night darkness, artificial lighting, static pose, disconnected characters, missing smoke effects, absent fire glow, wrong character placement, distorted anatomy, inconsistent color grading, blurred details, overexposed highlights, underexposed shadows, mismatched spatial context, reversed eyeline direction

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL002
- duration_seconds: 5
- required_refs: image_1
- optional_refs: image_2
- visible_character_assets: Carter shoulder profile, Sola full face upper body
- look_continuity_policy: preserve approved base frame composition and lighting
- intended_lighting_change: none
- composition_type: medium two shot over-the-shoulder
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: shoulder of Carter in foreground left, Sola approaching from background right
- dependency_policy: depends on CL001 establishing spatial context
- auto_advance_policy: standard
- fallback_strategy: shift to medium shot with both characters fully visible if shoulder framing unclear
- consistency_assist_policy: enabled
- consistency_assist_method: anatomy and lighting repair
- anatomy_repair_policy: maintain character proportions while fixing local issues
- consistency_targets: approved base frame image_1, secondary reference image_2
- style_profile: action-oriented awe-inspiring tense combat sequences
- batch_role: still_fix
- fix_of: CL002 still quality and continuity alignment

# Continuity Notes
- Capture reframe_same_moment continuity mode with medium two shot over-the-shoulder composition from Carter's perspective. Maintain shoulder of Carter in foreground left, Sola approaching from background right positioning. Preserve daylight with smoke and fire effects continuity. Keep exterior corridor setting with open ground plaza beyond city buildings. Ensure spatial context matches CL001 establishing shot without altering established geography.

# Repair Notes
- Fix local quality issues while maintaining composition and look from approved base frame image_1. Correct any anatomy inconsistencies without changing character proportions or placement. Adjust lighting to match daylight with smoke haze and distant fire glow continuity. Ensure visible character assets show Carter shoulder profile and Sola full face upper body as specified. Preserve urgent movement atmosphere and exterior corridor entrance threshold setting.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
