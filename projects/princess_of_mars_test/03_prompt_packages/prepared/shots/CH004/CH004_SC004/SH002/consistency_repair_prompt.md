# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH004_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sola. Use image2 as the environment reference for martian sleeping quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A weary traveler is led through hallways into a warm, decorated chamber containing a strange creature. The subject from image1 is * The Narrator, foreground right within martian sleeping quarters, Humanoid scale interaction between sola and The Narrator, front three-quarter right toward the scene action, entering chamber. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially martian sleeping quarters. medium, eye level, portrait lens, push in, zoom subtle in, shallow subject, soft even. Readable medium composition in featuring. narrator enters the decorated room and settles. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH004_SC004; SHOT_INDEX; DIALOGUE; sola
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH004_SC004
- chapter_id: CH004
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in martian_sleeping_quarters featuring * The Narrator, sola.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within martian_sleeping_quarters
- primary_subject_scale_relation: Humanoid scale interaction between sola and The Narrator.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: entering chamber
- subject_relation_summary: * The Narrator carries the frame alone
- scene_short_description: A weary traveler is led through hallways into a warm, decorated chamber containing a strange creature.
- shot_moment_summary: narrator enters the decorated room and settles
- required_environment_anchor_1: martian_sleeping_quarters
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Humanoid scale interaction between sola and The Narrator.
- camera_package_description: medium, eye level, portrait lens, push in, zoom subtle in, shallow subject, soft even
- environment_subzone: martian_sleeping_quarters
- prompt_family: shot_prompt
- reference_asset_ids: sola; martian_sleeping_quarters; DESC_CH004_SC004; DESC_CH004_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: environment reference for the scene location
- image2_asset: martian sleeping quarters

# Continuity Notes
- Scene: CH004_SC004 / SC004.
- Variant: Consistency Repair.
- Movement and limb count of the ten-legged creature
- Lighting transition from grand hall to private quarters
- Arrival and respite
- Resolve * The Narrator -> * The Narrator
- Resolve * Interior Hallways -> * Interior Hallways
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC004\SH002\DIALOGUE.json
