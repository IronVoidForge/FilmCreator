# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:45:20.095800+00:00
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

Chapter id: CH010

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

**Setting:** The city of the Tharks (Green Men) and the audience chamber of Lorquas Ptomel.

**Characters:**
- **John Carter:** An Earthman from Virginia, now possessing the status of a Martian chieftain through combat.
- **Woola:** A large, loyal Martian hound who has formed a deep bond with Carter.
- **Dejah Thoris:** The captive Princess of Helium, characterized by her grace and intelligence.
- **Tars Tarkas:** A Thark warrior/leader who observes Carter with curiosity and respect.
- **Lorquas Ptomel:** A Thark chieftain presiding over the council.
- **Sola:** A kind Martian woman (an "atavism") who has been teaching Carter the Martian language.
- **Sarkoja:** A cruel Green Martian woman guarding the prisoner.

**Events:**
- **Bonding with Woola:** Early in the morning, Carter tests his bond with Woola by using affection to overcome the creature's instinctual duty to keep him confined. He successfully establishes himself as Woola's undisputed master.
- **The Audience Chamber:** Carter observes a trial where Dejah Thoris defends her people's role in maintaining Mars' atmosphere against the "brutal" Green Men. Her plea for amity momentarily touches the Thark council, including Tars Tarkas.
- **The Outburst of Violence:** A young Thark warrior breaks the tension by striking Dejah Thoris across the face. Infuriated, John Carter intervenes, engaging the twelve-foot warrior in combat and killing him.
- **Ascension to Chieftaincy:** By killing the warrior, Carter inadvertently wins the "spoils" of the deceased, including regalia and weapons. Under Martian custom, he is now recognized as a Thark chieftain.
- **Confrontation with Tars Tarkas:** Tars Tarkas questions Carter's sudden mastery of the language and warns him of the responsibilities and dangers of his new status. Carter asserts his moral code, declaring that he will protect Dejah Thoris from any further insult or injury.
- **Departure:** Recognized as a conqueror/chieftain, Carter escorts Dejah Thoris out of the audience chamber, accompanied by Woola.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH010

