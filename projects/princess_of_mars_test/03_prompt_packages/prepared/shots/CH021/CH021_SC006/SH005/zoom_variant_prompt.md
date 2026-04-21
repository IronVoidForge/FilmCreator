# Title
SH005 Shot Prompt - Tighter Zoom

# ID
CH021_SC006_SH005_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Tension $\rightarrow$ Triumph/Grandeur.. Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with crossing the frame and maintaining readable movement.. Characters: [], No visual data provided in the evidence., unknown. Environment: described environment with stable spatial continuity. Keep continuity...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH005
- source_artifact_ids: CH021_SC006; SHOT_INDEX; DIALOGUE; john_carter; than_kosis; zodangan_scout
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
- scene_id: CH021_SC006
- chapter_id: CH021
- shot_type: action
- previous_shot_id: SH004
- next_shot_id: (none)
- shot_lineage_ids: SH004; SH005
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in Zodanga Central Plaza (ceremonial setting) with than_kosis crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: than_kosis
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH021_SC006 / SC006.
- Variant: Tighter Zoom.
- Carter's new uniform or insignia must be clearly established
- Presence and condition of the rescued scout
- Resolve Zodangan Military/Crowd -> Zodangan Military/Crowd
- Resolve Zodanga Central Plaza (ceremonial setting) -> Zodanga Central Plaza (ceremonial setting)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC006.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC006\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC006\SH005\DIALOGUE.json
