# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH003_SC001_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity. A naked man wakes in a yellowish mossy basin and struggles with low gravity leaps. The subject from image1 is described character with stable costume and silhouette, foreground inside incubator zone, preserve readable body-to-environment scale in frame, facing directly toward camera, sitting up. Preserve described environment with stable spatial anchors from image2, especially low walled enclosure. preserve readable body-to-environment scale in frame. close-up, eye level, portrait lens, handheld, shallow subject, diffuse ambient. Intimate composition that isolates against to capture the beat's emotional turn. protagonist looking around confusedly. incubator zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC001; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
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
- scene_id: CH003_SC001
- chapter_id: CH003
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: (none)
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist against circular_moss_basin to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside incubator zone
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: sitting up
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A naked man wakes in a yellowish mossy basin and struggles with low gravity leaps.
- shot_moment_summary: protagonist looking around confusedly
- required_environment_anchor_1: low walled enclosure
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: close-up, eye level, portrait lens, handheld, shallow subject, diffuse ambient
- environment_subzone: incubator zone
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC001; DESC_CH003_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC001 / SC001.
- Variant: Alternate Angle.
- Protagonist remains naked throughout
- Leap height and distance must remain consistent for physics logic
- Moss texture underfoot during contact
- Attempting to orient self
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SH002\DIALOGUE.json
