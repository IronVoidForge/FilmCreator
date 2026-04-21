# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH001_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Adrenaline $\rightarrow$ Shock/Grief/Desperation.. Active camera with tracking energy and clear spatial orientation.. continuity-preserving framing with exact pose and costume locks. Characters: described character with stable costume and silhouette, . Environment: described environment with stable spatial...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH001_SC004; SHOT_INDEX; DIALOGUE; john_carter; None
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
- scene_id: CH001_SC004
- chapter_id: CH001
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: continuity-preserving framing with exact pose and costume locks
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH001_SC004 / Deliver the emotional gut-punch and shift the tone from action to tra....
- Variant: Consistency Repair.
- Condition of Powell's clothing/body
- Presence of arrows
- Direction of pursuit.
- Carry the emotional arc through: Adrenaline $\rightarrow$ Shock/Grief/Desperation..
- Resolve Captain James K. Powell (deceased) -> Captain James K. Powell (deceased)
- Resolve The plateau/skirmish site -> The plateau/skirmish site
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC004\SH002\DIALOGUE.json
