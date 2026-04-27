# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH005_SC005_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for colossal creature lair. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A man pulls himself onto a ledge before being snatched by a massive ape-like creature. The subject from image1 is protagonist, foreground inside windowsill, Human scale vs Colossal predator scale, front three-quarter right toward the scene action, hands grasping edge. Preserve the environment from image2 Building interior with large windows overlooking a vast valley, high-altitude containment structure., monumental scale, dry open Martian terrain, especially windowsill. Keep one readable subject anchor: hands grasping edge. close-up, eye level, portrait lens, push in, shallow subject, diffuse ambient. Intimate composition that isolates against to capture the beat's emotional turn. protagonist reaches the ledge and exhales. windowsill. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH005_SC005; SHOT_INDEX; DIALOGUE; protagonist; the_colossal_creature
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
- scene_id: CH005_SC005
- chapter_id: CH005
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist against colossal_creature_lair to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside windowsill
- primary_subject_scale_relation: Human scale vs Colossal predator scale.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: hands grasping edge
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A man pulls himself onto a ledge before being snatched by a massive ape-like creature.
- shot_moment_summary: protagonist reaches the ledge and exhales
- required_environment_anchor_1: windowsill
- required_subject_anchor_1: hands grasping edge
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Human scale vs Colossal predator scale.
- camera_package_description: close-up, eye level, portrait lens, push in, shallow subject, diffuse ambient
- environment_subzone: windowsill
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; colossal_creature_lair; DESC_CH005_SC005; DESC_CH005_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: colossal creature lair

# Continuity Notes
- Scene: CH005_SC005 / SC005.
- Variant: Primary Keyframe.
- Physical contact point between the_colossal_creature and protagonist
- Hand placement during the grip
- Transition from windowsill to interior room floor
- protagonist reaches safety on the ledge
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC005\SH001\DIALOGUE.json
