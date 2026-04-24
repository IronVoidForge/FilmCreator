# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH001_SC005_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity.. A man follows his horse into a narrow cliffside cave and collapses within an ancient chamber.. The subject from image1 is described character with stable costume and silhouette, midground inside high_trail_entrance, cliffside height vs trail width, profile left toward the scene action, bright daylight on trail. Preserve described environment with stable spatial continuity from image2, especially narrow_cave_entrance. cliffside height vs trail width. wide, eye level, wide lens, track, deep focus, hard directional. Wide composition across with placed for immediate spatial orientation.. horse leads Carter toward narrow cave entrance. high_trail_entrance. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH001_SC005; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
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
- scene_id: CH001_SC005
- chapter_id: CH001
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across ancient_cliffside_cave with john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside high_trail_entrance
- primary_subject_scale_relation: cliffside height vs trail width
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: bright daylight on trail
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A man follows his horse into a narrow cliffside cave and collapses within an ancient chamber.
- shot_moment_summary: horse leads Carter toward narrow cave entrance
- required_environment_anchor_1: narrow_cave_entrance
- required_scale_proof_detail: cliffside height vs trail width
- camera_package_description: wide, eye level, wide lens, track, deep focus, hard directional
- environment_subzone: high_trail_entrance
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; ancient_cliffside_cave; DESC_CH001_SC005; DESC_CH001_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: ancient cliffside cave

# Continuity Notes
- Scene: CH001_SC005 / SC005.
- Variant: Alternate Angle.
- Lighting transition from bright exterior to dark/dim cave
- Visual cues for unnatural drowsiness (heavy eyelids, blurred vision)
- Carter follows horse to narrow cave entrance
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC005\SH001\DIALOGUE.json
