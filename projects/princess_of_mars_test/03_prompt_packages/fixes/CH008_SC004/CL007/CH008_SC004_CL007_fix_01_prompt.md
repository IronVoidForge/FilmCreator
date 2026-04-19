# Title
CH008_SC004 CL007 Fix 01 Prompt

# ID
CH008_SC004_CL007_fix_01_prompt

# Purpose
Corrective still-generation prompt preserving composition and look while fixing local issues. Stage intent is to maintain established visual style and camera positioning for the drifting vessel shot, ensuring continuity with previous beats while resolving generation artifacts.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Extreme wide shot context, gray-painted vessel drifting toward valley edge, smoke trail visible behind vessel, warriors watching from distance with concern, daylight, smoke from fire, missile impact flames, open plains, distant hills, green-skinned figures on rooftops, burning hull lightened by loot removal, full drift path visible, camera positioned to capture trajectory.

# Negative Prompt
blurry, distorted, extra limbs, low resolution, watermark, text, uneven lighting, floating elements, inconsistent anatomy, overexposed, underexposed, noise, artifacts, glitchy, warped perspective, missing smoke trail, disconnected vessel, static flames.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL007
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT002.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Vessel drifting toward valley edge, smoke trail visible behind vessel, warriors watching from distance with concern
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Extreme wide shot (context)
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
- Vessel lightened by loot removal visible on hull
- Roaring flames continuing but diminishing intensity
- Smoke trail visible behind vessel drifting unguided
- Camera positioned to capture full drift path across valley
- Green-skinned warriors maintaining observation positions from rooftops
- Daylight conditions with smoke from fire affecting visibility slightly

# Repair Notes
- Fix local generation artifacts while maintaining established visual style
- Preserve composition and camera positioning for drifting vessel shot
- Ensure smoke trail connects consistently to vessel rear
- Maintain hull lightening details without introducing new debris
- Keep warrior observation positions static during drift sequence
- Resolve any inconsistencies in flame color or intensity relative to beat context

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
