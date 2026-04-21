# Title
SH002 Shot Prompt - Tighter Zoom

# ID
CH024_SC006_SH002_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. High tension and stealthy focus.. Tight detail framing focused on a single visual object or gesture.. tighter framing on the same moment. Characters: described character with stable costume and silhouette, . Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette, lighting, and s...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH024_SC006; SHOT_INDEX; DIALOGUE; john_carter; None
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
- scene_id: CH024_SC006
- chapter_id: CH024
- shot_type: insert_detail
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH024_SC006 / Execute the first phase of the infiltration/action sequence..
- Variant: Tighter Zoom.
- Height/Scale of the walls
- lighting on the climbers' faces.
- Carry the emotional arc through: High tension and stealthy focus..
- Resolve Infiltration Team -> Infiltration Team
- Resolve The exterior walls of Zodanga (Carborundum) -> The exterior walls of Zodanga (Carborundum)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC006.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC006\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC006\SH002\DIALOGUE.json
