# Title
CH008_SC004 CL008 Scene Stage Prompt

# ID
CH008_SC004_CL008_scene_stage_prompt

# Purpose
Define the staging intent for this texture detail shot within the scene stage workflow. Focus on continuity of fire and smoke elements from the burning vessel, ensuring alignment with rooftop observer positions and environmental context established in previous beats. Maintain visual consistency regarding vessel damage state, loot distribution, and valley floor cleanliness relative to prior impact debris.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Roaring orange and yellow flames erupting from damaged hull, dark gray smoke plume rising above vessel, drifting unguided across valley floor, small items visible on warrior shoulders, daylight illumination, smoke from fire impacts, texture detail focus, open ground plaza background, building roofs in distance, no debris on valley surface.

# Negative Prompt
Clear sky, intact vessel hull, heavy debris on valley floor, distorted flame coloration, static composition, sudden appearance of new objects, wrong lighting conditions, blurred texture details, proper nouns or names, human faces in close-up, green skin distortion.

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
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: Action-oriented, awe-inspiring
- batch_role: 
- fix_of: 

# Continuity Notes
- Vessel lightened by loot removal visible on hull
- Roaring flames with orange/yellow coloration consistent across shots
- Dark gray plume rising above vessel without sudden density changes
- Valley floor remains clean of debris from previous impacts
- Small items visible on some warrior shoulders during drift sequence
- Drifting unguided path follows valley edge trajectory

# Repair Notes
- Ensure flame coloration matches orange/yellow specification
- Verify smoke density aligns with previous impact states
- Check for accidental debris appearance on valley floor
- Confirm vessel damage state remains consistent with loot removal
- Maintain texture focus without introducing unrelated elements

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
