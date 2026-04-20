# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:45:45.433474+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Work like a careful local planning assistant for chapter analysis and shot-prep authoring.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
Prefer short, concrete section bodies over long prose.
Follow the requested headings and record fields exactly.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
If information is missing, say so briefly instead of guessing.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH003

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
...character_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character
asset_id: <value>
canonical_character_id: <value>
aliases: <value>
is_fully_identified: <value>
manual_description_required: <value>
manual_description_reason: <value>
clarification_required: <value>
clarification_reason: <value>
clarification_question: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- every character record must include a non-empty markdown section

- if details are sparse, still write a short markdown file explaining the uncertainty instead of omitting markdown

- never omit the markdown section for any character record



Asset id rules:

- lowercase snake_case

- stable across later reruns



Each character Markdown file should include:

- display name and chapter role

- whether the character is physically present, referenced, or uncertain

- physical description that is actually supported by the source

- costume, silhouette, and continuity-critical traits when known

- useful descriptive noun phrases for later render-facing prompt writing

- explicit uncertainty notes when important details are missing



Chapter summary:

# Chapter Title
CHAPTER III: MY ADVENT ON MARS

# Visual Continuity Facts
- **Environment:** Yellowish mosslike vegetation covering a circular basin; midday sun with intense heat; quartz-bearing rock outcroppings; low hills in distance.
- **Physics:** Protagonist jumps ~3 yards high on Earth-equivalent effort; walking manifests as hops and sprawls due to reduced gravity/air pressure.
- **Young Martians (Eggs):** Large eggs (~2.5 ft diameter) inside a solid glass enclosure roof; creatures are head-heavy with six limbs, blood red iris, white teeth/tusks, dark slate skin, small cup-shaped antennae ears.
- **Adult Martians & Mounts:** Warriors ~15 feet tall on four-legged mounts (~10 ft shoulder height); mounts have yellow feet, broad flat tail, no hair; warriors carry forty-foot spears tipped with gleaming metal; mounted without reins/bridle.
- **Objects:** Metal armlet ornaments strapped to head/limbs/breast; rifles of white metal and wood stock; glass-walled incubator structure.

# Story Summary
Protagonist wakes on Mars, explores a glass-walled enclosure containing hatching Martians. Ambushed by adult Martians on mounts; leader's spear nearly kills him. Protagonist leaps 30 feet to safety. Martians observe his agility and decide to capture him rather than kill. Leader offers peace via metal armlet. Protagonist accepts, rides with the cavalcade toward distant hills.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter III: MY ADVENT ON MARS

| Character | Role | Physical Presence | Description Status |
|-----------|------|-------------------|--------------------|
| Protagonist | Main character, explorer | Present | Manual description required |
| Leader Martian | Adult warrior, peace offerer | Present | Manual description required |

*Note: Young Martians (Eggs) and Adult Martians are treated as groups/creatures rather than individual character records.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: protagonist
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter provides no physical description of the protagonist's appearance, body type, or facial features. Only their actions and movements are described (hops, sprawls, leaping). Without visual details, dependable image generation is not possible.
clarification_required: true
clarification_reason: Need physical description for later render-facing prompt writing
clarification_question: What does the protagonist look like? (height, build, skin tone, hair, facial features)

[[SECTION markdown]]
# Protagonist - Chapter III: MY ADVENT ON MARS

## Display Name
Protagonist

## Chapter Role
Main character, explorer on Mars

## Physical Presence
Present - Wakes on Mars, explores glass enclosure, gets ambushed by adult Martians, leaps to safety, accepts peace offer

## Physical Description
**Uncertain/Not Provided:** Chapter contains no physical description of the protagonist's appearance. Only their movements are described (hops, sprawls, leaping ~30 feet). No details about height, build, skin tone, hair, or facial features are given in this chapter.

## Costume/Silhouette
**Uncertain/Not Provided:** No costume or silhouette details mentioned in the chapter.

## Continuity-Critical Traits
- Leaps approximately 30 feet to safety (demonstrates agility)
- Accepts metal armlet as peace offering
- Rides with cavalcade toward distant hills

## Render-Facing Prompt Notes
**Missing Information:** Physical description not provided in source material. Cannot generate dependable images without manual description.

**Recommended Action:** Manual description required before image generation can proceed reliably.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: leader_martian
canonical_character_id: leader_martian
aliases: Leader, Martian Leader
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter describes the leader only as an adult Martian warrior with no specific physical details beyond general Martian traits (blood red iris, white teeth/tusks, dark slate skin). No individual distinguishing features or personal appearance described.
clarification_required: true
clarification_reason: Need specific physical description for later render-facing prompt writing
clarification_question: What does the leader look like specifically? (height, build, facial expression, distinguishing features beyond general Martian traits)

[[SECTION markdown]]
# Leader Martian - Chapter III: MY ADVENT ON MARS

## Display Name
Leader Martian

## Chapter Role
Adult warrior, peace offerer, ambush leader

## Physical Presence
Present - Ambushes protagonist with adult Martians on mounts, offers metal armlet as peace offering

## Physical Description
**Partially Known:** General Martian traits apply (blood red iris, white teeth/tusks, dark slate skin, small cup-shaped antennae ears). However, no individual distinguishing features or personal appearance details are provided beyond these general species characteristics.

## Costume/Silhouette
**Known:** Adult Martian warrior ~15 feet tall on four-legged mount (~10 ft shoulder height). Carries forty-foot spear tipped with gleaming metal. Metal armlet ornaments strapped to head/limbs/breast. Mounted without reins/bridle.

## Continuity-Critical Traits
- Offers peace via metal armlet to protagonist
- Leader's spear nearly kills protagonist before he leaps to safety
- Decides to capture rather than kill protagonist after observing agility
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_PACKET]]
````
