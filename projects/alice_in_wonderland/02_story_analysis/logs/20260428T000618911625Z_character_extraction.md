# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:06:18.911625+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

Chapter id: CH010

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question, character_type_hint, morphology_hint, scale_hint, renderability_hint, confidence, direct_identity_evidence, direct_visual_evidence, costume_or_covering_evidence, movement_evidence, associated_entities, alias_or_role_evidence, unknowns, source_refs sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the protagonist's physical form and origin?

character_type_hint: unknown

morphology_hint: unknown

scale_hint: unknown

renderability_hint: unknown

confidence: 0.3



[[SECTION markdown]]

# Protagonist

Short, grounded character markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



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

**Setting:** A seaside-adjacent environment where the Mock Turtle and Gryphon reside.

**Characters:**
* **Alice:** A young girl, currently feeling a mix of curiosity, confusion, and social pressure to conform to the creatures' logic.
* **The Mock Turtle:** An emotional, sobbing creature who sings melancholic songs about sea life.
* **The Gryphon:** An energetic, somewhat impatient creature who leads the group and explains things with authoritative nonsense.

**Key Events & Transitions:**
1.  **The Explanation of the Lobster Quadrille:** The Mock Turtle and Gryphon describe a complex dance involving lines of sea creatures and lobsters. They perform a "first figure" of the dance around Alice, stepping on her toes while the Mock Turtle sings a sad song about a whiting and a snail.
2.  **The Linguistic Puns:** A conversation ensues regarding the nature of "whiting" (the fish vs. shoe-making) and the pun on "porpoise/purpose." t
3.  **Alice’s Storytelling:** The Gryphon prompts Alice to tell her adventures. She recounts her journey from meeting the White Rabbit. The creatures listen with varying degrees of intensity, particularly when she mentions the Caterpillar.
4.  **The Repeating Lesson:** The Gryphon instructs Alice to repeat a poem ("'Tis the voice of the sluggard"). Due to her mind being on the dance, her version is a nonsensical variation involving lobsters and toes. This leads to a debate between the Mock Turtle and the Gryphon about the meaning of the verses.
5.  **The Second Song:** The Mock Turtle sings "Beautiful Soup" in a deep, sorrowful manner. 
6.  **The Sudden Exit:** A distant cry of "The trial's beginning!" interrupts the song. The Gryphon grabs Alice’s hand and leads her away in a hurried run, leaving the end of the song trailing behind them.

**Visual/Continuity Elements:**
* **Movement:** The Mock Turtle and Gryphon jump, caper, and dance around Alice.
* **Interaction:** The creatures physically crowd Alice (stepping on toes, being close to her face).
* **Soundscape:** Melancholic singing vs. the sudden, urgent call of the trial in the distance.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]
# Character Index
- [Alice](#alice)
- [The Mock Turtle](#the-mock-turtle)
- [The Gryphon](#the-gryphon)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH010 Alice
aliases: Alice
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: The Mock Turtle, The Gryphon
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Description:** A young girl experiencing a mix of curiosity and social pressure. She is physically interacted with by the creatures, specifically having her toes stepped on during their dance. 

**Visual Cues:** Small scale relative to the environment/creatures; human form.

**Uncertainty Notes:** Specific clothing details are not provided in this chapter text, though she is a young girl.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mock_turtle
canonical_character_id: CH010 Mock Turtle
aliases: The Mock Turtle
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: creature
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: Alice, The Gryphon
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Mock Turtle
**Role:** Melancholic Singer / Dancer

**Status:** Physically Present

**Description:** An emotional creature prone to sobbing and singing melancholic songs about sea life. The creature participates in the Lobster Quadrille, jumping and capcut around Alice.

**Visual Cues:** A sea-themed creature; likely has features evocative of a turtle but with fantastical elements. 

**Uncertainty Notes:** Specific anatomical fusion (shell vs. sea creature) is not explicitly detailed beyond the name.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: gryphon
canonical_character_id: CH010 Gryphon
aliases: The Gryphon
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: creature
morphology_hint: winged
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: Alice, The Mock Turtle
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Gryphon
**Role:** Energetic Leader / Instructor

**Status:** Physically Present

**Description:** An energetic and somewhat impatient creature. It leads the group, engages in the Lobster Quadrille, and instructs Alice on poetry. 

**Visual Cues:** A winged creature; authoritative presence.

**Unfocussed Details:** Specific physical morphology beyond being a gryphon is not detailed in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
