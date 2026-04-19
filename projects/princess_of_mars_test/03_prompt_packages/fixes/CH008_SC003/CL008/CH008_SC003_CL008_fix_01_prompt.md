# Title
CH008_SC003 CL008 Fix 01 Prompt

# ID
CH008_SC003_CL008_fix_01_prompt

# Purpose
Generate a tracking shot of the burning ship drifting southeast as a funeral pyre, adhering to scene continuity and visual style for still_fix stage.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
A low-profile gray vessel engulfed in flames, banners on stem and stern dissolving in fire, glowing devices on prow visible through smoke, ash and debris scattering on water surface, drifting southeast vector, distant green-skinned warriors observing from buildings, urban Martian architecture background, open valley setting, funeral pyre atmosphere.

# Negative Prompt
text, watermark, extra limbs, human faces close up, static image, wrong color palette, sharp focus on foreground debris obscuring ship, sudden movement stops, smoke obscuring entire vessel, bright daylight without fire glow.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL008
- duration_seconds: 5
- required_refs: BT003.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: None on vessel, Warriors (distant)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: tracking shot
- continuity_mode: insert
- starting_keyframe_strategy: open on burning ship drift vector
- dependency_policy: depends on CL007
- auto_advance_policy: 
- fallback_strategy: cutaway if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- Ship must drift southeast continuously, fire intensity increases over time, ash scatters on water, maintain ship orientation relative to horizon.

# Repair Notes
- Preserve composition and look while fixing local issues, ensure smoke/ash doesn't obscure key details, maintain color consistency with previous frames.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
