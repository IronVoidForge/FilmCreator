# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:19:10.613250+00:00
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

Chapter id: CH012

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

**Setting:** A courtroom where a jury sits in a box; later, a riverbank under trees as the sun sets.

**Characters:**
- **Alice:** Currently at her full size (nearly two miles high), then shrinking back to normal size.
- **The King:** An authoritative but somewhat bumbling figure who reads from a notebook and issues rules.
- **The Queen:** A temperamental ruler prone to sudden outbursts of anger.
- **The White Rabbit:** The court official/messenger, respectful yet hurried.
- **The Knave:** The prisoner, made of cardboard.
- **The Jury/Lizard (Bill):** A group of creatures; the Lizard is a specific jury member who gets knocked over and then has ink spilled on him by the Queen.
- **Alice's Sister:** Appears at the end in the real world.

**Key Events:**
1. **The Accident:** Alice, growing large, accidentally tips over the jury-box while jumping up. The jurymen fall out like goldfish; one is a Lizard (Bill) who is placed head-downward and then later has an inkstand thrown at him by the Queen.
2. **Rule 42:** The King reads "Rule Forty-two," stating those over a mile high must leave. Alice argues she is nearly two miles high, leading to a debate on the validity of the rule.
3. **The Evidence:** The White Rabbit presents a piece of paper—a set of verses found in the prisoner's possession. 
4. **Reading the Verses:** The White Rabbit reads a cryptic poem regarding "she," "him," and "the tarts." The King attempts to interpret the verses as evidence of the Knave's guilt regarding the stolen tarts.
5. **The Conflict:** Alice challenges the meaninglessness of the verses. The Queen, furious at the interruption, orders "Off with her head!" 
6. **The Escape/Awakening:** Alice tells the cards they are nothing but a pack of cards; the cards fly at her, causing her to wake up on the riverbank in the real world.
7. **The Epilogue:** Alice tells her sister about the dream. The sister watches the sunset, reflecting on how the sounds of the natural world (rustling grass, sheep-bells) mirror the sounds of Wonderland.

**Visual/Continuity Elements:**
- **Scale Shift:** Alice starts huge, causing the jury to fall; she ends as a normal girl in the real world.
- **The Jury Box:** A structure that is tipped over and then restored.
- **The Verses:** A physical piece of paper read by the White Rabbit.
- **The Knave's Physicality:** He is made of cardboard, making his "lack of ability to swim" a literal visual gag.
- **The Transition:** The transition from the "pack of cards" flying at Alice to her waking up on the grass serves as the bridge between the dream and reality.
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
- [The King](#the-king)
- [The Queen](#the-queen)
- [The White Rabbit](#the-white-rabbit)
- [The Knave](#the-knave)
- [Bill the Lizard](#bill-the-lizard)
- [Alice's Sister](#alice-s-sister)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH001 Alice
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: 
alias_or_role_evidence: false
unknowns: 
source_refs: 
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically present (shrinking from giant to human scale).

**Physical Description:**
Initially depicted as a giantess, nearly two miles high, before shrinking back to her natural size. As a human girl in the real world, she is of normal child/adolescent scale.

**Notes:** 
The transition between her massive scale and her human scale is a key visual element of this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_king
canonical_character_id: CH003 The King
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: 
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# The King
**Role:** Authority figure / Judge

**Status:** Physically present.

**Physical Description:**
An authoritative but somewhat bumbling ruler who reads from a notebook to issue rules and interpret evidence.

**Notes:** 
His role is centered on the legalistic absurdity of Rule 42 and the interpretation of the verses.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_queen
canonical_character_id: CH004 The Queen
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: 
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# The Queen
**Role:** Temperamental Ruler

**Status:** Physically present.

**Physical Description:**
A ruler prone to sudden, violent outbursts of anger.

**Notes:** 
She provides the primary conflict by ordering "Off with her head!" when Alice challenges the court.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_white_rabbit
canonical_character_id: CH005 The White Rabbit
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: 
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# The White Rabbit
**Role:** Court Official / Messenger

**Status:** Physically present.

**Physical Description:**
A small, hurried animal serving as a court official.

**Notes:** 
He is responsible for presenting the verses and managing the courtroom proceedings.
[[end_section]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_knave
canonical_character_id: CH006 The Knave
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: 
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# The Knave
**Role:** Prisoner

**Status:** Physically present (as a cardboard entity).

**Physical Description:**
A prisoner made of cardboard.

**Notes:** 
His physical composition as a cardboard figure makes the debate over his ability to "swim" or handle evidence visually absurd.
[[/SECTION]]
[[/FILcut_record]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bill_the_lizard
canonical_character_id: CH007 Bill the Lizard
aliases: Bill, The Lizard
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: 
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Bill the Lizard
**Role:** Jury Member

**Status:** Physically present.

**Physical Description:**
A lizard-like creature serving as a member of the jury.

**Notes:** 
He is knocked over when the jury box tips and later has an inkstand thrown at him by the Queen.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alices_sister
canonical_character_id: CH008 Alice's Sister
aliases: 
is_fully_identified: true
manual_description_required: false
manualdescription_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: 
alias_or_role_evidence: false
unknowns: 
source_refs: 
[[SECTION markdown]]
# Alice's Sister
**Role:** Observer / Real-world anchor

**Status:** Physically present (at the end).

**Physical Description:**
A human female of a slightly older/different scale than Alice, watching the sunset.

**Notes:** 
She represents the transition from the dream world to reality.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
