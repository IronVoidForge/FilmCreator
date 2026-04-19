# FilmCreator Prompt Writing Exchange
- timestamp_utc: 2026-04-19T19:33:09.301232+00:00
- stage: scene_stage
- clip_id: CL005
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
Target stage: scene_stage
Stage guidance: Describe staging intent, subject placement, environmental context, and the intended visible opening frame setup. This is authoring-only and should not read like a render prompt for a model.
Use descriptive noun phrases and avoid proper nouns in prompt text.
Keep duration and workflow metadata in inputs_markdown, not in the prompt body.
Follow the requested section names exactly.
````

## User Prompt
````text
Project: princess_of_mars_test

Scene: CH008_SC005

Clip: CL005

Prompt title: CH008_SC005 CL005 Scene Stage Prompt

Prompt id: CH008_SC005_CL005_scene_stage_prompt

Workflow type: authoring.scene_stage

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

stage: scene_stage

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

**Clip ID:** CL005  
**Shot Description:** Wide three-shot: All parties visual connection visible  
**Beat Reference:** BT003 (Emotional Anchor)  
**Coverage Family:** Wide three-shot  

**Continuity Mode:** Emotional anchor continuity  
**Composition Type:** Three-plane composition allowing all visual connections  
**Starting Keyframe Strategy:** Establish all three characters within visual range of each other  
**Dependency Policy:** Follows CL004; dependent on close-up reaction beat  
**Fallback Strategy:** Cut to next narrative beat if scene concludes here  
**Visible Character Assets:** Carter (primary), Sola (secondary), Prisoner (tertiary)  
**Required Refs:** Exterior corridor with clear sightlines, Character positions consistency  
**Optional Refs:** Weather effects on all characters for mood  
**Opening Keyframe Intent:** Show full emotional impact of visual connection between all parties  
**Cut Motion Intent:** Match cut to next narrative beat or scene end  
**Interval Beats:** 1. All parties establish visual awareness, 2. Tension created by multiple gaze dynamics, 3. Scene transitions

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
Initiate connection between Sola and Carter through urgent physical approach, establishing their relationship dynamic.

## Start State
- Sola in motion from left side of frame
- Carter standing center-right, unaware of approaching figure
- Exterior corridor entrance visible behind both characters

## End State
- Sola reaches Carter within arm's distance
- Physical contact or immediate verbal exchange occurs
- Carter's awareness shifts to approaching figure

## Character Placement and Movement Logic
- **Sola**: Active movement from left to center, diagonal trajectory toward Carter
- **Carter**: Static position center-right, minimal movement until Sola arrives
- **Movement Type**: Urgent approach (implies chase or rescue scenario)

## Geography, Axis, or Eyeline Facts
- **Location**: Exterior corridor entrance threshold
- **Axis**: Sola enters from left; Carter faces camera direction
- **Eyeline**: Sola's gaze directed at Carter; Carter initially unaware, then shifts to Sola
- **Depth**: Two-plane composition (Carter foreground, corridor background)

## Prop, Vehicle, Crowd, and Environmental State
- **Props**: None specific, focus on physical proximity
- **Environment**: Exterior lighting conditions, possible rain or weather effects
- **Crowd**: No bystanders, intimate two-character moment
- **Continuity**: Sola's clothing state (rushed appearance), Carter's position consistency

## Likely Coverage Families
1. Wide shot: Shows full approach trajectory and spatial relationship
2. Over-the-shoulder: From Carter's perspective watching Sola arrive
3. Close-up reaction: Carter's face as awareness shifts to approaching figure
4. Medium two-shot: Both characters in frame during connection moment

## BT002.md
# BT002 - Prisoner Dragged Through View (Conflict Introduction)

## Beat Purpose
Introduce conflict through visual disruption of the established two-character moment, creating narrative tension.

## Start State
- Carter and Sola in connection phase
- Prisoner visible in background moving right-to-left
- Building structure partially obscures prisoner's full form

