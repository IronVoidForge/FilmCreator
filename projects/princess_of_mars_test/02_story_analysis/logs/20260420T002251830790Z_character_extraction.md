# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:22:51.830790+00:00
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

Chapter id: CH004

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

**Story Flow:**
1. **Arrival:** Ground rises to mountains; party enters city via ruined road. Buildings appear ancient but not decayed.
2. **Observation:** Martians camped in plaza (900+). Appearance noted: naked except ornaments, women have larger tusks, children light colored. Life cycle details provided (death by violence vs sickness).
3. **Introduction:** Tars Tarkas (vice-chieftain) leads party to Chieftain's edifice. Ceremony involves name exchange between Martians.
4. **Conflict:** Martians surround narrator, demand performance ("sak"). Narrator struggles with walking/jumping.
5. **Fight:** Narrator punches a laughing Martian who bullied him. Crowd approves (applause).
6. **Performance:** Narrator performs "sakk" jump successfully.
7. **Resolution:** Narrator demands food/water. Sola (8ft female) takes him to quarters.
8. **Ending:** Ten-legged creature waddles into the room.

**Visual Continuity:**
- **Martians:** Naked except ornaments; women have larger tusks; adults 10-12ft tall.
- **Furniture:** Human-sized desks/chairs (too small for Martians).
- **Architecture:** White marble, gold inlay, broad steps.
- **Creature:** Ten short legs, frog-like head, three rows of sharp tusks.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH004

| Character Name | Role | Physical Presence | Description Status |
|----------------|------|-------------------|-------------------|
| Tars Tarkas | Vice-Chieftain of Martians | Present | Fully Identified |
| Chieftain | Leader of Martians | Referenced | Not Fully Identified |
| Narrator | Human Visitor | Present | Not Fully Identified |
| Sola | 8ft Female Martian | Present | Fully Identified |
| Ten-Legged Creature | Unnamed Entity | Present | Not Fully Identified |

**Notes:**
- All Martians described as naked except ornaments per visual continuity
- Narrator appears human based on physical struggles and demands
- Chieftain lacks stable identification beyond title
- Ten-legged creature has detailed description but no name
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars-tarkas
canonical_character_id: Tars-Tarkas
aliases: Vice-Chieftain
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas

**Display Name:** Tars Tarkas  
**Chapter Role:** Vice-Chieftain of Martians  
**Physical Presence:** Present - leads party to Chieftain's edifice  
**Physical Description:** Martian (naked except ornaments, 10-12ft tall per visual continuity)  
**Costume/Silhouette:** Ornamented naked form, broad steps architecture context  
**Continuity-Critical Traits:** Vice-chieftain status, leads ceremony with name exchange  
**Uncertainty Notes:** None - fully identified by name and role

**Render-Facing Prompt Elements:**
- Martian physical form
- Ornamentation details
- 10-12ft tall stature
- White marble/gold inlay environment context
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: chieftain
canonical_character_id: Chieftain
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided beyond title; lacks stable identification for image generation
clarification_required: true
clarification_reason: Character may exist under different name or be too weakly identified; needs clarification on identity
clarification_question: Is the Chieftain a separate character from Tars Tarkas, and what is their physical description?

[[SECTION markdown]]
# Chieftain

**Display Name:** Chieftain  
**Chapter Role:** Leader of Martians  
**Physical Presence:** Referenced - party enters Chieftain's edifice  
**Physical Description:** Unknown - no specific details provided in source material  
**Costume/Silhouette:** Undetermined - lacks physical description  
**Continuity-Critical Traits:** Highest authority among Martians, receives name exchange ceremony  
**Uncertainty Notes:** Not fully identified by name; lacks physical description for image generation; may be same as Tars Tarkas or separate entity

**Render-Facing Prompt Elements:**
- Martian form (if applicable)
- Ornamentation details (if applicable)
- 10-12ft tall stature (if applicable)
- White marble/gold inlay environment context
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: Narrator
aliases: Human Visitor
is_fully_identified: false
manual_description_required: true
manual_description_reason: No specific physical description beyond human context; lacks stable identification for image generation
clarification_required: true
clarification_reason: Character may be human or Martian; needs clarification on species and physical details
clarification_question: Is the narrator a human visitor, and what are their specific physical characteristics?

[[SECTION markdown]]
# Narrator

**Display Name:** Narrator  
**Chapter Role:** Human Visitor to Martian City  
**Physical Presence:** Present - struggles with walking/jumping, performs sakk jump  
**Physical Description:** Human (based on context of physical struggles and demands for food/water)  
**Costume/Silhouette:** Undetermined - lacks specific costume details  
**Continuity-Critical Traits:** Performs "sakk" jump successfully, punches bullying Martian, demands food/water  
**Uncertainty Notes:** Not fully identified by name; lacks specific physical description beyond human context; needs clarification for image generation

**Render-Facing Prompt Elements:**
- Human form
- Physical struggles (walking/jumping difficulties)
- Successful sakk jump performance
- Reaction to crowd approval (applause)
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 8ft Female Martian
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola

**Display Name:** Sola  
**Chapter Role:** 8ft Female Martian  
**Physical Presence:** Present - takes narrator to quarters  
**Physical Description:** Martian (naked except ornaments, 8ft tall female)  
**Costume/Silhouette:** Ornamented naked form, female physiology  
**Continuity-Critical Traits:** 8ft height specification, leads narrator to quarters after performance  
**Uncertainty Notes:** None - fully identified by name and role

**Render-Facing Prompt Elements:**
- Martian physical form
- Female anatomy
- 8ft tall stature
- Ornamentation details
- White marble/gold inlay environment context
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: ten-legged-creature
canonical_character_id: Ten-Legged-Creature
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No specific name provided; detailed description exists but lacks stable identification for image generation
clarification_required: true
clarification_reason: Creature may be new character or variant; needs clarification on identity and species
clarification_question: Is the ten-legged creature a new character type, and what is its full species classification?

[[SECTION markdown]]
# Ten-Legged Creature

**Display Name:** Ten-Legged Creature  
**Chapter Role:** Unnamed Entity in Narrator's Room  
**Physical Presence:** Present - waddles into room at ending  
**Physical Description:** Ten short legs, frog-like head, three rows of sharp tusks (per visual continuity)  
**Costume/Silhouette:** Undetermined - lacks specific costume details  
**Continuity-Critical Traits:** Waddling movement, ten short legs, frog-like head, three rows of sharp tusks  
**Uncertainty Notes:** Not fully identified by name; has detailed description but needs clarification for image generation; may be new character type

**Render-Facing Prompt Elements:**
- Ten short legs
- Frog-like head shape
- Three rows of sharp tusks
- Waddling movement style
- Room environment context
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
