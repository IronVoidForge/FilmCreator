# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH001_SC005_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Exhaustion/Fear $\rightarrow$ Confusion $\rightarrow$ Unnatural Lethargy.. Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with placed for immediate spatial orientation.. Characters: described character with stable costume and silhouette. Environment: described env...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH001_SC005; SHOT_INDEX; DIALOGUE; john_carter; None
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: neutral_reference
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
- scene_id: CH001_SC005
- chapter_id: CH001
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across Cliffside trail with john_carter placed for immediate spatial orientation.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH001_SC005 / Introduce the supernatural element and transition to the next narrati....
- Variant: Consistency Repair.
- Lighting transition (outdoor light to cave darkness)
- Carter's physical state (sweat/dirt).
- Carter's horse leads him to a large cave at the end of a cliffside trail. After checking Powell
- Carter enters the cave to scout it
- only to be overcome by an unnatural drowsiness that causes him to collapse.
- Resolve Captain James K. Powell (body) -> Captain James K. Powell (body)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC005\SH001\DIALOGUE.json
