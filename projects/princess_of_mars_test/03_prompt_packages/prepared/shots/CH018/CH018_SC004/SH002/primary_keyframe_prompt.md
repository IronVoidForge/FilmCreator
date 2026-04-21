# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH018_SC004_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Terror $\rightarrow$ Psychological Exhaustion/Madness. **Likely Visual Coverage Families:** - Low-key lighting; heavy use of shadows (Chi.... Stable medium framing that keeps action and character readable.. balanced framing with clear spatial separation. Characters: described character with stable costume and silhouette. Env...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH018_SC004; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH018_SC004
- chapter_id: CH018
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: balanced framing with clear spatial separation
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH018_SC004 / To establish the protagonist's psychological isolation and sensory de....
- Variant: Primary Keyframe.
- Chain length/position
- level of darkness/visibility.
- Carry the emotional arc through: Terror $\rightarrow$ Psychological Exhaustion/Madness.
- **Likely Visual Coverage Families:**
- - Low-key lighting; heavy use of shadows (Chiaroscuro).
- - Extreme close-ups on the protagonist's eyes and breathing.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC004\SH002\DIALOGUE.json
