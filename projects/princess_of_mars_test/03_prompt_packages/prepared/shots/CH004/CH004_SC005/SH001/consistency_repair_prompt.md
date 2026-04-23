# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH004_SC005_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Fatigue $\rightarrow$ Curiosity/Uncanniness. **Likely Visual Coverage Families:** * Medium shots of the chamber's decor. * Close-ups on t.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: . Environment: Cavernous interior with high v...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH004_SC005; SHOT_INDEX; DIALOGUE; sola
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
- scene_id: CH004_SC005
- chapter_id: CH004
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in grand_audience_chamber featuring The Narrator.
- prompt_family: shot_prompt
- reference_asset_ids: grand_audience_chamber; DESC_CH004_SC005; DESC_CH004_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH004_SC005 / Provide a moment of respite and introduce local fauna, grounding the....
- Variant: Consistency Repair.
- The appearance and movement of the small creature
- the level of light in the room.
- Sola leads the Narrator to a decorated sleeping chamber. Inside
- the Narrator encounters a strange ten-legged Martian creature with a frog-like head and tusks.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC005\SH001\DIALOGUE.json
