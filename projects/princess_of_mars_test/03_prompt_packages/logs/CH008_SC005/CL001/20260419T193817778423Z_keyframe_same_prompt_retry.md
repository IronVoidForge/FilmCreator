# FilmCreator Prompt Writing Exchange
- timestamp_utc: 2026-04-19T19:38:17.778423+00:00
- stage: keyframe
- clip_id: CL001
- retry_kind: same_prompt_retry

## System Prompt
````text
You are writing one FilmCreator prompt package for a local generation pipeline.
Your first output line must be exactly [[FILMCREATOR_PACKET]].
Your last output line must be exactly [[/FILMCREATOR_PACKET]].
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Do not omit the outer packet envelope.
Target stage: keyframe
Stage guidance: Write the exact visible state at cut start as a single frozen still. Avoid proper nouns. Use descriptive noun phrases only.
Use descriptive noun phrases and avoid proper nouns in prompt text.
Keep duration and workflow metadata in inputs_markdown, not in the prompt body.
Follow the requested section names exactly.
````

## User Prompt
````text
Project: princess_of_mars_test

Scene: CH008_SC005

Clip: CL001

Prompt title: CH008_SC005 CL001 Keyframe Prompt

Prompt id: CH008_SC005_CL001_keyframe_prompt

Workflow type: still.scene_build.four_ref.klein.distilled

Write improved content for this canonical prompt package.

Output rules:

1. First line must be [[FILMCREATOR_PACKET]]

2. Last line must be [[/FILMCREATOR_PACKET]]

3. No text before the first line

4. No text after the last line

5. Every required section must appear exactly once



Use this exact packet envelope and section names:

[[FILMCREATOR_PACKET]]

task: clip_prompt

stage: keyframe

version: 1



[[SECTION purpose]]

...purpose text...

[[/SECTION]]



[[SECTION positive_prompt]]

...positive prompt text...

[[/SECTION]]



[[SECTION negative_prompt]]

...negative prompt text...

[[/SECTION]]



[[SECTION inputs_markdown]]

- key: value

[[/SECTION]]



[[SECTION continuity_notes_markdown]]

- note

[[/SECTION]]



[[SECTION repair_notes_markdown]]

- note

[[/SECTION]]

[[/FILMCREATOR_PACKET]]



Clip context:

## Project Summary

# Project Summary

**Title:** A Princess of Mars Test Project
**Slug:** princess_of_mars_test

**Setting:** Barsoom (Mars). Primary locations include a large Martian city with spacious doorways, upper floors, roofs, and the surrounding valley/hills. The environment features open plains and distant hills.

**Key Characters:**
- **John Carter:** Human protagonist, observer of events from windows/roofs.
- **Sola:** Companion, present in the plaza and procession.
- **Woola:** Hound companion, follows Carter closely.
- **Green Martians:** Warriors inhabiting the city buildings; use chariots, mastodons, mounted warriors.
- **Air Fleet Crews:** Operate large gray-painted air craft with wireless finding apparatus.

**Core Themes:** Aerial warfare, inter-species conflict (Green Martians vs. Air Fleet), rescue operations, discovery of new life forms.

**Tone:** Action-oriented, awe-inspiring, tense during combat sequences, melancholic regarding the destruction of the fleet.

## Chapter Summaries

## CH008_summary.md
# Chapter Summary: CH008 - A Fair Captive from the Sky

## Story Summary
The narrative begins on the third day after an incubator ceremony. The procession retreats to a city building due to an immediate order. From a window, John Carter observes the arrival of twenty large gray air craft. A battle ensues between Green Martians firing from buildings and the Air Fleet returning fire. The fleet retreats after damage; one ship is disabled and unmanned. Warriors loot the vessel (arms, jewels, water), burn it, and tow it away before it explodes. Carter witnesses a human female prisoner being dragged from the burning ship into a nearby building by Green Martian females. At the city plaza, the prisoner turns to Carter as she enters the building; he fails to respond to her signal of appeal. She is dragged away into the depths of the edifice.

