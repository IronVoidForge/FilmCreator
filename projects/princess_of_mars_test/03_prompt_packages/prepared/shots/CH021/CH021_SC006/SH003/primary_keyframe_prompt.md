# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH021_SC006_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga central plaza. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A massive military ceremony in a walled plaza where a hero is publicly honored by royalty. The subject from image1 is john carter, foreground inside zodanga central plaza center, preserve readable body-to-environment scale in frame, front three-quarter left toward the scene action, Carter looking up at dais. The subject from image2 is john carter plays against than kosis in the same frame. Preserve the environment from image3 Central gathering space surrounded by palaces, mechanical cafes, and high-rise metal residences., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially ceremonial dais. close-up, low angle, wide lens, locked off, deep focus, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. Carter accepts the title of padwar. center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH021_SC006; SHOT_INDEX; DIALOGUE; john_carter; than_kosis; sab_than
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
- scene_id: CH021_SC006
- chapter_id: CH021
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, than_kosis against zodanga_central_plaza to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: than_kosis
- primary_subject_frame_position: foreground inside zodanga_central_plaza_center
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: Carter looking up at dais
- subject_relation_summary: john_carter plays against than_kosis in the same frame
- scene_short_description: A massive military ceremony in a walled plaza where a hero is publicly honored by royalty.
- shot_moment_summary: Carter accepts the title of padwar
- required_environment_anchor_1: ceremonial dais
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: close-up, low angle, wide lens, locked off, deep focus, high contrast ceremonial
- environment_subzone: zodanga_central_plaza_center
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; than_kosis; zodanga_central_plaza; DESC_CH021_SC006; DESC_CH021_SC006_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: than kosis
- image3_role: environment reference for the scene location
- image3_asset: zodanga central plaza

# Continuity Notes
- Scene: CH021_SC006 / SC006.
- Variant: Primary Keyframe.
- Armor/Uniform state for john_carter
- Crowd density and military formation placement
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC006.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC006\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC006\SH003\DIALOGUE.json
