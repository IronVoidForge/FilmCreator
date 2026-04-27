# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH024_SC005_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for zodanga walled city. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A small group scales massive dark walls under moonlight to infiltrate a city. The subject from image1 is john carter, foreground inside zodanga walled city/palace grounds, Massive verticality of carborundum walls vs. small character scale, facing directly toward camera, top of wall. Preserve the environment from image2 Fortified perimeter with massive walls surrounding a central palace complex., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially zodanga walled city/palace grounds. close-up, high angle, telephoto lens, push in, zoom subtle in, shallow subject, low key night. Intimate composition that isolates, against to capture the beat's emotional turn. Carter surveys the palace grounds from above. /palace grounds. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH024_SC005; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: telephoto
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
- scene_id: CH024_SC005
- chapter_id: CH024
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, Small Group of Tharks against zodanga_walled_city to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: high_angle
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside zodanga_walled_city/palace_grounds
- primary_subject_scale_relation: Massive verticality of carborundum walls vs. small character scale.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: top of wall
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A small group scales massive dark walls under moonlight to infiltrate a city.
- shot_moment_summary: Carter surveys the palace grounds from above
- required_environment_anchor_1: zodanga_walled_city/palace_grounds
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Massive verticality of carborundum walls vs. small character scale.
- camera_package_description: close-up, high angle, telephoto lens, push in, zoom subtle in, shallow subject, low key night
- environment_subzone: zodanga_walled_city/palace_grounds
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zodanga_walled_city; DESC_CH024_SC005; DESC_CH024_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: zodanga walled city

# Continuity Notes
- Scene: CH024_SC005 / SC005.
- Variant: Primary Keyframe.
- Moonlight direction and shadow consistency
- Height scale of carborundum walls relative to characters
- Physical placement and stability of the human ladder elements
- Establishing control within palace grounds
- Resolve Small Group of Tharks -> Small Group of Tharks
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC005\SH003\DIALOGUE.json
