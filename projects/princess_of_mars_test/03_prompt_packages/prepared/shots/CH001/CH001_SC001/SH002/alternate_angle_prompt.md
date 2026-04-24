# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH001_SC001_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity.. An elderly man sits in a reflective space, addressing the audience about his life.. The subject from image1 is described character with stable costume and silhouette, foreground right within Narrative framing space, Subject is centered within a tight, intimate framing to emphasize isolation and introspection., front three-quarter left toward the scene action, subject begins speaking. Preserve described environment with stable spatial continuity from image2, especially Narrative framing space. Subject is centered within a tight, intimate framing to emphasize isolation and introspection.. medium, eye level, normal lens, locked off, shallow subject, soft even. Readable medium composition in featuring .. medium shot of john_carter speaking. Narrative framing space. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH001_SC001; SHOT_INDEX; DIALOGUE; john_carter
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
- scene_id: CH001_SC001
- chapter_id: CH001
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Unspecified (Narrative framing space) featuring john_carter.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within Narrative framing space
- primary_subject_scale_relation: Subject is centered within a tight, intimate framing to emphasize isolation and introspection.
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: subject begins speaking
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: An elderly man sits in a reflective space, addressing the audience about his life.
- shot_moment_summary: medium shot of john_carter speaking
- required_environment_anchor_1: Narrative framing space
- required_scale_proof_detail: Subject is centered within a tight, intimate framing to emphasize isolation and introspection.
- camera_package_description: medium, eye level, normal lens, locked off, shallow subject, soft even
- environment_subzone: Narrative framing space
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; DESC_CH001_SC001; DESC_CH001_SC001_SH002
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
- Verbal introduction of the anomalous condition and purpose
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC001\SH002\DIALOGUE.json
