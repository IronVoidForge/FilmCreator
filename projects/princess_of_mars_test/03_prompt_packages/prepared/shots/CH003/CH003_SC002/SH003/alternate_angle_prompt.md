# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH003_SC002_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity.. A character investigates a glass-roofed incubator filled with large white eggs and multi-limbed creatures.. The subject from image1 is described character with stable costume and silhouette, foreground inside incubator_interior, The scale of the large white eggs relative to the small, grotesque hatchlings., front three-quarter right toward the scene action, stillness. The subject from image2 is described character with stable costume and silhouette, multi-limbed hatchlings plays against protagonist in the same frame. Preserve described environment with stable spatial continuity from image3, especially incubator_interior. The scale of the large white eggs relative to the small, grotesque hatchlings.. close-up, low angle, telephoto lens, handheld, rack focus, high contrast ceremonial. Intimate composition that isolates against to capture the beat's emotional turn.. hatchlings move near eggs. incubator_interior. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH003_SC002; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: telephoto
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
- scene_id: CH003_SC002
- chapter_id: CH003
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist against circular_moss_basin to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: multi-limbed hatchlings
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground inside incubator_interior
- primary_subject_scale_relation: The scale of the large white eggs relative to the small, grotesque hatchlings.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: stillness
- subject_relation_summary: multi-limbed hatchlings plays against protagonist in the same frame
- scene_short_description: A character investigates a glass-roofed incubator filled with large white eggs and multi-limbed creatures.
- shot_moment_summary: hatchlings move near eggs
- required_environment_anchor_1: incubator_interior
- required_scale_proof_detail: The scale of the large white eggs relative to the small, grotesque hatchlings.
- camera_package_description: close-up, low angle, telephoto lens, handheld, rack focus, high contrast ceremonial
- environment_subzone: incubator_interior
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC002; DESC_CH003_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: multi limbed hatchlings
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC002 / SC002.
- Variant: Alternate Angle.
- Hatchling movement patterns must remain consistent across cuts
- Lighting shifts through the glass roof must match sun position/environment
- realization of the hatchlings
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SH003\DIALOGUE.json
