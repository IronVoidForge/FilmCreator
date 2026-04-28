# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:10:10.135243+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Copy every FILMCREATOR structural tag literally.
Do not rename, translate, partially rewrite, or decorate any PACKET, RECORD, or SECTION tag.
The only valid closing tags are [[/FILMCREATOR_PACKET]], [[/FILMCREATOR_RECORD]], and [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

Chapter id: CH007

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question, character_type_hint, morphology_hint, scale_hint, renderability_hint, confidence, direct_identity_evidence, direct_visual_evidence, costume_or_covering_evidence, movement_evidence, associated_entities, alias_or_role_evidence, unknowns, source_refs sections=markdown



Literal tag rules:

- begin with [[FILMCREATOR_PACKET]] on its own line

- end with [[/FILMCREATOR_PACKET]] on its own line

- wrap each character item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]

- use [[SECTION character_index_markdown]] and [[SECTION markdown]] exactly as written

- do not invent alternate closing tags such as [[/FIL_RECORD]], [[end_section]], or misspelled FILMCREATOR tags

- do not echo this instruction block back as an example packet; return the actual packet only



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- emit one explicit character record per meaningful character mention

- every character record must have a FILMCREATOR_RECORD wrapper with type character

- every character record must include a non-empty markdown section

- if details are sparse, still write a short markdown file explaining the uncertainty instead of omitting markdown

- never omit the markdown section for any character record



Entity taxonomy rules:

- identify what the entity itself appears to be, not what it wears or rides

- do not confuse nearby/associated things with the entity

- if source says a person rides a mount, classify the person separately from the mount

- if source says a character wears foreign/alien/exotic clothing, do not change their species/type

- character_type_hint: human, humanoid_nonhuman, animal, creature, group, object, machine, abstract, unknown

- morphology_hint: biped, quadruped, multi_legged, serpentine, winged, constructed, amorphous, unknown

- scale_hint: tiny, small, human_scale, large, giant, unknown

- renderability_hint: renderable, context_only, alias_or_role, unknown

- confidence: 0.0 to 1.0 for each type/morphology/renderability hint

- if uncertain, use unknown and explain the missing evidence in the markdown section



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

**Setting:**
*   A large table set out under a tree in front of a house. 
*   The table is crowded with tea-things (tea, bread-and-butter, milk-jug).
*   Later: A wooded area containing a tree with a door built into it.
*   Final Location: The long hall with the little glass table, leading to the garden via a small door.

**Characters:**
*   **Alice:** Observant, easily frustrated by nonsense, attempts to maintain politeness and logic.
*   **The Hatter:** Eccentric, irritable, obsessed with time/clocks, prone to riddles without answers.
*   **The March Hare:** Erratic, defensive, participates in the nonsensical social cues of the party.
*   **The Dormouse:** Constantly sleeping or semi-conscious; provides interrupted, surreal storytelling.

**Key Events & Scene Beats:**
*   **Arrival at the Tea Party:** Alice approaches a large table under a tree where the March Hare, Hatter, and a sleeping Dormouse are crowded into one corner. They shout "No room!" despite there being plenty of space. Alice sits in a large armchair at the end of the table.
*   **The Failed Social Exchange:** The March Hare offers wine that isn't there; Alice calls him uncivil; the Hare retorts about her sitting without an invitation.
*   **The Riddle:** The Hatter makes a personal remark about Alice's hair and poses the riddle: "Why is a raven like a writing-desk?" He admits he doesn't know the answer.
*   **The Broken Watch:** The Hatter checks his watch, which shows the day of the month but not the time. He shakes it and holds it to his ear. He blames "butter" for the watch being two days wrong. The March Hare dips the watch into a cup of tea.
*   **The Personification of Time:** The Hatter explains that Time is a person ("him") with whom he quarreled last March at the Queen of Hearts' concert. Because of this quarrel, Time refuses to do anything for him, and it is perpetually six o'clock (tea-time).
*   **The Dormouse's Story:** After being pinched awake by the Hatter and Hare, the Dormouse tells a story about three sisters (Elsie, Lacie, and Tillie) who lived at the bottom of a treacle-well. Alice interrupts with logical questions about eating treacle and drawing from a well.
*   **The Seat Rotation:** To get a "clean cup," the Hatter initiates a move: The Hatter moves, the Dormouse follows him, the March Hare moves to the Dormouse's spot, and Alice reluctantly moves to the March Hare's spot (where she encounters spilled milk).
*   **Alice's Departure:** After being told "Then you shouldn't talk" by the Hatter, Alice leaves in disgust. She looks back once to see them trying to stuff the Dormouse into a teapot.
*   **The Tree Door:** Walking through the woods, Alice finds a door built into a tree. 
*   **Return to the Garden:** Alice enters the door, finds herself in the long hall, uses the golden key on the garden door, and nibbles the mushroom piece from her pocket to shrink to one foot tall. She successfully enters the beautiful garden.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index: Chapter 007

