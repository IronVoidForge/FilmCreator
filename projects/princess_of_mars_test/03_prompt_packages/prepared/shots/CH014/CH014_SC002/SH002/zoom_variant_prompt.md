# Title
SH002 Shot Prompt - Tighter Zoom

# ID
CH014_SC002_SH002_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Protest/Conflict $\rightarrow$ Quiet Compassion $\rightarrow$ Growing Dread.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuity ex...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH014_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tars_tarkas; sarkoja; zad
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
- scene_id: CH014_SC002
- chapter_id: CH014
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Camp/Chariot staging area featuring tars_tarkas.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH014_SC002 / Establish the logistical tension and the power dynamics within the gr....
- Variant: Tighter Zoom.
- The state of Dejah's fetters/chains
- the positioning of the chariot.
- Carter protests the heavy chains on Dejah's chariot
- which Tars Tarkas defends as necessary security.
- Resolve Camp/Chariot staging area -> Camp/Chariot staging area
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC002\SH002\DIALOGUE.json
