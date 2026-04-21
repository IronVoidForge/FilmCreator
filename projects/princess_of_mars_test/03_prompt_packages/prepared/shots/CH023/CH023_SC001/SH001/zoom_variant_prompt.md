# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH023_SC001_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. From tension/secrecy to righteous fury and resolve. **Likely Visual Coverage Families:** - Tight medium shots for intimate dialogue. - Cl.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: described character with stable costume and silhouette. Environment: describ...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH023_SC001; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
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
- scene_id: CH023_SC001
- chapter_id: CH023
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Kantos Kan's private quarters (Zodanga) featuring john_carter, kantos_kan.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH023_SC001 / Establish the alliance and the driving motivation (Dejah Thoris's pli....
- Variant: Tighter Zoom.
- Character positioning relative to the secret pact/vow
- props used during the planning.
- John Carter meets secretly with Kantos Kan to deliver the news of Dejah Thoris's engagement to Sab Than. Devastated
- Kantos Kan vows to assassinate the Zodangan ruler via a secret entrance
- leading to a pact where Kan strikes the palace while Carter heads for Helium.
- Resolve Kantos Kan's private quarters (Zodanga) -> Kantos Kan's private quarters (Zodanga)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH023\CH023_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC001\SH001\DIALOGUE.json
