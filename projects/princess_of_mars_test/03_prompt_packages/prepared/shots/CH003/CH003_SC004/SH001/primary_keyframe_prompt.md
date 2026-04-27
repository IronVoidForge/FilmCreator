# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH003_SC004_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian incubator enclosure. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A naked, agile fighter leaps thirty feet over a glass enclosure to escape a spear. The subject from image1 is protagonist, foreground inside martian incubator enclosure, spear length vs body, profile left toward the scene action, protagonist cornered. The subject from image2 is protagonist plays against martian warriors in the same frame. Preserve the environment from image3 Low walled enclosure containing an incubator area., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian incubator enclosure. medium-close, low angle, normal lens, handheld, shallow subject, diffuse ambient. Intimate composition that isolates, against to capture the beat's emotional turn. spear tip nears protagonist. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH003_SC004; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
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
- scene_id: CH003_SC004
- chapter_id: CH003
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist, martian_warriors against martian_incubator_enclosure to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: martian_warriors
- primary_subject_frame_position: foreground inside martian_incubator_enclosure
- primary_subject_scale_relation: spear length vs body
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: protagonist cornered
- subject_relation_summary: protagonist plays against martian_warriors in the same frame
- scene_short_description: A naked, agile fighter leaps thirty feet over a glass enclosure to escape a spear.
- shot_moment_summary: spear tip nears protagonist
- required_environment_anchor_1: martian_incubator_enclosure
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: spear length vs body
- camera_package_description: medium-close, low angle, normal lens, handheld, shallow subject, diffuse ambient
- environment_subzone: martian_incubator_enclosure
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; martian_warriors; martian_incubator_enclosure; DESC_CH003_SC004; DESC_CH003_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: martian warriors
- image3_role: environment reference for the scene location
- image3_asset: martian incubator enclosure

# Continuity Notes
- Scene: CH003_SC004 / SC004.
- Variant: Primary Keyframe.
- Precise landing point relative to the jump origin
- Proximity of spear tip to protagonist during flight
- Trajectory arc height over martian_incubator_enclosure
- Protagonist faces spear threat
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SH001\DIALOGUE.json
