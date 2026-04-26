# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:04:05.291834+00:00
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

Chapter id: CH023

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

**Summary:**
Following the news that Princess Dejah Thoris has been promised to Sab Than of Zodanga, John Carter meets secretly with Kantos Kan. The two devise a plan to separate: Kantos Kan will infiltrate the Zodanga palace via a secret entrance in the high tower to assassinate Sab Than, while John Carter will attempt to fly to Helium.

To reach the machine sheds, John Carter performs a perilous climb up the exterior of the massive Zodanga barracks and uses a grappling hook to swing onto the roof. After subduing a sentry and hanging him over the edge to delay discovery, Carter retrieves two air machines. During their departure, they are intercepted by Zodangan air patrols. Kantos Kan dives into darkness to evade capture, while Carter engages in a high-speed chase through the Martian sky. 

Despite using a specialized Heliumite gearing trick to increase his speed, Carter's machine is struck by a projectile from a cruiser. He survives a near-fatal plunge but emerges to find his compass and speedometer destroyed. Lost and flying blindly toward what he hopes is Helium, Carter spends hours traversing the Martian landscape, eventually realizing he has missed his destination and is lost over an unfamiliar territory.

**Characters:**
* **John Carter:** An adventurer attempting to reach Helium after a narrow escape from Zodangan pursuit.
* **Kantos Kan:** A Heliumite air-scout who vows to kill Sab Than to avenge the Princess and support Carter.
* **Sab Than (Mentioned):** The ruler of Zodanga to whom Dejah Thoris is promised.
* **Dejah Thoris (Mentioned):** The Princess of Helium.
* **Zodangan Sentry:** A guard on the barracks roof who is incapacitated by Carter.

**Settings:**
* **Zodanga:** A large, heavily guarded city characterized by high-rise architecture and air patrols.
* **The Barracks:** An enormous building in Zodanga, a thousand feet high, housing the air-scout squadron.
* **The Martian Sky:** The setting for the aerial pursuit and Carter's subsequent flight.
* **Dead Sea Bottom/Unidentified Cities:** The vast, desolate landscape Carter traverses while lost.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [John Carter](#john-carter)
- [Kantos Kan](#kantos-kan)
- [Sab Than](#sab-than)
- [Dejah Thoris](#dejah-thoris)
- [Zodangan Sentry](#zodangan-sentry)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: Carter
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
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: Kantos Kan, Dejah Thoris, Sab Than
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Adventurer

**Status:** Physically Present

**Description:** An adventurer currently operating an air machine. He is capable of extreme physical feats, including climbing a thousand-foot barracks and engaging in high-speed aerial combat.

**Notes:** Currently flying solo after a pursuit; his navigation equipment (compass/speedometer) has been destroyed.
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
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: John Carter, Sab Than
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Kantos Kan
**Role:** Heliumite Air-Scout / Assassin

**Status:** Physically Present

**Description:** A Heliumite scout who specializes in aerial maneuvers. He is motivated by vengeance against Sab Than.

**Notes:** Involved in a stealth infiltration mission via the Zodanga high tower.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sab_than
canonical_character_id: Sab Than
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
confidence: 0.5
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Dejah Thoris, Kantos Kan
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Sab Than
**Role:** Ruler of Zodanga

**Status:** Referenced

**Description:** The ruler of Zodanga who has been promised the hand of Princess Dejah Thoris. He is the target of Kantos Kan's assassination plot.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: Princess Dejah Thoris
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
confidence: 0.5
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Sab Than, John Carter
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess of Helium

**Status:** Referenced

**Description:** The Princess of Helium who has been promised to Sab Than of Zodanga.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: zodangan_sentry
canonical_character_id: Zodangan Sentry
aliases: Guard
is_fully_identified: false
manual_description_required: true
manual_description_reason: No specific physical description or uniform details provided beyond being a guard.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: 
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Zodangan Sentry
**Role:** Guard

**Status:** Physically Present (Incapacitated)

**Description:** A guard stationed on the roof of the Zodanga barracks. He was subdued by John Carter and hung over the edge of the building to prevent discovery.

**Uncertainty Note:** Specific physical appearance, race, or uniform details are not provided in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
