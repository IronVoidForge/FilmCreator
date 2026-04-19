# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:31:12.645563+00:00
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

Chapter id: CH001

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

# Chapter Summary: CH001

## Story Summary

- **Introduction:** Narrator reflects on his age and mortality. He is a soldier of fortune recounting strange events during ten years in an Arizona cave.
- **Backstory:** Carter finds a gold vein with Captain James K. Powell. They uncover over a million dollars worth of ore in three months.
- **Inciting Incident:** Powell leaves to buy machinery; Carter guards the claim alone.
- **Rising Action:** Carter sees Powell's party vanish into shadows. He follows tracks, discovering they are unshod ponies galloping away.
- **Climax:** Carter finds an Apache camp under moonlight. Powell is dead, riddled with arrows. Carter charges the warriors single-handedly.
- **Falling Action:** Carter escapes pursuit by taking a wrong trail into a defile. He reaches a cave mouth at dawn.
- **Resolution:** Carter lays Powell's body down. He enters the cave but collapses from exhaustion against the wall.

## Visual Continuity

- **Lighting:** Clear Arizona mornings; bright moonlight during night chase; sudden daylight without warning at cave entrance.
- **Props:** Colt revolvers, carbine, cartridge belts, saddle horse, burros, canteen water.
- **Locations:** Arizona hills, valley, plateau, Apache tepee camp, narrow gorge, cave mouth (4ft high, 3-4ft wide).
- **Environment:** Dusty trails, rocky ravines, jagged rock formations, dense shadow in cave back.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH001

## Characters Identified

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required |
|----------|------------------------|---------|------------------|------------------------------|
| carter_narrator | Carter | Carter (narrator) | true | true |
| captain_powell | Captain James K. Powell | Captain Powell, Captain James K. Powell | true | true |
| apache_warriors | Apache Warriors | Apache camp warriors | false | true |

## Character Notes

- **Carter**: Primary narrator and protagonist throughout the chapter. Physical description not provided in source material.
- **Captain James K. Powell**: Carter's companion found dead at Apache camp. Physical description not provided in source material.
- **Apache Warriors**: Multiple unnamed characters in Apache camp. Individual descriptions not provided; group reference only.

## Continuity Notes

All characters lack sufficient physical or visual description for dependable image generation. Manual descriptions required for all character records.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter_narrator
canonical_character_id: Carter
aliases: Carter (narrator)
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description, clothing, or visual traits provided in chapter summary. Only identified as "soldier of fortune" and narrator role.
clarification_required: false
clarification_reason: Character is clearly named and identified throughout chapter.
clarification_question: 

[[SECTION markdown]]
# carter_narrator.md

## Display Name
Carter (Narrator)

## Chapter Role
Primary protagonist and first-person narrator recounting events during ten years in an Arizona cave.

## Physical Presence
Physically present throughout the narrative as the telling voice of the story.

## Physical Description
**Status:** Uncertain - No physical description provided in source material.

**Known Traits:**
- Soldier of fortune (occupation)
- Narrator recounting strange events during ten years in an Arizona cave

**Uncertainty Notes:**
No height, build, hair color, eye color, facial features, or distinguishing marks are mentioned in the chapter summary. Physical description cannot be reliably generated from source material. Manual description required for image generation.

## Costume/Silhouette
**Status:** Uncertain - No costume details provided in source material.

**Known Traits:**
- None specified in chapter summary

**Uncertainty Notes:**
No clothing, accessories, or silhouette traits are mentioned. Cannot determine attire from source material.

## Continuity-Critical Traits
- Narrator voice throughout chapter
- Found dead companion: Captain James K. Powell
- Location progression: Arizona hills → Apache camp → cave mouth

## Render-Facing Prompt Notes
Use manual description for physical appearance. Focus on soldier of fortune occupation and narrator role for character context.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: captain_powell
canonical_character_id: Captain James K. Powell
aliases: Captain Powell, Captain James K. Powell
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description, clothing, or visual traits provided in chapter summary. Only identified as "Captain" and companion role. Found dead at Apache camp.
clarification_required: false
clarification_reason: Character is clearly named throughout chapter backstory and climax.
clarification_question: 

[[SECTION markdown]]
# captain_powell.md

## Display Name
Captain James K. Powell

## Chapter Role
Carter's companion and partner in finding gold vein; found dead at Apache camp.

## Physical Presence
Physically present as deceased body discovered at Apache camp under moonlight.

## Physical Description
**Status:** Uncertain - No physical description provided in source material.

**Known Traits:**
- Captain (rank)
- Companion to Carter during Arizona expedition
- Found dead, riddled with arrows

**Uncertainty Notes:**
No height, build, hair color, eye color, facial features, or distinguishing marks are mentioned in the chapter summary. Physical description cannot be reliably generated from source material. Manual description required for image generation.

## Costume/Silhouette
**Status:** Uncertain - No costume details provided in source material.

**Known Traits:**
- None specified in chapter summary

**Uncertainty Notes:**
No clothing, accessories, or silhouette traits are mentioned. Cannot determine attire from source material.

## Continuity-Critical Traits
- Partner with Carter during Arizona expedition
- Found dead at Apache camp (climax)
- Body laid down by Carter before entering cave
- Death method: riddled with arrows

## Render-Facing Prompt Notes
Use manual description for physical appearance. Focus on Captain rank and deceased companion role for character context. Arrow wounds may be relevant visual detail if manually described.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors
canonical_character_id: Apache Warriors
aliases: Apache camp warriors, Apache warriors
is_fully_identified: false
manual_description_required: true
manual_description_reason: No individual physical descriptions, clothing, or visual traits provided in chapter summary. Only referenced as group "warriors" at Apache camp. Multiple unnamed characters.
clarification_required: true
clarification_reason: Character is a group of multiple unnamed individuals without stable identification. Cannot determine if this refers to specific known Apache warriors or generic reference.
clarification_question: Does "Apache warriors" refer to specific named characters from established lore, or is this a generic group reference requiring manual description for each individual?

[[SECTION markdown]]
# apache_warriors.md

## Display Name
Apache Warriors (Group)

## Chapter Role
Antagonists in Apache camp scene; discover Powell's body and attack Carter.

## Physical Presence
Physically present as group at Apache camp under moonlight during climax sequence.

## Physical Description
**Status:** Uncertain - No individual physical descriptions provided in source material.

**Known Traits:**
- Group of warriors (multiple unnamed individuals)
- Located at Apache camp
- Attack Carter single-handedly after discovering Powell's body

**Uncertainty Notes:**
No height, build, hair color, eye color, facial features, or distinguishing marks are mentioned for any individual warrior. Physical description cannot be reliably generated from source material. Manual description required for image generation. Individual warriors not separately identified in chapter.

## Costume/Silhouette
**Status:** Uncertain - No costume details provided in source material.

**Known Traits:**
- None specified in chapter summary

**Uncertainty Notes:**
No clothing, accessories, or silhouette traits are mentioned. Cannot determine attire from source material.

## Continuity-Critical Traits
- Apache camp location (tepee camp)
- Moonlight during attack scene
- Carter charges warriors single-handedly
- Warriors escape pursuit by taking wrong trail into defile

## Render-Facing Prompt Notes
Use manual description for physical appearance. Focus on warrior group role and Apache cultural context if manually described. Individual warriors not separately identified; may require generic warrior template or clarification for specific character treatment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
