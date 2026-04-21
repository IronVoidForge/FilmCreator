# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH010_SC006_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Resignation to a tentative, uneasy freedom.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuity ex...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH010_SC006; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tars_tarkas; woola
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
- scene_id: CH010_SC006
- chapter_id: CH010
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Exit of the Council Chamber featuring john_carter, dejah_thoris.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH010_SC006 / Resolution and transition to next chapter..
- Variant: Consistency Repair.
- Group formation/walking order.
- Carry the emotional arc through: Resignation to a tentative
- uneasy freedom..
- Resolve Exit of the Council Chamber -> Exit of the Council Chamber
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC006.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC006\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC006\SH002\DIALOGUE.json
