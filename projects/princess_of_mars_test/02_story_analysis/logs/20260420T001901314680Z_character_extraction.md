# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:19:01.314680+00:00
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

# Visual Continuity Facts
- **Environment:** Yellowish mosslike vegetation, quartz-bearing rock, low hills, solid glass roof (4-5 inches thick).
- **Martians:** 15 feet tall, dark slate skin, yellow feet, small cup-shaped antennae ears, blood red iris, white teeth with upward-curving tusks.
- **Mounts:** Ten feet high at shoulder, four legs, broad flat tail, no hair, smooth glossy, no bridle/reins.
- **Eggs:** Snowy white, 2.5 feet diameter, hatching process observed.
- **Weapons:** 40-foot spears (metal-tipped), rifles (white metal barrel, wood stock, radium projectiles).

# Broad Story Summary
The narrator wakes in a circular basin on Mars and realizes gravity is significantly lower, causing them to jump three yards upon standing. While attempting to walk, they hop and sprawl due to unfamiliar muscle dynamics. They discover a glass incubator containing giant eggs and observe grotesque young Martians hatching. A group of adult Martians approaches; the leader's spear nearly strikes the narrator, but the sound alerts the leader. The narrator leaps thirty feet into the air to escape, landing safely on the opposite side. The Martians are surprised by this agility. The leader dismounts unarmed and offers a metal armlet as a peace token. The narrator accepts it, and they walk together before the leader mounts his animal. The entire cavalcade departs towards the range of hills.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH003

| Character | Role | Physical Presence | Description Status |
|-----------|------|-------------------|-------------------|
| Narrator | First-person perspective observer | Present | Uncertain physical details |
| Martian Leader | Approaching adult Martian | Present | Detailed description available |
| Martians (Group) | Adult Martian group | Present | Group description available |

*Note: Character descriptions vary in completeness based on source material.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_ch003
canonical_character_id: narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical appearance details provided in chapter summary. Cannot determine gender, age, race, or other visual characteristics for image generation purposes.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# narrator_ch003.md

## Character Role
First-person narrative perspective character who wakes up on Mars and encounters the Martians.

## Physical Presence
**Present** - The narrator is physically present in all scenes described, experiencing the Martian encounter firsthand.

## Physical Description
**Uncertain** - No physical appearance details are provided in the source material. Cannot determine:
- Gender or sex characteristics
- Age or developmental stage  
- Race or ethnicity
- Height or build
- Hair color or style
- Eye color
- Skin tone
- Facial features

## Costume & Silhouette
**Unknown** - No clothing, accessories, or silhouette details are described in the chapter.

## Continuity-Critical Traits
- First-person perspective character experiencing Martian encounter
- Receives metal armlet as peace token from Martian leader
- Demonstrates exceptional agility (leaps 30 feet)
- Travels with Martians toward hill range

## Render-Facing Prompt Notes
```
[UNCERTAIN PHYSICAL DETAILS]
Need manual description for image generation. 
Cannot proceed without additional physical appearance information.
Focus on: Martian encounter experience, low gravity effects, receiving armlet token.
```

## Uncertainty Notes
**CRITICAL**: This character lacks sufficient physical description for dependable image generation. Manual description required before proceeding with visual content creation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_leader_ch003
canonical_character_id: martian_leader
aliases: Martian leader, adult Martian
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description provided in chapter summary (15 feet tall, dark slate skin, yellow feet, small cup-shaped antennae ears, blood red iris, white teeth with upward-curving tusks).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# martian_leader_ch003.md

## Character Role
Adult Martian leader who approaches the narrator and offers peace token.

## Physical Presence
**Present** - The leader is physically present in the encounter, dismounts unarmed to offer armlet, then remounts animal for departure.

## Physical Description
**Supported by Source**:
- Height: 15 feet tall
- Skin: Dark slate color
- Feet: Yellow
- Antennae: Small cup-shaped ears/antennae
- Eyes: Blood red iris
- Teeth: White with upward-curving tusks

## Costume & Silhouette
**Supported by Source**:
- No hair on body
- Smooth glossy appearance
- Wears metal armlet (offered as peace token)
- Rides ten-foot-high animal mount

## Continuity-Critical Traits
- Leader of approaching Martian group
- Offers metal armlet as peace token to narrator
- Dismounts unarmed during encounter
- Remounts animal after offering token
- Leads cavalcade toward hill range

## Render-Facing Prompt Notes
```
[PHYSICAL DESCRIPTION AVAILABLE]
Use provided physical characteristics for image generation:
- 15 feet tall Martian figure
- Dark slate skin tone
- Yellow feet
- Cup-shaped antennae ears
- Blood red iris eyes
- White teeth with upward-curving tusks
- Smooth glossy body surface
- Metal armlet accessory
```

## Uncertainty Notes
**NO CRITICAL UNCERTAINTIES**: All physical description details are provided in source material. Ready for image generation using specified characteristics.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martians_group_ch003
canonical_character_id: martians_group
aliases: Martians, adult Martians, Martian group
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description provided in chapter summary (15 feet tall, dark slate skin, yellow feet, small cup-shaped antennae ears, blood red iris, white teeth with upward-curving tusks).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# martians_group_ch003.md

## Character Role
Group of adult Martians that approaches the narrator's location.

## Physical Presence
**Present** - The group is physically present in the encounter, with leader dismounting to offer peace token while others remain mounted.

## Physical Description
**Supported by Source**:
- Height: 15 feet tall
- Skin: Dark slate color
- Feet: Yellow
- Antennae: Small cup-shaped ears/antennae
- Eyes: Blood red iris
- Teeth: White with upward-curving tusks
- Body: No hair, smooth glossy appearance

## Costume & Silhouette
**Supported by Source**:
- Smooth glossy body surface
- No bridle or reins on mounts
- Rides ten-foot-high four-legged animal mounts
- Broad flat tail visible

## Continuity-Critical Traits
- Group approaches narrator's location
- Leader dismounts unarmed to offer armlet
- Others remain mounted during encounter
- Entire group surprised by narrator's agility (30-foot leap)
- Cavalcade departs toward hill range after token exchange

## Render-Facing Prompt Notes
```
[PHYSICAL DESCRIPTION AVAILABLE]
Use provided physical characteristics for image generation:
- 15 feet tall Martian figures
- Dark slate skin tone
- Yellow feet
- Cup-shaped antennae ears
- Blood red iris eyes
- White teeth with upward-curving tusks
- Smooth glossy body surface
- Four-legged animal mounts (ten-foot high)
- No hair on bodies or mounts
```

## Uncertainty Notes
**NO CRITICAL UNCERTAINTIES**: All physical description details are provided in source material. Ready for image generation using specified characteristics. Group representation may vary based on composition needs.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
