# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:40:59.853977+00:00
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

**Events:**
The protagonist joins Sola and a massive cavalcade of two hundred and fifty decorated chariots drawn by enormous animals to witness the hatching at a remote incubator. Upon arrival, the protagonist performs a feat of physical prowess (leaping over parked chariots) for the chieftain Lorquas Ptomel. The community executes a ritualized "capture" where women and youths form a gauntlet to collect the newly hatched, three-to-four-foot-tall Martians as they emerge from the incubator. Following the ceremony, the warriors transport eggs from subterranean vaults to the incubator for their next five-year incubation cycle. Back at the dead city, the protagonist undergoes intensive training in Martian language and telepathy under Sola's tutelage.

**Characters:**
* **The Protagonist:** An Earthman learning Martian customs; discovers he possesses a unique mental defense that prevents Martians from reading his thoughts.
* **Sola:** A female Martian who acts as the protagonist's guide and foster mother to a newly hatched male.
* **Tars Tarkas:** A warrior/chief involved in the coordination of the incubator ceremony.
* **Lorquas Ptomel (Jed):** The enormous principal chieftain overseeing the proceedings.
* **The Young Martian:** A physically perfect, four-foot-tall male captured during the hatching; becomes a rival to the protagonist during training.

**Settings:**
* **The Plaza:** The central gathering point of the Martian community.
* **The Dead Sea Bottom/Valley:** The terrain traversed by the massive chariot procession.
* **The Incubator:** A remote, walled enclosure where Martian eggs hatch after five years of exposure to sun rays.
* **The Dead City:** The protagonist's base of operations and site of his ongoing education.

**Key Concepts:**
* **Telepathy:** The universal Martian language used for communication between species and for guiding animals without bridles.
* **Martian Child-Rearing:** A pitiless system where children are communal property, raised by foster mothers to be warriors, with no concept of parental love.
* **Biological Selection:** A strict process involving the destruction of "imperfect" eggs and regulated birth rates to manage dwindling resources on a dying planet.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH007

- [Protagonist](#protagonist)
- [Sola](#sola)
- [Tars Tarkas](#tars-tarkas)
- [Lorquas Ptomel](#lorquas-ptomel)
- [The Young Martian](#the-young-martian)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: CH002 Protagonist
aliases: Earthman
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance (height, build, facial features) is not described in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Explicitly identified as an Earthman and the protagonist.
direct_visual_evidence: Performs a feat of leaping over parked chariots.
costume_or_covering_evidence: None provided.
movement_evidence: Capable of significant physical prowess/leaping.
associated_entities: Sola, Lorquas Ptomel
alias_or_role_evidence: Learning Martian customs and telepathy.
unknowns: Physical appearance, clothing.
source_refs: Chapter 007

[[SECTION markdown]]
# Protagonist
**Role:** Earthman learning Martian customs; student of Sola.
**Presence:** Physically present.
**Physical Description:** Not explicitly described in this chapter beyond physical capability (leaping over chariots).
**Costume/Silhouette:** Unknown.
**Notes:** Possesses a unique mental defense preventing Martians from reading his thoughts. High athletic ability.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH003 Sola
aliases: Guide, Foster Mother
is_fully_identified: true
manual_description_required: true
manual_description_reason: Specific physical morphology of the Martian female is not detailed in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: Identified as a female Martian and guide to the protagonist.
direct_visual_evidence: Present during training in the Dead City.
costume_or_covering_evidence: None provided.
movement_evidence: Teaching telepathy/language.
associated_entities: Protagonist, The Young Martian
alias_or_role_evidence: Acts as a tutor and foster mother.
unknowns: Specific facial features, skin texture, or exact height.
source_refs: Chapter 007

[[SECTION markdown]]
# Sola
**Role:** Female Martian guide and teacher.
**Presence:** Physically present.
**Physical Description:** Martian female; scale is human-scale relative to the protagonist.
**Costume/Silhouette:** Unknown.
**Notes:** Highly skilled in telepathy and Martian language; acts as a foster mother to a newly hatched male.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH004 Tars Tarkas
aliases: Warrior, Chief
is_fully_identified: true
manual_description_required: true
manual_description_reason: No specific physical description provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: Named as a warrior/chief involved in the ceremony.
direct_visual_evidence: Involved in coordination of the incubator ceremony.
costume_or_covering_evidence: None provided.
movement_evidence: Coordinating ritualized activities.
associated_entities: Lorquas Ptomel
alias_or_role_evidence: Warrior/Chief status.
unknowns: Physical appearance, specific Martian morphology details.
source_refs: Chapter 007

[[SECTION markdown]]
# Tars Tarkas
**Role:** Martian warrior and chief.
**Presence:** Physically present (referenced as coordinating).
**Physical Description:** Martian humanoid; scale is human-scale.
**Costume/Silhouette:** Unknown.
**Notes:** Involved in the coordination of the incubator ceremony.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: CH005 Lorquas Ptomel
aliases: Jed, Principal Chieftain
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance beyond "enormous" is not detailed.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: large
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: Identified as the principal chieftain.
direct_visual_evidence: Overseeing the proceedings at the incubator.
costume_or_covering_evidence: None provided.
movement_evidence: Overseeing/standing.
associated_entities: Tars Tarkas, Protagonist
alias_or_role_evidence: Referred to as "Jed".
unknowns: Specific facial features or exact scale beyond "enormous".
source_refs: Chapter 007

[[SECTION markdown]]
# Lorquas Ptomel
**Role:** Principal Chieftain.
**Presence:** Physically present.
**Physical Description:** Enormous Martian humanoid.
**Costume/Silhouette:** Unknown.
**Notes:** Also referred to as Jed; oversees the hatching ceremony and community proceedings.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: young_martian
canonical_character_id: CH006 Young Martian
aliases: Rival
is_fully_identified: true
manual_description_required: false
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Identified as a newly hatched male Martian.
direct_visual_evidence: Three-to-four-foot-tall; described as "physically perfect".
costume_or_covering_evidence: None (newly hatched).
movement_evidence: Captured during the hatching ceremony; training alongside protagonist.
associated_entities: Sola, Protagonist
alias_or_role_evidence: Becomes a rival to the protagonist.
unknowns: Specific skin color or eye details.
source_refs: Chapter 007

[[SECTION markdown]]
# The Young Martian
**Role:** Newly hatched Martian; rival to the protagonist.
**Presence:** Physically present.
**Physical Description:** Three-to-four-foot-tall male; described as "physically perfect".
**Costume/Silhouette:** None (newly hatched).
**Notes:** Part of the communal child-rearing system; undergoes training in telepathy and language.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
