# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH003_SC003_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A party of twenty mounted warriors passes a hiding figure near a mossy basin. The subject from image1 is protagonist, foreground inside yellowish moss vegetation area, preserve readable body-to-environment scale in frame, front three-quarter left toward the scene action, protagonist listening. The subject from image2 is protagonist plays against martian warriors in the same frame. Preserve the environment from image3 especially yellowish moss vegetation area. medium-close, eye level, normal lens, handheld, shallow subject, diffuse ambient. Intimate composition that isolates, against to capture the beat's emotional turn. protagonist hears equipment rattle. yellowish moss vegetation area. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH003_SC003; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH003_SC003
- chapter_id: CH003
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist, martian_warriors against circular_moss_basin to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: partial
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: martian_warriors
- primary_subject_frame_position: foreground inside yellowish moss vegetation area
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: protagonist listening
- subject_relation_summary: protagonist plays against martian_warriors in the same frame
- scene_short_description: A party of twenty mounted warriors passes a hiding figure near a mossy basin.
- shot_moment_summary: protagonist hears equipment rattle
- required_environment_anchor_1: yellowish moss vegetation area
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-close, eye level, normal lens, handheld, shallow subject, diffuse ambient
- environment_subzone: yellowish moss vegetation area
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; martian_warriors; circular_moss_basin; DESC_CH003_SC003; DESC_CH003_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: martian warriors
- image3_role: environment reference for the scene location
- image3_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC003 / SC003.
- Variant: Consistency Repair.
- Rhythmic speed and cadence of the twenty mounted martian_warriors
- Physical distance/proximity between the leader's spear and protagonist
- protagonist hears the rattle of equipment
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SH001\DIALOGUE.json
