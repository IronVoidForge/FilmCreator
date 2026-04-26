# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:48:10.560425+00:00
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

**Events:**
John Carter is summoned to an audience with Lorquas Ptomel, the Tharkian leader. Ptomel confronts Carter regarding his ambiguous status as a prisoner who commands respect, and accuses him of plotting an escape with a red Martian prisoner. Ptomel warns that while they are a just people, Carter may be killed in self-defense or if caught attempting to escape. He emphasizes the importance of delivering the red girl (Dejah Thoris) to Tal Hajus. 

Carter realizes that Sarkoja, a powerful female figure within the Thark community, has been spying on him and reporting his words to Ptomel. Fearing for Dejah Thoris's safety at the hands of the brutal Tal Hajus, Carter becomes more determined to escape. Tars Tarkas later approaches Carter and assists him in selecting quarters in a large building near Sola and the other prisoners. Carter chooses a room on the third floor to be closer to Dejah Thoris. He receives his spoils of war—weapons, silks, furs, and food—delivered by the retinues of the chieftains he defeated. Carter organizes these people into a functional unit to manage his new living quarters.

**Characters:**
* **John Carter:** The protagonist; a human/Earthman acting as a Tharkian chieftain.
* **Lorquas Ptomel:** A Tharkian leader who confronts Carter with warnings and accusations.
* **Tars Tarkas:** A respected Thark warrior who treats Carter with professional courtesy and assists him with housing.
* **Sarkoja:** An influential female figure (implied to be the source of the reports against Carter).
* **Dejah Thoris:** The red Martian princess; mentioned as the primary motivation for Carter's escape plans.
* **Tal Hajus:** A brutal and feared leader of the red Martians, described by Sola as a monster.

**Settings:**
* **The Audience Chamber:** Where Carter meets with Lorquas Ptomel.
* **The Plaza/Thark City:** A large area featuring buildings, courtyards, and streets where various warriors and animals are quartered.
* **Carter's New Quarters:** A room on the third floor of a multi-story building overlooking an overgrown central court filled with fountains and statuary.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter 012

| Asset ID | Canonical Name | Role/Status |
| :--- | :--- | :--- |
| john_carter | John Carter | Protagonist / Earthman Chieftain |
| lorquas_ptomel | Lorquas Ptomel | Tharkian Leader |
| tars_tarkas | Tars Tarkas | Thark Warrior |
| sarkoja | Sarkoja | Female Thark Spy/Influencer |
| dejah_thoris | Dejah Thoris | Red Martian Princess (Referenced) |
| tal_hajus | Tal Hajus | Brutal Leader (Referenced) |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: Earthman, Chieftain
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
direct_identity_evidence: "John Carter is the protagonist; an Earthman."
direct_visual_evidence: ""
costume_or_covering_evidence: "Receives spoils of war: weapons, silks, furs."
movement_evidence: ""
associated_entities: Lorquas Ptomel, Tars Tarkas, Dejah Thoris
alias_or_role_evidence: "Acting as a Tharkian chieftain."
unknowns: 
source_refs: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Earthman Chieftain.
**Status:** Physically Present.
**Description:** A human from Earth currently holding status as a Tharkian chieftain. He is characterized by his ability to command respect among the Tharks despite his different nature. 
**Visual Cues:** Likely wearing silks, furs, and carrying weapons acquired from defeated chieftains.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: Lorquas Ptomel
aliases: Tharkian Leader
is_fully_identified: true
manual_description_required: true
manual_description_reason: Specific physical morphology of the Thark species is not detailed in this chapter.
clarification_required: true
clarification_reason: Needs specific visual details for Thark physiology to ensure consistent rendering.
clarification_question: What are the defining physical characteristics of a Thark (e.g., skin color, eye count, limb structure)?
character_type_hint: humanoid_nonhuman
morphology_hint: unknown
scale_hint: large
renderability_hint: renderable
confidence: 0.5
direct_identity_evidence: "Tharkian leader who confronts Carter."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: John Carter, Sarkoja
alias_or_role_evidence: "Leader of the Tharks."
unknowns: Physical appearance.
source_refs: 
[[SECTION markdown]]
# Lorquas Ptomel
**Role:** Tharkian Leader.
**Status:** Physically Present.
**Description:** A high-ranking leader within the Thark community. He is authoritative and confrontational, warning Carter about his status as a prisoner/chieftain.
**Uncertainty Note:** Specific Thark physical traits (morphology) are not described in this text segment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: Thark Warrior
is_fully_identified: true
manual_description_required: true
manual_description_reason: Specific physical morphology of the Thark species is not detailed in this chapter.
clarification_required: true
clarification_reason: Needs specific visual details for Thark physiology.
clarification_question: What are the defining physical characteristics of a Thark?
character_type_hint: humanoid_nonhuman
morphology_hint: unknown
scale_hint: large
renderability_hint: renderable
confidence: 0.5
direct_identity_evidence: "A respected Thark warrior."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: John Carter
alias_or_role_evidence: "Respected warrior; assists Carter with housing."
unknowns: Physical appearance.
source_refs: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Thark Warrior.
**Status:** Physically Present.
**Description:** A respected and professional Thark warrior who shows courtesy to John Carter and assists him in settling into his new quarters.
**Uncertainty Note:** Physical appearance is unknown due to lack of species description in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: Female Thark Spy
is_fully_identified: true
manual_description_required: true
manual_description_reason: Specific physical morphology of the Thark species is not detailed in this chapter.
clarification_required: true
clarification_reason: Needs specific visual details for Thark physiology.
clarification_question: What are the defining physical characteristics of a female Thark?
character_type_hint: humanoid_nonhuman
morphology_hint: unknown
scale_hint: large
renderability_hint: renderable
confidence: 0.5
direct_identity_evidence: "A powerful female figure within the Thark community."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: John Carter, Lorquas Ptomel
alias_or_role_evidence: "Spy/informant for Ptomel."
unknowns: Physical appearance.
source_refs: 
[[SECTION markdown]]
# Sarkoja
**Role:** Influential Female Thark / Spy.
**Status:** Physically Present (implied presence/action).
**Description:** An influential female figure in the Thark community who has been spying on John Carter and reporting his activities to Lorquas Ptomel.
**Uncertainty Note:** Physical appearance is unknown due to lack of species description in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: Red Martian Princess
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
direct_identity_evidence: "The red Martian princess."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: John Carter, Tal Hajus
alias_or_role_evidence: "Primary motivation for Carter's escape."
unknowns: Specific facial features or clothing.
source_refs: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Red Martian Princess.
**Status:** Referenced.
**Description:** A princess of the red Martians and the primary motivation for John Carter's desire to escape Thark captivity.
**Visual Cues:** Described as a "red girl."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: Tal Hajus
aliases: Monster
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: unknown
scale_hint: large
renderability_hint: context_only
confidence: 0.6
direct_identity_evidence: "A brutal and feared leader of the red Martians."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: Dejah Thoris
alias_or_role_evidence: "Described by Sola as a monster."
unknowns: Specific physical appearance.
source_refs: 
[[SECTION markdown]]
# Tal Hajus
**Role:** Brutal Red Martian Leader.
**Status:** Referenced.
**Description:** A feared and brutal leader of the red Martians, characterized by Sola as a "monster." He is a figure of dread for Carter regarding Dejah Thoris's safety.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
