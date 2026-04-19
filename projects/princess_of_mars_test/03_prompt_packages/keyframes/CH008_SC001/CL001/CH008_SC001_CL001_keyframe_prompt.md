# Title
CH008_SC001 CL001 Keyframe Prompt

# ID
CH008_SC001_CL001_keyframe_prompt

# Purpose
Establish human protagonist curiosity at upper floor window as gray airships descend toward city. Start State: Observer standing at window frame with initial wonder visible on face. End State: Slight posture shift reflecting growing concern about incoming vessels.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Close-up portrait of human male observer at window frame edge, upper torso visible, face showing initial curiosity and wonder. Partial window frame on left side grounds viewer in location. Background valley floor stable with distant hills beyond creating depth. Daylight illumination with soft shadows. Cinematic composition, detailed facial textures, atmospheric red planet environment, dramatic lighting contrast between interior and exterior view.

# Negative Prompt
blurry, low resolution, modern clothing, extra characters, distorted faces, wrong color palette (blue sky instead of red atmosphere), static image without subtle motion cues, crowded composition, text, watermark, deformed limbs, bright harsh daylight, green-tinted lighting, urban transit vehicles, civilian structures, blue-tinted interior lighting, facial expression showing anger or sadness, window frame missing from left edge.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: human male observer (upper torso, face)
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: daylight_with_interior_contrast
- composition_type: close_up_face_with_window_frame
- continuity_mode: independent_no_prerequisites
- starting_keyframe_strategy: static_hold
- dependency_policy: standalone_tactical_context
- auto_advance_policy: none
- fallback_strategy: insert_alternate_close_angle_if_needed
- consistency_assist_policy: maintain_observer_position_and_expression_progression
- consistency_assist_method: visual_reference_matching
- anatomy_repair_policy: fix_distorted_facial_features
- consistency_targets: window_frame_visibility_observer_posture
- style_profile: cinematic_compositional
- batch_role: establishing_character_perspective
- fix_of: none
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain observer position at upper floor window frame throughout sequence.
- Keep facial expression progression from curiosity to growing concern consistent.
- Ensure window frame edge visible on left side in all frames.
- Preserve valley and hills background stability for continuity tracking.
- Match daylight illumination with interior contrast across shots.
- Red planet atmosphere must remain consistent throughout all keyframes.

# Repair Notes
- Fix any facial expression distortions showing inappropriate emotions.
- Ensure window frame edge appears consistently on left side.
- Correct color grading to maintain red planet atmosphere throughout.
- Verify observer posture shift reflects emotional progression appropriately.
- Check background valley/hills remain stable across consecutive frames.
- Address any lighting inconsistencies between interior and exterior view.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
