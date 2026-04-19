# FilmCreator Prompt Writing Exchange
- timestamp_utc: 2026-04-19T16:56:26.688667+00:00
- stage: still_fix
- clip_id: CL002
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
Target stage: still_fix
Stage guidance: Write a corrective still-generation prompt that preserves composition and look while fixing local issues. Assume image_1 is the approved still base and image_2 is a secondary reference when needed.
Use descriptive noun phrases and avoid proper nouns in prompt text.
Keep duration and workflow metadata in inputs_markdown, not in the prompt body.
Follow the requested section names exactly.
````

## User Prompt
````text
Project: princess_of_mars_test

Scene: CH008_SC001

Clip: CL002

Prompt title: CH008_SC001 CL002 Fix 01 Prompt

Prompt id: CH008_SC001_CL002_fix_01_prompt

Workflow type: still.scene_insert.two_ref.klein.distilled

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

stage: still_fix

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

**Clip ID:** CL002  
**Continuity Mode:** reframe_same_moment  
**Composition Type:** wide establishing shot from Carter's POV  
**Starting Keyframe Strategy:** static_hold  
**Dependency Policy:** none  
**Fallback Strategy:** insert  
**Visible Character Assets:** None (vessel focus), air craft fleet (20 vessels)  
**Required Refs:** BT002.md, CH008_SC001/BEAT_INDEX.md  
**Optional Refs:** None  
**Opening Keyframe Intent:** Show first air craft visible in distance  
**Cut Motion Intent:** cutaway_to_martians  
**Interval Beats:** 0-2s: First craft appears, 2-4s: fleet expands to 20 vessels, 4-5s: prepare for martian focus

**Shot Notes:** Wide shot showing air craft descending from upper sky toward city building. Gray-painted long low vessels with strange banners visible. Valley below and hills beyond maintain continuity.

## Scene Breakdown

**Scene Purpose:** Establish John Carter's perspective and introduce air craft arrival as a pivotal moment.

**Scene Summary:** From an upper floor window, John Carter watches twenty large gray air craft descend toward the city. The procession has retreated to a city building due to immediate orders. His observation sets the stage for the coming conflict.

**Participating Characters:** John Carter (observer), Green Martian figures (crowding forward decks of air craft)

**Participating Environments:** City building upper floor, window view, valley below, hills beyond

