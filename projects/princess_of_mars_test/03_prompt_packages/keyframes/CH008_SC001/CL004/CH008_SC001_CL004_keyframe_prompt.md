# Title
CH008_SC001 CL004 Keyframe Prompt

# ID
CH008_SC001_CL004_keyframe_prompt

# Purpose
Establish sudden halt and reverse movement of procession upon entering open ground. Capture shift from anticipation to urgency within wide composition.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide static shot of interior window looking out to valley floor. Central column of green-skinned warriors in mist melting into structures below. Twenty gray low-profile airships sailing toward valley center. Banners on stem/stern, glowing devices on prow visible on ships. Observer figure positioned at rear reacting to elevated command signal source visible above terrain. City architecture frames left and right edges. Open ground horizon visible ahead. Dramatic lighting emphasizes urgency.

# Negative Prompt
Motion blur, moving forward, running, chaotic crowd, modern clothing, bright daylight, sunny sky, empty background, distorted anatomy, extra limbs, text, watermark, signature, low resolution, blurry face, green screen, cartoonish style, human female prisoner, chariot, mastodon.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Observer rear_position, Warriors central_column
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide_halt_reverse
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static_opening_with_full_procession_visible_before_movement_change
- dependency_policy: dependent_on_CL003_reaction_clip_first
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Procession must fully cross threshold before halt command executes.
- Reverse movement must be coordinated toward city boundary.
- Command signal source must remain visible in elevated position.
- Character placement maintains rear observer at back, warriors in central column.
- Lighting continuity matches previous reaction clip.

# Repair Notes
- Ensure static image quality without motion blur artifacts.
- Correct any anatomical distortions on warrior armor or observer figure.
- Maintain consistent color palette for green attire and gray structures.
- Verify command signal visibility matches elevated source reference.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
