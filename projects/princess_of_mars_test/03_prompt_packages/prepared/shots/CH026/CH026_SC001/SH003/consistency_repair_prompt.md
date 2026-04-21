# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH026_SC001_SH003_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Tension $\rightarrow$ Chaotic Violence $\rightarrow$ Grim Triumph.. Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of the zodangans are decisively defeated, ending in the ritualistic suicide of their commanders... Characters: describe...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH026_SC001; SHOT_INDEX; DIALOGUE; tars_tarkas; kantos_kan; None; None
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH026_SC001
- chapter_id: CH026
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in The Martian Skies / Aerial Naval Theater that emphasizes the consequence of the zodangans are decisively defeated, ending in the ritualistic suicide of their commanders..
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH026_SC001 / To establish the military dominance of the Thark-Heliumite alliance a....
- Variant: Consistency Repair.
- Ship positions relative to one another
- Direction of flight paths
- Timing of small-arms fire vs. naval maneuvers.
- The Zodangans are decisively defeated
- ending in the ritualistic suicide of their commanders.
- Resolve John Carter (implied/observing) -> John Carter (implied/observing)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC001\SH003\DIALOGUE.json
