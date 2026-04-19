# Title
CH008_SC001 CL004 Fix 01 Prompt

# ID
CH008_SC001_CL004_fix_01_prompt

# Purpose
Generate corrected still for CL004 capturing human male protagonist growing concern while observing air craft arrival from window position, ensuring facial expression continuity and window frame edge preservation while fixing local generation issues. Maintain close-up composition with upper torso framing and valley background stability.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
close-up face view human male standing at window frame edge upper torso visible growing concern on facial expression window frame partial left side valley floor beyond hills distant horizon daylight atmospheric lighting smoke from fire missile impact flames subtle posture shift reflecting emotional change minimal movement sharp anatomy clear composition wide angle cinematic with tactical atmosphere

# Negative Prompt
blurry distorted anatomy wrong facial expression missing window frame proper nouns named characters individual names text artifacts low resolution noise flickering incorrect color palette inconsistent lighting motion blur excessive movement

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: john_carter_upper_torso_face_window_frame_partial
- look_continuity_policy: preserve_close_up_composition_with_window_framing
- intended_lighting_change: consistent_with_BT001_reaction_clip
- composition_type: close_up_face_with_window_edge
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
- dependency_policy: none
- auto_advance_policy: none
- fallback_strategy: maintain_original_composition_with_anatomy_fixes
- consistency_assist_policy: preserve_lighting_and_architecture_continuity
- consistency_assist_method: reference_previous_clip_lighting_patterns
- anatomy_repair_policy: correct_facial_expression_and_window_frame_distortions
- consistency_targets: facial_concern_visibility_and_window_frame_position
- style_profile: close_up_cinematic_with_emotional_atmosphere
- batch_role: still_fix_iteration_one
- fix_of: CL004_original_generation_issues
- image_1_ref: approved_still_base_close_up_face_with_window_edge
- image_2_ref: secondary_reference_for_lighting_continuity

# Continuity Notes
- John Carter facial expression must show growing concern matching emotional shift from curiosity to anticipation.
- Window frame edge must remain visible on left side of composition for spatial continuity.
- Valley floor background must stay stable for geographic consistency across clips.
- Lighting must match BT001 reaction sequence with daylight and smoke/fire effects.
- Upper torso framing must be preserved without cutting off key facial features.
- Minimal movement should reflect subtle posture shift rather than full body motion.

# Repair Notes
- Correct any facial expression distortions that don't show growing concern properly.
- Fix window frame edge visibility if partially missing or incorrectly positioned.
- Preserve valley background stability without introducing new geographic elements.
- Ensure lighting consistency with previous clips BT001 reaction sequence.
- Remove any proper nouns or named character references from prompt text.
- Verify upper torso framing doesn't cut off key facial features.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
