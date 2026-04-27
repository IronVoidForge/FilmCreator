# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH008_SC001_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for green martian warriors. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for deserted martian city plaza. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A sudden retreat by local warriors precedes a massive aerial assault on a deserted city. The subject from image1 is green martian warriors, foreground right within deserted martian city rooftops, warrior position vs ship distance, profile left toward the scene action, warriors taking cover. The subject from image2 is green martian warriors plays against protagonist, sola in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially deserted martian city rooftops. medium, eye level, telephoto lens, track, rack focus, high contrast ceremonial. Dynamic composition in clear pursuit vectors and readable movement. warriors firing from rooftops. deserted martian city rooftops. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH008_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola; green_martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: telephoto
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Environment reference conflict: prompt variables align more with `deserted_martian_city` than bound `deserted_martian_city_plaza`.; Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH008_SC001
- chapter_id: CH008
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in deserted_martian_city_plaza with clear pursuit vectors and readable movement for green_martian_warriors, protagonist, sola.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: green_martian_warriors
- visible_secondary_subject_ids: protagonist; sola
- primary_subject_frame_position: foreground right within deserted_martian_city rooftops
- primary_subject_scale_relation: warrior position vs ship distance
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: warriors taking cover
- subject_relation_summary: green_martian_warriors plays against protagonist, sola in the same frame
- scene_short_description: A sudden retreat by local warriors precedes a massive aerial assault on a deserted city.
- shot_moment_summary: warriors firing from rooftops
- required_environment_anchor_1: deserted_martian_city rooftops
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: warrior position vs ship distance
- camera_package_description: medium, eye level, telephoto lens, track, rack focus, high contrast ceremonial
- environment_subzone: deserted_martian_city rooftops
- prompt_family: shot_prompt
- reference_asset_ids: green_martian_warriors; protagonist; sola; deserted_martian_city_plaza; DESC_CH008_SC001; DESC_CH008_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: green martian warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: deserted martian city plaza
- image4_role: identity reference for an additional visible subject
- image4_asset: sola

# Continuity Notes
- Scene: CH008_SC001 / SC001.
- Variant: Alternate Angle.
- Position of protagonist and sola relative to deserted_martian_city structures
- Directional vector of gray vessels vs. green Martian fire trajectories
- Organized skirmish against the fleet
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC001\SH003\DIALOGUE.json
