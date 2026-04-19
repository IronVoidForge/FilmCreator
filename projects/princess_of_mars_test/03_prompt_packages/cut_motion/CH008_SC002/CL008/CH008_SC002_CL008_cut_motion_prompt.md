# Title
CH008_SC002 CL008 Cut Motion Prompt

# ID
CH008_SC002_CL008_cut_motion_prompt

# Purpose
Progressive tracking of damage indicators on retreating enemy vessels, emphasizing visible flame and smoke progression while maintaining battle atmosphere continuity.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Gray low-profile vessels with banners on stem and stern, glowing devices on prow, visible flame damage on fabric, smoke trails from damaged craft, retreating motion away from valley floor, battle conclusion atmosphere, medium close-up composition, progressive tracking of destruction indicators, swinging motion of airships, drifting smoke density.

# Negative Prompt
static image, sudden cut, blue sky, clean vessels without damage, distorted anatomy, text overlay, flickering artifacts, wrong color grade, bright sunlight, clear weather, sharp focus on distant hills, human figures in foreground.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5
- required_refs: BT004.md
- optional_refs: Damage detail close-ups coverage families
- visible_character_assets: Enemy Fleet (multiple vessels), Banners with flame damage
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: None (Battle haze consistency)
- composition_type: Medium close-up of vessels showing damage indicators
- continuity_mode: Close-up progressive tracking of damage indicators
- starting_keyframe_strategy: Open on multiple vessels with visible damage indicators
- dependency_policy: Soft dependency on CL007; can follow retreat sequence
- auto_advance_policy: 
- fallback_strategy: Use insert if need to emphasize damage progression timing
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain battle haze lighting consistency with previous clip.
- Ensure flame damage on banners progresses naturally without jumping states.
- Keep ship swing arcs smooth and consistent with retreat trajectory.
- Match smoke density to indicate time elapsed since engagement.
- Avoid introducing new characters or distinct environments not present in BT004.

# Repair Notes
- If vessels appear too clean, increase flame intensity on banners.
- If motion is jerky, smooth out camera tracking on retreating ships.
- If smoke trails are missing, add subtle drifting smoke effects.
- If lighting shifts to bright sun, revert to battle haze grade.
- If anatomy of crew becomes visible and distorted, obscure or correct.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
