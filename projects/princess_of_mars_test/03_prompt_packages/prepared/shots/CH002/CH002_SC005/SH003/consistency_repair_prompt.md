# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH002_SC005_SH003_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. From mesmerized trance to sudden, overwhelming cosmic displacement. **Likely Visual Coverage Families:** - Extreme Wide shots of the land.... Stable medium framing that transitions into violent motion/displacement.. Readable medium composition featuring during displacement.. Characters: . Environment: descr...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH002_SC005; SHOT_INDEX; DIALOGUE
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
- scene_id: CH002_SC005
- chapter_id: CH002
- shot_type: medium
- previous_shot_id: SH002
- next_shot_id: SH004
- shot_lineage_ids: SH002; SH003; SH004
- camera_description: Stable medium framing that transitions into violent motion/displacement.
- composition: Readable medium composition featuring scene_character during displacement.
- prompt_family: shot_prompt
- reference_asset_ids: DESC_CH002_SC005; DESC_CH002_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH002_SC005 / To trigger the protagonist's cosmic displacement and end the chapter....
- Variant: Consistency Repair.
- As he closes his eyes
- He is violently transported through space into darkness and cold
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SH003\DIALOGUE.json
