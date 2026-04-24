# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH003_SC003_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity. A party of twenty mounted warriors approaches a hiding figure within yellowish mossy vegetation. The subject from image1 is Large, four-armed humanoid military force with olive-green skin., readable production detail, Massive, 15-foot tall humanoids., Martian setting, midground inside transit_pathway, preserve readable body-to-environment scale in frame, facing directly toward camera, distant movement. The subject from image2 is An Earthman undergoing a supernatural transformation., readable production detail, agile and capable of high-intensity physical exertion., Earthman in a low-gravity environment, martian_warriors plays against protagonist in the same frame. Preserve described environment with stable spatial continuity from image3 especially transit_pathway. preserve readable body-to-environment scale in frame. wide, low angle, ultra-wide lens, track, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. cavalcade enters view. transit_pathway. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC003; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: ultra_wide
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
- scene_id: CH003_SC003
- chapter_id: CH003
- shot_type: establishing_wide
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across circular_moss_basin with martian_warriors, protagonist placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: martian_warriors
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: midground inside transit_pathway
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: distant movement
- subject_relation_summary: martian_warriors plays against protagonist in the same frame
- scene_short_description: A party of twenty mounted warriors approaches a hiding figure within yellowish mossy vegetation.
- shot_moment_summary: cavalcade enters view
- required_environment_anchor_1: transit_pathway
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: wide, low angle, ultra-wide lens, track, deep focus, diffuse ambient
- environment_subzone: transit_pathway
- prompt_family: shot_prompt
- reference_asset_ids: martian_warriors; protagonist; circular_moss_basin; DESC_CH003_SC003; DESC_CH003_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: martian warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC003 / SC003.
- Variant: Alternate Angle.
- Rhythmic speed and cadence of the twenty mounted martian_warriors
- Physical distance/proximity of the leader's spear to the protagonist
- The martian_warriors cavalcade approaches the basin
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SH002\DIALOGUE.json
