# Title
SH005 Shot Prompt - Primary Keyframe

# ID
CH017_SC001_SH005_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Terror/Despair $\rightarrow$ Sudden Action $\rightarrow$ Relief. **Likely Visual Coverage Families:** - Close-ups on Tal Hajus's cruelty.... Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of carter facilitates a swift escape for dejah and ... Character...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH005
- source_artifact_ids: CH017_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola; tal_hajus
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH017_SC001
- chapter_id: CH017
- shot_type: closing_reaction
- previous_shot_id: SH004
- next_shot_id: (none)
- shot_lineage_ids: SH004; SH005
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in The City of Thark (circular halls/raised platforms) that emphasizes the consequence of carter facilitates a swift escape for dejah and sola..
- prompt_family: shot_prompt
- reference_asset_ids: sola
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH017_SC001 / SC001.
- Variant: Primary Keyframe.
- Precise character positioning on the raised platforms.
- The specific moment/impact of Tal Hajus being incapacitated.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC001\SH005\DIALOGUE.json
