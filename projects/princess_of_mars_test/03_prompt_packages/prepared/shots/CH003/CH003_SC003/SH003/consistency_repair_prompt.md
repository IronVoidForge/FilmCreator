# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH003_SC003_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A party of twenty mounted warriors approaches a hiding figure within yellowish mossy vegetation. The subject from image1 is spear tip, foreground inside vegetation hiding spot, preserve readable body-to-environment scale in frame, profile right toward the scene action, spear descending. The subject from image2 is spear tip plays against protagonist in the same frame. Preserve the environment from image3 especially vegetation hiding spot. extreme-close-up, low angle, telephoto lens, locked off, rack focus, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. spear narrowly misses protagonist. vegetation hiding spot. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH003_SC003; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: telephoto
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
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates martian_warriors, protagonist against circular_moss_basin to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: low_angle
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: martian_warriors
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground inside vegetation_hiding_spot
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: spear descending
- subject_relation_summary: spear tip plays against protagonist in the same frame
- scene_short_description: A party of twenty mounted warriors approaches a hiding figure within yellowish mossy vegetation.
- shot_moment_summary: spear narrowly misses protagonist
- required_environment_anchor_1: vegetation_hiding_spot
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: extreme-close-up, low angle, telephoto lens, locked off, rack focus, high contrast ceremonial
- environment_subzone: vegetation_hiding_spot
- prompt_family: shot_prompt
- reference_asset_ids: martian_warriors; protagonist; circular_moss_basin; DESC_CH003_SC003; DESC_CH003_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: martian warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC003 / SC003.
- Variant: Consistency Repair.
- Rhythmic speed and cadence of the twenty mounted martian_warriors
- Physical distance/proximity of the leader's spear to the protagonist
- The leader's spear narrowly misses the protagonist
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SH003\DIALOGUE.json
