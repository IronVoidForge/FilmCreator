# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH003_SC005_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity. An unarmed leader offers a metal armlet to a transformed human in a yellowish moss basin. The subject from image1 is protagonist, foreground inside yellowish moss basin, armlet on protagonist arm, facing directly toward camera, hand reaches out to take the metal armlet. Preserve the environment from image2 especially yellowish moss basin. Keep one readable subject anchor: hand reaches out. physical height difference during lift context. medium-close, eye level, normal lens, locked off, zoom subtle in, rack focus, diffuse ambient. Detail composition centered on the key physical action of the armlet being taken inside. Protagonist accepts the armlet and makes eye contact. yellowish moss basin. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC005; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH003_SC005
- chapter_id: CH003
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action of the armlet being taken inside circular_moss_basin.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: rack_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside yellowish_moss_basin
- primary_subject_scale_relation: armlet on protagonist arm
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: hand reaches out to take the metal armlet
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: An unarmed leader offers a metal armlet to a transformed human in a yellowish moss basin.
- shot_moment_summary: Protagonist accepts the armlet and makes eye contact
- required_environment_anchor_1: yellowish_moss_basin
- required_subject_anchor_1: hand reaches out
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: physical height difference during lift context
- camera_package_description: medium-close, eye level, normal lens, locked off, zoom subtle in, rack focus, diffuse ambient
- environment_subzone: yellowish_moss_basin
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC005; DESC_CH003_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC005 / SC005.
- Variant: Alternate Angle.
- Armlet must remain visible on protagonist's arm after acceptance
- Height differential during mount lifting process
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SH002\DIALOGUE.json
