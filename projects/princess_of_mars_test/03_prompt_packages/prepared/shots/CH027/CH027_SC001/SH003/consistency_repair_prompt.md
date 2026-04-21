# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH027_SC001_SH003_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Contentment/Peace $\rightarrow$ Panic/Urgency. **Likely Visual Coverage Families:** - Warm, golden-hued close-ups of the incubator and th.... Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of land the scene consequence or transition c...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH027_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tardos_mors; None
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
- scene_id: CH027_SC001
- chapter_id: CH027
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in The Palace in Helium (Rooftop Shrine/Sunken Garden) that emphasizes the consequence of land the scene consequence or transition cleanly..
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH027_SC001 / Establish the status quo of peace and introduce the inciting incident....
- Variant: Consistency Repair.
- The appearance/age of the characters over the nine-year jump
- the physical state of the golden incubator.
- Land the scene consequence or transition cleanly.
- Resolve Dispatch Bearer -> Dispatch Bearer
- Resolve The Palace in Helium (Rooftop Shrine/Sunken Garden) -> The Palace in Helium (Rooftop Shrine/Sunken Garden)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SH003\DIALOGUE.json
