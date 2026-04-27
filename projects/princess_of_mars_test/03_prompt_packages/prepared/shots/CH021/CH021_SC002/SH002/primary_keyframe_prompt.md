# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH021_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga city gates. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A traveler approaches massive city walls and makes the difficult choice to leave a companion behind. The subject from image1 is john carter, foreground inside wall base perimeter, Massive Zodangan walls dwarf the human and creature scale, front three-quarter right toward the scene action, pausing and looking back at Woola. The subject from image2 is john carter plays against woola in the same frame. Preserve the environment from image3 A threshold point marking the boundary between open wild plains and the urban environment of Zodanga., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially wall base perimeter. Keep one readable subject anchor: Carter turns to face Woola. close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, soft even. Intimate composition that isolates, against to capture the beat's emotional turn. Carter looks at Woola with reluctance. wall base perimeter. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH021_SC002; SHOT_INDEX; DIALOGUE; john_carter; woola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH021_SC002
- chapter_id: CH021
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, woola against zodanga_city_gates to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: woola
- primary_subject_frame_position: foreground inside wall_base_perimeter
- primary_subject_scale_relation: Massive Zodangan walls dwarf the human and creature scale.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: pausing and looking back at Woola
- subject_relation_summary: john_carter plays against woola in the same frame
- scene_short_description: A traveler approaches massive city walls and makes the difficult choice to leave a companion behind.
- shot_moment_summary: Carter looks at Woola with reluctance
- required_environment_anchor_1: wall_base_perimeter
- required_subject_anchor_1: Carter turns to face Woola
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Massive Zodangan walls dwarf the human and creature scale.
- camera_package_description: close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, soft even
- environment_subzone: wall_base_perimeter
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; woola; zodanga_city_gates; DESC_CH021_SC002; DESC_CH021_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: woola
- image3_role: environment reference for the scene location
- image3_asset: zodanga city gates

# Continuity Notes
- Scene: CH021_SC002 / SC002.
- Variant: Primary Keyframe.
- Woola's physical proximity to Carter
- State of gear and clothing after travel
- The moment of decision
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC002\SH002\DIALOGUE.json
