# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:14:53.547187+00:00
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

Chapter id: CH010

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

**Setting:** An unspecified outdoor area near a seashore (implied by the discussion of the Lobster Quadrille).

**Characters:**
* **Alice:** A young girl, increasingly bewildered by the logic of her companions.
* **The Gryphon:** Energetic, impatient, and authoritative; acts as a guide/interlocutor.
* **The Mock Turtle:** Melancholic, prone to sobbing and singing; highly emotional.

**Events & Interactions:**
* **Emotional Beat:** The Mock Turtle sobs deeply; the Gryphon punches him in the back to help him recover his voice.
* **Dialogue/Exposition:** The Mock Turtle describes the "Lobster Quadrille" dance (lines of sea creatures, lobsters as partners, throwing lobsters into the sea, swimming after them, somersaults).
* **Performance (The Dance):** The Gryphon and Mock Turtle perform a mock version of the Lobster Quadrille around Alice. They tread on her toes. The Mock Turtle sings "Will you walk a little faster?" while dancing.
* **Dialogue/Exposition:** Discussion regarding "whiting" fish. The Mock Turtle claims they have tails in their mouths because they were thrown out to sea with lobsters. The Gryphon explains that "whiting" is used for polishing shoes and that soles are made of "soles and eels."
* **Wordplay:** A pun on "purpose" vs "porpoise" causes the Mock Turtle to take offense.
* **Narrative Shift (Alice's Story):** The Gryphon prompts Alice to tell her adventures. Alice describes her journey starting from seeing the White Rabbit. The Gryphon and Mock Turtle lean in close, opening their eyes/mouths wide to listen.
* **Performance (The Recitation):** The Gryphon commands Alice to repeat a poem ("'Tis the voice of the sluggard"). Due to her distraction, Alice recites a nonsensical version involving lobsters, sugar, and turning toes out with noses.
* **Conflict/Interruption:** The Mock Turtle demands explanations for the nonsense; the Gryphon impatiently tells Alice to continue to the next verse ("I passed by his garden..."). Alice stops when the Mock Turtle interrupts her again.
* **Performance (The Song):** At Alice's request, the Mock Turtle sings "Beautiful Soup" in a melancholy, sobbing tone. The Gryphon calls for a chorus.
* **Inciting Incident/Exit:** A distant cry of "The trial's beginning!" is heard. 
* **Action/Transition:** The Gryphon grabs Alice by the hand and hurries her away toward the sound. The Mock Turtle’s song fades into the distance as they run.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

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
scale_hint: small
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Alice is identified as a young girl."
direct_visual_evidence: "Identified as a young girl; participates in physical actions like being grabbed by the hand and having toes trodden on."
costume_or_covering_evidence: ""
movement_evidence: "Walks, stops reciting, is hurried away by the Gryphon."
associated_entities: ["the_gryphon", "the_mock_turtle"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Alice
**Role:** Protagonist / Listener

**Status:** Physically Present

**Physical Description:**
A young girl. Specific facial features or hair color are not detailed in this chapter, though she is small enough to have her toes trodden on by larger creatures.

**Costume & Silhouette:**
Not explicitly described in this chapter.

**Descriptive Noun Phrases:**
Young girl, bewildered child, listener.

**Uncertainty Notes:**
Visual details like hair color and specific clothing are absent from this text segment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_gryphon
canonical_character_id: gryphon
aliases: ["The Gryphon"]
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
direct_identity_evidence: "Identified as The Gryphon."
direct_visual_evidence: "Performs a dance, punches the Mock Turtle in the back, grabs Alice by the hand."
costume_or_covering_evidence: ""
movement_evidence: "Energetic movement, dancing (Lobster Quadrille), grabbing Alice's hand, hurrying away."
associated_entities: ["alice", "the_mock_turtle"]
alias_or_role_evidence: ""
unknowns: ["exact anatomical composition of the gryphon (wings/beak/body details)"]
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# The Gryphon
**Role:** Guide / Interlocutor

**Status:** Physically Present

**Physical Description:**
An energetic and authoritative creature. While the name implies a mythical hybrid, specific anatomical details (wings, beak, etc.) are not visually described in this chapter beyond its actions.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
Energetic creature, authoritative guide, dancing companion.

**Uncertainty Notes:**
The text relies on the reader's external knowledge of a "Gryphon." Specific visual traits (e.g., eagle head vs. lion body) are not provided in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_mock_turtle
canonical_character_id: mock_turtle
aliases: ["The Mock Turtle"]
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
confidence: 0.7
direct_identity_evidence: "Identified as The Mock Turtle."
direct_visual_evidence: "Sobs deeply, sings 'Beautiful Soup', dances the Lobster Quadrille, leans in close to listen to Alice."
costume_or_covering_evidence: ""
movement_evidence: "Melancholic movements, sobbing, dancing, leaning in with wide eyes/mouth."
associated_entities: ["alice", "the_gryphon"]
alias_or_role_evidence: ""
unknowns: ["exact physical form (is it a turtle-like creature or a hybrid?)"]
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# The Mock Turtle
**Role:** Melancholic Performer

**Status:** Physically Present

**Physical Description:**
A highly emotional, melancholic creature prone to deep sobbing. It has the ability to sing in a melancholy tone and can open its eyes and mouth very wide when listening intently.

**Costume & Silhouette:**
Not explicitly described.

**Descriptive Noun Phrases:**
Melancholic creature, sobbing singer, emotional companion.

**Uncertainty Notes:**
The exact morphology is not defined; it is a "mock" version of a turtle, but the specific hybrid features are not detailed in this text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
