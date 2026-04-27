# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH018_SC005_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for warhoon subterranean dungeon. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A naked man ambushes a deliverer with a heavy chain in a pitch-black dungeon. The subject from image1 is protagonist, foreground inside subterranean dungeon darkness, chain length vs protagonist height, profile left toward the scene action, protagonist coiled in dark. Preserve the environment from image2 Underground prison structure, specific spatial dimensions are unstated., monumental scale, dry open Martian terrain, especially subterranean dungeon darkness. medium-close, low angle, normal lens, handheld, shallow subject, low key night. Intimate composition that isolates, against to capture the beat's emotional turn. protagonist waiting in shadows. subterranean dungeon darkness. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH018_SC005; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
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
- scene_id: CH018_SC005
- chapter_id: CH018
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist, Jailer (deceased) against warhoon_subterranean_dungeon to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: silhouette
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside subterranean_dungeon_darkness
- primary_subject_scale_relation: chain length vs protagonist height
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: protagonist coiled in dark
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A naked man ambushes a deliverer with a heavy chain in a pitch-black dungeon.
- shot_moment_summary: protagonist waiting in shadows
- required_environment_anchor_1: subterranean_dungeon_darkness
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: chain length vs protagonist height
- camera_package_description: medium-close, low angle, normal lens, handheld, shallow subject, low key night
- environment_subzone: subterranean_dungeon_darkness
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; warhoon_subterranean_dungeon; DESC_CH018_SC005; DESC_CH018_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: warhoon subterranean dungeon

# Continuity Notes
- Scene: CH018_SC005 / SC005.
- Variant: Alternate Angle.
- Heavy chain weapon state and handling
- Precise positioning of jailer's keys after kill
- Timing of glowing eyes relative to protagonist movement
- Protagonist stalks jailer in darkness
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC005\SH001\DIALOGUE.json
