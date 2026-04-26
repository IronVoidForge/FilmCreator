# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:55:24.617216+00:00
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

Chapter id: CH017

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

**Events:**
The narrator infiltrates the city of Thark to rescue Dejah Thoris from the clutches of the Thark Jeddak, Tal Hajus. After witnessing Tal Hajus's cruel intentions and his plan to torture the Princess, the narrator intervenes, knocking the Jeddak unconscious with a single blow. The narrator, Dejah Thoris, and Sola escape the city on thoats, heading northeast across a mossy waste toward Helium.

The journey becomes perilous as the party runs out of food and water, eventually becoming lost. During their trek, they are joined by the narrator's faithful hound, Woola. After one of their thoats collapses from exhaustion, the group is spotted by a Thark chieftain scanning the area with a fieldglass. The narrator uses his Martian rifle to kill the charging chieftain and then forces Dejah Thoris and Sola to flee toward the hills to ensure their safety. As the narrator stays behind to provide cover fire with his rifle, he is eventually overwhelmed by a massive force of Thark warriors. The chapter ends with the narrator being beaten into unconsciousness after attempting a desperate defense.

**Characters:**
* **The Narrator:** A resourceful and heroic figure who rescues Dejah Thoris and sacrifices his own safety to ensure her escape.
* **Dejah Thoris:** The Princess of Helium; she displays immense dignity and courage even when facing the Thark Jeddak.
* **Sola:** A companion to Dejah Thoris who assists in the escape.
* **Tal Hajus:** The cruel and beastly Jeddak of the Tharks, characterized by his hatred for the red men of Helium.
* **Tars Tarkas:** A Thark warrior who observes the scene with deep loathing for Tal Hajus, though he does not intervene.
* **Woola:** The narrator's loyal Martian hound who tracks them through the waste.

**Settings:**
* **The City of Thark:** Specifically the brilliantly lighted apartments and the immense circular hall of the Jeddak.
* **The Mossy Waste:** A vast, trackless, and dangerous terrain between Thark and Helium.
* **The Low Mountains/Hills:** The destination the party seeks for shelter and navigation.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH017

- [Protagonist](#protagonist)
- [Dejah Thoris](#dejah-thoris)
- [Sola](#sola)
- [Tal Hajus](#tal-hajus)
- [Tars Tarkas](#tars-tarkas)
- [Woola](#woola)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: CH002 Protagonist
aliases: Narrator
is_fully_identified: false
manual_description_required: true
manual_description_reason: Physical appearance, clothing, and specific morphology are not described in this chapter.
clarification_required: true
clarification_reason: Physical identity is unknown from text alone.
clarification_question: What is the protagonist's physical appearance, race/species, and attire?
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.5
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: Dejah Thoris, Sola, Woola
alias_or_role_evidence: true
unknowns: physical appearance, clothing, specific height/build
source_refs: chapter summary
[[SECTION markdown]]
# Protagonist
**Role:** Heroic rescuer and defender.
**Status:** Physically present.
**Description:** A resourceful individual who uses a Martian rifle and engages in hand-to-hand combat. He acts as the protector for Dejah Thoris and Sola, eventually sacrificing his safety to cover their retreat against Thark warriors.
**Uncertainty:** No visual description of face, body, or clothing is provided in this text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH003 Dejah Thoris
aliases: Princess of Helium
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
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: Protagonist, Sola, Tal Hajus
alias_or_role_evidence: true
unknowns: 
source_refs: chapter summary
[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess of Helium; captive/rescued party.
**Status:** Physically present.
**Description:** A woman of immense dignity and courage, even when facing the Thark Jeddak. She is part of the escape party fleeing toward Helium.
**Uncertainty:** While her character traits are established, specific visual details like hair color or clothing are not detailed in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: SOLA_01
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: Dejah Thoris, Protagonist
alias_or_role_evidence: true
unknowns: physical appearance
source_refs: chapter summary
[[SECTION markdown]]
# Sola
**Role:** Companion to Dejah Thoris.
**Status:** Physically present.
**Description:** An associate of the Princess who assists in the escape from the City of Thark and travels through the mossy waste.
**Uncertainty:** Physical appearance is entirely unstated.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: TAL_HAJUS_01
aliases: Thark Jeddak
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Tars Tarkas
alias_or_role_evidence: true
unknowns: specific Thark morphology
source_refs: chapter summary
[[SECTION markdown]]
# Tal Hajus
**Role:** Cruel Jeddak of the Tharks.
**Status:** Physically present (referenced/encountered).
**Description:** A beastly and cruel ruler characterized by his hatred for the red men of Helium. He intends to torture Dejah Thoris.
**Uncertainty:** Specific physical morphology of the Thark species is not detailed in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: TARS_TARKAS_01
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Tal Hajus
alias_or_role_evidence: true
unknowns: physical appearance
source_refs: chapter summary
[[SECTION markdown]]
# Tars Tarkas
**Role:** Thark warrior.
**Status:** Physically present (observer).
**Description:** A warrior who observes the actions of Tal Hajus with deep loathing, though he chooses not to intervene in the immediate conflict.
**Uncertainty:** Physical appearance and specific Thark morphology are not described here.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: WOOLA_01
aliases: Martian hound
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: unknown
scale_hint: large
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: Protagonist
alias_or_role_evidence: true
unknowns: specific morphology/species details
source_refs: chapter summary
[[SECTION markdown]]
# Woola
**Role:** Loyal Martian hound.
**Status:** Physically present.
**Description:** A faithful animal companion to the protagonist who tracks the group through the mossy waste.
**Uncertainty:** Specific biological features of the "Martian hound" are not detailed in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
