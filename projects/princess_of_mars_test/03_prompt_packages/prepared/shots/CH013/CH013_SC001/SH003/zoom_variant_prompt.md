# Title
SH003 Shot Prompt - Tighter Zoom

# ID
CH013_SC001_SH003_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. From struggle/tension to wonder and social validation. **Likely Visual Coverage Families:** - Wide shots of the Martian cityscape/trainin.... Controlled closing frame that lands the consequence of the beat.. tighter framing on the same moment. Characters: described character with stable costume and silhouette. Environment: described envir...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH013_SC001; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; lorquas_ptomel; None
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
- scene_id: CH013_SC001
- chapter_id: CH013
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH013_SC001 / To demonstrate John Carter's unique approach to Martian life and esta....
- Variant: Tighter Zoom.
- The appearance/placement of the gold anklet on Carter
- the physical state of the thoats during training.
- His success earns him respect from the community and a gold anklet reward from Lorquas Ptomel.
- Resolve various Tharks -> various Tharks
- Resolve The city of the Tharks (plazas/stables area) -> The city of the Tharks (plazas/stables area)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC001\SH003\DIALOGUE.json
