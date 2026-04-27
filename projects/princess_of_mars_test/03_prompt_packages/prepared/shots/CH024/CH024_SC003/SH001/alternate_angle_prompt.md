# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH024_SC003_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for thark city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A political challenge leads to a ritual duel within a massive assembly chamber. The subject from image1 is john carter, foreground inside Council Seating Zone, Scale of council vs single human, front three-quarter right toward the scene action, Carter standing alone. The subject from image2 is john carter plays against tal hajus in the same frame. Preserve the environment from image3 Massive scale with wide thoroughfares and high-ceilinged communal areas., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially Council Seating Zone. medium-close, eye level, portrait lens, push in, zoom subtle in, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. John Carter challenges Tal Hajus's fitness to rule. Council Seating Zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH024_SC003; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; tal_hajus; lorquas_ptomel
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
- scene_id: CH024_SC003
- chapter_id: CH024
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, tal_hajus against thark_city_complex to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: tal_hajus
- primary_subject_frame_position: foreground inside Council Seating Zone
- primary_subject_scale_relation: Scale of council vs single human
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Carter standing alone
- subject_relation_summary: john_carter plays against tal_hajus in the same frame
- scene_short_description: A political challenge leads to a ritual duel within a massive assembly chamber.
- shot_moment_summary: John Carter challenges Tal Hajus's fitness to rule
- required_environment_anchor_1: Council Seating Zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Scale of council vs single human
- camera_package_description: medium-close, eye level, portrait lens, push in, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: Council Seating Zone
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tal_hajus; thark_city_complex; DESC_CH024_SC003; DESC_CH024_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
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
- John Carter challenges Tal Hajus's fitness to rule
- Resolve Thark Council Members -> Thark Council Members
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC003\SH001\DIALOGUE.json
