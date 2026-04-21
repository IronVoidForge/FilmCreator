# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH025_SC004_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. From the grimness of war to romantic intimacy and profound connection. **Likely Visual Coverage Families:** - Medium close-ups of the cou.... Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with and for spatial orientation.. Characters: [], unknown. Environment: described environment with stable...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH025_SC004; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
- reference_mode: shot_prompt_bundle
- variant_name: zoom_variant
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: zoom_variant
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH025_SC004
- chapter_id: CH025
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across The Throne Room (post-battle) with john_carter and dejah_thoris for spatial orientation.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH025_SC004 / SC004.
- Variant: Tighter Zoom.
- Costume damage (blood/dust) on john_carter and dejah_thoris
- Lighting level consistency relative to SC002
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH025\CH025_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC004\SH001\DIALOGUE.json
