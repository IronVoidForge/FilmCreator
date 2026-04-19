# Title
CH008_SC001 CL003 Keyframe Prompt

# ID
CH008_SC001_CL003_keyframe_prompt

# Purpose
Capture the visible state of green-skinned warriors at a doorway threshold, beginning to melt into interior shadows. Freeze the moment of vanishing action and retreat timing constraint.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Close-up view of dark doorway threshold, green-skinned warriors standing at edge, figures melting into interior darkness, vanishing motion active, high contrast between exterior light and interior shadows, close-up framing on doorway frame axis.

# Negative Prompt
Human skin tone, static pose, fully visible faces, bright interior lighting, crowded scene, distorted anatomy, blurry text, low resolution, modern clothing, weapons visible on protagonist.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: green-skinned warriors, interior shadows
- look_continuity_policy: match_previous_clip_lighting
- intended_lighting_change: none
- composition_type: close-up_doorway_threshold
- continuity_mode: insert
- starting_keyframe_strategy: static_on_face_with_signal_visible
- dependency_policy: independent_can_follow_any_previous_clip
- auto_advance_policy: manual_review_required
- fallback_strategy: cut_to_wide_halt_if_reaction_misread
- consistency_assist_policy: enabled
- consistency_assist_method: reference_alignment
- anatomy_repair_policy: strict
- consistency_targets: facial_expression
- style_profile: cinematic_realism
- batch_role: keyframe_generation
- fix_of: none
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Focus on doorway threshold and vanishing action. Ensure shadow swallowing figures is visible. Maintain lighting consistency with exterior daylight. Freeze frame on initial retreat moment before full movement starts.

# Repair Notes
- If figures look static, increase intensity of melting motion. Ensure background remains open valley terrain or building exterior, not city architecture interior. Verify green skin tone is consistent.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
