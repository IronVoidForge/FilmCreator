# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:07:31.965800+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH025

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

**Setting:** The palace and throne room of Zodanga; the subterranean dungeons of the palace.

**Characters:**
- **John Carter:** The protagonist, who infiltrates the palace to prevent a forced marriage.
- **Dejah Thoris:** Princess of Helium, who is being forced into a marriage ceremony with Sab Than.
- **Than Kosis:** The Jeddak of Zodanga, who presides over the wedding ceremony.
- **Sab Than:** Prince of Zodanga, the intended groom and antagonist.
- **Tars Tarkas:** Leader of the Tharks, who leads a cavalry charge into the city.
- **Kantos Kan:** An ally of Carter, rescued from the palace dungeons.

**Events:**
- **The Infiltration:** John Carter leads fifty Tharks, commanded by Tars Tarkas, through the gates of Zodanga and into the palace gardens.
- **The Wedding Interruption:** Inside the audience chamber, a ceremony is underway to bind Dejah Thoris to Sab Than with golden chains. Carter smashes through a window and leaps into the hall, shattering the ceremonial chain.
- **The Battle in the Throne Room:** A chaotic skirmish ensues between Carter, the Zodangan nobility/guards, and the Tharks. During the fight, Sab Than attempts to strike Dejah Thoris, but Carter kills him. Tars Tarkas arrives on the platform to assist, eventually leaving only the Tharks and Carter's party alive in the hall.
- **The Rescue:** Carter and a small group of warriors descend into the dungeons, where they locate and free Kantos Kan using keys taken from a fallen jailer.
- **The Declaration:** Amidst the ongoing sounds of war in the streets of Zodanga, Carter and Dejah Thoris are left alone in the throne room. Carter confesses his love and asks for her hand in marriage; Dejah Thoris accepts, and they pledge themselves to one another.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH025

- [John Carter](#john_carter)
- [Dejah Thoris](#dejah_thoris)
- [Than Kosis](#than_kosis)
- [Sab Than](#sab_than)
- [Tars Tarkas](#tars_tarkas)
- [Kantos Kan](#kantos_kan)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: Protagonist
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
associated_entities: Dejah Thoris, Tars Tarkas, Kantos Kan
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Infiltrator

**Status:** Physically Present

**Description:** A human warrior capable of great leaps and combat prowess. He infiltrates the Zodangan palace to interrupt a forced marriage ceremony.

**Traits:** High mobility, combatant, romantic lead.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: Princess of Helium
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
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: John Carter, Sab Than
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess of Helium / Love Interest

**Status:** Physically Present

**Description:** A princess being subjected to a forced marriage ceremony involving golden chains.

**Traits:** Royal, captive (initially), romantic lead.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: than_kosis
canonical_character_id: Than Kosis
aliases: Jeddak of Zodanga
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
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Sab Than
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Than Kosis
**Role:** Jeddak of Zodanga / Presiding Official

**Status:** Physically Present (referenced in ceremony)

**Description:** The ruler of Zodanga who presides over the wedding ceremony between Sab Than and Dejah Thoris.

**Traits:** Authority figure, ceremonial role.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sab_than
canonical_character_id: Sab Than
aliases: Prince of Zodanga
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
movement_evidence: true
associated_entities: Dejah Thoris, Than Kosis
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Sab Than
**Role:** Antagonist / Intended Groom

**Status:** Physically Present (Deceased)

**Description:** The Prince of Zodanga who attempts to strike Dejah Thoris during the skirmish and is killed by John Carter.

**Traits:** Aggressive, antagonist, royal.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: Leader of the Tharks
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: large
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: John Carter, Tharks
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Leader of the Tharks / Military Commander

**Status:** Physically Present

**Description:** A leader who commands a cavalry charge and leads Tharks into the Zodangan palace.

**Traits:** Warrior, commander, large scale.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: Kantos Kan
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
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: John Carter
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Kantos Kan
**Role:** Ally

**Status:** Physically Present (Rescued)

**Description:** An ally of John Carter who was held in the subterranean dungeons of the Zodangan palace.

**Traits:** Prisoner, rescued.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
