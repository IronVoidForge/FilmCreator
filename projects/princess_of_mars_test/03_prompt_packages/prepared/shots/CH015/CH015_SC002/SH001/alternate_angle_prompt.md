# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH015_SC002_SH001_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Awe/Solemnity. **Likely Visual Coverage Families:** - Extreme wide shots of the massive caravan moving across the moss. - Low-angle shots.... Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with and for spatial orientation.. Characters: . Environment: A featureless, endless expanse with a flat...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH015_SC002; SHOT_INDEX; DIALOGUE
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH015_SC002
- chapter_id: CH015
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across mossy_sea_bottom with John Carter (observing) and various caravan members/warriors for spatial orientation.
- prompt_family: shot_prompt
- reference_asset_ids: mossy_sea_bottom
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH015_SC002 / SC002.
- Variant: Alternate Angle.
- Movement patterns of the large group (hundreds of units).
- Lighting transitions from day travel to night camping.
- The massive caravan (chariots, warriors, beasts) moves silently across the trackless mossy sea bottom.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH015\CH015_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH015\CH015_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH015\CH015_SC002\SH001\DIALOGUE.json
