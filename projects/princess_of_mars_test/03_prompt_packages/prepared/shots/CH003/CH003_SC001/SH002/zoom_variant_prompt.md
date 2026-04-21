# Title
SH002 Shot Prompt - Tighter Zoom

# ID
CH003_SC001_SH002_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Confusion $\rightarrow$ Physical Bewilderment/Surprise. **Likely Visual Coverage Families:** - Wide shots of the Martian landscape. - Med.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: [], unknown. Environment: described environment with stable spatial continuit...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC001; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: zoom_variant
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: zoom_variant
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH003_SC001
- chapter_id: CH003
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in A circular basin on Mars covered in yellowish featuring protagonist.
- prompt_family: shot_prompt
- reference_asset_ids: protagonist
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH003_SC001 / SC001.
- Variant: Tighter Zoom.
- Leap height and distance consistency
- Protagonist's physical state (nakedness/exposure)
- The protagonist attempts to move, discovering the effects of low gravity.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SH002\DIALOGUE.json
