# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH013_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for green martian city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. Two figures walk through a Martian city under the light of two moons. The subject from image1 is john carter, foreground inside martian city streets, Vast celestial scale (dual moons) vs intimate character proximity, facing directly toward camera, extreme close-up. The subject from image2 is john carter plays against dejah thoris in the same frame. Preserve the environment from image3 Features wide thoroughfares, central leadership hubs, and large-scale enclosures/pens for beasts., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian city streets. tight focus on eyes. extreme-close-up, eye level, telephoto lens, locked off, shallow subject, low key night. Over-the-shoulder composition in sharing the frame for dialogue or tension. Carter's realization. martian city streets. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH013_SC004; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
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
- scene_id: CH013_SC004
- chapter_id: CH013
- shot_type: over_the_shoulder
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Shoulder-level conversational framing with visible foreground presence.
- composition: Over-the-shoulder composition in green_martian_city_complex with john_carter, dejah_thoris sharing the frame for dialogue or tension.
- shot_size: extreme_close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: dejah_thoris
- primary_subject_frame_position: foreground inside martian_city_streets
- primary_subject_scale_relation: Vast celestial scale (dual moons) vs intimate character proximity.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: extreme close-up
- subject_relation_summary: john_carter plays against dejah_thoris in the same frame
- scene_short_description: Two figures walk through a Martian city under the light of two moons.
- shot_moment_summary: Carter's realization
- required_environment_anchor_1: martian_city_streets
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: tight focus on eyes
- camera_package_description: extreme-close-up, eye level, telephoto lens, locked off, shallow subject, low key night
- environment_subzone: martian_city_streets
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; green_martian_city_complex; DESC_CH013_SC004; DESC_CH013_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: green martian city complex

# Continuity Notes
- Scene: CH013_SC004 / SC004.
- Variant: Primary Keyframe.
- Moonlight direction consistency across all shots
- Precise timing of chieftain dialogue
- Carter's emotional expression shift at conclusion
- Romantic realization
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC004\SH003\DIALOGUE.json
