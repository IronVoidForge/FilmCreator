# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH024_SC003_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for thark city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A political challenge leads to a ritual duel within a massive assembly chamber. The subject from image1 is tars tarkas, foreground right within Duel Arena, preserve readable body-to-environment scale in frame, profile left toward the scene action, Combatants facing off. The subject from image2 is tars tarkas plays against tal hajus in the same frame. Preserve the environment from image3 Massive scale with wide thoroughfares and high-ceilinged communal areas., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially Duel Arena. medium, low angle, wide lens, track, deep focus, high contrast ceremonial. Readable medium composition in featuring. The duel begins between Tars Tarkas and Tal Hajus. Duel Arena. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH024_SC003; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; tal_hajus; lorquas_ptomel
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
- scene_id: CH024_SC003
- chapter_id: CH024
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in thark_city_complex featuring tars_tarkas, tal_hajus, Thark Council Members.
- shot_size: medium
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: tal_hajus
- primary_subject_frame_position: foreground right within Duel Arena
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: Combatants facing off
- subject_relation_summary: tars_tarkas plays against tal_hajus in the same frame
- scene_short_description: A political challenge leads to a ritual duel within a massive assembly chamber.
- shot_moment_summary: The duel begins between Tars Tarkas and Tal Hajus
- required_environment_anchor_1: Duel Arena
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, low angle, wide lens, track, deep focus, high contrast ceremonial
- environment_subzone: Duel Arena
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; tal_hajus; thark_city_complex; DESC_CH024_SC003; DESC_CH024_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: identity reference for the secondary visible subject
- image2_asset: tal hajus
- image3_role: environment reference for the scene location
- image3_asset: thark city complex

# Continuity Notes
- Scene: CH024_SC003 / SC003.
- Variant: Alternate Angle.
- Weaponry used in the duel
- Wounds sustained by Tal Hajus
- Seating arrangements of the council
- The ritual duel between Tars Tarkas and Tal Hajus
- Resolve Thark Council Members -> Thark Council Members
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC003\SH002\DIALOGUE.json
