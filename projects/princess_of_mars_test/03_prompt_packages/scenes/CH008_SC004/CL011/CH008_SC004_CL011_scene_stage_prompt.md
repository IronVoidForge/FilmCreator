# Title
CH008_SC004 CL011 Scene Stage Prompt

# ID
CH008_SC004_CL011_scene_stage_prompt

# Purpose
Define the visual staging intent for this specific clip within the broader scene sequence. Establish character placement, environmental context, and the intended visible opening frame setup for the scene generation pipeline at the scene level. Focus on bridging the beat's narrative (warriors returning to plaza) with the visual detail (loot carrying). Ensure continuity with previous shots regarding smoke density and vessel state.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green Martian warrior close-up, carrying loot containers, small items visible in hands or on shoulders, some warriors holding weapons, others with empty hands, smoke clearing significantly but still present in valley air, flames diminished to background elements, Martian city buildings upper floors and roofs in background, daylight lighting, open ground plaza area, detailed facial features, green skin tone, ornamental clothing, dynamic movement toward gathering point.

# Negative Prompt
John Carter face, human female prisoner, Air Fleet craft, explosion debris, morphing artifacts, wrong lighting conditions, night scene, indoor setting, blurry focus, distorted anatomy, extra limbs, missing loot items, vessel wreckage in foreground, heavy smoke obscuring details, static pose, lack of movement.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL011
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT003.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Warriors, Loot
- look_continuity_policy: match_previous_clip
- intended_lighting_change: smoke_clearing
- composition_type: Close-up (detail)
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: reframe_same_moment
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: enabled
- consistency_assist_method: texture_match
- anatomy_repair_policy: strict
- consistency_targets: green_skin, loot_items, smoke_density
- style_profile: action_adventure
- batch_role: scene_stage
- fix_of: null

# Continuity Notes
- Smoke density must decrease gradually from previous beat shots while remaining visible in valley air.
- Vessel state remains lightened by loot removal, drifting away in background or out of frame.
- Warriors maintain consistent green skin tone and ornamental clothing style across all clips in this sequence.
- Loot items should be small containers or weapons, not large cargo.
- Camera angle shifts from wide to close-up for detail focus on warrior carrying loot.

# Repair Notes
- If smoke obscures facial details too much, reduce smoke opacity slightly while maintaining atmospheric context.
- Ensure warrior anatomy remains consistent with Green Martian character design (green skin, ornaments).
- Verify lighting matches daylight conditions with haze from fire impacts.
- Check that loot items are clearly visible and not blending into background textures.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL011.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
