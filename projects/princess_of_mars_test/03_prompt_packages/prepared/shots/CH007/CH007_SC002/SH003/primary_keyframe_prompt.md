# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH007_SC002_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the environment reference for the incubator enclosure. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A ritualized capture of three-to-four-foot hatchlings emerging from an incubator enclosure. The visible subject is foreground right within gauntlet path, height differential between youths and 4ft Martians, profile left toward the scene action, hatchlings moving toward gauntlet. Preserve the environment from image1 Walled perimeter enclosing a central egg-hatching zone and a communal gathering area., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially the incubator enclosure walls. medium, eye level, wide lens, handheld, deep focus, high contrast ceremonial. Closing composition in that emphasizes the consequence of the ritualized capture gauntlet. the gauntlet intercepts the hatchlings. gauntlet path. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH007_SC002; SHOT_INDEX; DIALOGUE; protagonist; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
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
- scene_id: CH007_SC002
- chapter_id: CH007
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in the_incubator_enclosure that emphasizes the consequence of the ritualized capture gauntlet.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: (none)
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within gauntlet_path
- primary_subject_scale_relation: height differential between youths and 4ft Martians
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: hatchlings moving toward gauntlet
- subject_relation_summary: Martian women/youths carries the frame alone
- scene_short_description: A ritualized capture of three-to-four-foot hatchlings emerging from an incubator enclosure.
- shot_moment_summary: the gauntlet intercepts the hatchlings
- required_environment_anchor_1: the_incubator_enclosure walls
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: height differential between youths and 4ft Martians
- camera_package_description: medium, eye level, wide lens, handheld, deep focus, high contrast ceremonial
- environment_subzone: gauntlet_path
- prompt_family: shot_prompt
- reference_asset_ids: the_incubator_enclosure; DESC_CH007_SC002; DESC_CH007_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: environment reference for the scene location
- image1_asset: the incubator enclosure

# Continuity Notes
- Scene: CH007_SC002 / SC002.
- Variant: Primary Keyframe.
- Physical size of Newly Hatched Martians (3 to 4 feet tall)
- Movement patterns and rhythm of the gauntlet
- The ritualized capture gauntlet
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH007\CH007_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC002\SH003\DIALOGUE.json