**Dominant Emotional Shift:** Curiosity → Anticipation (Carter's growing concern as he witnesses the arrival)

**Likely Visual Coverage Families:** Wide establishing shots from Carter's POV, medium shots of air craft descending, close-ups on Carter's face observing

**Likely Continuity Sensitivities:** Air craft appearance consistency (long, low, gray-painted vessels with strange banners), Carter's position in window, valley/hills background continuity

## Beat Bundles

## BT001.md
**Beat BT001 - John Carter at Window Observing Arrival**

**Purpose:** Establish Carter's POV and emotional state as he watches air craft descend.

**Start State:** Carter standing at upper floor window, initial curiosity visible on face.

**End State:** Carter's expression shifts to growing concern/anticipation as more craft appear.

**Character Placement:** John Carter positioned at window frame, body angled toward city view below.

**Movement Logic:** Minimal movement - subtle shifts in posture reflecting emotional change.

**Geography/Axis/Eyeline:** Eyeline directed downward toward valley/city; vertical axis from upper floor to ground level.

**Continuity State:** Window frame visible, Carter's clothing consistent, background valley/hills stable.

**Likely Coverage Families:** Close-up on Carter's face (POV), medium shot showing window and partial view outside, over-the-shoulder establishing shot.

## BT002.md
**Beat BT002 - Air Craft Descending Toward City Building**

**Purpose:** Show the procession arrival as central visual element of scene.

**Start State:** First air craft visible in distance, beginning descent trajectory.

**End State:** Twenty air craft fully visible descending toward city building facade.

**Character Placement:** No characters on air craft yet - focus on vessels themselves.

**Movement Logic:** Downward diagonal movement from upper sky to lower city level.

**Geography/Axis/Eyeline:** Horizontal axis across valley; vertical descent path; eyeline from Carter's POV downward.

**Continuity State:** Air craft appearance consistent (long, low, gray-painted with strange banners), number of vessels tracked at 20.

**Likely Coverage Families:** Wide establishing shot showing multiple craft, medium shots tracking individual vessel descent, POV shots from Carter's window perspective.

## BT003.md
**Beat BT003 - Green Martian Figures Crowding Forward Decks**

**Purpose:** Introduce secondary character element and build tension for arrival moment.

**Start State:** Green Martians visible on forward decks of air craft, crowding toward front.

**End State:** Martians positioned at front edge of vessels, preparing for city building approach.

**Character Placement:** Multiple Green Martian figures distributed across forward sections of descending air craft.

**Movement Logic:** Forward movement along vessel length toward front edge; coordinated with vessel descent.

**Geography/Axis/Eyeline:** Horizontal axis along vessel deck; eyeline from Carter's POV includes Martians as secondary focus.

**Continuity State:** Green Martian costume/figure consistency, positioning on forward decks maintained across shots.

**Likely Coverage Families:** Medium shots showing Martians on vessel decks, close-ups of individual figures, wide shots including both Martians and descending craft.

## Clip Roster

# Clip Roster - CH008_SC001

| Clip ID | Description | Duration Target |
|---------|-------------|-----------------|
| CL001 | John Carter at Window - Initial Observation | 5s |
| CL002 | Air Craft Descending - Wide Establishing | 5s |
| CL003 | Green Martians on Forward Decks - Medium | 5s |
| CL004 | John Carter Reaction - Growing Concern | 5s |

**Scene:** CH008_SC001  
**Project:** princess_of_mars_test  
**Total Clips:** 4

## Clip State

{
  "project_id": "princess_of_mars_test",
  "scene_id": "CH008_SC001",
  "clip_id": "CL002",
  "status": "planning",
  "inputs": {
    "shared_character_refs": [],
    "shared_environment_refs": [],
    "scene_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC001/CL002/CH008_SC001_CL002_scene_stage_prompt.md",
    "scene_stage_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC001/CL002/CH008_SC001_CL002_scene_stage_prompt.md",
    "keyframe_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/keyframes/CH008_SC001/CL002/CH008_SC001_CL002_keyframe_prompt.md",
    "fix_prompt_packages": [
      "projects/princess_of_mars_test/03_prompt_packages/fixes/CH008_SC001/CL002/CH008_SC001_CL002_fix_01_prompt.md"
    ],
    "anchor_prompt_packages": [],
    "video_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC001/CL002/CH008_SC001_CL002_cut_motion_prompt.md",
    "cut_motion_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC001/CL002/CH008_SC001_CL002_cut_motion_prompt.md",
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
    },
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
    }
  }
}



Existing prompt draft:

# Title
CH008_SC001 CL002 Fix 01 Prompt

# ID
CH008_SC001_CL002_fix_01_prompt

# Purpose
Corrective still-generation prompt that preserves composition and look while fixing local issues. Image_1 serves as approved base, image_2 as secondary reference when needed.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Group of Green Martian warriors entering dark doorways in deserted city buildings. Medium shot composition showing synchronized entry motion from exterior perspective. Doorway frames visible with interior shadows swallowing figures. Deserted valley city architecture surrounding entrances. Martians wearing green attire moving inward into darkness. Over-the-shoulder angle from doorway threshold looking into building interiors. Synchronized steps maintaining formation integrity as they vanish within three minutes.

