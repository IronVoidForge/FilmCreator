# Title
CH008_SC001 CL004 Fix 01 Prompt

# ID
CH008_SC001_CL004_fix_01_prompt

# Purpose
Generate a corrected still for CL004 that captures the arrival of enemy airships and the narrator's observation from the window, ensuring continuity with the melting Martians beat. Preserve the wide composition and lighting while fixing local generation issues.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
interior room view narrator standing at window observing valley floor twenty gray low-profile airships sailing toward valley banners on stem stern glowing devices on prow urban structures bordering left and right sides tense mood anticipation turning to fear atmospheric lighting consistent with previous clips

# Negative Prompt
blurry distorted anatomy wrong movement direction missing characters inconsistent lighting text artifacts low resolution noise flickering incorrect color palette

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Narrator window_position, Martians melting_state, Airships entering_valley
- look_continuity_policy: wide_establishing
- intended_lighting_change: atmospheric_consistency
- composition_type: wide_establishing
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static_opening_with_full_procession_visible_before_movement_change
- dependency_policy: dependent_on_CL003_reaction_clip_first
- auto_advance_policy: none
- fallback_strategy: retry_with_refined_prompt
- consistency_assist_policy: enabled
- consistency_assist_method: prompt_reinforcement
- anatomy_repair_policy: strict
- consistency_targets: ship_banners_device_visibility, narrator_eyeline_alignment
- style_profile: cinematic_martian
- batch_role: fix_01
- fix_of: CH008_SC001_CL004_KF01_v001.png

# Continuity Notes
- Martians must have melted into mist before airships enter frame.
- Airships must move steadily toward valley center.
- Narrator remains stationary at window.
- City architecture frames the shot.

# Repair Notes
- Correct any anatomy distortions in narrator or ship details.
- Fix movement artifacts that suggest incorrect direction (ensure steady approach).
- Preserve lighting consistency with previous clips.
- Verify command signal visibility matches elevated position description.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
