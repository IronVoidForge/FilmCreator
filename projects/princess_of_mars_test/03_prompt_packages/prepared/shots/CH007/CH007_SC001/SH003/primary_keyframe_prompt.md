# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH007_SC001_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for the incubator enclosure. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A massive procession of decorated chariots travels across a desert floor toward an incubator site. The subject from image1 is protagonist, foreground right within the incubator enclosure, leap height vs chariot width, profile left toward the scene action, running toward line. Preserve the environment from image2 Walled perimeter enclosing a central egg-hatching zone and a communal gathering area., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially the incubator enclosure. full, low angle, wide lens, track, shallow subject, high contrast ceremonial. Closing composition in that emphasizes the consequence of performs the leap. protagonist leaps over parked chariots. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH007_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola; lorquas_ptomel_jed
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
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
- scene_id: CH007_SC001
- chapter_id: CH007
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in the_incubator_enclosure that emphasizes the consequence of the protagonist performs the leap.
- shot_size: full
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within the_incubator_enclosure
- primary_subject_scale_relation: leap height vs chariot width
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: running toward line
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A massive procession of decorated chariots travels across a desert floor toward an incubator site.
- shot_moment_summary: protagonist leaps over parked chariots
- required_environment_anchor_1: the_incubator_enclosure
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: leap height vs chariot width
- camera_package_description: full, low angle, wide lens, track, shallow subject, high contrast ceremonial
- environment_subzone: the_incubator_enclosure
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; the_incubator_enclosure; DESC_CH007_SC001; DESC_CH007_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: the incubator enclosure

# Continuity Notes
- Scene: CH007_SC001 / SC001.
- Variant: Primary Keyframe.
- Chariot decoration patterns must remain consistent
- Physical height ratio between enormous beasts and protagonist
- Sequential order of chariot jump obstacles
- Chariot decoration patterns must remain consistent across wide and medium shots
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH007\CH007_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC001\SH003\DIALOGUE.json
