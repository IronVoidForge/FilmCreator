# Title
CH008_SC004 CL002 Fix 01 Prompt

# ID
CH008_SC004_CL002_fix_01_prompt

# Purpose
Correct lighting and anatomy inconsistencies while maintaining ship exterior composition and prisoner appearance continuity with approved still base. Preserve dim industrial texture and green-skinned warrior visual style.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
gray low-profile vessel with banners on stem and stern, glowing devices on prow, slender girlish figure with oval face and large lustrous eyes, coal black waving hair, light reddish copper skin, crimson cheeks, ruby lips, green-skinned warriors in view, dim lighting, industrial texture, open portal, building interior light visible through entrance

# Negative Prompt
distorted anatomy, extra limbs, wrong colors, bright sunlight, text, logos, blurry details, floating objects, inconsistent lighting, missing portal, wrong skin tone, overexposed shadows, distorted ship hull

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md, Environmental state: dim lighting, industrial texture
- optional_refs: Wide shot warriors dragging action notes
- visible_character_assets: Green Warriors, Human Woman, Ship Hull
- look_continuity_policy: preserve dim lighting and industrial texture
- intended_lighting_change: 
- composition_type: Wide ship exterior showing portal
- continuity_mode: cutaway
- starting_keyframe_strategy: interior to exterior transition
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: 
- fallback_strategy: Use medium shot warriors dragging if wide unavailable
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Ensure green skin tone matches approved still base for warrior figures
- Maintain ship gray color consistency across frames
- Preserve prisoner appearance details (oval face, coal black hair) in close-ups
- Keep lighting dim and industrial throughout the sequence

# Repair Notes
- Fix lighting inconsistencies to match dim industrial state
- Ensure portal is clearly open in wide shot composition
- Correct warrior anatomy if distorted or inconsistent with reference
- Adjust ship hull visibility to match environmental boundary requirements

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
