# Title
SC001 CL005 Keyframe Prompt

# ID
SC001_CL005_keyframe_prompt

# Purpose
Generate frozen still of intricate mechanical devices mounted on prows of gray vessels observed from upper floor window perspective, emphasizing continuity with previous banner visibility and maintaining lighting consistency for observation sequence. Focus on visible state at cut start as single frozen still. Avoid proper nouns. Use descriptive noun phrases only.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Close examination of odd devices mounted on prows of gray airships, visible through dark wood window frame, observer's eyeline focused on specific vessel details, red planet valley landscape in background, dust motes floating in sunlight beam, cinematic lighting, high detail, mysterious objects, intricate shapes, abandoned city rooftops below horizon, tense atmosphere, smoke trails from damaged hulls, banners showing minor damage indicators

# Negative Prompt
blurry, distorted faces, extra limbs, text, watermark, low resolution, dark shadows, oversaturated colors, wrong perspective, floating objects, missing window frame, incorrect device count, proper nouns, names, logos, bright daylight exterior only, interior figure blocking main observation line, banners dominating frame, green-skinned figure facing interior

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL005
- duration_seconds: 5
- required_refs: upper_floor_window_view
- optional_refs: building_interior_portal
- visible_character_assets: human_male_warrior, green_skinned_figure
- look_continuity_policy: match_previous_clip_lighting_and_position
- intended_lighting_change: natural_sunlight_contrasting_interior_darkness
- composition_type: detail_insert_device_focus
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert_device_detail_focus
- dependency_policy: dependent_on_banner_visibility_and_device_shapes
- auto_advance_policy: manual_review_required
- fallback_strategy: cutaway_to_ship_prow_detail
- consistency_assist_policy: enabled_for_character_features
- consistency_assist_method: feature_matching
- anatomy_repair_policy: strict_enforcement
- consistency_targets: face_shape, hair_style, clothing_details, device_shapes
- style_profile: cinematic_realism_klein_distilled
- batch_role: keyframe_generation
- fix_of: none

# Continuity Notes
- Ensure window frame geometry matches BT003 establishing shot
- Maintain observer's anxious expression consistent with retreat tension
- Keep interior lighting dimmer than exterior valley view
- Verify device shapes align with banner visibility from CL004
- Check for text artifacts on interior walls and remove if present

# Repair Notes
- If window glass appears distorted, regenerate with corrected refraction settings
- If device details are unclear, increase focus pull to specific vessel prows
- Check for text artifacts on interior walls and remove if present
- Ensure observer does not block main observation line of devices

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
