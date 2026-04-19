# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:53:56.415159+00:00
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

## Scene Breakdown (Story Summary)

### Scene 1: Journey to the City
*   **Action:** Narrator and guard travel ten miles; ground rises rapidly.
*   **Location:** Edge of dead sea, foot of mountains, narrow gorge, open valley, table land.
*   **Visual:** Enormous city beheld at far extremity of valley. Ruined roadway leads to edge of table land with broad steps.

### Scene 2: Observation of Martians in the City
*   **Action:** Narrator observes Martians camped on plaza and surrounding buildings (approx. 900-1000 creatures).
*   **Visual Details:** Naked except ornaments; women have larger tusks curving to ears, lighter bodies, rudimentary nails. Children look alike, light in color.
*   **Societal Info:** Life expectancy details (maturity ~40 years, voluntary pilgrimage at 1000 years). Death causes: sickness (rare), voluntary pilgrimage (~20%), violent death (duels, hunting, aviation, war).

### Scene 3: Arrival at the Chieftain's Building
*   **Action:** Party surrounded by hundreds of creatures; leader stilled clamor. Proceed to magnificent edifice (low, enormous area, white marble/gold/stones).
*   **Visual:** Main entrance 100 feet wide with huge canopy. No stairway, gentle incline to first floor. Chamber encircled by galleries, dotted with wooden desks/chairs sized for humans.
*   **Ceremony:** Martians assembled around rostrum (40-50 males). Chieftain squats on platform (enormous warrior loaded with ornaments/feathers/leather). Greeting ritual: Names exchanged (Tars Tarkas and Chieftain titles).

### Scene 4: Physical Limitations & Martial Interaction
*   **Action:** Narrator lowered to ground. Captor explains expedition/capture. Narrator replies in English to show lack of understanding; smiles slightly.
*   **Visual:** Martians examine narrator's muscles/skin texture. Furniture mismatch (Martians too large for desks/chairs).
*   **Conflict:** Narrator skips/flits like grasshopper, bruises self. Punches a towering fellow who laughed heartily; opponent falls like felled ox. Martians break into wild peals of laughter/applause.

### Scene 5: "Sak" Exhibition & Demands
*   **Action:** Chieftain orders narrator to perform "sak". Narrator jumps 150 feet successfully, lands squarely. Returns by easy jumps.
*   **Conflict:** Narrator hungry/thirsty; ignores commands, motions mouth/stomach. Tars Tarkas and chief exchange words.
*   **Action:** Narration accompanied young female (Sola) to sleeping quarters.

### Scene 6: Sleeping Quarters & New Creature
*   **Location:** Spacious chamber in building fronting plaza.
*   **Visual:** Well lighted by large windows; decorated with mural paintings and mosaics (touch of antiquity). Silks/furs on floor.
*   **Action:** Sola seated, makes hissing sound. New Martian wonder waddles in on ten short legs (size of Shetland pony, frog-like head, three rows of long sharp tusks).

## Visual Details (Continuity for Scene Decomposition)

### Architecture & Materials
*   **Primary Material:** Gleaming white marble inlaid with gold and brilliant stones.
*   **Structure:** Low buildings covering enormous areas; main entrance 100 feet wide with huge canopy above entrance hall.
*   **Interior:** Chamber encircled by galleries, dotted with highly carved wooden desks and chairs sized for humans (not Martians).
*   **Decoration:** Mural paintings and mosaics on sleeping quarters; silks and furs littering floors.

### Martian Appearance & Features
*   **General:** Naked except for ornaments; bodies smaller and lighter in color than males.
*   **Women:** Tusks much larger in proportion to height, curving nearly to high-set ears; rudiments of nails on fingers/toes.
*   **Height:** Adult females range from ten to twelve feet; young female (Sola) about eight feet tall.
*   **Children:** Light in color, even lighter than women; all look precisely alike.

### Creature Features
*   **Legs:** Ten short legs (waddling like an obedient puppy).
*   **Head:** Slight resemblance to frog head, except jaws equipped with three rows of long, sharp tusks.
*   **Size:** About the size of a Shetland pony.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1
[[SECTION character_index_markdown]]
# Character Index - Chapter 4 (CH004)

| Character | Role | Presence | Description Status |
| :--- | :--- | :--- | :--- |
| **Narrator** | Human Protagonist | Physically Present | Attire Uncertain |
| **Tars Tarkas** | Chieftain / Leader | Physically Present | Ornaments Vague |
| **Sola** | Young Female Martian | Physically Present | Ornaments Vague |
| **New Martian Creature** | Specimen / Wonder | Physically Present | Specific Features |
| **Guard** | Human Companion | Referenced Only | No Description |

