# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH014_SC003_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for zad. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for duel arena open plains. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Two warriors face off in a formal duel within an open Martian plain. The subject from image1 is zad, foreground inside duel circle, zad height vs horizon, front three-quarter right toward the scene action, static tension. The subject from image2 is zad plays against john carter in the same frame. Preserve the environment from image3 A wide combat clearing providing sufficient space for chariot maneuvering and formal dueling., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially duel circle. Keep celestial anchor zad stares down john carter stable in the frame. medium-close, low angle, portrait lens, locked off, shallow subject, diffuse ambient. Intimate composition that isolates, against to capture the beat's emotional turn. zad stares down john carter. duel circle. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH014_SC003; SHOT_INDEX; DIALOGUE; john_carter; zad; tars_tarkas; sarkoja
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
- scene_id: CH014_SC003
- chapter_id: CH014
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates Zad, john_carter against duel_arena_open_plains to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: low_angle
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: zad
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside duel_circle
- primary_subject_scale_relation: zad height vs horizon
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: static tension
- subject_relation_summary: zad plays against john_carter in the same frame
- scene_short_description: Two warriors face off in a formal duel within an open Martian plain.
- shot_moment_summary: zad stares down john_carter
- required_environment_anchor_1: duel_circle
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: zad stares down john_carter
- required_scale_proof_detail: zad height vs horizon
- camera_package_description: medium-close, low angle, portrait lens, locked off, shallow subject, diffuse ambient
- environment_subzone: duel_circle
- prompt_family: shot_prompt
- reference_asset_ids: zad; john_carter; duel_arena_open_plains; DESC_CH014_SC003; DESC_CH014_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: zad
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: duel arena open plains

# Continuity Notes
- Scene: CH014_SC003 / SC003.
- Variant: Alternate Angle.
- Weapon types must be long-swords
- Precise positioning of the duel circle/area
- Tension builds through eye contact
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC003\SH001\DIALOGUE.json
