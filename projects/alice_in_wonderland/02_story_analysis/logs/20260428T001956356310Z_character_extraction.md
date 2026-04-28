# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:19:56.356310+00:00
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
- [The Jury / Bill the Lizard](#the-jury---bill-the-lizard)
- [Alice's Sister](#alice_s-sister)
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
confidence: 1.0
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

**Status:** Physically present (Dream/Reality)

**Description:**
Alice undergoes a massive scale shift, starting at nearly two miles high before shrinking back to her normal human size upon waking. In the dream sequence, she is an enormous figure compared to the jury. In the real world, she is a young girl lying on a riverbank.

**Notes:** 
- Dream version: Giant/Colossal scale.
- Reality version: Human scale.
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
confidence: 0.9
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
**Role:** Authority Figure / Judge

**Status:** Physically present (Dream)

**Description:**
An authoritative but somewhat bumbling ruler who presides over the court. He reads from a notebook and attempts to interpret cryptic verses as legal evidence.

**Notes:** 
- Likely a playing card or humanoid creature based on context.
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
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: 
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# The Queen
**Role:** Ruler / Antagonist

**Status:** Physically present (Dream)

**Description:**
A temperamental ruler known for sudden outbursts of anger. She is prone to ordering executions ("Off with her head!") when challenged or interrupted.

**Notes:** 
- Likely a playing card or humanoid creature.
[[
/SECTION]]
[[/FILMCRECTOR_RECORD]]

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
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: 
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# The White Rabbit
**Role:** Court Official / Messenger

**Status:** Physically present (Dream)

**Description:**
A respectful yet hurried official who presents evidence and reads verses to the court.

**Notes:** 
- Likely an anthropomorphic rabbit.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_knave
canonical_character_id: CH006 The Knave
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance is defined by his material rather than biological features.
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
# The Knave
**Role:** Prisoner

**Status:** Physically present (Dream)

**Description:**
The prisoner accused of stealing the tarts. He is uniquely made of cardboard, which makes his supposed inability to swim a literal physical trait.

**Notes:** 
- A cardboard figure/card entity.
[[/SECTION]]
[[/FILcut_record]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_jury_bill_the_lizard
canonical_character_id: CH007 The Jury / Bill the Lizard
aliases: Bill, The Lizard
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: animal
morphology_hint: biped
scale_hint: tiny
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
# The Jury / Bill the Lizard
**Role:** Jurors

**Status:** Physically present (Dream)

**Description:**
A group of creatures serving as the jury. One specific member is a Lizard named Bill, who is placed head-downward in the jury box and later has an inkstand thrown at him by the Queen.

**Notes:** 
- The jury members are small enough to fall out of the box like goldfish.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCIT_RECORD]]
type: character
asset_id: alices_sister
canonical_character_id: CH008 Alice's Sister
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
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
**Role:** Observer / Reality Anchor

**Status:** Physically present (Reality)

**Description:**
Alice's sister, who watches the sunset on the riverbank. She listens to Alice recount her dream.

**Notes:** 
- Human scale; provides a contrast to the dream world.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
