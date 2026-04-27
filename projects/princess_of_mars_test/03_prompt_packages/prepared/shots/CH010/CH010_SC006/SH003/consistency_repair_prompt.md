# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH010_SC006_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for lorquas ptomel audience chamber. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A group consisting of a man, a woman, and a creature exits a massive ceremonial hall. The subject from image1 is dejah thoris, midground inside thark audience chamber hallways, length of hallway vs character size, back to camera with head turned toward the action, group entering hallway. The subject from image2 is dejah thoris plays against john carter, woola in the same frame. Preserve the environment from image3 Large scale, centered around a focal point for the presiding chieftain., monumental scale, dry open Martian terrain, especially hallway corridor walls. Keep one readable subject anchor: back to camera with head turned toward the action. wide, eye level, ultra-wide lens, track, deep focus, low key night. Wide composition across placed for immediate spatial orientation. the group recedes into the distance of the hallway. thark audience chamber hallways. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH010_SC006; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; woola
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: ultra_wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH010_SC006
- chapter_id: CH010
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across lorquas_ptomel_audience_chamber with dejah_thoris, john_carter, woola placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: back
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: john_carter; woola
- primary_subject_frame_position: midground inside thark_audience_chamber hallways
- primary_subject_scale_relation: length of hallway vs character size
- primary_subject_facing_direction: back to camera with head turned toward the action
- primary_subject_pose_description: group entering hallway
- subject_relation_summary: dejah_thoris plays against john_carter, woola in the same frame
- scene_short_description: A group consisting of a man, a woman, and a creature exits a massive ceremonial hall.
- shot_moment_summary: the group recedes into the distance of the hallway
- required_environment_anchor_1: hallway corridor walls
- required_subject_anchor_1: back to camera with head turned toward the action
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: length of hallway vs character size
- camera_package_description: wide, eye level, ultra-wide lens, track, deep focus, low key night
- environment_subzone: thark_audience_chamber hallways
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; john_carter; woola; lorquas_ptomel_audience_chamber; DESC_CH010_SC006; DESC_CH010_SC006_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: lorquas ptomel audience chamber
- image4_role: identity reference for an additional visible subject
- image4_asset: woola

# Continuity Notes
- Scene: CH010_SC006 / SC006.
- Variant: Consistency Repair.
- Tight grouping of john_carter, dejah_thoris, and woola
- Consistent character spacing during movement through hallways
- Movement into the hallways
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC006.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC006\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC006\SH003\DIALOGUE.json
