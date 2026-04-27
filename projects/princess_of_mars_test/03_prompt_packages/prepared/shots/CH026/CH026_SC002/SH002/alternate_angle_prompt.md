# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH026_SC002_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the environment reference for aerial battle skies. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A celebratory reunion on a flagship deck overlooking a victorious naval fleet. The subject from image1 is dejah thoris, foreground inside Flagship Deck (Center), The scale shifts from the individual emotional reunion to the macro-scale of the impending land campaign, facing directly toward camera, Dejah looking around. Preserve the environment from image2 High-altitude, expansive vertical combat space., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially Flagship Deck (Center). close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, soft even. Intimate composition that isolates, against to capture the beat's emotional turn. Close up of Dejah's relief. Flagship Deck (Center). Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH026_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
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
- scene_id: CH026_SC002
- chapter_id: CH026
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates dejah_thoris, Heliumite Sailors against aerial_battle_skies to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside Flagship Deck (Center)
- primary_subject_scale_relation: The scale shifts from the individual emotional reunion to the macro-scale of the impending land campaign.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Dejah looking around
- subject_relation_summary: dejah_thoris carries the frame alone
- scene_short_description: A celebratory reunion on a flagship deck overlooking a victorious naval fleet.
- shot_moment_summary: Close up of Dejah's relief
- required_environment_anchor_1: Flagship Deck (Center)
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: The scale shifts from the individual emotional reunion to the macro-scale of the impending land campaign.
- camera_package_description: close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, soft even
- environment_subzone: Flagship Deck (Center)
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; aerial_battle_skies; DESC_CH026_SC002; DESC_CH026_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: environment reference for the scene location
- image2_asset: aerial battle skies

# Continuity Notes
- Scene: CH026_SC002 / SC002.
- Variant: Alternate Angle.
- Dejah Thoris physical state (transition from exhaustion to relief)
- Visual presence of Thark fleet in background horizon
- Celebration of the Princess
- Resolve Heliumite Sailors -> Heliumite Sailors
- Resolve The Heliumite Flagship (Deck) -> The Heliumite Flagship (Deck)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC002\SH002\DIALOGUE.json
