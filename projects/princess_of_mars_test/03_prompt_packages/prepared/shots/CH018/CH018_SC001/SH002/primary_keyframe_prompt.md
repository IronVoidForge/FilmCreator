# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH018_SC001_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for female healer. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for warhoon camp interior. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A wounded man regains consciousness in a camp before being bound to a beast for transport. The subject from image1 is An ancient, ugly Warhoon woman., Ancient / Elderly, lean athletic build, Warhoon culture/setting, foreground inside warhoon camp interior, preserve readable body-to-environment scale in frame, front three-quarter left toward the scene action, healer enters frame. The subject from image2 is female healer plays against protagonist in the same frame. Preserve the environment from image3 Cramped, enclosed tent interior., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially warhoon camp interior. Keep one readable subject anchor: healer's hands. medium shot of facial texture. medium-close, high angle, normal lens, push in, rack focus, torch firelight. Intimate composition that isolates, against to capture the beat's emotional turn. healer's face approaching. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH018_SC001; SHOT_INDEX; DIALOGUE; protagonist; female_healer
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
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
- scene_id: CH018_SC001
- chapter_id: CH018
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates female_healer, protagonist against warhoon_camp_interior to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: high_angle
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: torch_firelight
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: female_healer
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground inside warhoon_camp_interior
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: healer enters frame
- subject_relation_summary: female_healer plays against protagonist in the same frame
- scene_short_description: A wounded man regains consciousness in a camp before being bound to a beast for transport.
- shot_moment_summary: healer's face approaching
- required_environment_anchor_1: warhoon_camp_interior
- required_subject_anchor_1: healer's hands
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: medium shot of facial texture
- camera_package_description: medium-close, high angle, normal lens, push in, rack focus, torch firelight
- environment_subzone: warhoon_camp_interior
- prompt_family: shot_prompt
- reference_asset_ids: female_healer; protagonist; warhoon_camp_interior; DESC_CH018_SC001; DESC_CH018_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: female healer
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: warhoon camp interior

# Continuity Notes
- Scene: CH018_SC001 / SC001.
- Variant: Primary Keyframe.
- Wound placement and severity on naked protagonist
- Grotesque medical treatment
- Binding/strap tension and configuration to the thoat
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC001\SH002\DIALOGUE.json
