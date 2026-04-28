# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:52:00.322013+00:00
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

Chapter id: CH007

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

**Setting:** A large table set under a tree in front of a house; later, a wooded path leading to a long hall with a glass table, and finally the beautiful garden.

**Characters:**
- **Alice:** A young girl attempting to apply logic to an illogical situation.
- **The March Hare:** An eccentric host, prone to arguing about social etiquette and butter.
- **The Hatter:** A curious, somewhat rude figure who possesses a watch that tracks the day of the month rather than time.
- **The Dormouse:** A sleepy creature used as a cushion/object by the others; tells a surreal story about three sisters in a treacle-well.

**Key Events & Transitions:**
- **The Tea Party Arrival:** Alice approaches a table where the March Hare, Hatter, and Dormouse are crowded at one corner. They cry "No room!" despite there being plenty of space. Alice sits in a large armchair.
- **The Riddle/Argument:** The Hatter asks, "Why is a raven like a writing-desk?" leading to a circular debate about language and meaning. 
- **The Watch Reveal:** The Hatter shows his watch; it tracks the date but not the hour. He explains that because of a quarrel with "Time" (personified), it is always tea-time, necessitating the constant movement around the table to use clean dishes.
- **The Dormouse’s Story:** The Dormouse tells a story about three sisters (Elsie, Lacie, and Tillie) living in a treacle-well. Alice's questions about the logic of the story cause friction with the hosts.
- **The Seat Shift:** To keep the tea-things clean, the group moves one place on: The Hatter moves, the Dormouse follows him, the March Hare takes the Dormouse’s spot, and Alice reluctantly takes the March Hare's spot (getting splashed by milk).
- **Alice’s Departure:** Frustrated by the Hatter's rudeness ("Then you shouldn't talk"), Alice walks off in disgust. She looks back to see them putting the Dormouse into a teapot.
- **The Return to the Garden:** Walking through the woods, Alice finds a door in a tree. She enters the long hall, uses the golden key on the glass table, nibbles the mushroom to shrink herself, and successfully enters the beautiful garden.

**Visual Continuity/Objects:**
- Large tea table with tea-set (no wine).
- The Hatter's watch (held to ear, dipped in tea).
- A piece of mushroom (kept in Alice's pocket).
- The golden key and glass table.
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
- [The March Hare](#the-march-hare)
- [The Hatter](#the-hatter)
- [The Dormouse](#the-dormouse)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH001 Alice
aliases: Alice
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
confidence: 0.9
direct_identity_evidence: "Alice is the central protagonist interacting with the tea party guests."
direct_visual_evidence: "A young girl; later seen shrinking via a mushroom and navigating a hall/garden."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: The March Hare, The Hatter, The Dormouse
alias_or_role_evidence: ""
unknowns: ""
source_refs: "CH007"

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Guest at the tea party.

**Status:** Physically present.

**Description:** A young girl attempting to apply logic to ansilly situations. She is capable of navigating through woods, halls, and gardens.

**Notes:** In this chapter, she experiences a shrinking effect via a mushroom.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: march_hare
canonical_character_id: CH003 March Hare
aliases: The March Hare
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
confidence: 0.8
direct_identity_evidence: "Identified as the March Hare during the tea party."
direct_visual_evidence: "An eccentric host at a tea table."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: Alice, The Hatter, The Dormouse
alias_or_role_evidence: ""
unknowns: ""
source_refs: "CH007"

[[SECTION markdown]]
# The March Hare
**Role:** Host / Tea party guest.

**Status:** Physically present.

**Description:** An eccentric host prone to arguing about social etiquette and the practicality of butter.

**Notes:** Part of a group that constantly shifts seats around a tea table to maintain cleanliness.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_hatter
canonical_character_id: CH004 The Hatter
aliases: The Hatter
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
confidence: 0.8
direct_identity_evidence: "Identified as the Hatter during the tea party."
direct_visual_evidence: "A curious, somewhat rude figure; possesses a unique watch."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: Alice, The March Hare, The Dormouse
alias_or_role_evidence: ""
unknowns: ""
source_refs: "CH007"

[[SECTION markdown]]
# The Hatter
**Role:** Host / Tea party guest.

**Status:** Physically present.

**Description:** A curious and somewhat rude figure. He carries a watch that tracks the day of the month rather than the hour.

**Notes:** His relationship with "Time" is a central driver for his constant tea-time state.
[[end_section]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dormouse
canonical_character_id: CH005 Dormouse
aliases: The Dormouse
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
confidence: 0.8
direct_identity_evidence: "Identified as the Dormouse during the tea party."
direct_visual_evidence: "A sleepy creature used as a cushion/object by others; tells surreal stories."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: Alice, The March Hare, The Hatter
alias_or_role_evidence: ""
unknowns: ""
source_refs: "CH007"

[[SECTION markdown]]
# The Dormouse
**Role:** Guest / Tea party guest.

**Status:** Physically present.

**Description:** A sleepy creature who tells surreal stories about sisters in a treacle-well. 

**Notes:** Often used as a cushion or object by the other guests; seen being put into a teapot at the end of the scene.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
