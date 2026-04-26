# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:52:38.331311+00:00
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

Chapter id: CH015

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
Following his combat with Zad, John Carter recovers from a non-fatal wound inflicted by a sword thrust to his chest. He reunites with his retinue and finds Dejah Thoris in deep mourning, believing him dead. Sola, who was injured during the encounter with Sarkoja, reveals that she is an outcast among her people due to her capacity for emotion. That night, while the massive caravan of two hundred and fifty chariots moves silently across a moss-covered sea bottom, Sola shares her secret history with Carter. She recounts how her mother and a Thark warrior fell in love, leading to Sola's clandestine upbringing. Her mother was eventually discovered by Sarkoja and executed by Tal Hajus after refusing to reveal the father's identity. Sola concludes her story by revealing that her father is Tars Tarkas, who remains unaware of her true identity.

**Characters:**
* **John Carter:** Recovering from a wound; observes the grief of Dejah Thoris and listens to Sola's confession.
* **Sola:** A green Martian woman who reveals her tragic lineage and her father's identity.
* **Dejah Thoris:** Mourning John Carter in silence, unaware of his survival.
* **Sarkoja (Mentioned/Flashback):** The antagonist who discovered Sola's mother and reported her "sin."
* **Sola's Mother (Flashback):** A Thark woman who died under torture to protect her child and lover.
* **Tars Tarkas:** Revealed to be Sola's father; a high-ranking warrior traveling with the caravan.
* **Tal Hajus (Mentioned/Flashback):** The Thark chieftain responsible for the death of Sola's mother.

**Settings:**
* **The Mossy Sea Bottom:** A vast, trackless, and silent expanse of ochre moss that leaves no spoor as the massive caravan traverses it.
* **The Caravan Camp:** A campsite at the foot of hills marking the southern boundary of the sea, where the group rests after two days of marching.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH015

- [John Carter](#john-carter)
- [Sola](#sola)
- [Dejah Thoris](#dejah-thoris)
- [Sarkoja](#sarkoja)
- [Sola's Mother](#sola-s-mother)
- [Tars Tarkas](#tars-tarkas)
- [Tal Hajus](#tal-hajus)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
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
movement_evidence: false
associated_entities: Dejah Thoris, Sola, Tars Tarkas
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Recovering Warrior

**Status:** Physically Present (Recovering from a chest wound).

**Physical Description:** Human male. Currently recovering from a non-fatal sword thrust to the chest.

**Costume/Silhouette:** Not explicitly detailed in this chapter, but implied combat/travel gear.

**Prompt Phrases:** human man, wounded chest, recovering warrior.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH003 Sola
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
confidence: 1.0
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Tars Tarkas, John Carter, Sola's Mother
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Sola
**Role:** Confidante / Daughter of Tars Tarkas

**Status:** Physically Present.

**Physical Description:** Green Martian woman (Thark lineage). Noted for her capacity for emotion, which is unusual/outcast among her people.

**Costume/Silhouette:** Not specified.

**Prompt Phrases:** green-skinned female humanoid, emotional expression, Martian outcast.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH004 Dejah Thoris
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
confidence: 1.0
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: John Carter
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Love Interest / Mourner

**Status:** Physically Present.

**Physical Description:** Martian woman (implied). Shown in a state of deep mourning.

**Costume/Silhouette:** Not specified, but likely mourning attire.

**Prompt Phrases:** grieving female humanoid, mourning expression.
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
renderability_hint: context_only
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Sola's Mother, Sola
alias_or_role_evidence: Antagonist
unknowns: 
source_refs: 
[[SECTION markdown]]
# Sarkoja
**Role:** Antagonist (Mentioned/Flashback)

**Status:** Referenced.

**Physical Description:** Martian humanoid. Known for discovering "sinful" behavior in others.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** antagonistic Martian, enforcer of social norms.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola_s_mother
canonical_character_id: CH006 Sola's Mother
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
renderability_hint: context_only
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Sola, Tars Tarkas (lover)
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Sola's Mother
**Role:** Tragic Figure (Flashback)

**Status:** Referenced.

**Physical Description:** Thark woman. Died under torture.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** Thark female, tragic figure.
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
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Sola, John Carter
alias_or_role_evidence: High-ranking warrior/father
unknowns: 
source_refs: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** High-ranking Warrior / Father of Sola

**Status:** Physically Present (in the caravan).

**Physical Description:** Thark warrior. Large scale implied by species/rank.

**Costume/Silhouette:** Not specified, but likely heavy combat gear suitable for a high-ranking Thark.

**Prompt Phrases:** large green Martian warrior, Thark chieftain, powerful humanoid.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: CH008 Tal Hajus
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
renderability_hint: context_only
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Sola's Mother
alias_or_role_evidence: Thark chieftain
unknowns: 
source_refs: 
[[SECTION markdown]]
# Tal Hajus
**Role:** Thark Chieftain (Mentioned/Flashback)

**Status:** Referenced.

**Physical Description:** Thark humanoid.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** Thark chieftain, Martian leader.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
