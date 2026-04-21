# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH021_SC001_SH001_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Wonder (at technology) $\rightarrow$ Tension (political discourse).. Wide establishing frame with a steady or lightly drifting camera.. shifted perspective with preserved subject spacing. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuit...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH021_SC001; SHOT_INDEX; DIALOGUE; john_carter; None
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH021_SC001
- chapter_id: CH021
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: shifted perspective with preserved subject spacing
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH021_SC001 / Establish the scale of Barsoomian technology and the political tensio....
- Variant: Alternate Angle.
- Carter's travel gear and position relative to the landscape.
- John Carter travels toward Zodanga
- observing the massive irrigation systems pumping water from polar ice caps. He encounters Zodangan nobility who discuss the unjust war with Helium and the disappearance of Princess Dejah Thoris.
- Resolve Zodangan Nobility (unnamed) -> Zodangan Nobility (unnamed)
- Resolve The Barsoomian plains/deserts -> The Barsoomian plains/deserts
- Resolve near irrigation conduits -> near irrigation conduits
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC001\SH001\DIALOGUE.json
