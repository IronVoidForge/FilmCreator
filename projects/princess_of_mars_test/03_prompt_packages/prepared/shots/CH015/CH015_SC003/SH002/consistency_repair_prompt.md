# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH015_SC003_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Intimacy to Tragic Revelation. **Likely Visual Coverage Families:** - Tight two-shot of Carter and by the fire. - Close-ups on 's face du.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: Young female, Interacts with Tars Tarkas (rec...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH015_SC003; SHOT_INDEX; DIALOGUE; john_carter; sola
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
- scene_id: CH015_SC003
- chapter_id: CH015
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in The Caravan Camp (Night) featuring sola.
- prompt_family: shot_prompt
- reference_asset_ids: sola
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH015_SC003 / SC003.
- Variant: Consistency Repair.
- Firelight/lighting consistency throughout the night setting.
- Character positioning within the camp environment.
- Sola recounts her tragic history, specifically the death of her mother caused by Tal Hajus and Sarkoja.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH015\CH015_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH015\CH015_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH015\CH015_SC003\SH002\DIALOGUE.json
