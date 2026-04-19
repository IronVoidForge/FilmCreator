# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:07:19.826911+00:00
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

Chapter id: CH007

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

# Chapter VII Summary: Child-Raising on Mars

## Opening Scene Sequence
- Location: City plaza after breakfast (exact replica of preceding day's meal)
- Visual: Sola escorts narrator to plaza where entire community watches harnessing of 250 three-wheeled chariots
- Each chariot drawn by single mastodonian animal, gorgeously decorated with metal ornaments, jewels, silks, furs
- Female Martians seated in chariots loaded with ornaments; young Martian drivers perched on beasts
- Warriors at head (five abreast) and rear of caravan; outriders flank sides

## Procession to Incubator
- Formation: Single file line of march
- Warrior count: ~200 at head, 200 at rear, 25-30 outriders on each side
- All but narrator heavily armed
- Draft animals guided entirely by telepathic means (no bit or bridle)
- Narrator dragged into empty chariot with Sola

## Incubator Ceremony - Key Visual Sequences
1. Arrival at incubator: Chariots parked with military precision on four sides of enclosure
2. Dismounting warriors: Half a score led by enormous chieftain Lorquas Ptomel, Jed; includes Tars Tarkas and lesser chiefs
3. Narrator's performance: Leaps entirely over parked chariots for edification of Lorquas Ptomel
4. Incubator contents: All but very few eggs hatched; hideous little devils 3-4 feet tall moving restlessly
5. Opening creation: Warriors break opening in wall large enough for exit

## Release Ceremony Visual Flow
- Formation: Women and younger Martians form two solid walls leading through chariots into plain
- Action: Little Martians scamper wild as deer, captured one at a time by women/older children
- Last in line captures first to reach end; opposite captures second, continuing until all leave enclosure
- Women who catch young fall out of line and return to respective chariots
- Young men's captives later turned over to some women

## Post-Ceremony Scene
- Sola found in narrator's chariot with hideous little creature held tightly in arms
- Narrator advances to incubator side under Tars Tarkas command (mastered walking under Martian conditions)
- Tars Tarkas points over incubator, says "Sak" - wants narrator to repeat performance

## Educational System Revealed
- Work of rearing: Teaching to talk and use weapons from first year of life
- Incubation period: Five years in subterranean vaults where temperature too low for incubation
- Birth rate: Each adult female brings forth about thirteen eggs each year
- Selection process: Council of twenty chieftains examines yearly supply; all but ~100 most perfect destroyed
- Final selection: About five hundred almost perfect eggs chosen from thousands after five years
- Hatching event: All but about one per cent hatching in two days

## Community Details
- Population: Approximately thirty thousand souls
- Territory: Arid and semi-arid land between forty and eighty degrees south latitude
- Headquarters: Southwest corner near crossing of two Martian canals
- Incubator location: Remote fastnesses, little likelihood of discovery by other tribes
- Journey ahead: Tremendous journey from dead city to incubator (narrator knew nothing)

## Character Development Notes
- Sola's duties doubled: Care for young Martian and narrator
- Both equally advanced in Martian education
- Narrator develops telepathic powers so he can sense practically everything around him
- Martian language extremely simple; week to make all wants known and understand nearly everything said
- Unique ability: Can catch telepathic messages from others but no one can read from his mind

## Setting Transitions
- Route: Out across little valley before city, through hills, down into dead sea bottom
- Incubator as terminal point of journey this day
- After return to dead city: Several days in comparative idleness
- Next day: All warriors ride forth early morning, don't return until just before darkness fell
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter VII

| Character | Role | Status |
|-----------|------|--------|
| Sola | Female Martian escort/caretaker | Identified |
| Narrator | Main protagonist | Identified |
| Lorquas Ptomel | Enormous chieftain | Identified |
| Jed | Title/alternate designation | Uncertain |
| Tars Tarkas | Warrior commander | Identified |

*Note: Lesser chiefs mentioned but not individually identified.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Limited physical description provided - only gender (female), race (Martian), and role (escorts narrator) are known. No facial features, height, build, or distinguishing marks documented in source material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola

## Display Name
Sola

## Chapter Role
Female Martian escort and caretaker for narrator and young creature

## Physical Presence
Referenced throughout chapter; found in narrator's chariot with hideous little creature at end of ceremony

## Physical Description (Supported by Source)
- Female Martian
- Both equally advanced in Martian education as narrator
- Duties doubled: care for young Martian and narrator

## Costume/Silhouette/Continuity Traits
- Seated in chariots during procession
- Found holding young creature tightly in arms at chapter end
- No specific costume details provided in source material

## Render-Facing Prompt Notes
"Female Martian character, advanced education level, caretaker role, found with young creature, no detailed physical features documented"

## Uncertainty Notes
Physical appearance beyond gender and race is not described in source. Facial features, height, build, or distinguishing marks are unknown. Costume details are sparse.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: Narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in source material. Character is only identified by role (narrator/main protagonist) and actions taken during chapter events.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator

## Display Name
Narrator (unnamed protagonist)

## Chapter Role
Main character being dragged through harnessing ceremony and incubator events

## Physical Presence
Physically present throughout chapter; dragged into empty chariot with Sola, advances to incubator side under Tars Tarkas command

## Physical Description (Supported by Source)
- No physical description provided in source material
- Both equally advanced in Martian education as narrator
- Developed telepathic powers so he can sense practically everything around him

## Costume/Silhouette/Continuity Traits
- Dragged into empty chariot with Sola
- Leaps over parked chariots for edification of Lorquas Ptomel
- Advances to incubator side under Tars Tarkas command
- Mastered walking under Martian conditions

## Render-Facing Prompt Notes
"Unnamed protagonist character, advanced education level, telepathic abilities, no physical features documented in source"

## Uncertainty Notes
Physical appearance is completely unknown - no facial features, height, build, or distinguishing marks provided. Costume details are sparse beyond being dragged through chariot and advancing to incubator.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: Lorquas Ptomel
aliases: Jed
is_fully_identified: true
manual_description_required: true
manual_description_reason: Limited physical description provided - only described as "enormous chieftain" with no specific facial features, height, build, or distinguishing marks documented.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel

## Display Name
Lorquas Ptomel (also referred to as Jed)

## Chapter Role
Enormous chieftain leading warriors during procession and ceremony

## Physical Presence
Referenced throughout chapter; half a score led by enormous chieftain Lorquas Ptomel, Jed at incubator arrival

## Physical Description (Supported by Source)
- Enormous chieftain
- Leads warriors with half a score
- Receives narrator's leap performance for edification

## Costume/Silhouette/Continuity Traits
- Leads warriors during procession
- Present at incubator ceremony
- No specific costume details provided in source material

## Render-Facing Prompt Notes
"Enormous chieftain character, leadership role, no detailed physical features documented beyond size description"

## Uncertainty Notes
Physical appearance beyond being "enormous" is not described. Facial features, height specifics, build, or distinguishing marks are unknown. Costume details are sparse.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Limited physical description provided - only identified as warrior and commander with no specific facial features, height, build, or distinguishing marks documented.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas

## Display Name
Tars Tarkas

## Chapter Role
Warrior commander directing narrator's movements at incubator

## Physical Presence
Referenced throughout chapter; points over incubator, commands narrator to advance, wants narrator to repeat performance

## Physical Description (Supported by Source)
- Warrior
- Commander/mastered walking under Martian conditions
- Points over incubator, says "Sak" - wants narrator to repeat performance

## Costume/Silhouette/Continuity Traits
- Warriors at head and rear of caravan
- All but narrator heavily armed
- Commands narrator's movements at incubator ceremony

## Render-Facing Prompt Notes
"Warrior commander character, leadership role, no detailed physical features documented beyond warrior status"

## Uncertainty Notes
Physical appearance is not described in source material. Facial features, height, build, or distinguishing marks are unknown. Costume details are sparse beyond being heavily armed warrior.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_PACKET]]
````
