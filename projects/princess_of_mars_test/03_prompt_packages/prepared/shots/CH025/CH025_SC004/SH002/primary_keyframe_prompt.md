# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH025_SC004_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Urgency $\rightarrow$ Relief.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette,...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH025_SC004; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan; None
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
- scene_id: CH025_SC004
- chapter_id: CH025
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Zodanga Dungeons (Labyrinthine/Dark) featuring john_carter, kantos_kan.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH025_SC004 / Expand the scope of the rescue and introduce an ally..
- Variant: Primary Keyframe.
- Torch/light source movement
- key/lock interaction
- character wounds from the previous battle.
- Carry the emotional arc through: Urgency $\rightarrow$ Relief..
- Resolve Zodangan Jailers (defeated) -> Zodangan Jailers (defeated)
- Resolve Zodanga Dungeons (Labyrinthine/Dark) -> Zodanga Dungeons (Labyrinthine/Dark)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH025\CH025_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC004\SH002\DIALOGUE.json
