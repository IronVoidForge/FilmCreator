# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:14:41.482281+00:00
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

Chapter id: CH006

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

**Story Summary:**
The narrator is captured by a large bull ape warrior who intends to kill him with a cudgel. His beast attacks the executioner, leading to a fierce battle between the beast and the ape's mate. The narrator intervenes with a cudgel, killing the mate. The bull ape returns enraged, but Tars Tarkas and warriors arrive. The narrator fights and defeats the bull ape alone. Upon seeing his beast threatened by a warrior with a pistol, the narrator defends it, shooting the window to save it. Sola examines him for wounds. The narrator gains further respect and friendship from the Martians, specifically noted by Sola's care and the warriors' applause.

**Visual Continuity:**
- Bull Ape: Ten or fifteen feet tall, four great arms, laterally located ears, snouts like African gorilla.
- Beast: Four great arms, paws transcending Martian men's muscles, eyes bulging from sockets during fight.
- Setting: Interior of building, doorway, window, plaza.
- Objects: Cudgel (stone), pistol (wooden casing of window).
- Martians: Worship physical prowess and bravery; devoid of finer sentiments like friendship or affection in this context.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH006

| Asset ID | Canonical Character ID | Display Name | Chapter Role | Physical Presence | Description Status |
|----------|------------------------|--------------|---------------|-------------------|--------------------|
| narrator_main | narrator_main | The Narrator | Protagonist, captured by bull ape | Referenced throughout chapter | Manual description required |
| bull_ape_warrior | bull_ape_warrior | Bull Ape Warrior | Antagonist, large ape creature | Present in battle scenes | Partial physical description |
| sola | sola | Sola | Caretaker, examines narrator for wounds | Referenced in final scenes | Manual description required |
| tars_tarkas | tars_tarkas | Tars Tarkas | Arriving warrior leader | Mentioned as arriving with warriors | No physical description provided |

*Note: All characters lack sufficient visual continuity details for dependable image generation.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_main
canonical_character_id: narrator_main
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary or visual continuity notes. Cannot determine facial features, body type, hair, skin tone, or other appearance details needed for image generation.
clarification_required: false
clarification_reason: Character is clearly the main protagonist with no indication of existing under another name.
clarification_question: 

[[SECTION markdown]]
# The Narrator - CH006

## Display Name
The Narrator

## Chapter Role
Protagonist, captured by bull ape warrior who intends to kill him with cudgel

## Physical Presence Status
Referenced throughout chapter; physically present in battle scenes and final confrontation

## Physical Description
**Uncertain:** No physical description provided in source material. Cannot determine:
- Facial features or expression
- Body build or height
- Hair style or color
- Skin tone
- Eye appearance
- Clothing or attire

## Costume & Silhouette
**Unknown:** No costume details available from chapter summary or visual continuity notes.

## Continuity-Critical Traits
- Intervenes with cudgel to kill bull ape's mate
- Defends beast when threatened by warrior with pistol
- Receives care and examination from Sola after battle
- Gains respect and friendship from Martians through physical prowess display

## Render-Facing Prompt Notes
```
[Uncertainty: Physical description missing - requires manual description before image generation]
Key actions: cudgel wielder, beast defender, Martian respected fighter
```
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bull_ape_warrior
canonical_character_id: bull_ape_warrior
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: While some physical traits are described (ten or fifteen feet tall, four arms, African gorilla snout), these are creature-type descriptions rather than character-specific details. Cannot determine facial expression, individual markings, or other appearance nuances needed for dependable image generation.
clarification_required: false
clarification_reason: Character is clearly a bull ape antagonist with no indication of existing under another name.
clarification_question: 

[[SECTION markdown]]
# Bull Ape Warrior - CH006

## Display Name
Bull Ape Warrior

## Chapter Role
Antagonist, large ape creature who captures and threatens narrator

## Physical Presence Status
Present in battle scenes; physically attacks executioner with cudgel

## Physical Description
**Partially Supported:**
- Height: Ten or fifteen feet tall
- Limbs: Four great arms (laterally located ears)
- Snout: Like African gorilla
- Eyes: Bulging from sockets during fight

**Uncertain:** Cannot determine:
- Facial expression or emotion
- Individual markings or scars
- Fur texture or color variations
- Specific posture or stance details

## Costume & Silhouette
**Unknown:** No costume details available; appears as natural creature form.

## Continuity-Critical Traits
- Attacks executioner with cudgel (stone)
- Mate killed by narrator's intervention
- Returns enraged after mate's death
- Defeated alone by narrator in final battle
- Threatens beast with pistol, requiring narrator to defend it

## Render-Facing Prompt Notes
```
[Uncertainty: Creature-type description lacks character-specific details]
Key actions: cudgel wielder, ape antagonist, enraged fighter
Physical traits: four arms, gorilla snout, large stature
```
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary or visual continuity notes. Cannot determine facial features, body type, hair, skin tone, or other appearance details needed for image generation.
clarification_required: false
clarification_reason: Character is clearly a Martian caretaker with no indication of existing under another name.
clarification_question: 

[[SECTION markdown]]
# Sola - CH006

## Display Name
Sola

## Chapter Role
Caretaker, examines narrator for wounds after battle

## Physical Presence Status
Referenced in final scenes; physically examines narrator

## Physical Description
**Uncertain:** No physical description provided in source material. Cannot determine:
- Facial features or expression
- Body build or height
- Hair style or color
- Skin tone
- Eye appearance
- Clothing or attire

## Costume & Silhouette
**Unknown:** No costume details available from chapter summary or visual continuity notes.

## Continuity-Critical Traits
- Examines narrator for wounds after battle
- Shows care and concern for narrator's physical state
- Represents Martian respect and friendship through actions
- Receives applause from warriors alongside her care

## Render-Facing Prompt Notes
```
[Uncertainty: Physical description missing - requires manual description before image generation]
Key actions: wound examiner, caretaker figure, Martian respected individual
```
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary or visual continuity notes. Cannot determine facial features, body type, hair, skin tone, or other appearance details needed for image generation.
clarification_required: false
clarification_reason: Character is mentioned as arriving warrior leader with no indication of existing under another name.
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas - CH006

## Display Name
Tars Tarkas

## Chapter Role
Arriving warrior leader, brings warriors to scene

## Physical Presence Status
Mentioned as arriving with warriors; not physically detailed in chapter

## Physical Description
**Uncertain:** No physical description provided in source material. Cannot determine:
- Facial features or expression
- Body build or height
- Hair style or color
- Skin tone
- Eye appearance
- Clothing or attire

## Costume & Silhouette
**Unknown:** No costume details available from chapter summary or visual continuity notes.

## Continuity-Critical Traits
- Arrives with warriors after narrator defeats bull ape
- Represents Martian warrior presence and support
- Part of group that arrives to scene (no individual physical description provided)

## Render-Facing Prompt Notes
```
[Uncertainty: Physical description missing - requires manual description before image generation]
Key actions: arriving leader, warrior figure, Martian respected individual
```
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
