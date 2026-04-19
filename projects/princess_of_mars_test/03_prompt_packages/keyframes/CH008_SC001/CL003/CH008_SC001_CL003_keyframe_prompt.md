# Title
CH008_SC001 CL003 Keyframe Prompt

# ID
CH008_SC001_CL003_keyframe_prompt

# Purpose
Capture the protagonist's facial reaction to an overhead command signal during a sudden halt of a procession. Freeze the moment of emotional shift from anticipation to urgency.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Close-up portrait of a human male with determined expression transitioning to shock. Overhead vertical signal visible in upper frame. Dusty open valley background. Natural daylight with high contrast shadows. Cinematic composition. Medium close-up framing.

# Negative Prompt
Distorted face, extra limbs, blurry text, low resolution, cartoonish, oversaturated, wrong lighting, crowded background, modern clothing, weapons visible on protagonist.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: protagonist face_reaction, implied_command_signal_source
- look_continuity_policy: match_previous_clip_lighting
- intended_lighting_change: none
- composition_type: medium_close_up_reaction
- continuity_mode: cutaway
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
- Maintain lighting consistency with previous procession shots. Ensure command signal is visible in upper third without obscuring face. Freeze frame on initial reaction moment before full movement starts.

# Repair Notes
- If facial expression looks too neutral, increase intensity of shock or urgency. Ensure background remains open valley terrain, not city architecture.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