- [Alice](#alice)
- [The Hatter](#the-hatter)
- [The March Hare](#the-march-hare)
- [The Dormouse](#the-dormouse)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Explicitly named as Alice throughout the text."
direct_visual_evidence: "Mentioned in relation to her hair and her physical actions (sitting, moving, shrinking)."
costume_or_covering_evidence: ""
movement_evidence: "Walks through woods, enters a door, sits in an armchair, nibbles a mushroom to shrink."
associated_entities: ["the-hatter", "the-march-hare", "the-dormouse"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Alice
**Role:** Protagonist / Observer

**Status:** Physically Present

**Physical Description:**
Alice is a young girl. While specific facial features are not detailed in this chapter, the Hatter makes a personal remark regarding her hair. She undergoes a significant scale change at the end of the chapter, shrinking to one foot tall after eating a piece of mushroom.

**Costume & Silhouette:**
No specific costume details are provided in this chapter beyond her presence as a human girl.

**Descriptive Noun Phrases:**
- Young girl
- Observant child
- Shrinking girl (one foot tall)

**Uncertainty Notes:**
Specific hair color or clothing style is not explicitly described in this text, though the Hatter's comment implies it is a notable feature.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_hatter
canonical_character_id: the_hatter
aliases: ["Hatter"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as 'The Hatter'."
direct_visual_evidence: "Engages in social interaction, checks a watch, shakes a watch, moves seats."
costume_or_covering_evidence: ""
movement_evidence: "Moves around the tea table; shakes his watch and holds it to his ear."
associated_entities: ["alice", "the-march-hare", "the-dormouse"]
alias_or_role_evidence: "The Hatter"
unknowns: []
source_refs: []
[[SECTION markdown]]
# The Hatter
**Role:** Eccentric Host / Riddler

**Status:** Physically Present

**Physical Description:**
An eccentric figure. He possesses a watch that shows the day of the month but not the time. He is capable of interacting with tea-things and moving around a crowded table.

**Costume & Silhouette:**
The text does not provide specific details on his clothing, though his title implies he wears headwear associated with a hatter.

**Descriptive Noun Phrases:**
- Eccentric man
- Riddling host
- Irritable tea-party guest

**Uncertainty Notes:**
Specific visual appearance (face, clothes) is not detailed in this chapter; relies on the archetype of a "Hatter."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_march_hare
canonical_character_id: the_march_hare
aliases: ["March Hare"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as 'The March Hare'."
direct_visual_evidence: "Offers wine, dips a watch into tea, moves seats."
costume_or_covering_evidence: ""
movement_evidence: "Participates in the seat rotation at the table."
associated_entities: ["alice", "the-hatter", "the-dormouse"]
alias_or_role_evidence: "The March Hare"
unknowns: []
source_refs: []
[[SECTION markdown]]
# The March Hare
**Role:** Erratic Tea-Party Guest

**Status:** Physically Present

**Physical Description:**
An erratic animal (hare) participating in a tea party. 

**Costume & Silhouette:**
No specific clothing is mentioned for the hare.

**Descriptive Noun Phrases:**
- Erratic hare
- Defensive guest
- Tea-drinking animal

**Uncertainty Notes:**
Visual specifics of the hare's appearance (fur color, etc.) are not provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_dormouse
canonical_character_id: the_dormouse
aliases: ["Dormouse"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: unknown
scale_hint: tiny
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Identified as 'The Dormouse'."
direct_visual_evidence: "Sleeping, being pinched awake, telling a story, being stuffed into a teapot."
costume_or_covering_evidence: ""
movement_evidence: "Constantly sleeping; follows the Hatter during seat rotation; is stuffed into a teapot."
associated_entities: ["alice", "the-hatter", "the-march-hare"]
alias_or_role_evidence: "The Dormouse"
unknowns: []
source_refs: []
[[SECTION markdown]]
# The Dormouse
**Role:** Sleeping Storyteller

**Status:** Physically Present

**Physical Description:**
A small, sleepy creature. 

**Costume & Silhouette:**
No specific clothing is mentioned.

**Descriptive Noun Phrases:**
- Sleepy dormouse
- Semi-conscious storyteller
- Teapot-dwelling creature (at the end of the chapter)

**Uncertainty Notes:**
The exact morphology (whether it is a humanoid animal or a standard small rodent) is not explicitly detailed, though "Dormouse" implies a small rodent. It is small enough to be stuffed into a teapot.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
