# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:04:18.244679+00:00
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

Chapter id: CH009

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

**Setting:** A path leading away from the kitchen; a croquet-ground with players/soldiers; a sunny area where a Gryphon sleeps; a rocky ledge where the Mock Turtle sits.

**Characters:**
*   **Alice:** Curious, polite but increasingly frustrated by the illogical nature of her companions' conversation.
*   **The Duchess:** Sharp-featured, affectionate in an intrusive way, constantly offering "morals."
*   **The Queen of Hearts:** Sudden, terrifying, authoritative; she issues death sentences and then pardons everyone with a word.
*   **The Gryphon:** A creature that seems to find the Queen's whims amusing; it acts as a guide for Alice.
*   **The Mock Turtle:** A sorrowful, sobbing creature who tells a story of his past life as a real turtle.

**Events/Sequence:**
1.  **The Walk:** The Duchess and Alice walk together. The Duchess constantly offers "morzers" (morals) based on her own logic (e.g., linking pepper to temper). Alice finds the Duchess's sharp chin uncomfortable.
2.  **The Queen’s Arrival:** The Queen appears suddenly, startling them. She gives the Duchess a choice: execution or being sent off. The Duchess chooses to leave immediately.
3.  **The Game/Executiones:** Alice follows the Queen back to the croquet-ground. The Queen spends the game ordering executions of players (who are soldiers). Eventually, everyone except the King, Queen, and Alice is in custody.
4.  **The Departure:** The Queen asks if Alice has seen a Mock Turtle. After explaining it's what soup is made from, she sends Alice with the Gryphon to find him. The King pardons the prisoners as they leave.
5.  **Meeting the Gryphon:** They encounter the Gryphon sleeping in the sun. The Gryphon leads Alice toward the sound of sobbing.
6.  **The Mock Turtle’s Tale:** They find the Mock Turtle on a rocky ledge, weeping. He begins telling his history: he was once a real turtle who went to school in the sea under a master named Tortoise.
7.  **Schooling Logic:** The Mock Turtle describes his curriculum: Reeling and Writhing; Arithmetic (Ambition, Distraction, Uglification, Derision); Mystery; Seaography; and Drawling (taught by an old conger-eel). 
8.  **The Lesson Paradox:** It is revealed that "lessons" are called such because they "lessen" in duration each day. The chapter ends as the Gryphon prepares to transition from the story of school to the story of games.
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
- [The Duchess](#the-duchess)
- [The Queen of Hearts](#the-queen-of-hearts)
- [The Gryphon](#the-gryphon)
- [The Mock Turtle](#the-mock-turtle)
- [The King of Hearts](#the-king-of-hearts)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH001 Alice
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: bdiff-biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_duchess, the_queen_of_hearts, the_gryphon, the_mock_turtle]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Traveler.  
**Status:** Physically present.  

Alice is a curious and polite girl who finds herself navigating the illogical whims of those around her. She is often caught between the sharp-featured Duchess and the terrifying Queen of Hearts. In this chapter, she experiences frustration at the Duchess's constant moralizing and the arbitrary nature of the Queen's judgments.

**Visual Cues:**
- Human girl, human scale.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_duchess
canonical_character_id: CH003 The Duchess
aliases: []
is_fully_identified: true
manual_description_required: false
manualdescription_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [alice, the_queen_of_hearts]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Duchess
**Role:** Companion / Moralizer.  
**Status:** Physically present.  

The Duchess is characterized by her sharp features, specifically a sharp chin that Alice finds uncomfortable. She is prone to offering constant "morals" (or morzers) to Alice. Her personality is intrusive and authoritative until she is faced with the Queen's whims.

**Visual Cues:**
- Sharp-featured, sharp chin.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_queen_of_hearts
canonical_character_id: CH004 The Queen of Hearts
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
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [alice, the_duchess, the_king_of_hearts]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Queen of Hearts
**Role:** Authority Figure / Antagonist.  
**Status:** Physically present.  

A sudden and terrifying figure, the Queen is authoritative and unpredictable. She issues death sentences with ease but can also pardon everyone in a single word. Her presence is marked by suddenness and command.

**Visual Cues:**
- Authoritative presence, sudden movements.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_gryphon
canonical_character_id: CH005 The Gryphon
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical morphology is not explicitly detailed in this chapter beyond being a guide/creature.
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: creature
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [alice, the_mock_turtle]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Gryphon
**Role:** Guide / Companion.  
**Status:** Physically present.  

The Gryphon is a creature that finds the Queen's whims amusing and serves as a guide for Alice, leading her toward the sound of the Mock Turtle's sobbing.

**Visual Cues:**
- Creature-type entity.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_mock_turtle
canonical_character_id: CH006 The Mock Turtle
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical morphology is described through metaphor and history, but specific visual design is not fully established.
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: creature
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_gryphon, alice]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Mock Turtle
**Role:** Storyteller / Mourner.  
**Status:** Physically present.  

A sorrowful, sobbing creature sitting on a rocky ledge. He tells the story of his past life as a real turtle and describes his old school lessons (Reeling, Writhing, etc.).

**Visual Cues:**
- A shell-bearing or sea-creature hybrid; prone to weeping/sobbing.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_king_of_hearts
canonical_character_id: CH007 The King of Hearts
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only mentioned as a figure in the game/pardon process.
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_queen_of_hearts]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The King of Hearts
**Role:** Authority Figure.  
**Status:** Referenced/Present in background.  

The King is part of the croquet game and provides a counterpoint to the Queen's authority by issuing pardons as they leave.

**Visual Cues:**
- Humanoid, likely royal attire (implied).
[[/end_section]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
