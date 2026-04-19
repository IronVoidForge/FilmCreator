# Title
CH008_SC004 CL012 Fix 01 Prompt

# ID
CH008_SC004_CL012_fix_01_prompt

# Purpose
Corrective still generation for CL012 Fix 01 within CH008_SC004. Maintains over-the-shoulder observer perspective from Carter's viewpoint during battle aftermath sequence. Fixes local artifacts while preserving composition of warriors returning to plaza and smoke clearing significantly. Ensures continuity with BT003 start state regarding vessel drift and group gathering logic without introducing new motion or character errors.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Over-the-shoulder shot human observer shoulder view, green skin warriors moving toward plaza entrance, urban structures background upper floors windows roofs, daylight smoke clearing significantly, valley floor beyond city, hills crests distant horizon, battle aftermath acknowledged by group, stationary observer throughout beat, partial view warriors moving, open ground plaza area, smoke spurt of flame from impacts fading

# Negative Prompt
excessive motion blur, wrong character count, incorrect lighting, blurry details, extra limbs, distorted anatomy, vessel explosion visible, prisoner visible, green martian females dragging, air craft visible, night time, indoor setting, close-up only, extreme wide shot, fire glare overpowering scene, debris on plaza surface

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL012
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT003.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: john_carter, green_martian_warrior
- look_continuity_policy: preserve_composition_and_look
- intended_lighting_change: none
- composition_type: Over-the-shoulder shot (observer perspective)
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

# Continuity Notes
- Carter remains stationary as observer throughout beat
- Partial view of warriors moving toward plaza entrance
- Smoke clearing significantly by 2.5s mark
- Battle aftermath acknowledged by group at 5s
- No character movement until post-launch observation phase
- Vessel drift consistent with BT003 start state if visible in background

# Repair Notes
- Ensure smoke density matches clearing state described in BT003
- Maintain daylight atmosphere without fire glare overpowering scene
- Verify warrior count matches group gathering logic at plaza entrance
- Correct vessel drift trajectory if visible to match valley floor geography
- Fix any local artifacts in observer shoulder view anatomy

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL012.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
