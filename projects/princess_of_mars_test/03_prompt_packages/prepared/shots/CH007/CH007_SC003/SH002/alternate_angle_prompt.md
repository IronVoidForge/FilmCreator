# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH007_SC003_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for martian warriors. Use image2 as the environment reference for the incubator enclosure. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Massive four-armed humanoids perform heavy labor transporting eggs from dark vaults to an incubator. The subject from image1 is eggs, foreground right within Transit Path, preserve readable body-to-environment scale in frame, profile left toward the scene action, movement begins. Preserve the environment from image2 Walled perimeter enclosing a central egg-hatching zone and a communal gathering area., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially Transit Path. medium-full, eye level, normal lens, track, shallow subject, diffuse ambient. Readable medium composition in featuring. montage of transport. Transit Path. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH007_SC003; SHOT_INDEX; DIALOGUE; martian_warriors
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
- scene_id: CH007_SC003
- chapter_id: CH007
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in the_incubator_enclosure featuring martian_warriors.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: martian_warriors
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within Transit Path
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: movement begins
- subject_relation_summary: eggs carries the frame alone
- scene_short_description: Massive four-armed humanoids perform heavy labor transporting eggs from dark vaults to an incubator.
- shot_moment_summary: montage of transport
- required_environment_anchor_1: Transit Path
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-full, eye level, normal lens, track, shallow subject, diffuse ambient
- environment_subzone: Transit Path
- prompt_family: shot_prompt
- reference_asset_ids: martian_warriors; the_incubator_enclosure; DESC_CH007_SC003; DESC_CH007_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: martian warriors
- image2_role: environment reference for the scene location
- image2_asset: the incubator enclosure

# Continuity Notes
- Scene: CH007_SC003 / SC003.
- Variant: Alternate Angle.
- Egg appearance and handling consistency
- Lighting transitions from Subterranean Vaults to the_incubator_enclosure
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH007\CH007_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC003\SH002\DIALOGUE.json
