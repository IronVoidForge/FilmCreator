# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH027_SC001_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Peace/Contentment $\rightarrow$ Tranquility.. Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with, placed for immediate spatial orientation.. Characters: [], unknown. Environment: described environment with stable spatial continuity. Keep continuity exact across c...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH027_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
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
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across The Palace of Helium with john_carter, dejah_thoris placed for immediate spatial orientation.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH027_SC001 / SC001.
- Variant: Consistency Repair.
- Aging/passage of time indicators (clothing, hair, or subtle physical changes)
- Montage sequence establishing years of prosperity in Helium and lush Martian landscapes.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SH001\DIALOGUE.json