## Visual Continuity
- **Air Craft:** Long, low, gray-painted vessels with strange banners and odd devices on prows. Figures crowd forward decks.
- **Green Martians:** Green skin, wear ornaments, carry spears, fire from windows/roofs.
- **Prisoner:** Slender, girlish figure. Skin is light reddish copper. Features finely chiseled. Eyes large/lustrous. Hair coal black, waving, caught loosely into a strange coiffure. Naked except for highly wrought ornaments. Cheeks crimson, lips ruby.
- **Locations:** City buildings (upper floors, windows, roofs), open ground/plaza, valley, hills beyond.
- **Action Details:** Ships swing broadside, dip below hill crests, drift southeast/southwesterly. Fire causes spurt of flame from missile impact. Guy ropes release simultaneously.

## Character Index

# Character Index - Chapter CH008

| Asset ID | Canonical Character ID | Display Name | Role | Physical Presence |
|----------|------------------------|--------------|------|-------------------|
| john_carter | john_carter | John Carter | Observer, Witness | Present |
| human_female_prisoner | prisoner_human_female | Human Female Prisoner | Captive, Appeal Signal | Referenced |
| green_martian_warriors | green_martian_warrior | Green Martian Warriors | Combatants, Looters | Referenced |
| green_martian_females | green_martian_female | Green Martian Females | Draggers, Enforcers | Referenced |

**Notes:**
- John Carter: Physically present observing from window; witnesses prisoner's appeal
- Human Female Prisoner: Detailed visual description provided in chapter; signals to Carter
- Green Martians: Multiple individuals; described as group with consistent physical traits
- All characters have sufficient identification for continuity tracking

## Environment Index

# Environment Index - CH008

## Extracted Environments

| Asset ID | Role | Primary Geography | Atmosphere Cues |
|----------|------|-------------------|-----------------|
| city_buildings | primary | urban structures, upper floors, windows, roofs | daylight, smoke from fire, missile impact flames |
| open_ground_plaza | transit | open ground, plaza area | daylight, spurt of flame from impacts |
| valley | secondary | valley floor beyond city | daylight, distant horizon |
| hills_beyond | secondary | hill crests, slopes southeast/southwesterly | daylight, dip below crests |

## Environment Families Summary

- **city_buildings**: Primary observation and action setting with multiple levels
- **open_ground_plaza**: Transit zone for fleet movement and battle effects
- **valley**: Background geography establishing scale
- **hills_beyond**: Distant geography providing directional context

## Clip Plan

# CL001 - Sola Rushes In (Connection Initiation)

## Continuity Mode
continuous_follow

## Composition Type
wide_two_shot

## Starting Keyframe Strategy
left_entering_character_focus

## Dependency Policy
independent_start

## Fallback Strategy
OTS_close_up_alternate

## Visible Character Assets
- Sola: full body, urgent motion blur
- Carter: center-right stationary, facing camera
- Background: exterior corridor lighting visible

## Required Refs
- CH008_SC005/BEAT_INDEX.md (BT001)
- Exterior corridor transition space reference

## Optional Refs
- Sola entrance animation guide
- Carter waiting stance reference

## Opening Keyframe Intent
Sola enters from left edge, moving toward center-right where Carter stands

## Cut Motion Intent
smooth_approach_motion, no hard cuts during beat

## Interval Beats
- 0s: Sola off-screen left, visible motion blur entering frame
- 2.5s: Sola reaches arm's reach from Carter
- 5s: Physical proximity established, Carter acknowledges arrival

## Scene Breakdown

# CH008_SC005 - Carter & Prisoner Connection

## Scene Purpose
Establish connection between Carter and prisoner through Sola's intervention, creating emotional anchor for the narrative.

## Scene Summary
Sola rushes to Carter from left side, glimpse of prisoner dragged into building background right-to-left, eye contact established between all parties creating tension.

