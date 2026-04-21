# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH024_SC002_SH003_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Exhaustion $\rightarrow$ Relief/Joy.. Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of emotional shift from exhaustion to relief/joy as the bond is established/reaffirmed... Characters: [], unknown, [], No visual description is provi...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH024_SC002; SHOT_INDEX; DIALOGUE; john_carter; woola
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
- scene_id: CH024_SC002
- chapter_id: CH024
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in The Battlefield that emphasizes the consequence of emotional shift from exhaustion to relief/joy as the bond is established/reaffirmed..
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; woola
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH024_SC002 / SC002.
- Variant: Consistency Repair.
- Dirt/blood on Carter's clothing
- Woola's physical state
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC002\SH003\DIALOGUE.json
