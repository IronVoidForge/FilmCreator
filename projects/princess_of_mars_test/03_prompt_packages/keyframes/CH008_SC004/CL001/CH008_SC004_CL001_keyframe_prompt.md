# Title
CH008_SC004 CL001 Keyframe Prompt

# ID
CH008_SC004_CL001_keyframe_prompt

# Purpose
Insert a frozen still at cut start to establish warrior preparation phase on roof level, maintaining vertical axis from roofs down to valley floor context.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
A medium shot of a green-skinned warrior standing on a stone roof surface, holding a large missile in hands ready for deployment, front-facing view, partial view of upper floor structure behind, daylight illumination with rising smoke plume visible in background distance, vertical axis from roofs down to valley floor implied.

# Negative Prompt
blurry, distorted hands, extra fingers, modern clothing, text, logos, watermark, low resolution, dark shadows, night time, indoor setting, civilian attire, weapon malfunction, missing missile, floating objects, close-up of vessel, ground level view.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL001
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: green_warrior, roof_surface
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert
- dependency_policy: 
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain vertical axis from roofs down to valley floor.
- Ensure warrior is front-facing holding missile ready at 0s mark.
- Include partial roof surface context without obscuring subject.
- Match daylight lighting with smoke presence.
- Avoid showing vessel directly in this medium shot, focus on preparation phase.

# Repair Notes
- If anatomy is distorted, prioritize hand and missile connection.
- If lighting is too dark, adjust to match valley floor daylight conditions.
- Ensure no modern elements appear on warrior or roof.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
