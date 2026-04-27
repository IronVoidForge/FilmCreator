# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH018_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for warhoon subterranean dungeon. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A lone figure undergoes physical and mental decay within a pitch-black subterranean cell. The subject from image1 is protagonist, foreground inside pitch black void, Micro-scale focus on facial textures and eyes against infinite blackness, facing directly toward camera, blank stare. Preserve the environment from image2 Underground prison structure, specific spatial dimensions are unstated., monumental scale, dry open Martian terrain, especially pitch black void. Keep one readable subject anchor: protagonist face. extreme-close-up, eye level, telephoto lens, handheld, shallow subject, low key night. Intimate composition that isolates against to capture the beat's emotional turn. eyes wide in near-madness. pitch black void. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH018_SC004; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: telephoto
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
- scene_id: CH018_SC004
- chapter_id: CH018
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist against warhoon_subterranean_dungeon to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside pitch_black_void
- primary_subject_scale_relation: Micro-scale focus on facial textures and eyes against infinite blackness.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: blank stare
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A lone figure undergoes physical and mental decay within a pitch-black subterranean cell.
- shot_moment_summary: eyes wide in near-madness
- required_environment_anchor_1: pitch_black_void
- required_subject_anchor_1: protagonist face
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Micro-scale focus on facial textures and eyes against infinite blackness.
- camera_package_description: extreme-close-up, eye level, telephoto lens, handheld, shallow subject, low key night
- environment_subzone: pitch_black_void
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; warhoon_subterranean_dungeon; DESC_CH018_SC004; DESC_CH018_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: warhoon subterranean dungeon

# Continuity Notes
- Scene: CH018_SC004 / SC004.
- Variant: Primary Keyframe.
- Protagonist weight loss progression
- Protagonist hair growth and unkemptness
- Transition from clothed combatant to naked state
- Psychological break into near-madness
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC004\SH003\DIALOGUE.json
