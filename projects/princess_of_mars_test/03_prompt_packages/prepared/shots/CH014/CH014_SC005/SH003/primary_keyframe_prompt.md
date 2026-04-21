# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH014_SC005_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Combat/Intensity $\rightarrow$ Chaos $\rightarrow$ Tragedy/Loss.. Tight detail framing focused on a single visual object or gesture.. Detail composition centered on the key physical action or prop inside .. Characters: described character with stable costume and silhouette. Environment: described environment with stable spat...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH014_SC005; SHOT_INDEX; DIALOGUE; john_carter; zad; sarkoja; sola; dejah_thoris
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
- scene_id: CH014_SC005
- chapter_id: CH014
- shot_type: insert_detail
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside Duel site/Camp area.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH014_SC005 / Execute the action climax and the tragic turning point..
- Variant: Primary Keyframe.
- The angle of the sun/mirror reflection
- blood/wound location on Carter
- Sola's position relative to Dejah.
- Land the scene consequence or transition cleanly.
- Resolve Duel site/Camp area -> Duel site/Camp area
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC005\SH003\DIALOGUE.json
