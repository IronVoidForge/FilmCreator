# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH006_SC005_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian interior chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A quieted interior chamber where a survivor reflects on his dual bonds amidst the stillness. The subject from image1 is protagonist, foreground inside martian interior chamber window zone, The scale of individual emotional connection vs. the vastness of Martian survival, profile left toward the scene action, staring into distance. The subject from image2 is protagonist plays against sola in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially martian interior chamber window zone. close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, soft even. Intimate composition that ites, against to capture the beat's emotional turn. Protagonist reflects on Sola and Watch-thing in the quiet aftermath. window zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH006_SC005; SHOT_INDEX; DIALOGUE; protagonist; sola; tars_tarkas; watch_thing
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
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
- scene_id: CH006_SC005
- chapter_id: CH006
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that ites reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist, sola against martian_interior_chamber to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: internal_monologue
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: sola
- primary_subject_frame_position: foreground inside martian_interior_chamber window zone
- primary_subject_scale_relation: The scale of individual emotional connection vs. the vastness of Martian survival.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: staring into distance
- subject_relation_summary: protagonist plays against sola in the same frame
- scene_short_description: A quieted interior chamber where a survivor reflects on his dual bonds amidst the stillness.
- shot_moment_summary: Protagonist reflects on Sola and Watch-thing in the quiet aftermath.
- required_environment_anchor_1: martian_interior_chamber window zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: The scale of individual emotional connection vs. the vastness of Martian survival.
- camera_package_description: close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, soft even
- environment_subzone: martian_interior_chamber window zone
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; sola; martian_interior_chamber; DESC_CH006_SC005; DESC_CH006_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber

# Continuity Notes
- Scene: CH006_SC005 / SC005.
- Variant: Primary Keyframe.
- Post-battle physical state (bruises, dirt)
- Protagonist nudity/metamorphosis status
- The aftermath of the concession settles into silence
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC005\SH002\DIALOGUE.json
