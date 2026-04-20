# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:22:18.185683+00:00
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

Visual Continuity: Arizona hills, clear mornings, moonlight, horse/burro tracks, Apache tepees, cave chamber with smooth floor and shadowed back.

Story Summary: March 3, 1866. Powell departs to buy mining equipment. Carter follows his trail after discovering signs of an Apache ambush at a water hole. He finds Powell dead in the cave. Carter enters the cave, lays Powell down, and succumbs to drowsiness/exhaustion on the floor.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH001

## Characters Identified

| Asset ID | Canonical Character ID | Display Name | Status |
|----------|------------------------|--------------|--------|
| powell | POWELL | Powell | Referenced, deceased |
| carter | CARTER | Carter | Present, exhausted |

## Notes

- Chapter summary mentions two primary characters: Powell and Carter
- Both characters lack detailed physical descriptions in source material
- Powell is found dead in cave chamber
- Carter follows Powell's trail and succumbs to exhaustion on floor
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: powell
canonical_character_id: POWELL
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary only mentions Powell departs to buy mining equipment and is found dead in cave. No physical description, appearance details, or visual characteristics provided in source material. Cannot support dependable image generation without additional manual description.
clarification_required: true
clarification_reason: Character might already exist under another name or is too weakly identified for reliable continuity tracking across chapters.
clarification_question: What are Powell's physical characteristics (age, build, distinguishing features) and what name variations should be used for continuity?

[[SECTION markdown]]
# Powell - Chapter CH001

## Display Name
Powell

## Chapter Role
Protagonist/Deceased character whose trail is followed by Carter

## Physical Presence Status
Referenced only - found dead in cave chamber. Not physically present during chapter events.

## Physical Description
**Source-supported details:** None available in chapter summary. Character is mentioned as departing to buy mining equipment and being discovered dead in a cave with smooth floor and shadowed back.

**Missing details requiring manual description:**
- Age and build
- Facial features and expression
- Hair color and style
- Eye color
- Height and weight
- Distinguishing marks or scars
- Typical clothing style (before death)
- Build/silhouette characteristics

## Costume/Silhouette Traits
**Known:** None - character is deceased in cave chamber. No costume details provided in source material.

**Continuity-critical notes:** Character's appearance must be established through manual description for later image generation and continuity tracking across chapters.

## Descriptive Noun Phrases for Render Prompts
- "mining equipment buyer"
- "deceased in cave chamber"
- "trail follower subject"
- "Powell character from 1866 narrative"

## Uncertainty Notes
⚠️ **CRITICAL:** No physical description available in source material. Character must be manually described for reliable image generation and continuity tracking. Appearance details are completely unknown from chapter summary alone.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: CARTER
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary only mentions Carter follows Powell's trail and succumbs to exhaustion on cave floor. No physical description, appearance details, or visual characteristics provided in source material. Cannot support dependable image generation without additional manual description.
clarification_required: false
clarification_reason: Character is clearly identified as the protagonist following Powell's trail with no indication of existing under another name or weak identification for continuity purposes.
clarification_question: 

[[SECTION markdown]]
# Carter - Chapter CH001

## Display Name
Carter

## Chapter Role
Protagonist/Active character who follows Powell and succumbs to exhaustion

## Physical Presence Status
Present during chapter events - enters cave chamber, lays Powell down, succumbs to drowsiness/exhaustion on floor.

## Physical Description
**Source-supported details:** None available in chapter summary. Character is mentioned as following trail after discovering Apache ambush signs at water hole and finding Powell dead.

**Missing details requiring manual description:**
- Age and build
- Facial features and expression
- Hair color and style
- Eye color
- Height and weight
- Distinguishing marks or scars
- Typical clothing style (before exhaustion)
- Build/silhouette characteristics

## Costume/Silhouette Traits
**Known:** None - character succumbs to exhaustion on cave floor. No costume details provided in source material.

**Continuity-critical notes:** Character's appearance must be established through manual description for later image generation and continuity tracking across chapters.

## Descriptive Noun Phrases for Render Prompts
- "trail follower"
- "Apache ambush discoverer"
- "exhausted protagonist"
- "Carter character from 1866 narrative"

## Uncertainty Notes
⚠️ **CRITICAL:** No physical description available in source material. Character must be manually described for reliable image generation and continuity tracking. Appearance details are completely unknown from chapter summary alone.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
