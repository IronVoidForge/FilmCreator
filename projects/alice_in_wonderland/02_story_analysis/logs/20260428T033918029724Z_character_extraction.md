# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:39:18.029724+00:00
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
A large table set under a tree in front of a house. A tea party is in progress. Later, Alice moves through a wood to find a door in a tree, leading back to a long hall with a glass table, and finally into a beautiful garden with flower-beds and fountains.

**Characters:**
* **Alice:** Curious, indignant, and easily confused by the nonsensical logic of others.
* **The Hatter:** Eccentric, rude, and obsessed with Time; carries a watch that tells the day but not the hour.
* **The March Hare:** Erratic and argumentative; involved in a dispute with the Hatter regarding butter.
* **The Dormouse:** Perpetually sleepy, used as a cushion/object by the others; tells a nonsensical story about three sisters.

**Key Events & Visual Continuity:**
* **Entrance:** Alice approaches the tea party; the Hare and Hatter shout "No room!" despite there being space. Alice sits in a large armchair at one end of the table.
* **Object Interaction (The Watch):** The Hatter examines his watch, shakes it, and holds it to his ear. He dips it into his tea cup. The watch displays the day of the month but not the time.
* **Riddle Exchange:** The Hatter asks, "Why is a raven like a writing-desk?" No answer is provided by anyone.
* **The Conflict with Time:** The Hatter explains that he quarreled with "Time" (personified) last March at a Queen of Hearts concert, causing Time to stay perpetually at six o'clock.
* **The Tea Party Loop:** Because it is always tea-time, the characters move around the table to use clean dishes as they run out. 
    * **Shift/Movement:** The Hatter moves one seat; the Dormouse follows him; the March Hare moves into the Dormouse’s old spot; Alice reluctantly takes the March Hare's old spot (noting a spilled milk-jug in the plate).
* **The Story:** The Dormouse tells a story about three sisters (Elsie, Lacie, and Tillie) living at the bottom of a "treacle-well" and drawing things starting with the letter 'M'.
* **Exit:** Alice, disgusted by the Hatter's rudeness ("Then you shouldn't talk"), stands up and walks away. The others ignore her; the last visual is the Hare and Hatter attempting to put the Dormouse into a teapot.
* **Transformation/Navigation Sequence:** 
    1. Alice finds a door in a tree.
    2. She enters the long hall.
    3. She uses a golden key to unlock the garden door.
    4. She nibbles a piece of mushroom from her pocket, shrinking until she is one foot high.
    5. She walks down a passage and enters the beautiful garden.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
[[markdown]]
# Character Index: Chapter 007

