# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T19:53:32.302072+00:00
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

# CHAPTER I: ON THE ARIZONA HILLS

## Story Summary

### Introduction
Narrator introduces himself as an old man who does not age, fearing death despite having died twice before. He intends to write a chronicle of his life and death.

### The Mine and Departure
Carter and Powell locate a gold-bearing quartz vein in late winter 1865. Powell leaves to purchase machinery; Carter guards the claim.

### The Chase
Carter sees Powell's trail vanish. He investigates, finding tracks of unshod ponies galloping away. He chases them through the valley and up the mountainside.

### Discovery and Escape
Carter finds Powell dead in an Apache camp surrounded by tepees. He charges into the camp, shooting at warriors who flee. He retrieves Powell's body and escapes pursuit by taking a wrong trail into a cave.

### The Cave
Carter enters a large cave chamber (approx 100 feet diameter). He lays Powell down, confirms death, then collapses from exhaustion on the floor.

## Visual Continuity

- **Landscape:** Arizona hills, clear mornings, valley views, moonlight illumination.
- **Camp:** White with Indian tepees, half a thousand warriors clustered around center object.
- **Cave:** Large chamber, smooth and well-worn floor, back lost in dense shadow, four feet high opening.
- **Lighting:** Moonlight (clear rays), daylight without warning at cave entrance.

## Uncertainties & Notes

- Narrator's exact age is unknown ("possibly a hundred").
- Cave has openings into other apartments (visibility unclear).
- Exact location of trail to pass vs. defile is ambiguous to narrator.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter I: On The Arizona Hills

## Characters Identified

| Asset ID | Canonical ID | Role | Physical Presence | Description Status |
|----------|--------------|------|-------------------|-------------------|
| narrator | narrator | Narrator/Chronicle Writer | Referenced | Manual description required |
| carter | carter | Claim Guardian | Physically Present | Manual description required |
| powell | powell | Machinery Purchaser | Deceased/Referenced | Manual description required |

## Notes

- All characters lack physical descriptions in source material
- Narrator's age uncertain ("possibly a hundred")
- Carter and Powell roles clearly defined but appearance unknown
- No visual continuity data available for any character

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical or visual description provided in source material. Only described as "old man who does not age" with uncertain age ("possibly a hundred").
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator - Chapter I

## Display Name
Narrator

## Chapter Role
Chronicle Writer / First-Person Observer

## Physical Presence
Referenced (narrative voice throughout chapter)

## Physical Description
**Supported by Source:** None. Only described as "old man who does not age" with uncertain age ("possibly a hundred").

**Uncertainty Notes:** 
- No physical features documented (height, build, hair, eyes, etc.)
- No costume or silhouette information available
- No facial expression or mannerism details provided
- Age remains ambiguous despite "old man" designation

## Continuity-Critical Traits
- Narrates entire chronicle from first-person perspective
- Claims to have died twice before current existence
- Intends to write life and death chronicle

## Render-Facing Prompt Noun Phrases
- elderly male narrator
- aged figure without aging
- chronicler of life and death
- uncertain age possibly hundred years old

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical or visual description provided in source material. Only identified by name and role as claim guardian/chaser.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Carter - Chapter I

## Display Name
Carter

## Chapter Role
Claim Guardian / Pursuer

## Physical Presence
Physically Present (active throughout chapter)

## Physical Description
**Supported by Source:** None. Only identified by name and role as claim guardian who chases Powell's trail.

**Uncertainty Notes:** 
- No physical features documented (height, build, hair, eyes, etc.)
- No costume or silhouette information available
- No facial expression or mannerism details provided
- No distinguishing marks or accessories mentioned

## Continuity-Critical Traits
- Guards gold-bearing quartz vein claim
- Locates Powell's trail vanishing
- Investigates and chases through valley to mountainside
- Finds Powell dead in Apache camp
- Charges into camp shooting at warriors
- Retrieves Powell's body
- Escapes by taking wrong trail into cave

## Render-Facing Prompt Noun Phrases
- male claim guardian
- gold vein protector
- mountain pursuer
- Apache camp survivor
- exhausted cave dweller

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: powell
canonical_character_id: powell
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical or visual description provided in source material. Only identified by name and role as machinery purchaser who is found dead.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Powell - Chapter I

## Display Name
Powell

## Chapter Role
Machinery Purchaser / Deceased Companion

## Physical Presence
Deceased/Referenced (found dead in Apache camp)

## Physical Description
**Supported by Source:** None. Only identified by name and role as machinery purchaser who leaves to buy equipment.

**Uncertainty Notes:** 
- No physical features documented (height, build, hair, eyes, etc.)
- No costume or silhouette information available
- No facial expression or mannerism details provided
- Cause of death not specified in source material

## Continuity-Critical Traits
- Purchases machinery for claim operations
- Leaves Carter to buy equipment
- Trail vanishes from valley floor
- Found dead surrounded by Apache camp and tepees
- Body retrieved by Carter after camp charge
- Death occurs before Carter's cave discovery

## Render-Facing Prompt Noun Phrases
- deceased male companion
- machinery purchaser
- gold claim associate
- Apache camp victim
- body in cave chamber

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
