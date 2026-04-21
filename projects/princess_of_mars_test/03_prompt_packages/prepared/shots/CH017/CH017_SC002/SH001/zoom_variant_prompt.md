# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH017_SC002_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Relief $\rightarrow$ Physical Exhaustion/Desperation. **Likely Visual Coverage Families:** - Wide shots of the vast, empty landscape to e.... Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with, placed for immediate spatial orientation.. Characters: [], unknown, Young female, Interacts with Tars...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH017_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
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
- scene_id: CH017_SC002
- chapter_id: CH017
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across The Mossy Waste (desolate, trackless expanse) with john_carter, dejah_thoris, sola placed for immediate spatial orientation.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; sola
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH017_SC002 / SC002.
- Variant: Tighter Zoom.
- Progressive depletion/state of supplies and water skins
- Increasing levels of dirt and sweat on character skin/costumes
- The group attempts the trek across the Mossy Waste toward Helium.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC002\SH001\DIALOGUE.json
