# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH025_SC002_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for audience chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A formal ceremony is violently interrupted by a man smashing through a window and leaping into the hall. The subject from image1 is john carter, foreground right within ritual center, Large scale audience chamber vs single intruder, facing directly toward camera, mid-air leap. The subject from image2 is john carter plays against dejah thoris in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially ritual center. full, low angle, wide lens, track, zoom subtle in, rack focus, high contrast ceremonial. Closing composition in that emphasizes the consequence of impact and disruption. Carter landing and breaking chains. ritual center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH025_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sab_than; than_kosis
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
- scene_id: CH025_SC002
- chapter_id: CH025
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in audience_chamber that emphasizes the consequence of impact and disruption.
- shot_size: full
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: subtle_in
- focus_strategy: rack_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: dejah_thoris
- primary_subject_frame_position: foreground right within ritual_center
- primary_subject_scale_relation: Large scale audience chamber vs single intruder.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: mid-air leap
- subject_relation_summary: john_carter plays against dejah_thoris in the same frame
- scene_short_description: A formal ceremony is violently interrupted by a man smashing through a window and leaping into the hall.
- shot_moment_summary: Carter landing and breaking chains
- required_environment_anchor_1: ritual_center
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Large scale audience chamber vs single intruder.
- camera_package_description: full, low angle, wide lens, track, zoom subtle in, rack focus, high contrast ceremonial
- environment_subzone: ritual_center
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; audience_chamber; DESC_CH025_SC002; DESC_CH025_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: audience chamber

# Continuity Notes
- Scene: CH025_SC002 / SC002.
- Variant: Alternate Angle.
- Broken state of golden chains
- Scattered glass shards on floor
- Dejah Thoris ceremonial attire integrity
- Impact and disruption
- Resolve Zodangan Nobility/Guards -> Zodangan Nobility/Guards
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH025\CH025_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC002\SH003\DIALOGUE.json
