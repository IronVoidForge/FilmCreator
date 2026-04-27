# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH026_SC002_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for aerial battle skies. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A celebratory reunion on a flagship deck overlooking a victorious naval fleet. The subject from image1 is john carter, foreground right within Flagship Deck (Center), Low angle hero scale, front three-quarter left toward the scene action, Carter watching celebration. The subject from image2 is john carter plays against tars tarkas in the same frame. Preserve the environment from image3 High-altitude, expansive vertical combat space., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially Flagship Deck (Center). medium-full, low angle, wide lens, push in, deep focus, backlit. Closing composition in that emphasizes the consequence of carter's tactical decision. Carter and Tars Tarkas deciding to stay. Flagship Deck (Center). Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH026_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tars_tarkas
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
- scene_id: CH026_SC002
- chapter_id: CH026
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in aerial_battle_skies that emphasizes the consequence of carter's tactical decision.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: backlit
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: tars_tarkas
- primary_subject_frame_position: foreground right within Flagship Deck (Center)
- primary_subject_scale_relation: Low angle hero scale
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: Carter watching celebration
- subject_relation_summary: john_carter plays against tars_tarkas in the same frame
- scene_short_description: A celebratory reunion on a flagship deck overlooking a victorious naval fleet.
- shot_moment_summary: Carter and Tars Tarkas deciding to stay
- required_environment_anchor_1: Flagship Deck (Center)
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Low angle hero scale
- camera_package_description: medium-full, low angle, wide lens, push in, deep focus, backlit
- environment_subzone: Flagship Deck (Center)
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tars_tarkas; aerial_battle_skies; DESC_CH026_SC002; DESC_CH026_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: tars tarkas
- image3_role: environment reference for the scene location
- image3_asset: aerial battle skies

# Continuity Notes
- Scene: CH026_SC002 / SC002.
- Variant: Primary Keyframe.
- Dejah Thoris physical state (transition from exhaustion to relief)
- Visual presence of Thark fleet in background horizon
- Carter's tactical decision
- Resolve Heliumite Sailors -> Heliumite Sailors
- Resolve The Heliumite Flagship (Deck) -> The Heliumite Flagship (Deck)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC002\SH003\DIALOGUE.json
