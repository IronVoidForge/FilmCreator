# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH027_SC001_SH001_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Contentment/Peace $\rightarrow$ Panic/Urgency. **Likely Visual Coverage Families:** - Warm, golden-hued close-ups of the incubator and th.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: described character with stable costume and silhouette, . Envi...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH027_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tardos_mors; None
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
- scene_id: CH027_SC001
- chapter_id: CH027
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in The Palace in Helium (Rooftop Shrine/Sunken Garden) featuring john_carter, Dispatch Bearer.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH027_SC001 / Establish the status quo of peace and introduce the inciting incident....
- Variant: Primary Keyframe.
- The appearance/age of the characters over the nine-year jump
- the physical state of the golden incubator.
- A montage/sequence showing nine years of prosperity for John Carter and Dejah Thoris
- centered around their golden egg incubator. This peace is shattered by a dispatch bearer announcing the murder of the Atmosphere Plant keeper and the subsequent drop in planetary air pressure.
- Resolve Dispatch Bearer -> Dispatch Bearer
- Resolve The Palace in Helium (Rooftop Shrine/Sunken Garden) -> The Palace in Helium (Rooftop Shrine/Sunken Garden)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SH001\DIALOGUE.json
