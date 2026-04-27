# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH005_SC001_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sola. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for captive chamber murals. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A captive studies detailed Martian murals while a ferocious beast watches from the doorway. The subject from image1 is sola, foreground entry line within doorway threshold, room width vs door size, profile left toward the scene action, sola moving toward exit. The subject from image2 is sola plays against protagonist in the same frame. Preserve the environment from image3 Interior cell containing a sleeping area, a Watch Dog is positioned at the threshold., monumental scale, dry open Martian terrain, especially chamber doorway. medium-full, eye level, wide lens, pan, shallow subject, diffuse ambient. Wide composition across placed for immediate spatial orientation. Sola leaves the protagonist alone. doorway threshold. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH005_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola; the_watch_dog
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
- scene_id: CH005_SC001
- chapter_id: CH005
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across captive_chamber_murals with sola, protagonist placed for immediate spatial orientation.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground entry line within doorway threshold
- primary_subject_scale_relation: room width vs door size
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: sola moving toward exit
- subject_relation_summary: sola plays against protagonist in the same frame
- scene_short_description: A captive studies detailed Martian murals while a ferocious beast watches from the doorway.
- shot_moment_summary: Sola leaves the protagonist alone
- required_environment_anchor_1: chamber doorway
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: room width vs door size
- camera_package_description: medium-full, eye level, wide lens, pan, shallow subject, diffuse ambient
- environment_subzone: doorway threshold
- prompt_family: shot_prompt
- reference_asset_ids: sola; protagonist; captive_chamber_murals; DESC_CH005_SC001; DESC_CH005_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: captive chamber murals

# Continuity Notes
- Scene: CH005_SC001 / SC001.
- Variant: Alternate Angle.
- Mural detail consistency across macro shots
- Lighting shifts indicating passage of time
- Watch Dog position relative to the door
- Sola departs the chamber
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC001\SH001\DIALOGUE.json
