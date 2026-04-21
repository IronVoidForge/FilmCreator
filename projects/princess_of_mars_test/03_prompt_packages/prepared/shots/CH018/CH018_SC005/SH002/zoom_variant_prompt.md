# Title
SH002 Shot Prompt - Tighter Zoom

# ID
CH018_SC005_SH002_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Desperation $\rightarrow$ Primal Violence $\rightarrow$ Sudden Clarity/Hope. **Likely Visual Coverage Families:** - High-tension close-up.... Stable medium framing that keeps action and character readable.. tighter framing on the same moment. Characters: described character with stable costume and silhouette. Environment: described enviro...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH018_SC005; SHOT_INDEX; DIALOGUE; protagonist; None
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
- scene_id: CH018_SC005
- chapter_id: CH018
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH018_SC005 / To provide a moment of violent agency and a potential path to escape..
- Variant: Tighter Zoom.
- Position of the corpse
- state of the chains
- lighting (minimal light source from the door).
- Carry the emotional arc through: Desperation $\rightarrow$ Primal Violence $\rightarrow$ Sudden Clarity/Hope.
- **Likely Visual Coverage Families:**
- - High-tension close-ups of the protagonist's movement in the dark.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC005\SH002\DIALOGUE.json
