# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH003_SC004_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A desperate escape via a massive thirty-foot leap across a mossy circular basin. The subject from image1 is described character with stable costume and silhouette, foreground entry line within incubator enclosure, proximity to martian_warriors establishes tension, front three-quarter right toward the scene action, protagonist cornered against low wall. The subject from image2 is described character with stable costume and silhouette, protagonist plays against martian_warriors in the same frame. Preserve described environment with stable spatial anchors from image3, especially low walled enclosure. proximity to martian_warriors. medium-full, low angle, wide lens, push in, shallow subject, diffuse ambient. Wide composition across with and placed for immediate spatial orientation. protagonist prepares for the jump. incubator enclosure. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH003_SC004; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH003_SC004
- chapter_id: CH003
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across circular_moss_basin with protagonist and martian_warriors placed for immediate spatial orientation.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: martian_warriors
- primary_subject_frame_position: foreground entry line within incubator enclosure
- primary_subject_scale_relation: proximity to martian_warriors establishes tension
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: protagonist cornered against low wall
- subject_relation_summary: protagonist plays against martian_warriors in the same frame
- scene_short_description: A desperate escape via a massive thirty-foot leap across a mossy circular basin.
- shot_moment_summary: protagonist prepares for the jump
- required_environment_anchor_1: low walled enclosure
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: proximity to martian_warriors
- camera_package_description: medium-full, low angle, wide lens, push in, shallow subject, diffuse ambient
- environment_subzone: incubator enclosure
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; martian_warriors; circular_moss_basin; DESC_CH003_SC004; DESC_CH003_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: martian warriors
- image3_role: environment reference for the scene location
- image3_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC004 / SC004.
- Variant: Consistency Repair.
- Precise trajectory and landing point of the jump relative to the enclosure walls
- Visual scale relationship between martian_warriors and protagonist
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SH001\DIALOGUE.json