# Negative Prompt
Anatomical errors, inconsistent lighting, wrong character count, misplaced elements, blurred details, incorrect color palette, anatomical distortions, extra limbs, missing weapons, wrong environmental state, inconsistent motion blur, poor depth of field, low resolution artifacts, facial expression mismatches, weapon placement errors, background element intrusions, Carter, Earthling Woman, bright daylight interiors, open ground valley floor.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md building_entry_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Green Martian warriors group_clusters_entrance
- look_continuity_policy: preserve_building_entry_motion_and_architecture_style
- intended_lighting_change: maintain_valley_transition_atmosphere_dark_interiors
- composition_type: medium_shot_over_the_shoulder
- continuity_mode: insert
- starting_keyframe_strategy: follow_group_entry_from_doorway_threshold
- dependency_policy: dependent_on_CL001_wide_establishing_first
- auto_advance_policy: none
- fallback_strategy: cut_to_medium_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: composition_lock
- anatomy_repair_policy: strict
- consistency_targets: character_placement_environment_state_motion_logic
- style_profile: cinematic_warfare_valley_transition
- batch_role: still_fix_stage_01
- fix_of: CL002_medium_tracking_shot

# Continuity Notes
- Martians enter doorways in groups maintaining formation integrity
- Green attire visible against dark building interiors
- Doorway frames clear and accessible with no obstacles
- Interior shadows swallowing figures as they vanish
- Deserted city buildings frame the entrance axis
- Valley terrain visible beyond building exteriors
- Motion logic follows forward progression into darkness

# Repair Notes
- Preserve overall composition and architectural style while correcting local issues
- Maintain character placement consistency with approved base image
- Fix any anatomical errors or misplaced elements without altering motion logic
- Ensure lighting continuity matches dark interior atmosphere
- Correct environmental state transitions between exterior and doorway interiors
- Repair any inconsistent details while preserving cinematic warfare aesthetic

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: clip_prompt
stage: still_fix
version: 1

[[SECTION purpose]]
Corrective still-generation prompt that preserves composition and look while fixing local issues. Image_1 serves as approved base, image_2 as secondary reference when needed.
[[/SECTION]]

[[SECTION positive_prompt]]
Wide establishing shot showing twenty large gray air craft descending from upper sky toward city building facade. Long low vessels with strange banners visible on prows. Valley below and hills beyond maintain continuity. Figures crowd forward decks of vessels. Downward diagonal movement from upper sky to lower city level. Gray-painted vessels with odd devices on prows.
[[/SECTION]]

[[SECTION negative_prompt]]
Anatomical errors, inconsistent lighting, wrong character count, misplaced elements, blurred details, incorrect color palette, anatomical distortions, extra limbs, missing weapons, wrong environmental state, inconsistent motion blur, poor depth of field, low resolution artifacts, facial expression mismatches, weapon placement errors, background element intrusions, John Carter, Earthling Woman, bright daylight interiors, open ground valley floor.
[[/SECTION]]

[[SECTION inputs_markdown]]
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md air_craft_descending_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: air_craft_fleet_20_vessels
- look_continuity_policy: preserve_air_craft_descending_motion_and_architecture_style
- intended_lighting_change: maintain_valley_transition_atmosphere_daylight
- composition_type: wide_establishing_shot_from_pov
- continuity_mode: insert
- starting_keyframe_strategy: show_first_air_craft_visible_in_distance
- dependency_policy: dependent_on_CL001_wide_establishing_first
- auto_advance_policy: none
- fallback_strategy: cut_to_wide_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: composition_lock
- anatomy_repair_policy: strict
- consistency_targets: character_placement_environment_state_motion_logic
- style_profile: cinematic_warfare_valley_transition
- batch_role: still_fix_stage_01
- fix_of: CL002_wide_establishing_shot
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
- Air craft appear consistent (long, low, gray-painted with strange banners)
- Number of vessels tracked at 20
- Valley terrain visible beyond building exteriors
- Hills beyond maintain directional context
- Downward diagonal movement from upper sky to lower city level
- Figures crowd forward decks of vessels
[[/SECTION]]

[[SECTION repair_notes_markdown]]
- Preserve overall composition and architectural style while correcting local issues
- Maintain character placement consistency with approved base image
- Fix any anatomical errors or misplaced elements without altering motion logic
- Ensure lighting continuity matches daylight atmosphere
- Correct environmental state transitions between exterior and valley/hills
- Repair any inconsistent details while preserving cinematic warfare aesthetic
[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
