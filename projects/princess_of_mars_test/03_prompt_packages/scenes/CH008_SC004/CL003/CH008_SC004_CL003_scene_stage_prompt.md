# Title
CH008_SC004 CL003 Scene Stage Prompt

# ID
CH008_SC004_CL003_scene_stage_prompt

# Purpose
Extreme wide shot establishing missile flight trajectory toward distant vessel. Camera positioned at plaza level looking upward and across valley floor. Subject placement shows multiple missiles mid-flight with visible vessel burning in valley distance. Environmental context includes smoke rising from previous impact sites on valley floor. Intended visible opening frame setup displays missiles traveling diagonally across composition with vessel appearing small in background to establish scale and action context.

# Workflow Type
authoring.scene_stage

# Positive Prompt
missiles in flight, burning vessel in valley floor distance, smoke plume rising from impact sites, green warrior silhouettes on building roofs above, daylight illumination, open plains geography, distant hills beyond city buildings, missile trajectory lines visible, flame spurt from previous impacts, gray-painted vessel hull, banners on prows, figures crowding forward decks

# Negative Prompt
close-up shots, character faces visible, detailed weapon mechanics, indoor settings, night scenes, heavy debris on valley floor, explosion effects dominating frame, green skin close-ups, air craft interiors, prisoner visible, building interior spaces, smoke obscuring entire composition, missile impact moment, vessel destroyed completely, Carter in foreground, plaza surface debris

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL003
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: missiles in flight, vessel visible in valley floor distance, smoke rising from previous impacts
- look_continuity_policy: cutaway to next clip maintaining action context
- intended_lighting_change: daylight consistent with scene
- composition_type: extreme wide shot (action context)
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: none
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: enabled
- consistency_assist_method: visual_match
- anatomy_repair_policy: minimal
- consistency_targets: vessel position, smoke trail continuity, missile trajectory path
- style_profile: action_context_wide_shot
- batch_role: third_test_clip
- fix_of: none

# Continuity Notes
- Vessel must appear small in background to establish scale and distance from camera position
- Smoke plume should show rising from previous impact sites on valley floor, not obscuring entire composition
- Missiles traveling diagonally across frame with visible trajectory path
- Green warrior silhouettes on building roofs above maintain static observation positions
- Daylight illumination consistent throughout scene with no lighting changes
- Valley floor geography shows open plains with distant hills beyond city buildings
- No debris on plaza surface in foreground, only smoke rising from valley floor impacts
- Vessel hull lightened by loot removal visible as slight damage marks
- Flame spurt from previous impacts should appear as background elements not dominating frame
- Camera positioned at plaza level looking upward and across maintaining vertical axis from roofs down to valley floor

# Repair Notes
- If vessel appears too large in frame, reframe to show more valley floor distance
- If smoke obscures entire composition, reduce smoke density while maintaining rising plume effect
- If missile trajectory not visible, adjust angle to show diagonal flight path across composition
- If green warrior silhouettes missing from building roofs above, add minimal observation figures
- If lighting appears inconsistent with daylight scene, correct illumination to match valley floor conditions
- If debris appears on plaza surface, remove all foreground debris while maintaining smoke rising from valley
- If vessel damage marks not visible, add slight hull lightening effect consistent with loot removal
- If flame spurt too prominent, reduce intensity to background element level
- If camera angle does not show vertical axis from roofs down to valley floor, adjust composition accordingly

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
