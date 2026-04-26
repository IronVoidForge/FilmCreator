# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:54:02.229138+00:00
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

Chapter id: CH016

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
After a twenty-day journey across Martian sea bottoms and canals, John Carter and his companions arrive at the great city of Thark. Upon arrival, Carter is assigned a large building in the city plaza. He reunites with Dejah Thoris and Sola, during which he formally declares his devotion to Dejah Thoris and commands her cooperation in planning an escape. Sola reveals that the priest Sarkoja has influenced Tal Hajus to sentence Dejah Thoris to death in the upcoming games. 

The trio plans a midnight escape via a northern waterway to avoid detection. Carter successfully sneaks out of the city with his thoats, but upon reaching the rendezvous point, he discovers that the plan has been compromised. Realizing the women have likely been intercepted, Carter maneuvers through the city's inner courts and uses his agility to climb into Dejah Thoris's quarters. There, he overhears a Thark chieftain instructing warriors to ambush him and imprison him in the vaults once he returns to the apartment, noting that Dejah Thoris is already in the custody of Tal Hajus.

**Characters:**
* **John Carter:** A warrior and Earthman; driven by his love for Dejah Thoris; demonstrates tactical thinking and physical prowess.
* **Dejah Thoris:** A captive princess of Helium; agrees to cooperate with Carter's escape plan.
* **Sola:** A Thark woman who harbors resentment toward her people's customs; joins the escape plot.
* **Woola:** John Carter's loyal, multi-tusked Martian hound.
* **Thark Chieftain:** An unnamed leader who orchestrates the ambush of John Carter.
* **Tal Hajus (Mentioned):** The Jeddak of Thark, who holds Dejah Thoris captive.
* **Sarkoja (Mentioned):** A powerful priest whose influence has doomed the captives.

**Settings:**
* **The Road to Thark:** A landscape of ruined cities, Martian canals, and cultivated fields with enormous trees.
* **Thark:** A massive ancient city inhabited by green Martians, characterized by grand architecture and large communal plazas.
* **Dejah Thoris's Quarters:** A large, multi-story building in the Thark plaza featuring marble floors and winding stairways.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH016

- [John Carter](#john_carter)
- [Dejah Thoris](#dejah_thoris)
- [Sola](#sola)
- [Woola](#woola)
- [Thark Chieftain](#thark_chieftain)
- [Tal Hajus](#tal_hajus)
- [Sarkoja](#sarkoja)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
aliases: Earthman, Warrior
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
associated_entities: Dejah Thoris, Sola, Woola
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Warrior
**Presence:** Physically Present
**Description:** An Earthman characterized by extreme physical prowess and agility. He is capable of climbing multi-story buildings with ease.
**Traits:** Tactical, driven, highly mobile.
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
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: John Carter, Sola, Tal Hajus
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess / Captive
**Presence:** Physically Present
**Description:** A princess of Helium currently held in custody by the Tharks.
**Traits:** Cooperative, high-status captive.
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
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Dejah Thoris, John Carter
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Sola
**Role:** Thark Woman / Ally
**Presence:** Physically Present
**Description:** A woman of the Thark people who harbors resentment toward her culture's customs.
**Traits:** Rebellious, conspiratorial.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: CH005 Woola
aliases: Martian Hound
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: quadruped
scale_hint: large
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: John Carter
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Woola
**Role:** Loyal Companion
**Presence:** Physically Present
**Description:** A loyal Martian hound characterized by having multiple tusks.
**Traits:** Canine-like, multi-tusked, large scale.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: thark_chieftain
canonical_character_id: UNKNOWN Thark Chieftain
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No specific physical description provided beyond role and species.
clarification_required: true
clarification_reason: Physical appearance is not detailed in the text.
clarification_question: What are the visual characteristics of the Thark Chieftain?
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Thark warriors
alias_or_role_evidence: true
unknowns: Physical appearance, specific features.
source_refs: 
[[SECTION markdown]]
# Thark Chieftain
**Role:** Antagonist / Leader
**Presence:** Physically Present (heard/observed)
**Description:** An unnamed leader of the Tharks who orchestrates an ambush against John Carter.
**Uncertainty Note:** Physical appearance is unknown; only his role and authority are established.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: UNKNOWN Tal Hajus
aliases: Jeddak of Thark
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character is only mentioned/referenced; no physical description provided.
clarification_required: true
clarification_reason: No visual data available in text.
clarification_question: What does Tal Hajus look like?
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.4
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Dejah Thoris, Sarkoja
alias_or_role_evidence: true
unknowns: Physical appearance.
source_refs: 
[[SECTION markdown]]
# Tal Hajus
**Role:** Jeddak of Thark (Mentioned)
**Presence:** Referenced
**Description:** The ruler of Thark who has sentenced Dejah Thoris to death in the games.
**Uncertainty Note:** No physical description is provided in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: UNKNOWN Sarkoja
aliases: Priest
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character is only mentioned/referenced; no physical description provided.
clarification_required: true
clarification_reason: No visual data available in text.
clarification_question: What are the visual characteristics of Sarkoja?
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.4
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Tal Hajus
alias_or_role_evidence: true
unknowns: Physical appearance.
source_refs: 
[[SECTION markdown]]
# Sarkoja
**Role:** Priest (Mentioned)
**Presence:** Referenced
**Description:** A powerful priest whose influence has manipulated the political situation in Thark.
**Uncertainty Note:** No physical description is provided in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
