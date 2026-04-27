# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH004_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the environment reference for martian sleeping quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A weary traveler is led through hallways into a warm, decorated chamber containing a strange creature. The visible subject is foreground inside martian sleeping quarters, Humanoid scale interaction between sola and The Narrator, facing directly toward camera, narrator noticing movement. Preserve the environment from image1 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially martian sleeping quarters. Keep one readable subject anchor: creature on floor/surface. close-up, low angle, telephoto lens, locked off, shallow subject, soft even. Intimate composition that isolates The Narrator against to capture the beat's emotional turn. close up of the ten-legged creature. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH004_SC004; SHOT_INDEX; DIALOGUE; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: telephoto
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: SH003: visible primary subject id is missing for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH004_SC004
- chapter_id: CH004
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates The Narrator against martian_sleeping_quarters to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: (none)
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside martian_sleeping_quarters
- primary_subject_scale_relation: Humanoid scale interaction between sola and The Narrator.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: narrator noticing movement
- subject_relation_summary: ten-legged creature carries the frame alone
- scene_short_description: A weary traveler is led through hallways into a warm, decorated chamber containing a strange creature.
- shot_moment_summary: close up of the ten-legged creature
- required_environment_anchor_1: martian_sleeping_quarters
- required_subject_anchor_1: creature on floor/surface
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Humanoid scale interaction between sola and The Narrator.
- camera_package_description: close-up, low angle, telephoto lens, locked off, shallow subject, soft even
- environment_subzone: martian_sleeping_quarters
- prompt_family: shot_prompt
- reference_asset_ids: martian_sleeping_quarters; DESC_CH004_SC004; DESC_CH004_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: environment reference for the scene location
- image1_asset: martian sleeping quarters

# Continuity Notes
- Scene: CH004_SC004 / SC004.
- Variant: Primary Keyframe.
- Movement and limb count of the ten-legged creature
- Lighting transition from grand hall to private quarters
- Discovery of the creature
- Resolve The Narrator -> The Narrator
- Resolve Interior Hallways -> Interior Hallways
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC004\SH003\DIALOGUE.json