[[/SECTION]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: human, prisoner, captor
is_fully_identified: true
manual_description_required: true
manual_description_reason: Attire and specific clothing state are not explicitly detailed in the text; skin texture is examined implying potential nudity or partial undressing.
clarification_required: false
clarification_reason: None.
clarification_question: Is the Narrator wearing clothes during the examination?
[[SECTION markdown]]
# Narrator (CH004)

**Role:** Protagonist / Human Captive
**Presence:** Physically Present

**Description:**
The Narrator is a human male lowered to the ground by Martians. He is examined for muscle and skin texture. He possesses the ability to skip/flit like a grasshopper, jump 150 feet, and perform "sak". He speaks English.

**Uncertainty:**
*   **Attire:** The text does not specify if the Narrator is clothed or unclothed during the examination, only that his skin texture is examined. This creates ambiguity for visual representation.
*   **Physical State:** While human features are implied, specific details of his current physical condition (e.g., injuries from jumping) are not detailed beyond "bruises self".

**Visual Notes:**
*   Human build.
*   Capable of high jumps and agility.
*   Skin texture examined by Martians.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: chieftain, leader, enormous warrior
is_fully_identified: true
manual_description_required: true
manual_description_reason: Specific ornament types and arrangement are not detailed; general description "loaded with ornaments/feathers/leather" is vague for image generation.
clarification_required: false
clarification_reason: None.
clarification_question: What specific ornaments does Tars Tarkas wear?
[[SECTION markdown]]
# Tars Tarkas (CH004)

**Role:** Chieftain / Leader
**Presence:** Physically Present

**Description:**
Tars Tarkas is the leader of the Martian party. He is an enormous warrior loaded with ornaments, feathers, and leather. He squats on a platform to still the clamor and orders the Narrator to perform "sak". He exchanges names with the Narrator (Tars Tarkas).

**Uncertainty:**
*   **Ornaments:** The text describes him as "loaded with ornaments/feathers/leather" but does not specify the types, colors, or arrangement of these items. This is insufficient for detailed visual generation.
*   **Height:** While implied to be large ("enormous"), specific height measurements are not provided for him individually (general Martian female height is given elsewhere).

**Visual Notes:**
*   Naked except ornaments.
*   Squatting posture on platform.
*   Enormous build compared to human furniture.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: young female, eight-foot female
is_fully_identified: true
manual_description_required: true
manual_description_reason: Specific ornament types and arrangement are not detailed; general description "Naked except ornaments" applies to all Martians but lacks specific detail for this individual.
clarification_required: false
clarification_reason: None.
clarification_question: What specific ornaments does Sola wear?
[[SECTION markdown]]
# Sola (CH004)

**Role:** Young Female Martian
**Presence:** Physically Present

**Description:**
Sola is a young female Martian accompanied by the Narrator to sleeping quarters. She is about eight feet tall. She makes a hissing sound while seated. She has tusks much larger in proportion to height, curving nearly to high-set ears, and rudiments of nails on fingers/toes.

**Uncertainty:**
*   **Ornaments:** Like other Martians, she is "Naked except ornaments," but the specific types or arrangement of these ornaments are not detailed in the text.
*   **Tusks:** While described as large and curving to ears, specific coloration or texture of tusks is not mentioned.

**Visual Notes:**
*   Naked except ornaments.
*   Tusks curve nearly to high-set ears.
*   Rudiments of nails on fingers/toes.
*   Height: Approximately eight feet.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: new_martian_creature
canonical_character_id: new_martian_creature
aliases: wonder, specimen
is_fully_identified: false
manual_description_required: false
manual_description_reason: N/A
clarification_required: true
clarification_reason: Character is unnamed and generic; may represent a class of creatures rather than a specific individual with a stable identity.
clarification_question: Does this creature have a specific name or designation beyond "New Martian Creature"?
[[SECTION markdown]]
# New Martian Creature (CH004)

**Role:** Specimen / Wonder
**Presence:** Physically Present

**Description:**
A new Martian creature waddles into the sleeping quarters. It is about the size of a Shetland pony with ten short legs (waddling like an obedient puppy). It has a frog-like head and three rows of long, sharp tusks.

**Uncertainty:**
*   **Identity:** The creature is unnamed and referred to only as "New Martian Creature" or "wonder". It may be a specimen rather than a named character.
*   **Behavior:** While it waddles in, its personality or specific role beyond being a curiosity is not detailed.

**Visual Notes:**
*   Size: About the size of a Shetland pony.
*   Legs: Ten short legs.
*   Head: Slight resemblance to frog head.
*   Tusks: Three rows of long, sharp tusks.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: guard
canonical_character_id: guard
aliases: human, companion
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in text; only referenced as traveling with the Narrator.
clarification_required: false
clarification_reason: None.
clarification_question: What does the Guard look like?
[[SECTION markdown]]
# Guard (CH004)

**Role:** Human Companion
**Presence:** Referenced Only

**Description:**
The Guard is mentioned in Scene 1 as traveling ten miles with the Narrator. He is part of the party that arrives at the city and is surrounded by Martians. No further physical details are provided in the text.

**Uncertainty:**
*   **Physical Description:** The text provides no visual or physical description for the Guard beyond his role as a companion to the Narrator. This makes him impossible to depict visually without external assumptions.
*   **Attire:** Clothing state is not mentioned.

**Visual Notes:**
*   Human build (implied).
*   Traveling companion to Narrator.
*   Part of the party surrounded by Martians.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
