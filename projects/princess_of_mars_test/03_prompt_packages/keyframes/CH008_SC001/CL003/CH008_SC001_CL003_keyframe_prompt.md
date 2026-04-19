# Title
CH008_SC001 CL003 Keyframe Prompt

# ID
CH008_SC001_CL003_keyframe_prompt

# Purpose
Capture the visible state of green-skinned warriors distributed across forward sections of descending air craft vessel. Freeze the moment of coordinated movement along deck surface.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Medium shot view of long low gray-painted vessel forward section, multiple green-skinned figures standing on deck surface, daylight exterior lighting illuminating scene, horizontal axis aligned with vessel length, figures crowding toward front edge, high contrast between bright sky and dark vessel hull, static hold framing on initial retreat moment.

# Negative Prompt
Human skin tone, interior shadows, doorway threshold, building architecture, crowded plaza, distorted anatomy, blurry text, low resolution, modern clothing, weapons visible on protagonist, static pose, fully visible faces (unless specified), bright interior lighting.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: green-skinned warriors, air craft forward section
- look_continuity_policy: match_previous_clip_lighting
- intended_lighting_change: none
- composition_type: medium_shot_vessel_deck
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
- dependency_policy: independent_can_follow_any_previous_clip
- auto_advance_policy: manual_review_required
- fallback_strategy: cut_to_wide_halt_if_reaction_misread
- consistency_assist_policy: enabled
- consistency_assist_method: reference_alignment
- anatomy_repair_policy: strict
- consistency_targets: facial_expression
- style_profile: cinematic_realism
- batch_role: keyframe_generation
- fix_of: none
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Focus on vessel deck and coordinated movement. Ensure shadow swallowing figures is visible if retreating. Maintain lighting consistency with exterior daylight. Freeze frame on initial crowding moment before full movement starts.

# Repair Notes
- If figures look static, increase intensity of crowding motion. Ensure background remains open valley terrain or building exterior, not city architecture interior. Verify green skin tone is consistent.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
