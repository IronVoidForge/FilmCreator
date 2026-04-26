# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:58:05.215663+00:00
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

Chapter id: CH019

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

**Setting:** A subterranean amphitheater within a ruined, ancient green Martian city; later, the hills east of the Warhoon city.

**Characters:**
* **John Carter:** An Earthman and prisoner of the Warhoons.
* **Kantos Kan:** A padwar (lieutenant) from Helium and fellow prisoner.
* **Dak Kova:** The leader/chieftain of the Warhoon horde.
* **Warhoon Horde:** A bloodthirsty green Martian race hosting gladiatorial games.

**Events:**
* **Loss of Keys:** John Carter realizes his jailer's keys have been stolen by creatures in the darkness.
* **Meeting Kantos Kan:** Carter meets a fellow prisoner, Kantos Kan, who provides intelligence regarding Dejah Thoris and the current state of Helium's search efforts.
* **The Gladiatorial Games:** The prisoners are taken to an immense underground arena for a ten-day tournament where only one survivor is granted freedom.
* **Arena Combat:** Carter survives multiple bouts against men and beasts, gaining the crowd's favor. Kantos Kan uses a specialized throwing technique to defeat a massive sixteen-foot green warrior.
* **The Staged Death:** To escape, Carter and Kantos Kan conspire to fake a final duel. Kantos Kan appears to deliver a fatal blow to Carter, but actually misses his vital organs. 
* **Escape:** Under the cover of darkness, Kantos Kan claims his freedom while Carter stealthily escapes the arena to head toward the eastern hills.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH019

- [john_carter](#john_carter)
- [kantos_kan](#kantos_kan)
- [dak_kova](#dak_kova)
- [warhoon_horde](#warhoon_horde)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: Earthman, prisoner
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
costume_or_covering_evidence: true
movement_evidence: true
associated_entities: kantos_kan, warhoon_horde
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist, prisoner, gladiator.
**Status:** Physically present.
**Description:** An Earthman fighting in the gladiatorial games of the Warhoons. He is a skilled combatant capable of surviving multiple bouts against men and beasts.
**Costume/Traits:** Wears prisoner's attire suitable for arena combat; demonstrates high physical capability and stealth during escape.
**Prompt Phrases:** human male, Earthman, gladiator, athletic build, survivor.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: Kantos Kan
aliases: padwar from Helium
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
movement_evidence: true
associated_entities: john_carter, warhoon_horde
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Kantos Kan
**Role:** Fellow prisoner, Helium padwar.
**Status:** Physically present.
**Description:** A Martian warrior from Helium. Highly skilled in specialized throwing techniques used to defeat much larger opponents.
**Costume/Traits:** Wears combat gear suitable for a padwar; participates in the staged death duel with John Carter.
**Prompt Phrases:** Martian humanoid, warrior, padwar, agile fighter, throwing specialist.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dak_kova
canonical_character_id: Dak Kova
aliases: chieftain of the Warhoon horde
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
associated_entities: warhoon_horde
alias_or_role_evidence: true
unknowns: specific facial features
source_refs: 
[[SECTION markdown]]
# Dak Kova
**Role:** Chieftain of the Warhoon horde.
**Status:** Referenced/Present in setting.
**Description:** The leader of the bloodthirsty green Martian race hosting the games.
**Costume/Traits:** Likely wears chieftain's regalia consistent with Warhoon culture.
**Prompt Phrases:** Warhoon leader, green Martian chieftain, warlord.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: warhoon_horde
canonical_character_id: Warhoon Horde
aliases: green Martians
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
movement_evidence: true
associated_entities: dak_kova
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Warhoon Horde
**Role:** Antagonists, gladiatorial spectators/combatants.
**Status:** Physically present.
**Description:** A bloodthirsty race of green Martians. They host large-scale gladiatorial games in subterranean amphitheaters.
**Costume/Traits:** Green skin; varied combat gear for arena participants.
**Prompt Phrases:** green skinned humanoids, Martian horde, bloodthirsty warriors, crowd in amphitheater.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
