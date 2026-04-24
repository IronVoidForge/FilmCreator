# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH003_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity. A transformed man performs a massive leap across a mossy enclosure to escape captors. The subject from image1 is An Earthman undergoing a supernatural transformation., readable production detail, agile and capable of high-intensity physical exertion., Earthman in a low-gravity environment, foreground entry line within inner_moss_zone, Protagonist's 30-foot jump vs. the scale of martian_warriors and circular_moss_basin walls, front three-quarter right toward the scene action, protagonist crouched/tense. The subject from image2 is Large, four-armed humanoid military force with olive-green skin., readable production detail, Massive, 15-foot tall humanoids., Martian setting, protagonist plays against martian_warriors in the same frame. Preserve described environment with stable spatial continuity from image3 especially low walled enclosure. Proximity of martian_warriors to protagonist. medium-full, low angle, wide lens, push in, shallow subject, diffuse ambient. Wide composition across placed for immediate spatial orientation. protagonist prepares for leap. inner_moss_zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH003_SC004; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
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
- composition: Wide composition across circular_moss_basin with protagonist, martian_warriors placed for immediate spatial orientation.
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
- primary_subject_frame_position: foreground entry line within inner_moss_zone
- primary_subject_scale_relation: Protagonist's 30-foot jump vs. the scale of martian_warriors and circular_moss_basin walls.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: protagonist crouched/tense
- subject_relation_summary: protagonist plays against martian_warriors in the same frame
- scene_short_description: A transformed man performs a massive leap across a mossy enclosure to escape captors.
- shot_moment_summary: protagonist prepares for leap
- required_environment_anchor_1: low walled enclosure
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Proximity of martian_warriors to protagonist
- camera_package_description: medium-full, low angle, wide lens, push in, shallow subject, diffuse ambient
- environment_subzone: inner_moss_zone
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
- Variant: Alternate Angle.
- Precise trajectory and landing point of the 30ft jump
- Visual scale relationship between protagonist and martian_warriors
- Protagonist prepares for the leap
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SH001\DIALOGUE.json
