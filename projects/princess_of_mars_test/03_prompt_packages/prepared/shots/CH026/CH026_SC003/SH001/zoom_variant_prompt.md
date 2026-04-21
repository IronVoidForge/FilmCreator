# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH026_SC003_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Determination $\rightarrow$ High-Stakes Combat $\rightarrow$ Decisive Victory.. Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with, placed for immediate spatial orientation.. Characters: described character with stable costume and silhouette. Environment: described environment with stable spati...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH026_SC003; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; thark_warriors; None; None
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
- scene_id: CH026_SC003
- chapter_id: CH026
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across The Plains near Helium with tars_tarkas, thark_warriors placed for immediate spatial orientation.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH026_SC003 / To resolve the remaining ground-based threat and demonstrate Thark ma....
- Variant: Tighter Zoom.
- The number of troops visible in wide shots
- The direction of the charge
- Weaponry usage (small arms vs melee).
- Carter and Tars Tarkas lead a land assault against the remaining Zodangan ground forces on the plains near Helium. Despite being outnumbered ten to one
- the combined force of Thark warriors and Heliumite reinforcements crushes the Zodangan camp.
- Resolve Heliumite Reinforcements -> Heliumite Reinforcements
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC003\SH001\DIALOGUE.json
