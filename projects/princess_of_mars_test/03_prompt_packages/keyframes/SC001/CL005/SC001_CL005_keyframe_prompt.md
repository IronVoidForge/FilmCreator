# Title
SC001 CL005 Keyframe Prompt

# ID
SC001_CL005_keyframe_prompt

# Purpose
Generate frozen still of narrator observing deserted valley from upper floor window during retreat sequence

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
narrator standing at upper floor window frame looking outward, deserted valley hills visible beyond glass, interior room walls visible, natural sunlight gleaming on devices, tense atmosphere, abandoned city streets below, hound resting nearby, female companion entering corridor in background, cinematic lighting, high detail

# Negative Prompt
blurry, distorted faces, extra limbs, text, watermark, low resolution, dark shadows, oversaturated colors, wrong perspective, floating objects, missing window frame, incorrect character count

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL005
- duration_seconds: 5
- required_refs: upper_floor_window_view
- optional_refs: building_interior_portal
- visible_character_assets: narrator,hound,female_companion
- look_continuity_policy: match_previous_clip_lighting_and_position
- intended_lighting_change: natural_sunlight_contrasting_interior_darkness
- composition_type: medium_shot_window_view
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: frozen_observation_point
- dependency_policy: independent_generation_with_ref_check
- auto_advance_policy: manual_review_required
- fallback_strategy: retry_with_higher_resolution_seed
- consistency_assist_policy: enabled_for_character_features
- consistency_assist_method: feature_matching
- anatomy_repair_policy: strict_enforcement
- consistency_targets: face_shape,hair_style,clothing_details
- style_profile: cinematic_realism_klein_distilled
- batch_role: keyframe_generation
- fix_of: none

# Continuity Notes
- Ensure window frame geometry matches BT003 establishing shot
- Maintain narrator's anxious expression consistent with retreat tension
- Keep interior lighting dimmer than exterior valley view
- Verify hound position does not block main observation line

# Repair Notes
- If window glass appears distorted, regenerate with corrected refraction settings
- If female companion is missing from corridor background, add subtle silhouette reference
- Check for text artifacts on interior walls and remove if present

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