## Staging Facts
- **Location**: Exterior corridor / Building entrance threshold (transition space)
- **Axis**: Sola enters from left; Carter stands center-right facing camera; Prisoner moves background right-to-left
- **Time**: Immediate urgency (Sola's rush implies chase or rescue scenario)
- **Key Props**: None specific, focus on physical movement and gaze dynamics

## Beat Breakdown
1. **BT001**: Sola Rushes In (Connection Initiation)
2. **BT002**: Prisoner Dragged Through View (Conflict Introduction)
3. **BT003**: Eye Contact & Reaction (Emotional Anchor)

## Beat Bundles

## BT001.md
# BT001 - Sola Rushes In (Connection Initiation)

## Beat Purpose
Establish connection between Carter and Sola through urgent physical approach, creating immediate narrative momentum.

## Start State
- Sola positioned off-screen left side
- Carter standing center-right facing camera
- No physical contact between characters
- Exterior corridor lighting active

## End State
- Sola reaches Carter's position
- Physical proximity established (within arm's reach)
- Carter acknowledges Sola's arrival
- Transition from waiting to interaction mode

## Character Placement and Movement Logic
- **Sola**: Enters from left moving right with urgent forward motion; minimal lateral deviation
- **Carter**: Stationary facing camera initially, may turn slightly toward Sola upon arrival
- **Movement Type**: Urgent approach by Sola contrasts with Carter's waiting stance

## Geography, Axis, or Eyeline Facts
- **Axis**: Left-to-right movement vector (Sola entering from left)
- **Eyeline Dynamics**: Sola's eyeline directed at Carter; Carter's eyeline follows Sola's trajectory
- **Spatial Relationship**: Foreground interaction space established between characters

## Prop, Vehicle, Crowd, and Environmental State
- **Props**: None specific required for this beat
- **Environmental**: Exterior corridor with transition to building interior visible
- **Crowd**: No crowd elements; focus on two-character dynamic
- **Continuity Factors**: Lighting consistency between exterior and threshold space

## Likely Coverage Families
- Over-the-shoulder (OTS) shots from Sola's perspective
- Wide two-shot establishing spatial relationship
- Close-up reaction shots for emotional beats
- Tracking shot following Sola's approach

## BT002.md
# BT002 - Prisoner Dragged Through View (Conflict Introduction)

## Beat Purpose
Introduce conflict element through prisoner's forced movement, creating narrative tension and stakes.

## Start State
- Prisoner visible in background on right side
- Carter and Sola engaged in foreground interaction
- Building entrance threshold framing the scene
- Interior-exterior transition visible

## End State
- Prisoner moves through frame to left side of background
- All characters' attention may shift toward prisoner
- Conflict element now integrated into scene dynamics
- Background movement completes across depth plane

## Character Placement and Movement Logic
- **Prisoner**: Positioned in background depth; forced dragging motion with minimal agency
- **Carter & Sola**: Foreground interaction continues, may acknowledge prisoner's movement
- **Movement Type**: Forced lateral movement right-to-left across background plane

## Geography, Axis, or Eyeline Facts
- **Axis**: Background right-to-left movement vector
- **Eyeline Dynamics**: Potential multi-point eyeline convergence if characters track prisoner
- **Spatial Relationship**: Depth layering with foreground interaction and background conflict element

## Prop, Vehicle, Crowd, and Environmental State
- **Props**: None specific; focus on physical movement dynamics
- **Environmental**: Building entrance threshold maintaining exterior urgency
- **Crowd**: No crowd elements; prisoner's forced movement creates isolation effect
- **Continuity Factors**: Background depth consistency; interior-exterior lighting transition

## Likely Coverage Families
- Wide shot showing full depth plane and background movement
- Background focus shots emphasizing prisoner's plight
- Foreground reaction shots from Carter/Sola perspective
- Depth-revealing two-shot with background element visible

## BT003.md
# BT003 - Eye Contact & Reaction (Emotional Anchor)

## Beat Purpose
Create emotional anchor through multi-party gaze dynamics, establishing tension and narrative connection.

## Start State
- All parties establish visual connection
- Carter center-right; Sola left foreground; Prisoner background right-to-left
- Exterior corridor lighting active
- Transition space maintaining narrative tension

## End State
- Tension peaks through sustained eye contact
- Emotional stakes communicated through gaze dynamics
- Multi-party acknowledgment complete
- Scene reaches emotional climax point

## Character Placement and Movement Logic
- **Carter**: Center-right facing camera, may shift eyeline between Sola and prisoner
- **Sola**: Left foreground, maintains connection with Carter while acknowledging prisoner
- **Prisoner**: Background right-to-left, minimal physical movement, emphasis on gaze
- **Movement Type**: Minimal physical movement; emphasis on facial expression and eye direction

## Geography, Axis, or Eyeline Facts
- **Axis**: Multi-point eyeline convergence creating visual triangle
- **Eyeline Dynamics**: All parties acknowledge each other through sustained gaze
- **Spatial Relationship**: Foreground-to-background visual connection established

## Prop, Vehicle, Crowd, and Environmental State
- **Props**: None specific; focus on physical movement and gaze dynamics
- **Environmental**: Transition space between exterior urgency and interior threat
- **Crowd**: No crowd elements; isolation emphasizes emotional weight
- **Continuity Factors**: Lighting consistency across foreground-background depth

## Likely Coverage Families
- Close-up reactions for each character's emotional state
- Two-shot with background element maintaining tension
- Wide establishing shot showing full spatial relationship
- Over-the-shoulder shots emphasizing eyeline dynamics

## Clip Roster

# CH008_SC005 - Clip Roster

| Clip ID | Beat | Duration | Continuity Mode | Composition Type |
|---------|------|----------|-----------------|------------------|
| CL001 | BT001 - Sola Rushes In | 5s | continuous_follow | wide_two_shot |
| CL002 | BT002 - Prisoner Dragged Through View | 5s | cutaway | wide_shot_depth |
| CL003 | BT003 - Eye Contact & Reaction | 5s | reframe_same_moment | close_up_reaction |

## Clip State

{
  "project_id": "princess_of_mars_test",
  "scene_id": "CH008_SC005",
  "clip_id": "CL001",
  "status": "planning",
  "inputs": {
    "shared_character_refs": [],
    "shared_environment_refs": [],
    "scene_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC005/CL001/CH008_SC005_CL001_scene_stage_prompt.md",
    "scene_stage_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC005/CL001/CH008_SC005_CL001_scene_stage_prompt.md",
    "keyframe_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/keyframes/CH008_SC005/CL001/CH008_SC005_CL001_keyframe_prompt.md",
    "fix_prompt_packages": [
      "projects/princess_of_mars_test/03_prompt_packages/fixes/CH008_SC005/CL001/CH008_SC005_CL001_fix_01_prompt.md"
    ],
    "anchor_prompt_packages": [],
    "video_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC005/CL001/CH008_SC005_CL001_cut_motion_prompt.md",
    "cut_motion_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC005/CL001/CH008_SC005_CL001_cut_motion_prompt.md",
    "legacy_anchor_prompt_packages": [],
    "legacy_video_prompt_package": null
  },
  "approved_assets": {
    "golden_frame": null,
    "approved_keyframe": null,
    "approved_video": null,
    "still_fixes": [],
    "anchor_frames": [],
    "interval_frames": [],
    "cut_motion_videos": []
  },
  "approved_video_last_frame": null,
  "current_continuity_source": null,
  "latest_runs": {},
  "review_batches": [],
  "latest_review_decision": null,
  "notes": [],
  "stage_style_preferences": {
    "cut_motion": {
      "literal_descriptive": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "cinematic_compositional": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "performance_action_led": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "sparse_conservative": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      }
    },
    "keyframe": {
      "literal_descriptive": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "cinematic_compositional": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "performance_action_led": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "sparse_conservative": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      }
    },
    "still_fix": {
      "literal_descriptive": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "cinematic_compositional": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "performance_action_led": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "sparse_conservative": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      }
    }
  }
}