- [John Carter](#john_carter)
- [Woola](#woola)
- [Dejah Thoris](#dejah_thoris)
- [Tars Tarkas](#tars_tarkas)
- [Lorquas Ptomel](#lorquas_ptomel)
- [Sola](#sola)
- [Sarkoja](#sarkoja)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
aliases: Earthman, Martian Chieftain
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
direct_identity_evidence: Explicitly named as John Carter, an Earthman from Virginia.
direct_visual_evidence: Implied presence through combat and movement.
costume_or_covering_evidence: Wears the regalia/spoils of a deceased Thark warrior after combat.
movement_evidence: Engages in combat with a twelve-foot warrior; escorts Dejah Thoris.
associated_entities: Woola, Dejah Thoris, Tars Tarkas
alias_or_role_evidence: Recognized as a Martian chieftain through combat.
unknowns: 
source_refs: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / New Thark Chieftain
**Status:** Physically Present
**Description:** An Earthman from Virginia who has adapted to Mars. He possesses superior strength/combat skills, capable of killing a twelve-foot Thark warrior.
**Costume/Traits:** Currently wearing the regalia and weapons acquired from a fallen Thark warrior.
**Prompt Phrases:** Human male, Earthman, combatant, Martian chieftain regalia, assertive posture.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: CH003 Woola
aliases: Martian hound
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
confidence: 0.9
direct_identity_evidence: Explicitly named as Woola, a Martian hound.
direct_visual_evidence: Described as a large Martian hound.
costume_or_covering_evidence: 
movement_evidence: Forms a deep bond with Carter; follows him.
associated_entities: John Carter
alias_or_role_evidence: Loyal companion/hound.
unknowns: 
source_refs: 
[[SECTION markdown]]
# Woola
**Role:** Companion
**Status:** Physically Present
**Description:** A large, loyal Martian hound with a deep bond to John Carter.
**Costume/Traits:** Large quadrupedal creature.
**Prompt Phrases:** Large Martian hound, loyal beast, quadruped, alien canine.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH004 Dejah Thoris
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
confidence: 0.8
direct_identity_evidence: Explicitly named as Dejah Thoris, Princess of Helium.
direct_visual_evidence: Described as having grace and intelligence; subject to an assault.
costume_or_covering_evidence: Captive status implies specific attire/restraint.
movement_evidence: Defends her people in council; escorted out by Carter.
associated_entities: John Carter, Tars Tarkas
alias_or_role_evidence: Princess of Helium.
unknowns: 
source_refs: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Captive Princess
**Status:** Physically Present
**Description:** The Princess of Helium, noted for her grace and intelligence. She is a captive during the council.
**Costume/Traits:** Graceful silhouette, captive status.
**Prompt Phrases:** Graceful princess, humanoid female, intelligent expression, captive.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH005 Tars Tarkas
aliases: Thark warrior
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
direct_identity_evidence: Explicitly named as Tars Tarkas.
direct_visual_evidence: Observed to be a Thark warrior/leader.
costume_or_covering_evidence: Warrior attire implied.
movement_evidence: Observes Carter with curiosity and respect; questions him.
associated_entities: John Carter, Lorquas Ptomel
alias_or_role_evidence: Thark leader/warrior.
unknowns: 
source_refs: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Thark Leader
**Status:** Physically Present
**Description:** A Thark warrior and leader who observes John Carter with respect and curiosity.
**Costume/Traits:** Large humanoid, Green Man (Thark).
**Prompt Phrases:** Large green humanoid, Thark warrior, imposing presence, Martian leader.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: CH006 Lorquas Ptomel
aliases: Thark chieftain
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
confidence: 0.7
direct_identity_evidence: Explicitly named as Lorquas Ptomel.
direct_visual_evidence: Presiding over the council in the audience chamber.
costume_or_covering_evidence: Chieftain regalia implied.
movement_evidence: Presides over the trial/council.
associated_entities: Tars Tarkas
alias_or_role_evidence: Thark chieftain.
unknowns: 
source_refs: 
[[SECTION markdown]]
# Lorquas Ptomel
**Role:** Council Presider
**Status:** Physically Present
**Description:** A Thark chieftain presiding over the council in the audience chamber.
**Costume/Traits:** Large green humanoid, chieftain status.
**Prompt Phrases:** Green Martian chieftain, presiding authority, large humanoid.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH007 Sola
aliases: Martian woman, atavism
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
direct_identity_evidence: Explicitly named as Sola.
direct_visual_evidence: Described as a kind Martian woman ("atavism").
costume_or_covering_evidence: 
movement_evidence: Has been teaching Carter the language.
associated_entities: John Carter
alias_or_role_evidence: Teacher of Martian language.
unknowns: 
source_refs: 
[[SECTION markdown]]
# Sola
**Role:** Teacher/Companion
**Status:** Referenced
**Description:** A kind Martian woman, referred to as an "atavism," who has been teaching John Carter the Martian language.
**Costume/Traits:** Humanoid female (Martian).
**Prompt Phrases:** Kind Martian woman, humanoid female, atavism.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: CH008 Sarkoja
aliases: Green Martian woman
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
direct_identity_evidence: Explicitly named as Sarkoja.
direct_visual_evidence: Described as a cruel Green Martian woman.
costume_or_covering_evidence: Guarding the prisoner.
movement_evidence: Guarding Dejah Thoris.
associated_entities: Dejah Thoris
alias_or_role_evidence: Guard.
unknowns: 
source_refs: 
[[SECTION markdown]]
# Sarkoja
**Role:** Guard
**Status:** Physically Present
**Description:** A cruel Green Martian woman tasked with guarding the prisoner (Dejah Thoris).
**Costume/Traits:** Green humanoid, female.
**Prompt Phrases:** Cruel green Martian woman, guard, humanoid female.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
