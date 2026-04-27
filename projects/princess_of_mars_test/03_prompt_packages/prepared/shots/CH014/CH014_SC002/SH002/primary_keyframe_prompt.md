# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH014_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian plains and march route. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A party discovers a Warhoon incubator containing green eggs before it is violently destroyed. The subject from image1 is Warhoon incubator, midground inside incubator site, Small biological objects (eggs) vs large scale environmental destruction, front three-quarter left toward the scene action, intact incubator. The subject from image2 is Warhoon incubator plays against tars tarkas, sarkoja in the same frame. Preserve the environment from image3 Continuous stretch of undulating terrain, long-distance vistas., monumental scale, dry open Martian terrain, especially incubator site. wide, low angle, wide lens, handheld, deep focus, high contrast ceremonial. Wide composition across placed for immediate spatial orientation. the incubator is destroyed. incubator site. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH014_SC002; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; sarkoja; dejah_thoris
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH014_SC002
- chapter_id: CH014
- shot_type: establishing_wide
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across martian_plains_and_march_route with john_carter, tars_tarkas, sarkoja placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: tars_tarkas; sarkoja
- primary_subject_frame_position: midground inside incubator_site
- primary_subject_scale_relation: Small biological objects (eggs) vs large scale environmental destruction.
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: intact incubator
- subject_relation_summary: Warhoon incubator plays against tars_tarkas, sarkoja in the same frame
- scene_short_description: A party discovers a Warhoon incubator containing green eggs before it is violently destroyed.
- shot_moment_summary: the incubator is destroyed
- required_environment_anchor_1: incubator_site
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Small biological objects (eggs) vs large scale environmental destruction.
- camera_package_description: wide, low angle, wide lens, handheld, deep focus, high contrast ceremonial
- environment_subzone: incubator_site
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tars_tarkas; sarkoja; martian_plains_and_march_route; DESC_CH014_SC002; DESC_CH014_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: tars tarkas
- image3_role: environment reference for the scene location
- image3_asset: martian plains and march route
- image4_role: identity reference for an additional visible subject
- image4_asset: sarkoja

# Continuity Notes
- Scene: CH014_SC002 / SC002.
- Variant: Primary Keyframe.
- Incubator state transition (intact to destroyed)
- Debris pattern consistency post-destruction
- The destruction of the incubator via sabotage or defense
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC002\SH002\DIALOGUE.json