Existing prompt draft:

# Title
CH008_SC005 CL001 Keyframe Prompt

# ID
CH008_SC005_CL001_keyframe_prompt

# Purpose
Establishes spatial relationship between approaching green-skinned humanoid companion and stationary human observer within exterior corridor threshold. Static wide frame captures urgent diagonal movement vector from left edge toward center-right position, setting up connection initiation beat start state with daylight smoke haze atmosphere and burning vessel visible in background distance.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide exterior corridor threshold, green-skinned humanoid companion entering from left edge moving rightward across frame, human male observer standing center-right partial profile facing camera, daylight atmosphere with smoke haze, burning vessel visible in background distance, open plaza ground texture, gray painted air craft debris scattered near horizon, minimal crowd presence, building entrance threshold visible behind characters.

# Negative Prompt
blur, motion artifacts on static subjects, wrong character count, text overlay, distorted anatomy, dark shadows obscuring faces, extra limbs, missing eyes, low resolution, color shift, green skin on observer, fire on companion face, inconsistent proportions, facial feature distortion, background element misplacement, overexposed highlights, underexposed shadows, wrong skin tone for characters.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL001
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001
- optional_refs: 
- visible_character_assets: observer, companion_human
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: daylight with smoke haze
- composition_type: Wide shot, exterior corridor threshold
- continuity_mode: static wide frame
- starting_keyframe_strategy: Companion at left edge moving right
- dependency_policy: No dependencies; standalone establishing shot
- auto_advance_policy: Hold on wide frame for 3-4 seconds
- fallback_strategy: Tighten to medium wide if entry unclear
- consistency_assist_policy: Apply four_ref consistency targets
- consistency_assist_method: 
- anatomy_repair_policy: Active for humanoid figures
- consistency_targets: 
- style_profile: Martian environment, daylight, smoke haze
- batch_role: establishing_shot
- fix_of: 

