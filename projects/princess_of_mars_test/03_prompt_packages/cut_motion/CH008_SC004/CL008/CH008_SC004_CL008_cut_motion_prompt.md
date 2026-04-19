# Title
CH008_SC004 CL008 Cut Motion Prompt

# ID
CH008_SC004_CL008_cut_motion_prompt

# Purpose
Execute cut motion stage for CL008 within BT002 beat sequence. Maintain close-up texture focus on burning vessel flames and smoke plume while transitioning camera drift to match interval beats. Ensure continuity with previous impact damage and loot removal context visible on warrior shoulders.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Roaring orange and yellow flames consuming vessel hull, dark gray smoke plume rising vertically above burning ship, flickering fire light illuminating nearby valley floor, slight camera drift maintaining focus on flame texture, Green Martian warrior shoulders visible in background carrying loot items, smoke particles drifting southeast, ambient daylight with smoke haze

# Negative Prompt
Static image, blue fire, human faces in extreme close-up, sudden camera cuts, debris scattered on valley floor, wrong color smoke (white or black), vessel exploding instantly, clear sky without smoke haze, cartoon style, low resolution

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
- composition_type: Close-up (texture detail)
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Vessel lightened by loot removal visible
- Roaring flames consistent with previous impact
- Drifting unguided path southeast/southwesterly
- Valley floor no debris from previous impacts

# Repair Notes
- Ensure flame intensity doesn't obscure vessel structure needed for next beat context
- Maintain smoke color consistency (dark gray) across interval frames

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
