# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH009_SC002_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for plaza training grounds. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Intensive combat training in a plaza involving martial exchanges against a stronger opponent. The subject from image1 is protagonist, midground inside central combat zone, wide view of both fighters relative to plaza size, front three-quarter left toward the scene action, fighters at distance. The subject from image2 is Small-scale humanoid non-human biped., Youthful (per display name)., Small scale, bipedal morphology, protagonist plays against martian youth in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially central combat zone. Keep one readable subject anchor: plaza floor surface. wide, eye level, wide lens, track, deep focus, diffuse ambient. Dynamic composition in clear pursuit vectors and readable movement. protagonist and martian youth square off in the plaza. central combat zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH009_SC002; SHOT_INDEX; DIALOGUE; protagonist; martian_youth
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
- scene_id: CH009_SC002
- chapter_id: CH009
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in plaza_training_grounds with clear pursuit vectors and readable movement for protagonist, martian_youth.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: martian_youth
- primary_subject_frame_position: midground inside central combat zone
- primary_subject_scale_relation: wide view of both fighters relative to plaza size
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: fighters at distance
- subject_relation_summary: protagonist plays against martian_youth in the same frame
- scene_short_description: Intensive combat training in a plaza involving martial exchanges against a stronger opponent.
- shot_moment_summary: protagonist and martian_youth square off in the plaza
- required_environment_anchor_1: central combat zone
- required_subject_anchor_1: plaza floor surface
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: wide view of both fighters relative to plaza size
- camera_package_description: wide, eye level, wide lens, track, deep focus, diffuse ambient
- environment_subzone: central combat zone
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; martian_youth; plaza_training_grounds; DESC_CH009_SC002; DESC_CH009_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: martian youth
- image3_role: environment reference for the scene location
- image3_asset: plaza training grounds

# Continuity Notes
- Scene: CH009_SC002 / SC002.
- Variant: Alternate Angle.
- Weapon positions must remain consistent between beats
- Sweat and dirt accumulation on protagonist
- Lighting consistency for time of day
- Initial engagement and circling
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH009\CH009_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC002\SH001\DIALOGUE.json
