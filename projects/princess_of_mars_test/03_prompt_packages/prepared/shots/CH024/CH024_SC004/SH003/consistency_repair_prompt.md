# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH024_SC004_SH003_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Solemnity to Inspiration/Aggression.. Controlled closing frame that lands the consequence of the beat.. continuity-preserving framing with exact pose and costume locks. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH024_SC004; SHOT_INDEX; DIALOGUE; tars_tarkas; john_carter; thark_warriors
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
- scene_id: CH024_SC004
- chapter_id: CH024
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: continuity-preserving framing with exact pose and costume locks
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH024_SC004 / Establish the new status quo and set the primary mission objective..
- Variant: Consistency Repair.
- Regalia or markings denoting new ranks.
- Land the scene consequence or transition cleanly.
- Resolve The Thark Palace/Assembly area -> The Thark Palace/Assembly area
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC004\SH003\DIALOGUE.json
