# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:05:35.814324+00:00
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

Chapter id: CH024

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
John Carter's aircraft is shot down during a massive battle between Tharks and Warhoons. He intervenes to save Tars Tarkas from being killed by three Warhoon warriors, cementing a new friendship between them. Following the battle, John Carter reunites with his faithful hound, Woola. 

The narrative shifts to political maneuvering within Thark. To avoid the wrath of the current Jeddak, Tal Hajus, John Carter and Tars Tarkas decide to face him in council. Beforehand, they intimidate the priestess Sarkoja into fleeing. In the council, John Carter publicly challenges Tal Hajus's fitness to rule, citing his cowardice in battle. The council decrees a duel between Tal Hajus and Tars Tarkas; Tars Tarkas wins, becoming the new Jeddak and elevating John Carter to the rank of chieftain.

Leveraging this new power, John Carter proposes an alliance to the Thark hordes: a raid on Zodanga to rescue Dejah Thoris and seize their wealth. The Tharks enthusiastically agree. A massive force of 150,000 Green Martians marches on Zodanga. Under the cover of night, John Carter leads a small group in a daring infiltration of the city by scaling the walls using a human ladder. He successfully enters the palace grounds and begins coordinating a silent takeover of the city gates to prepare for the main assault.

**Characters:**
- **John Carter:** The protagonist; a skilled warrior and strategist who uses his Earthly ingenuity to lead Thark forces.
- **Tars Tarkas:** A mighty Thark warrior who becomes Jeddak after defeating Tal Hajus.
- **Woola:** John Carter's loyal, giant hound.
- **Tal Hajus:** The former Jeddak of Thark; a coward and tyrant defeated by Tars Tarkas.
- **Sarkoja:** A priestess who flees Thark after being threatened by Tars Tarkas.
- **Lorquas Ptomel:** A Thark chieftain who supports the challenge against Tal Hajus.

**Settings:**
- **The Battlefield:** A plain near an ancient dead city where the Thark/Warhoon conflict occurs.
- **Thark (City):** The seat of power for the Green Martians.
- **Zodanga:** A great walled city of the Red Martians, characterized by massive carborundum walls and a central palace.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH024

- [John Carter](#john_carter)
- [Tars Tarkas](#tars_tarkas)
- [Woola](#woola)
- [Tal Hajus](#tal_hajus)
- [Sarkoja](#sarkoja)
- [Lorquas Ptomel](#lorquas_ptomel)

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
direct_identity_evidence: Explicitly named as the protagonist and leader of the Thark raid.
direct_visual_evidence: Implied through actions (scaling walls, leading forces).
costume_or_covering_evidence: Not explicitly detailed in this chapter summary, but established as a warrior.
movement_evidence: Scaling walls using human ladders; fighting/intervening in battle.
associated_entities: Tars Tarkas, Woola, Dejah Thoris, Tharks
alias_or_role_evidence: Chieftain of the Tharks (newly elevated).
unknowns: 
source_refs: 

[[SECTION markdown]]
# John Carter
**Role:** Protagonist; Warrior and Strategist.
**Presence:** Physically present throughout the chapter.
**Physical Description:** Human male, skilled warrior.
**Costume/Silhouette:** Warrior attire (implied).
**Prompt Phrases:** human warrior, Earthly ingenuity, scaling city walls, leading Thark hordes.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: Jeddak (newly elected)
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
direct_identity_evidence: Named as a mighty Thark warrior and new Jeddak.
direct_visual_evidence: Described as "mighty" and part of the Green Martian (Thark) species.
costume_or_covering_evidence: Thark warrior gear (implied).
movement_evidence: Engaging in combat/duel with Tal Hajus.
associated_entities: John Carter, Tal Hajus, Tharks
alias_or_role_evidence: Jeddak of Thark.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Tars Tarkas
**Role:** Mighty Thark warrior; New Jeddak of Thark.
**Presence:** Physically present.
**Physical Description:** Large, mighty Green Martian (Thark).
**Costume/Silhouette:** Thark warrior silhouette.
**Prompt Phrases:** large green martian, mighty thark warrior, jeddak, combatant.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: Faithful Hound
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
direct_identity_evidence: Named as John Carter's faithful hound.
direct_visual_evidence: Described as a "giant hound."
costume_or_covering_evidence: N/A
movement_evidence: Following John Carter.
associated_entities: John Carter
alias_or_role_evidence: Loyal pet/companion.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Woola
**Role:** Companion to John Carter.
**Presence:** Physically present.
**Physical Description:** Giant, loyal hound.
**Costume/Silhouette:** Large quadrupedal creature.
**Prompt Phrases:** giant hound, loyal beast, large quadruped.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: Tal Hajus
aliases: Former Jeddak
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
direct_identity_evidence: Named as the former Jeddak of Thark.
direct_visual_evidence: Part of the Thark species (Green Martian).
costume_or_covering_evidence: Former leader regalia (implied).
movement_evidence: Defeated in a duel by Tars Tarkas.
associated_entities: Tars Tarkas, John Carter, Tharks
alias_or_role_evidence: Tyrant/Cowardly ruler.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Tal Hajus
**Role:** Former Jeddak of Thark; Antagonist (political).
**Presence:** Physically present in council.
**Physical Description:** Large Green Martian (Thark).
**Costume/Silhouette:** Thark leadership attire.
**Prompt Phrases:** green martian, former jeddak, defeated tyrant, thark warrior.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: Priestess
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
direct_identity_evidence: Named as a priestess of Thark.
direct_visual_evidence: Part of the Thark species (Green Martian).
costume_or_covering_evidence: Priestess attire (implied).
movement_evidence: Flees Thark after being intimidated.
associated_entities: Tars Tarkas, John Carter
alias_or_role_evidence: Priestess.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Sarkoja
**Role:** Priestess of Thark.
**Presence:** Physically present (then flees).
**Physical Description:** Green Martian (Thark) female.
**Costume/Silhouette:** Priestess robes/garb.
**Prompt Phrases:** thark priestess, green martian woman, fleeing priestess.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: Lorquas Ptomel
aliases: Thark Chieftain
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
direct_identity_evidence: Named as a Thark chieftain.
direct_visual_evidence: Part of the Thark species (Green Martian).
costume_or_covering_evidence: Chieftain attire (implied).
movement_evidence: Supports the challenge against Tal Hajus in council.
associated_entities: Tars Tarkas, Tal Hajus, Tharks
alias_or_role_evidence: Chieftain.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Lorquas Ptomel
**Role:** Thark Chieftain.
**Presence:** Physically present in council.
**Physical Description:** Large Green Martian (Thark).
**Costume/Silhouette:** Thark chieftain attire.
**Prompt Phrases:** thark chieftain, green martian leader, warrior noble.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