# Continuity Notes
- Keyframe must match start state of beat BT001.
- Companion at left edge moving right towards observer.
- Observer static center-right maintaining eye line on companion.
- No motion blur on observer during initial frame lock.
- Background smoke and fire effects consistent with chapter summary.
- Spatial axis: Left-to-center-right (companion to observer).
- Environment continuity: Exterior corridor threshold with building entrance.

# Repair Notes
- Apply four_ref consistency targets for humanoid figures.
- Ensure anatomy repair policy active for green-skinned entities.
- Maintain style profile for Martian environment lighting conditions.
- Verify character count matches visible assets list strictly.
- Check skin tone consistency between companion and observer.
- Confirm background elements match chapter visual continuity requirements.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: clip_prompt
stage: keyframe
version: 1

[[SECTION purpose]]
Establishes spatial relationship between approaching human companion and stationary human observer within exterior corridor threshold. Static wide frame captures urgent diagonal movement vector from left edge toward center-right position, setting up connection initiation beat start state with daylight smoke haze atmosphere and burning vessel visible in background distance.
[[/SECTION]]

[[SECTION positive_prompt]]
Wide exterior corridor threshold, human companion entering from left edge moving rightward across frame, human male observer standing center-right partial profile facing camera, daylight atmosphere with smoke haze, burning vessel visible in background distance, open plaza ground texture, gray painted air craft debris scattered near horizon, minimal crowd presence, building entrance threshold visible behind characters.
[[/SECTION]]

[[SECTION negative_prompt]]
blur, motion artifacts on static subjects, wrong character count, text overlay, distorted anatomy, dark shadows obscuring faces, extra limbs, missing eyes, low resolution, color shift, green skin on observer, fire on companion face, inconsistent proportions, facial feature distortion, background element misplacement, overexposed highlights, underexposed shadows, wrong skin tone for characters.
[[/SECTION]]

[[SECTION inputs_markdown]]
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL001
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001
- optional_refs: 
- visible_character_assets: observer, companion_human
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: daylight with smoke haze
- composition_type: Wide shot, exterior corridor threshold
- continuity_mode: static wide frame
- starting_keyframe_strategy: Companion at left edge moving right
- dependency_policy: No dependencies; standalone establishing shot
- auto_advance_policy: Hold on wide frame for 3-4 seconds
- fallback_strategy: Tighten to medium wide if entry unclear
- consistency_assist_policy: Apply four_ref consistency targets
- consistency_assist_method: 
- anatomy_repair_policy: Active for humanoid figures
- consistency_targets: 
- style_profile: Martian environment, daylight, smoke haze
- batch_role: establishing_shot
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
- Keyframe must match start state of beat BT001.
- Companion at left edge moving right towards observer.
- Observer static center-right maintaining eye line on companion.
- No motion blur on observer during initial frame lock.
- Background smoke and fire effects consistent with chapter summary.
- Spatial axis: Left-to-center-right (companion to observer).
- Environment continuity: Exterior corridor threshold with building entrance.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
- Apply four_ref consistency targets for humanoid figures.
- Ensure anatomy repair policy active for human entities.
- Maintain style profile for Martian environment lighting conditions.
- Verify character count matches visible assets list strictly.
- Check skin tone consistency between companion and observer.
- Confirm background elements match chapter visual continuity requirements.
[[/SECTION]]
[[/FILMCREATOR_PACKET]]
````
