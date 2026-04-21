# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH018_SC001_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Confusion/Pain $\rightarrow$ Dread/Disorientation. **Likely Visual Coverage Families:** - Extreme close-ups of eyes opening/pain. - Wide.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: described character with stable costume and silhouette. Environment: described...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH018_SC001; SHOT_INDEX; DIALOGUE; protagonist; female_healer; warhoon_warriors
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
- scene_id: CH018_SC001
- chapter_id: CH018
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Small medical room featuring protagonist.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH018_SC001 / Establish the protagonist's vulnerability and his new status as a cap....
- Variant: Tighter Zoom.
- Wound placement/bandaging
- tightness of the restraints on the thoat.
- The protagonist regains consciousness in a medical setting
- treated by an ancient Warhoon healer. He is subsequently strapped to a wild thoat and forced into the middle of a massive military column.
- Resolve Small medical room -> Small medical room
- Resolve Martian plains (during the march) -> Martian plains (during the march)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC001\SH001\DIALOGUE.json
