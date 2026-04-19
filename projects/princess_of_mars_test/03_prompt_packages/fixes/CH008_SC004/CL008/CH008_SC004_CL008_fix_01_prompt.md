# Title
CH008_SC004 CL008 Fix 01 Prompt

# ID
CH008_SC004_CL008_fix_01_prompt

# Purpose
Corrective still-generation prompt for CL008 within CH008_SC004. Preserves composition and look of approved still base while fixing local texture issues in flames and smoke detail. Maintains continuity with BT002 beat context regarding vessel drift and battle aftermath.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Close-up texture detail of roaring orange and yellow flames with dark gray smoke plume rising above burning vessel hull, daylight illumination with fire glow, Martian environment aesthetic, Green Martian battle aftermath context, vessel lightened by loot removal visible on hull surface, no debris on valley floor, high fidelity texture focus, cinematic lighting, detailed smoke particles, intense heat haze effect.

# Negative Prompt
blurry, out of focus, distorted anatomy, extra characters, modern technology, clean sky without smoke, bright sun glare obscuring flames, low resolution, watermark, text, signature, oversaturated, underexposed, floating debris not from battle, green skin on vessel, human figures in close-up, clean valley floor with debris.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL008
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT002.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Flames, Smoke
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Close-up texture detail
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- Maintain vessel drift trajectory across valley floor.
- Preserve flame coloration as orange and yellow with fire glow.
- Ensure smoke plume is dark gray rising above vessel.
- Keep valley floor clean of debris from previous impacts.
- Match lighting intensity from approved still base.
- Vessel hull must show signs of loot removal if visible.

# Repair Notes
- Fix any local artifacts in the flames and smoke texture.
- Ensure vessel hull shows loot removal details without adding new elements.
- Avoid introducing new characters or elements not in the beat plan.
- Correct any color bleeding between fire and daylight illumination.
- Maintain high fidelity on smoke particle density.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
