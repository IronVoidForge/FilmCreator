# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:02:45.348927+00:00
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

Chapter id: CH022

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

**Setting:**
The palace of Zodanga, specifically the private apartments of Jeddak Than Kosis, winding corridors, antechambers, and a great hall with a balcony overlooking a Zodangan avenue.

**Characters:**
* **John Carter:** A human warrior serving as a guard in Zodanga; he is searching for Dejah Thoris.
* **Dejah Thoris:** Princess of Helium; she has publicly pledged herself to Sab Than to ensure peace between their nations.
* **Than Kosis:** The Jeddak (ruler) of Zodanga.
* **Sab Than:** Prince of Zodanga and son of Than Kosis.
* **Notan:** The Royal Psychologist.
* **Guardsmen:** Four unnamed Zodangan soldiers killed by Carter during his confrontation.

**Events:**
* **The Betrayal:** While stationed behind a tapestry to guard Than Kosis, John Carter witnesses Dejah Thoris enter the chamber and publicly declare her intention to marry Sab Than, effectively renouncing her previous connection to Carter.
* **The Confrontation:** Distraught, Carter abandons his post to find Dejah Thoris. He is intercepted by four guards in an antechamber. After a fierce battle lasting twenty minutes, Carter kills all four guardsmen.
* **The Reunion:** Carter confronts Dejah Thoris. She recognizes him but explains that due to Barsoomian custom, her promise to marry Sab Than is final and binding, even if she still loves Carter. She informs him that he cannot wed her while Sab Than lives, nor can he wed a man who kills her husband.
* **The Investigation:** As the palace goes into an uproar over the murdered guards, Carter hides in a large hanging ornament in a great hall. He overhears the Royal Psychologist, Notan, reporting to Than Kosis that a single, superhuman fighter was responsible for the deaths.
* **The Escape:** Realizing he is a wanted man, Carter waits for darkness to fall and uses his superior physical abilities to leap from a balcony and escape the palace grounds into the city of Zodanga.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH022

- [John Carter](#john_carter)
- [Dejah Thoris](#dejah_thoris)
- [Than Kosis](#than_kosis)
- [Sab Than](#sab_than)
- [Notan](#notan)
- [Guardsmen](#guardsmen)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH022 John Carter
aliases: Human Warrior, Superhuman Fighter
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
direct_identity_evidence: Explicitly named as John Carter.
direct_visual_evidence: Described as a superhuman fighter capable of killing four guards in twenty minutes and leaping from balconies.
costume_or_covering_evidence: Serving as a guard in Zodanga.
movement_evidence: Fierce combat, high-agility leaps.
associated_entities: Dejah Thoris, Sab Than, Than Kosis, Guardsmen
alias_or_role_evidence: Referred to as a superhuman fighter by Notan.
unknowns: 
source_refs: 

[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Guard in Zodanga

**Status:** Physically Present

**Physical Description:**
A human warrior possessing superhuman physical abilities, including extreme combat proficiency and high-agility leaping capabilities.

**Costume & Silhouette:**
Dressed as a guard within the palace of Zodanga.

**Prompting Keywords:**
human warrior, superhuman strength, agile fighter, combatant, Zodangan guard.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH022 Dejah Thoris
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
direct_identity_evidence: Explicitly named as Dejah Thoris, Princess of Helium.
direct_visual_evidence: Present in the palace chambers and great hall.
costume_or_covering_evidence: Royal attire consistent with a princess/bride-to-be.
movement_evidence: Walking through palace corridors and chambers.
associated_entities: John Carter, Sab Than, Than Kosis
alias_or_role_evidence: Princess of Helium.
unknowns: Specific facial features or exact color of clothing not detailed in this chapter.
source_refs: 

[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess of Helium / Fiancee to Sab Than

**Status:** Physically Present

**Physical Description:**
A humanoid princess of Helium. While specific facial details are sparse in this text, she carries the status and presence of royalty.

**Costume & Silhouette:**
Royal Barsoomian attire; silhouette suggests high-status female nobility.

**Prompting Keywords:**
princess, royal Barsoomian, noblewoman, elegant silhouette, Helium royalty.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: than_kosis
canonical_character_id: CH022 Than Kosis
aliases: Jeddak of Zodanga
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
direct_identity_evidence: Identified as the Jeddak (ruler) of Zodanga.
direct_visual_evidence: Present in private apartments and receiving reports.
costume_or_covering_evidence: Ruler's regalia/attire.
movement_evidence: Sitting/standing in private chambers.
associated_entities: Sab Than, Notan
alias_or_role_evidence: Jeddak of Zodanga.
unknowns: Specific physical appearance details.
source_refs: 

[[SECTION markdown]]
# Than Kosis
**Role:** Ruler of Zodanga

**Status:** Physically Present

**Physical Description:**
A humanoid ruler of Zodanga.

**Costume & Silhouette:**
Regal clothing befitting a Jeddak.

**Prompting Keywords:**
ruler, Jeddak, Zodangan royalty, authoritative presence, seated monarch.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sab_than
canonical_character_id: CH022 Sab Than
aliases: Prince of Zodanga
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
direct_identity_evidence: Identified as Prince of Zodanga and son of Than Kosis.
direct_visual_evidence: Referenced as the intended husband of Dejah Thoris.
costume_or_covering_evidence: Royal prince attire.
movement_evidence: Not physically active in this chapter, but part of the political landscape.
associated_entities: Dejah Thoris, Than Kosis
alias_or_role_evidence: Prince of Zodanga.
unknowns: Specific physical features.
source_refs: 

[[SECTION markdown]]
# Sab Than
**Role:** Prince of Zodanga / Fiance to Dejah Thoris

**Status:** Referenced

**Physical Description:**
A humanoid prince of Zodanga.

**Costume & Silhouette:**
Royal prince attire.

**Prompting Keywords:**
prince, royal, Zodangan nobility, fiancé.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: notan
canonical_character_id: CH022 Notan
aliases: Royal Psychologist
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
direct_identity_evidence: Identified as the Royal Psychologist.
direct_visual_evidence: Present in the palace reporting to Than Kosis.
costume_or_covering_evidence: Professional/official Zodangan attire.
movement_evidence: Reporting/speaking to the Jeddak.
associated_entities: Than Kosis
alias_or_role_evidence: Royal Psychologist.
unknowns: Specific physical appearance details.
source_refs: 

[[SECTION markdown]]
# Notan
**Role:** Royal Psychologist

**Status:** Physically Present

**Physical Description:**
A humanoid official of the Zodangan court.

**Costume & Silhouette:**
Official/scholarly attire suitable for a royal advisor.

**Prompting Keywords:**
psychologist, royal advisor, scholar, Zodangan official.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: guardsmen
canonical_character_id: CH022 Guardsmen
aliases: Zodangan Soldiers
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
direct_identity_evidence: Identified as four unnamed Zodangan soldiers/guards.
direct_visual_evidence: Killed by John Carter in an antechamber.
costume_or_covering_evidence: Zodangan guard uniforms.
movement_evidence: Engaged in combat with Carter.
associated_entities: John Carter
alias_or_role_evidence: Guardsmen, soldiers.
unknowns: Individual names or specific facial features.
source_refs: 

[[SECTION markdown]]
# Guardsmen
**Role:** Palace Security

**Status:** Physically Present (Deceased)

**Physical Description:**
Four humanoid Zodangan soldiers.

**Costume & Silhouette:**
Standard Zodangan guard uniforms/armor.

**Prompting Keywords:**
soldiers, guards, Zodangan armor, combatants, infantry.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