## End State
- Prisoner moves behind building structure or out of clear view
- Visual disruption creates emotional impact on Carter
- Connection moment interrupted by external conflict

## Character Placement and Movement Logic
- **Carter**: Static center-right position, minimal movement during beat
- **Sola**: May pause or react to prisoner's appearance
- **Prisoner**: Background movement right-to-left, diagonal trajectory
- **Movement Type**: Forced/disrupted movement (implies capture or escape)

## Geography, Axis, or Eyeline Facts
- **Location**: Building entrance threshold with depth
- **Axis**: Prisoner moves background right-to-left; Carter faces camera
- **Eyeline**: Carter's gaze may shift from Sola to prisoner; Sola may react to prisoner
- **Depth**: Three-plane composition (Carter foreground, corridor middle, building background)

## Prop, Vehicle, Crowd, and Environmental State
- **Props**: Building structure serves as visual obstruction element
- **Environment**: Exterior lighting, possible shadows from building structure
- **Crowd**: No bystanders, focus on three-character dynamic
- **Continuity**: Prisoner's clothing state (rushed/disheveled), Carter's position consistency

## Likely Coverage Families
1. Wide establishing: Shows all three characters in spatial relationship
2. Medium two-shot: Carter and Sola with prisoner visible in background
3. Profile shot: Prisoner moving through frame right-to-left
4. Over-the-shoulder: From Carter's perspective watching prisoner appear

## BT003.md
# BT003 - Eye Contact & Reaction (Emotional Anchor)

## Beat Purpose
Create emotional anchor through established visual connection between all parties, grounding the scene's emotional impact.

## Start State
- All three characters establish visual awareness of each other
- Carter and Sola maintain connection while prisoner visible
- Tension created by multiple gaze dynamics

## End State
- Reaction shots showing emotional impact on each character
- Visual connection sustained or interrupted
- Scene transitions to next narrative beat

## Character Placement and Movement Logic
- **Carter**: Primary focus, minimal movement, reaction-driven
- **Sola**: Secondary focus, may react to both Carter and prisoner
- **Prisoner**: Background presence, limited movement during this beat
- **Movement Type**: Reaction-based, minimal physical movement

## Geography, Axis, or Eyeline Facts
- **Location**: Exterior corridor with clear sightlines between all parties
- **Axis**: All three characters within visual range of each other
- **Eyeline**: Multiple gaze dynamics (Carter→Sola, Carter→Prisoner, Sola→Carter/Prisoner)
- **Depth**: Three-plane composition allowing all visual connections

## Prop, Vehicle, Crowd, and Environmental State
- **Props**: None specific, focus on gaze dynamics
- **Environment**: Exterior lighting conditions, possible weather effects
- **Crowd**: No bystanders, intimate three-character moment
- **Continuity**: Character positions consistent across reaction shots

## Likely Coverage Families
1. Close-up reaction: Carter's face showing emotional impact
2. Over-the-shoulder: From Sola's perspective watching both Carter and prisoner
3. Wide three-shot: All three characters in frame with visual connections visible
4. Medium close-up: Focus on primary character (Carter) with background elements

## Clip Roster

# Clip Roster - CH008_SC005

| Clip ID | Shot Description | Beat Reference | Coverage Family | Duration Target |
| :--- | :--- | :--- | :--- | :--- |
| CL001 | Wide: Sola rushes in from left, Carter center-right | BT001 | Wide shot | 5s |
| CL002 | Over-the-shoulder: Carter's perspective watching Sola arrive | BT001 | Over-the-shoulder | 5s |
| CL003 | Medium two-shot: Prisoner dragged through background view | BT002 | Medium two-shot | 5s |
| CL004 | Close-up: Carter reaction & eye contact established | BT003 | Close-up reaction | 5s |
| CL005 | Wide three-shot: All parties visual connection visible | BT003 | Wide three-shot | 5s |

## Clip State

