# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH027_SC004_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Intense Concentration $\rightarrow$ Relief $\rightarrow$ Physical Collapse. **Likely Visual Coverage Families:** - Wide shots of the mass.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: described character with stable costume and silhouette. Environment: describe...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH027_SC004; SHOT_INDEX; DIALOGUE; john_carter; surviving_technician
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
- scene_id: CH027_SC004
- chapter_id: CH027
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in The Atmosphere Plant (Interior/Exterior) featuring surviving_technician.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH027_SC004 / The Climax; resolve the immediate threat through mental and physical....
- Variant: Tighter Zoom.
- The mechanical state of the pumps
- the visual representation of the thought waves (if any)
- the physical exhaustion level of John Carter.
- John arrives at the Atmosphere Plant to find a graveyard of workers. He uses his mental "thought waves" to unlock the three great doors
- finds a surviving technician
- and commands him to restart the pumps before John collapses from exhaustion and hypoxia.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC004\SH001\DIALOGUE.json
