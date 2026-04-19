# Title
CH008_SC002 CL004 Scene Stage Prompt

# ID
CH008_SC002_CL004_scene_stage_prompt

# Purpose
Define staging intent for CL004 within Battle Initiation scene CH008_SC002. Establish medium shot composition of enemy fleet deck crew firing operations during ship swing arc. Focus on action detail work, weapon activation state, and environmental context of gray airship vessel in Martian valley battle zone. Ensure opening keyframe shows crew already positioned with active weapons to match soft dependency on CL003.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Medium shot of gray airship deck crew firing weapons during ship swing arc. Green-skinned warriors or enemy personnel positioned on low-profile vessel with banners and glowing devices. Weapons active with smoke trails from firing points visible. Ship swinging broadside to complete circular motion in open aerial space. Martian valley architecture visible in background. Daytime lighting with clear visibility of deck details. Crew faces showing concentration during combat operations.

# Negative Prompt
blurry motion, static composition, wrong anatomy, missing weapons, incorrect lighting, night scene, indoor setting, close-up only, wide shot, empty deck, calm atmosphere, no smoke trails, ship stationary, wrong banner placement, flickering objects, distorted faces, low resolution.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: Deck crew close-ups coverage families
- visible_character_assets: Enemy Fleet, Weapons active during swing
- look_continuity_policy: Soft dependency on CL003; can follow ship swing arc
- intended_lighting_change: Daytime consistent with battle zone
- composition_type: Medium shot of crew positioned on deck for firing
- continuity_mode: Close-up action detail work on deck crew operations
- starting_keyframe_strategy: Open on crew already in firing positions, weapons active
- dependency_policy: Soft dependency on CL003; can follow ship swing arc
- auto_advance_policy: Standard interval beats
- fallback_strategy: Use insert if need to emphasize crew action timing
- consistency_assist_policy: Maintain weapon discharge timing and ship movement
- consistency_assist_method: Track smoke trails and banner damage progression
- anatomy_repair_policy: Fix crew face consistency if flickering occurs
- consistency_targets: Ship swing arc completion, weapon activation state
- style_profile: Martian city battle aesthetic
- batch_role: Action detail coverage
- fix_of: CL003 ship tracking shot continuity

# Continuity Notes
- Maintain ship swing continuity with CL003 to ensure smooth transition during enemy response sequence.
- Ensure weapon discharge timing matches BT002 beat bundle for consistent impact reaction shots.
- Track smoke trails from firing points across interval beats for visual consistency.
- Verify banner placement and flame damage progression does not flicker incorrectly between frames.
- Keep crew positioning static on deck while ship rotates around central pivot point.

# Repair Notes
- Fix crew face consistency if flickering occurs during ship swing motion.
- Correct banner flame damage progression to match established damage state from previous clips.
- Adjust weapon activation state if discharge timing appears inconsistent with smoke trails.
- Ensure ship rotation axis remains horizontal without vertical drift during swing arc.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