- [Alice](#alice)
- [The Hatter](#the-hatter)
- [The March Hare](#the-march-hare)
- [The Dormouse](#the-dormouse)
- [Time](#time) (Referenced)
- [Elsie, Lacie, and Tillie](#elsie-lacie-and-tillie) (Referenced/Story)

[[/SECTION]]
[[/FILMCREATOR_PACKET]]

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
scale_hint: unknown
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Explicitly named as Alice throughout the text."
direct_visual_evidence: "Alice is physically present and interacts with the tea party characters and environment."
costume_or_covering_evidence: ""
movement_evidence: "Walks to the tea party, sits in an armchair, stands up to leave, walks through a wood, enters a hall, and walks into a garden. Shrinks to one foot high after eating mushroom."
associated_entities: ["the_hatter", "the_march_hare", "the_dormouse"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH007"]
[[SECTION markdown]]
# Alice
**Role:** Protagonist / Participant in the tea party.

**Status:** Physically Present.

**Physical Description:** 
Alice is a young girl who undergoes a significant scale change during this chapter. After consuming a piece of mushroom, she shrinks to approximately one foot in height.

**Costume & Silhouette:** 
No specific costume details are provided in this chapter text, though her silhouette changes from human-scale to tiny (one foot high).

**Descriptive Noun Phrases:** 
Curious girl, shrinking child, indignant visitor, small explorer.

**Uncertainty Notes:** 
Specific clothing colors or patterns are not mentioned in this chapter.
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
direct_identity_evidence: "Explicitly identified as The Hatter."
direct_visual_evidence: "Physically present at the tea party; interacts with a watch and tea."
costume_or_covering_evidence: ""
movement_evidence: "Moves one seat along the table during the tea-time loop."
associated_entities: ["alice", "the_march_hare", "the_dormouse", "time"]
alias_or_role_evidence: "Referred to as 'the Hatter'."
unknowns: []
source_refs: ["CH007"]
[[SECTION markdown]]
# The Hatter
**Role:** Eccentric host/participant at the tea party.

**Status:** Physically Present.

**Physical Description:** 
An eccentric individual obsessed with Time. He is seen examining, shaking, and even dipping a watch into his tea cup.

**Costume & Silhouette:** 
No specific costume details provided in this chapter.

**Descriptive Noun Phrases:** 
Eccentric host, riddle-asking madman, tea-drinking Hatter.

**Uncertainty Notes:** 
Visual appearance (clothing/facial features) is not described in the text.
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
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Explicitly identified as The March Hare."
direct_visual_evidence: "Physically present at the tea party; shouts 'No room!' and argues about butter."
costume_or_covering_evidence: ""
movement_evidence: "Shouts, argues, and moves one seat along the table during the tea-time loop."
associated_entities: ["the_hatter", "the_dormouse"]
alias_or_role_evidence: "Referred to as 'the March Hare'."
unknowns: []
source_refs: ["CH007"]
[[SECTION markdown]]
# The March Hare
**Role:** Erratic participant at the tea party.

**Status:** Physically Present.

**Physical Description:** 
An erratic and argumentative animal character.

**Costume & Silhouette:** 
No specific costume details provided.

**Descriptive Noun Phrases:** 
Erratic hare, argumentative guest, tea-party rabbit.

**Uncertainty Notes:** 
Specific breed or visual appearance of the hare is not detailed beyond its name/species.
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
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Explicitly identified as The Dormouse."
direct_visual_evidence: "Physically present; used as a cushion/object by others; tells a story; is nearly put into a teapot."
costume_or_covering_evidence: ""
movement_evidence: "Sleepy, moves one seat along the table following the Hatter."
associated_entities: ["the_hatter", "the_march_hare"]
alias_or_role_evidence: "Referred to as 'the Dormouse'."
unknowns: []
source_refs: ["CH007"]
[[SECTION markdown]]
# The Dormouse
**Role:** Sleepy participant at the tea party.

**Status:** Physically Present.

**Physical Description:** 
A perpetually sleepy creature. Often treated as an object or cushion by the Hatter and March Hare.

**Costume & Silhouette:** 
No specific costume details provided.

**Descriptive Noun Phrases:** 
Sleepy dormouse, drowsy guest, teapot-bound mouse.

**Uncertainty Notes:** 
Exact morphology (is it a literal mouse or a humanoid creature?) is implied by "Dormouse" but not visually described.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: time
canonical_character_id: time
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Time is personified in dialogue but has no physical description provided in the text."
clarification_required: true
clarification_reason: "It is unclear if Time should be rendered as a human-like entity or an abstract concept/force."
clarification_question: "Should 'Time' be depicted as a humanoid character or an abstract visual effect?"
character_type_hint: abstract
morphology_hint: unknown
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "Mentioned by the Hatter as having quarreled with him."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["the_hatter"]
alias_or_role_evidence: ""
unknowns: ["physical form", "appearance"]
source_refs: ["CH007"]
[[SECTION markdown]]
# Time
**Role:** Personified entity (referenced).

**Status:** Referenced.

**Physical Description:** 
No physical description is provided. The Hatter claims to have quarreled with Time, causing Time to stay at six o'clock.

**Costume & Silhouette:** 
Unknown.

**Descriptive Noun Phrases:** 
Personified time, the quarrelsome hour.

**Uncertainty Notes:** 
This character is purely conceptual/dialogue-driven in this chapter. Visual representation is entirely speculative based on the Hatter's personification.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: treacle_well_sisters
canonical_character_id: treacle_well_sisters
aliases: ["Elsie", "Lacie", "Tillie"]
is_fully_identified: true
manual_description_required: true
manual_description_reason: "These characters only exist within a story told by the Dormouse and have no physical description."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: unknown
renderability_hint: context_only
confidence: 0.4
direct_identity_evidence: "Named by the Dormouse in his story."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: "Identified as 'three sisters'."
unknowns: ["physical appearance", "age", "clothing"]
source_refs: ["CH007"]
[[SECTION markdown]]
# Elsie, Lacie, and Tillie
**Role:** Characters in the Dormouse's story.

**Status:** Referenced (Story).

**Physical Description:** 
No physical description is provided. They are described as living at the bottom of a "treacle-well" and drawing things starting with the letter 'M'.

**Costume & Silhouette:** 
Unknown.

**Descriptive Noun Phrases:** 
Treacle-well sisters, storybook characters.

**Uncertainty Notes:** 
These are purely narrative entities within this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
