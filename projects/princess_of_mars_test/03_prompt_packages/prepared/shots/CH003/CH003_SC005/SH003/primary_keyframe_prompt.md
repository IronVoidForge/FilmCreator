# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH003_SC005_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement. An unarmed leader offers a metal armlet to a protagonist in a yellowish mossy basin. The subject from image1 is described character with stable costume and silhouette, midground inside martian_distant_hills, height difference during lift, rear three-quarter left away from camera, protagonist being lifted. The subject from image2 is described character with stable costume and silhouette, protagonist plays against martian_warriors in the same frame. Preserve described environment with stable spatial anchors from image3, especially martian_distant_hills. height difference during lift. wide, low angle, wide lens, pan, deep focus, diffuse ambient. Wide composition across with, placed for immediate spatial orientation. Protagonist is lifted onto the mount and departs. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH003_SC005; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
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
- scene_id: CH003_SC005
- chapter_id: CH003
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across martian_distant_hills with protagonist, martian_warriors, The Leader placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: martian_warriors
- primary_subject_frame_position: midground inside martian_distant_hills
- primary_subject_scale_relation: height difference during lift
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: protagonist being lifted
- subject_relation_summary: protagonist plays against martian_warriors in the same frame
- scene_short_description: An unarmed leader offers a metal armlet to a protagonist in a yellowish mossy basin.
- shot_moment_summary: Protagonist is lifted onto the mount and departs
- required_environment_anchor_1: martian_distant_hills
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: height difference during lift
- camera_package_description: wide, low angle, wide lens, pan, deep focus, diffuse ambient
- environment_subzone: martian_distant_hills
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; martian_warriors; martian_distant_hills; DESC_CH003_SC005; DESC_CH003_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: martian warriors
- image3_role: environment reference for the scene location
- image3_asset: martian distant hills

# Continuity Notes
- Scene: CH003_SC005 / SC005.
- Variant: Primary Keyframe.
- Metal armlet must remain visible on protagonist's arm after acceptance
- Height differential between protagonist and Martian mount during lifting
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SH003\DIALOGUE.json
