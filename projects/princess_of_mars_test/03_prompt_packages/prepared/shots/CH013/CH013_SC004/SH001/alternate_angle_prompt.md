# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH013_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for green martian city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Two figures walk through a Martian city under the light of two moons. The subject from image1 is john carter, midground inside martian city streets, Vast celestial scale (dual moons) vs intimate character proximity, profile left toward the scene action, wide view of city. The subject from image2 is john carter plays against dejah thoris in the same frame. Preserve the environment from image3 Features wide thoroughfares, central leadership hubs, and large-scale enclosures/pens for beasts., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian city streets. Keep celestial anchor the moon stable in the frame. moons visible above city skyline. wide, eye level, wide lens, track, deep focus, low key night. Wide composition across placed for immediate spatial orientation. couple walking under moons. martian city streets. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH013_SC004; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
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
- scene_id: CH013_SC004
- chapter_id: CH013
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across green_martian_city_complex with john_carter, dejah_thoris placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: dejah_thoris
- primary_subject_frame_position: midground inside martian_city_streets
- primary_subject_scale_relation: Vast celestial scale (dual moons) vs intimate character proximity.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: wide view of city
- subject_relation_summary: john_carter plays against dejah_thoris in the same frame
- scene_short_description: Two figures walk through a Martian city under the light of two moons.
- shot_moment_summary: couple walking under moons
- required_environment_anchor_1: martian_city_streets
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: dual moons
- required_scale_proof_detail: moons visible above city skyline
- camera_package_description: wide, eye level, wide lens, track, deep focus, low key night
- environment_subzone: martian_city_streets
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; green_martian_city_complex; DESC_CH013_SC004; DESC_CH013_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: green martian city complex

# Continuity Notes
- Scene: CH013_SC004 / SC004.
- Variant: Alternate Angle.
- Moonlight direction consistency across all shots
- Precise timing of chieftain dialogue
- Carter's emotional expression shift at conclusion
- Walking and discussing war
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC004\SH001\DIALOGUE.json
