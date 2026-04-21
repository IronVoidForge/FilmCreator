# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH008_SC001_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Anticipation $\rightarrow$ Sudden Alarm/Tension.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: [], unknown, Young female, Interacts with Tars Tarkas (receives instructions from him)., Commands a "wicked-looking" Martian watch dog.,...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH008_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola
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
- scene_id: CH008_SC001
- chapter_id: CH008
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Deserted Martian City / Valley overlook featuring protagonist, sola.
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; sola
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH008_SC001 / SC001.
- Variant: Consistency Repair.
- Precise positioning of protagonist relative to the city exit during departure
- Synchronized timing of airship descent with the retreat of Green Martian Warriors (background/distant)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC001\SH002\DIALOGUE.json
