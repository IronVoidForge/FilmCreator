# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH011_SC002_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Curiosity $\rightarrow$ Disbelief $\rightarrow$ Deepened Trust. **Likely Visual Coverage Families:** - Tight close-ups on faces to captur.... Controlled closing frame that lands the consequence of the beat.. balanced framing with clear spatial separation. Characters: described character with stable costume and silhouette. En...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH011_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
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
- scene_id: CH011_SC002
- chapter_id: CH011
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: balanced framing with clear spatial separation
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH011_SC002 / To bridge the gap between Carter's mystery and Dejah Thoris's underst....
- Variant: Primary Keyframe.
- Eye contact patterns
- the physical distance between characters as trust is established.
- Though the concept is alien to her
- Dejah Thoris relies on her intuition and Carter's sincerity to accept his truth.
- Resolve The luxurious ancient quarters -> The luxurious ancient quarters
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH011\CH011_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC002\SH003\DIALOGUE.json
