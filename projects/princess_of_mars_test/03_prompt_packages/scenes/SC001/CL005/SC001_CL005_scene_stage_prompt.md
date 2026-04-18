# Title
SC001 CL005 Scene Stage Prompt

# ID
SC001_CL005_scene_stage_prompt

# Purpose
Describe staging intent for scene stage of SC001 CL005 detail insert shot focusing on mysterious devices mounted on individual gray airship prows, maintaining visual continuity from preceding banner close-up while establishing narrator's eyeline shift toward specific ship details, emphasizing depth context provided by hill crests and interior observation point framing

# Workflow Type
authoring.scene_stage

# Positive Prompt
detail insert of mysterious odd devices mounted on prows of gray painted airships, human observer visible in frame with eyeline directed toward specific ships, upper floor window frame establishing interior boundary, dark wood window structure with metal accents visible, hill crests providing depth reference points for ship positioning, soft morning light transitioning to brighter midday illumination, stone floor material consistent in medium shots, vertical axis showing interior warm lighting contrast to exterior cool daylight, focus axis moving from horizontal fleet distribution to vertical ship prow details, specific device shapes now identifiable as mysterious objects

# Negative Prompt
full fleet formation visible without detail focus, airships landing or taking off, text labels or readable signage on devices, bright interior lighting overwhelming exterior view, dark exterior view obscuring ship details, chaotic movement patterns, blurred faces or distorted anatomy, low resolution artifacts, crowds in immediate area, enemy combatants close up, ships positioned at wrong elevation relative to hill crests, inconsistent window frame elements, mismatched stone floor material

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL005
- duration_seconds: 5
- required_refs: SC001 beat bundle BT003.md, device shapes continuity markers across shots, ship prow details visible in frame
- optional_refs: hill crests depth context for close-ups, lighting consistency notes, banner designs as visual reference points
- visible_character_assets: human observer, green warriors static or minimal movement on selected vessels with visible devices
- look_continuity_policy: match previous beats from CL004 banner close-up
- intended_lighting_change: interior dimmer than exterior daylight view
- composition_type: detail insert of devices on ship prows
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert_device_detail_focus
- dependency_policy: dependent_on_banner_visibility_and_device_shapes
- auto_advance_policy: none
- fallback_strategy: cutaway_to_ship_prow_detail
- consistency_assist_policy: enabled
- consistency_assist_method: reference frames
- anatomy_repair_policy: enabled
- consistency_targets: character positions, lighting consistency, device shape clarity
- style_profile: cinematic realism
- batch_role: scene_stage
- fix_of: none

# Continuity Notes
- Maintain narrator's position relative to window frame throughout sequence matching CL004 banner close-up framing
- Ensure fleet formation and positioning consistency across shots with hill crests as depth reference points
- Track lighting shift from soft morning to bright midday as scene progresses maintaining interior-exterior contrast
- Keep interior stone floor material consistent in medium shots matching previous keyframes
- Align eyelines with narrator's shoulder height approximately 5 feet 8 inches camera level for continuity
- Preserve device shape clarity and mysterious quality across detail insert shots
- Maintain ship positions relative to hill crests as established in BT003 beat bundle
- Ensure banner designs remain identifiable as visual reference points across shots

# Repair Notes
- Correct any distortion in character anatomy if visible particularly narrator's face and upper body
- Fix lighting mismatches between interior warm tones and exterior cool daylight views
- Adjust composition to match previous keyframes for continuity with CL004 banner close-up
- Ensure window frame shadows deepen slightly as light changes maintaining consistency
- Address device shape clarity ensuring mysterious objects remain identifiable across shots
- Correct elevation of ships relative to hill crests if positioned incorrectly
- Fix any blurred faces or distorted anatomy artifacts in detail insert shots
- Adjust interior-exterior lighting contrast if mismatched between frames

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
