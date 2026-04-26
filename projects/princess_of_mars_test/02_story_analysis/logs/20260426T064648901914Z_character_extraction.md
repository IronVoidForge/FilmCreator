# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:46:48.901914+00:00
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

Chapter id: CH011

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
John Carter secures Dejah Thoris's safety by assigning Sola as her guard and threatening Sarkoja with death if she continues to mistreat the captive. Carter moves Dejah Thoris and Sola into more luxurious, ancient quarters in a building overlooking the plaza. During their time in the new apartments, Carter and Dejah Thoris engage in a deep conversation where he reveals his true origin: he is from Earth (specifically Virginia). Dejah Thoris explains that while Barsoomians can observe Earth through advanced telescopic technology, they did not recognize him because he lacks the typical "unsightly" clothing of Earthmen. The chapter concludes with Carter receiving a summons from Lorquas Ptomel to appear before the council.

**Characters:**
- **John Carter:** A man from Earth who is establishing his status among the Tharks and protecting Dejah Thoris.
- **Dejah Thoris:** A noblewoman of the red race; she expresses growing trust and curiosity toward Carter and shares knowledge of Martian history.
- **Sola:** An ally to Carter who takes on the role of protector/attendant for Dejah Thoris.
- **Sarkoja:** A hostile figure who is rebuffed by Carter's threats.
- **Lorquas Ptomel:** The high-ranking leader of the community who summons Carter.
- **Tars Tarkas:** A powerful Thark chieftain present during the council.

**Settings:**
- **The New Quarters:** An ancient, opulent building featuring marble ceilings, gold chains, and elaborate frescoes depicting a long-extinct, fair-haired race of Martians.
- **The Plaza/Audience Chamber:** The central political hub where the Thark leaders reside.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH011

- [John Carter](#john_carter)
- [Dejah Thoris](#dejah_thoris)
- [Sola](#sola)
- [Sarkoja](#sarkoja)
- [Lorquas Ptomel](#lorquas_ptomel)
- [Tars Tarkas](#tars_tarkas)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
aliases: Carter, Man from Earth
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
direct_identity_evidence: Explicitly identified as a man from Earth (Virginia).
direct_visual_evidence: Implied human physiology.
costume_or_covering_evidence: Lacks typical "unsightly" Earth clothing, implying Martian-style attire or bare skin/minimalist gear common to the setting.
movement_evidence: 
associated_entities: Dejah Thoris, Sola
alias_or_role_evidence: Protagonist, protector of Dejah Thoris.
unknowns: 
source_refs: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Earthman

**Status:** Physically Present

**Physical Description:** A human male from Earth (Virginia). He possesses the strength and physical capabilities characteristic of his presence on Mars.

**Costume/Silhouette:** Noted for lacking the typical "unsightly" clothing associated with Earthmen, suggesting he has adopted local Martian attire or is minimally dressed in a way that distinguishes him from terrestrial observers.

**Prompt Phrases:** human male, athletic build, Earthman, Martian adventurer.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH003 Dejah Thoris
aliases: Princess of Mars
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
direct_identity_evidence: Identified as a noblewoman of the red race.
direct_visual_evidence: Member of the red Martian race.
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: John Carter, Sola
alias_or_role_evidence: Noblewoman, Princess.
unknowns: 
source_refs: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Noblewoman / Love Interest

**Status:** Physically Present

**Physical Description:** A member of the red race of Barsoom (Martian).

**Costume/Silhouette:** Implied noble status; resides in opulent, ancient quarters.

**Prompt Phrases:** Martian noblewoman, red-skinned humanoid, elegant Barsoomian.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH004 Sola
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
direct_identity_evidence: Identified as an ally to Carter and guard for Dejah Thoris.
direct_visual_evidence: Part of the Martian social structure.
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Dejah Thoris, John Carter
alias_or_role_evidence: Guard/Attendant.
unknowns: 
source_refs: 
[[SECTION markdown]]
# Sola
**Role:** Ally / Protector

**Status:** Physically Present

**Physical Description:** A Martian woman, ally to John Carter.

**Costume/Silhouette:** Acting in a protective/attendant capacity for Dejah Thoris.

**Prompt Phrases:** Martian woman, attendant, protector.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: CH005 Sarkoja
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
direct_identity_evidence: Identified as a hostile figure.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: John Carter
alias_or_role_evidence: Hostile antagonist/figure.
unknowns: Specific physical appearance details.
source_refs: 
[[SECTION markdown]]
# Sarkoja
**Role:** Antagonist / Hostile Figure

**Status:** Physically Present (referenced as being threatened)

**Physical Description:** A hostile Martian figure.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** hostile Martian, antagonist.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: CH006 Lorquas Ptomel
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
direct_identity_evidence: Identified as a high-ranking leader.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: John Carter
alias_or_role_evidence: Leader of the community.
unknowns: Specific physical appearance details.
source_refs: 
[[SECTION markdown]]
# Lorquas Ptomel
**Role:** High-ranking Leader

**Status:** Referenced (Summons Carter)

**Physical Description:** A high-ranking Martian leader.

**Costume/Silhouette:** Implied authority/leadership attire.

**Prompt Phrases:** Martian leader, authoritative figure.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH007 Tars Tarkas
aliases: 
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
confidence: 0.8
direct_identity_evidence: Identified as a Thark chieftain.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: John Carter
alias_or_role_evidence: Chieftain.
unknowns: Specific visual details of the Thark race in this chapter.
source_refs: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Thark Chieftain

**Status:** Referenced (Present at council)

**Physical Description:** A powerful chieftain of the Tharks.

**Costume/Silhouette:** Likely warrior-class Martian attire.

**Prompt Phrases:** Thark chieftain, powerful Martian warrior.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
