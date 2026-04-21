# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH018_SC003_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Observation $\rightarrow$ Growing Horror/Despair. **Likely Visual Coverage Families:** - Tracking shots following the movement of the arm.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: described character with stable costume and silhouette. Environment: describe...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH018_SC003; SHOT_INDEX; DIALOGUE; protagonist; None
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
- scene_id: CH018_SC003
- chapter_id: CH018
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Martian plains (moving towards Warhoon) featuring protagonist.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH018_SC003 / To illustrate the cultural brutality of the Warhoon and build atmosph....
- Variant: Tighter Zoom.
- Movement direction of the column
- lighting (time of day transition).
- The army turns back toward the city of Warhoon. The protagonist observes the constant
- casual violence and dueling that defines the Warhoon march.
- Resolve various Warhoon Warriors -> various Warhoon Warriors
- Resolve Martian plains (moving towards Warhoon) -> Martian plains (moving towards Warhoon)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC003\SH001\DIALOGUE.json
