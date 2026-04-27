# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH015_SC003_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sola. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for caravan camp hills. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A private nocturnal confession shared between two characters by a dying campfire. The subject from image1 is sola, foreground inside campfire radius, Small intimate scale within a vast night environment, front three-quarter right toward the scene action, seated facing fire. The subject from image2 is sola plays against john carter in the same frame. Preserve the environment from image3 Located at the foot of rising hills where the terrain transitions from the flat mossy sea to elevated topography., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially campfire. medium-close, eye level, normal lens, locked off, shallow subject, torch firelight. Intimate composition that ites, against to capture the beat's emotional turn. Sola begins speaking of her isolation. campfire radius. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH015_SC003; SHOT_INDEX; DIALOGUE; john_carter; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
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
- scene_id: CH015_SC003
- chapter_id: CH015
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that ites reaction and emotional emphasis.
- composition: Intimate composition that isolates sola, john_carter against caravan_camp_hills to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: torch_firelight
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside campfire_radius
- primary_subject_scale_relation: Small intimate scale within a vast night environment.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: seated facing fire
- subject_relation_summary: sola plays against john_carter in the same frame
- scene_short_description: A private nocturnal confession shared between two characters by a dying campfire.
- shot_moment_summary: Sola begins speaking of her isolation
- required_environment_anchor_1: campfire
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Small intimate scale within a vast night environment.
- camera_package_description: medium-close, eye level, normal lens, locked off, shallow subject, torch firelight
- environment_subzone: campfire_radius
- prompt_family: shot_prompt
- reference_asset_ids: sola; john_carter; caravan_camp_hills; DESC_CH015_SC003; DESC_CH015_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: caravan camp hills

# Continuity Notes
- Scene: CH015_SC003 / SC003.
- Variant: Primary Keyframe.
- Lighting consistency relative to campfire flicker
- Character positioning relative to the fire source
- Sola shares her status as an outcast due to emotion
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH015\CH015_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH015\CH015_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH015\CH015_SC003\SH001\DIALOGUE.json