{
  "project_id": "princess_of_mars_test",
  "scene_id": "CH008_SC005",
  "clip_id": "CL005",
  "status": "planning",
  "inputs": {
    "shared_character_refs": [],
    "shared_environment_refs": [],
    "scene_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC005/CL005/CH008_SC005_CL005_scene_stage_prompt.md",
    "scene_stage_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC005/CL005/CH008_SC005_CL005_scene_stage_prompt.md",
    "keyframe_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/keyframes/CH008_SC005/CL005/CH008_SC005_CL005_keyframe_prompt.md",
    "fix_prompt_packages": [
      "projects/princess_of_mars_test/03_prompt_packages/fixes/CH008_SC005/CL005/CH008_SC005_CL005_fix_01_prompt.md"
    ],
    "anchor_prompt_packages": [],
    "video_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC005/CL005/CH008_SC005_CL005_cut_motion_prompt.md",
    "cut_motion_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC005/CL005/CH008_SC005_CL005_cut_motion_prompt.md",
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
CH008_SC005 CL005 Scene Stage Prompt

# ID
CH008_SC005_CL005_scene_stage_prompt

# Purpose
Establish emotional anchor through eye contact between Carter and prisoner; show Carter's reaction to prisoner's state in background movement; medium shot composition with both characters visible for connection

# Workflow Type
authoring.scene_stage

# Positive Prompt
Carter face and upper body in foreground, eyes focused on prisoner in background, Martian city buildings with windows and roofs, daylight atmosphere, open ground plaza area, partial visibility of slender girlish figure with light reddish copper skin, coal black hair caught loosely into strange coiffure, highly wrought ornaments visible, green Martian warriors firing from buildings in distance, smoke from fire effects, missile impact flames spurt

# Negative Prompt
full body shots, other characters entering frame, excessive camera movement, close-up only on eyes, wide shot showing entire city, night lighting, indoor corridor setting, no prisoner visible, green Martian females dragging prisoner, air craft in foreground, explosion effects dominating frame

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL005
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT003, CH008_SC005/BT003.md Start State
- optional_refs: None
- visible_character_assets: Carter (face and upper body), Prisoner (background, partial visibility)
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: daylight with smoke from fire
- composition_type: Medium shot, both Carter and prisoner in frame for eye contact
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Static frame showing Carter's face locked on prisoner's background movement
- dependency_policy: Depends on CL004 establishing conflict context; no reverse dependency
- auto_advance_policy: None
- fallback_strategy: If eye contact unclear, tighten to close-up on Carter's eyes or widen to show more of prisoner's expression
- consistency_assist_policy: None
- consistency_assist_method: None
- anatomy_repair_policy: None
- consistency_targets: Eye contact clarity, character identification
- style_profile: Action-oriented, awe-inspiring
- batch_role: scene_stage
- fix_of: None

# Continuity Notes
- Capture the continuity rules for this stage. Maintain eye line between Carter and prisoner throughout clip duration. Keep background movement consistent with previous shots showing prisoner being dragged into building. Ensure lighting matches daylight conditions with fire smoke effects from previous battle sequence. Character identification must remain clear - Carter as observer, prisoner as captive with distinctive reddish copper skin and coal black hair.

# Repair Notes
- Capture any repair or corrective guidance for this stage. If eye contact is not clearly established in initial render, tighten framing to close-up on Carter's eyes while maintaining background visibility of prisoner. If prisoner becomes too obscured by environment, widen shot slightly to show more of her upper body and distinctive features. Ensure no other characters enter frame during this emotional anchor moment.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL005.md
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
stage: scene_stage
version: 1

[[SECTION purpose]]
Establish emotional anchor through eye contact between Carter and prisoner; show Carter's reaction to prisoner's state in background movement; wide three-shot composition with all parties visible for visual connection
[[/SECTION]]

[[SECTION positive_prompt]]
John Carter standing center-right facing camera, Sola entering from left side in motion, Human Female Prisoner moving background right-to-left partially obscured by building structure. Martian city buildings with windows and roofs in daylight atmosphere, smoke from fire effects, open ground plaza area. Slender girlish figure with light reddish copper skin, coal black hair caught
````
