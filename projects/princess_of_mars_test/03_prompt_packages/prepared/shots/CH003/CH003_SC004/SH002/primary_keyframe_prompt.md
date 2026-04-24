# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH003_SC004_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement. A desperate escape via a massive thirty-foot leap across a mossy circular basin. The subject from image1 is described character with stable costume and silhouette, midground inside mossy floor, distance from enclosure to far side, profile left toward the scene action, mid-air launch. Preserve described environment with stable spatial anchors from image2, especially mossy floor. distance from enclosure to far side. wide, eye level, ultra-wide lens, track, deep focus, diffuse ambient. Dynamic composition in with clear pursuit vectors and readable movement for . the thirty-foot leap in flight. mossy floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC004; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: ultra_wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH003_SC004
- chapter_id: CH003
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in circular_moss_basin with clear pursuit vectors and readable movement for protagonist.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside mossy floor
- primary_subject_scale_relation: distance from enclosure to far side
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: mid-air launch
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A desperate escape via a massive thirty-foot leap across a mossy circular basin.
- shot_moment_summary: the thirty-foot leap in flight
- required_environment_anchor_1: mossy floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: distance from enclosure to far side
- camera_package_description: wide, eye level, ultra-wide lens, track, deep focus, diffuse ambient
- environment_subzone: mossy floor
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC004; DESC_CH003_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC004 / SC004.
- Variant: Primary Keyframe.
- Precise trajectory and landing point relative to enclosure walls
- Visual scale relationship between martian_warriors and protagonist
- Precise trajectory and landing point of the jump relative to the enclosure walls
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SH002\DIALOGUE.json
