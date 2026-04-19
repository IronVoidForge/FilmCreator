# Title
CH008_SC003 CL008 Keyframe Prompt

# ID
CH008_SC003_CL008_keyframe_prompt

# Purpose
Establish the opening keyframe for a tracking shot following a burning vessel drifting southeast as a funeral pyre. Capture the visual state at the start of the cut, emphasizing the drift vector, fire intensity, and environmental smoke without visible characters on the hull.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Gray low-profile vessel with banners dissolving in flame, smoke plume rising vertically then dispersing with wind, drifting southeast vector, ash debris scatter on water surface, fire intensity increasing across hull, distant green-skinned figures observing from fortified structures, open valley background, funeral pyre atmosphere, cinematic lighting, high contrast smoke effects, no people standing on vessel.

# Negative Prompt
People standing on vessel, clear blue sky without smoke, static ship orientation, wrong drift direction, close-up of faces, modern elements, bright daylight without fire glow, sharp focus on distant buildings only, clean hull without fire damage, visible crew members, calm water without ash.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL008
- duration_seconds: 5
- required_refs: BT003.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: None on vessel, Warriors (distant)
- look_continuity_policy: insert
- intended_lighting_change: fire glow intensifies
- composition_type: tracking shot
- continuity_mode: insert
- starting_keyframe_strategy: open on burning ship drift vector
- dependency_policy: depends on CL007
- auto_advance_policy: none
- fallback_strategy: cutaway if needed
- consistency_assist_policy: enabled
- consistency_assist_method: frame matching
- anatomy_repair_policy: disabled
- consistency_targets: drift vector, fire spread pattern
- style_profile: cinematic sci-fi
- batch_role: keyframe
- fix_of: CL007

# Continuity Notes
- Maintain southeast drift vector consistency with previous clip.
- Ensure smoke plume rises vertically then disperses naturally.
- Fire intensity must increase visibly during the interval.
- Ash and debris must scatter on water surface at 0:4 mark.
- Distant warriors remain static or move slightly in background only.
- Banners on stem/stern must show signs of burning.

# Repair Notes
- If smoke is too thin, increase density to match funeral pyre weight.
- If ship orientation shifts, correct drift vector to southeast.
- Ensure fire does not consume hull instantly at start frame.
- Verify distant figures do not appear on vessel deck.
- Adjust lighting contrast if fire glow is insufficient.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
