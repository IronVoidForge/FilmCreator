# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH007_SC001_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the incubator enclosure. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A massive procession of decorated chariots travels across a desert floor toward an incubator site. The subject from image1 is protagonist, foreground right within dead sea bottom, beast size vs protagonist, front three-quarter right toward the scene action, riding. The subject from image2 is protagonist plays against sola in the same frame. Preserve the environment from image3 Walled perimeter enclosing a central egg-hatching zone and a communal gathering area., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially dead sea bottom. medium, eye level, normal lens, track, shallow subject, diffuse ambient. Readable medium composition in featuring. protagonist riding with sola. dead sea bottom. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH007_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola; lorquas_ptomel_jed
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
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
- scene_id: CH007_SC001
- chapter_id: CH007
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in the_incubator_enclosure featuring protagonist, sola, various Martian warriors/drivers.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: sola
- primary_subject_frame_position: foreground right within dead_sea_bottom
- primary_subject_scale_relation: beast size vs protagonist
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: riding
- subject_relation_summary: protagonist plays against sola in the same frame
- scene_short_description: A massive procession of decorated chariots travels across a desert floor toward an incubator site.
- shot_moment_summary: protagonist riding with sola
- required_environment_anchor_1: dead_sea_bottom
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: beast size vs protagonist
- camera_package_description: medium, eye level, normal lens, track, shallow subject, diffuse ambient
- environment_subzone: dead_sea_bottom
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; sola; the_incubator_enclosure; DESC_CH007_SC001; DESC_CH007_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: the incubator enclosure

# Continuity Notes
- Scene: CH007_SC001 / SC001.
- Variant: Consistency Repair.
- Chariot decoration patterns must remain consistent
- Physical height ratio between enormous beasts and protagonist
- Chariot decoration patterns must remain consistent across wide and medium shots
- Sequential order of chariot jump obstacles
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH007\CH007_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC001\SH002\DIALOGUE.json
