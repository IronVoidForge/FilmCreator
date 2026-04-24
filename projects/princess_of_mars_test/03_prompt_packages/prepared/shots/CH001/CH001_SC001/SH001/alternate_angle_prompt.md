# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH001_SC001_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity.. An elderly man sits in a reflective space, addressing the audience about his life.. The subject from image1 is described character with stable costume and silhouette, foreground inside Narrative framing space, Subject is centered within a tight, intimate framing to emphasize isolation and introspection., facing directly toward camera, eyes opening or focusing. Preserve described environment with stable spatial continuity from image2, especially Narrative framing space. Subject is centered within a tight, intimate framing to emphasize isolation and introspection.. extreme-close-up, eye level, telephoto lens, locked off, shallow subject, soft even. Intimate composition that isolates against to capture the beat's emotional turn.. extreme close up of weathered skin and eyes. Narrative framing space. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH001_SC001; SHOT_INDEX; DIALOGUE; john_carter
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
- scene_id: CH001_SC001
- chapter_id: CH001
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter against Unspecified (Narrative framing space) to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside Narrative framing space
- primary_subject_scale_relation: Subject is centered within a tight, intimate framing to emphasize isolation and introspection.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: eyes opening or focusing
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: An elderly man sits in a reflective space, addressing the audience about his life.
- shot_moment_summary: extreme close up of weathered skin and eyes
- required_environment_anchor_1: Narrative framing space
- required_scale_proof_detail: Subject is centered within a tight, intimate framing to emphasize isolation and introspection.
- camera_package_description: extreme-close-up, eye level, telephoto lens, locked off, shallow subject, soft even
- environment_subzone: Narrative framing space
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; DESC_CH001_SC001; DESC_CH001_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: none

# Continuity Notes
- Scene: CH001_SC001 / SC001.
- Variant: Alternate Angle.
- Consistent elderly physical appearance for john_carter
- Stable vocal tone and delivery rhythm
- Visual introduction of the physical toll of aging
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC001\SH001\DIALOGUE.json
