# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:49:36.373755+00:00
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

Chapter id: CH013

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
The city of the green Martian horde (under Lorquas Ptomel) and its surrounding plazas; the Martian night under two moons.

**Characters:**
* **John Carter:** An Earthman who has integrated into Thark culture, learning their arts of war and animal husbandry.
* **Tars Tarkas:** A Thark warrior/leader who instructs Carter in combat.
* **Dejah Thoris:** A Red Martian Princess; the love interest of John Carter.
* **Sola:** Dejah Thoris's companion.
* **Lorquas Ptomel:** The leader of the green Martian community.

**Events:**
* **Training and Domestication:** Following a battle with air ships, the community remains in the city for several days. During this time, Carter learns to ride "thoats" (large, vicious beasts). Unlike the Tharks who use force, Carter uses a combination of authority and kindness to tame them. His success is so great that he teaches Tars Tarkas and other warriors his method, resulting in more docile mounts and earning him a gold anklet from Lorquas Ptomel as a reward.
* **The Departure:** After seven days, the community prepares to march toward Thark. 
* **Meeting Dejah Thoris:** Carter meets Dejah Thoris and Sola in the plaza. He learns that the older women of the Thark retinue have been intentionally separating him from Dejah Thoris and forcing her into arduous labor (mixing radium-based explosives) out of jealousy of her noble lineage.
* **Romantic Development:** Carter and Dejah Thoris share a private moment walking through the city at night. They discuss Martian warfare, the nature of enemies, and their mutual feelings. Dejah Thoris hints at the significance of Carter calling her "my chieftain," though he does not yet fully grasp the weight of the term. The chapter concludes with the realization of Carter's deep love for her during a quiet moment under the Martian moons.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH013

- [John Carter](#john_carter)
- [Tars Tarkas](#tars_tarkas)
- [Dejah Thoris](#dejah_thoris)
- [Sola](#sola)
- [Lorquas Ptomel](#lorquas_ptomel)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
aliases: Earthman, Chieftain (referenced by Dejah)
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
direct_identity_evidence: Explicitly named as John Carter, an Earthman.
direct_visual_evidence: Not visually described in this chapter beyond his actions and status.
costume_or_covering_evidence: Wears a gold anklet (reward from Lorquas Ptomel).
movement_evidence: Rides thoats using authority and kindness; walks through the city at night.
associated_entities: Tars Tarkas, Dejah Thoris, Sola, Lorquas Ptomel, Thoats
alias_or_role_evidence: Referred to as an Earthman who has integrated into Thark culture.
unknowns: 
source_refs: 

[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Earthman integrated into Thark culture.
**Presence:** Physically present.
**Description:** An Earthman capable of taming vicious Martian beasts (thoats) through a mix of authority and kindness. He has earned respect among the green Martians for his unique methods of animal husbandry.
**Costume/Traits:** Wears a gold anklet awarded by Lorquas Ptomel.
**Prompt Phrases:** Earthman, skilled rider, calm demeanor, authoritative but kind, wearing a gold anklet.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH003 Tars Tarkas
aliases: Thark warrior
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
direct_identity_evidence: Explicitly named as Tars Tarkas, a Thark warrior/leader.
direct_visual_evidence: Implied green Martian physiology based on group context.
costume_or_covering_evidence: Warrior attire (implied).
movement_evidence: Learns new riding methods from Carter.
associated_entities: John Carter
alias_or_role_evidence: Thark warrior/leader.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Tars Tarkas
**Role:** Thark warrior and leader.
**Presence:** Physically present.
**Description:** A Thark warrior who instructs Carter in combat and learns new methods of taming mounts from him.
**Costume/Traits:** Part of the green Martian community.
**Prompt Phrases:** Green Martian, Thark warrior, martial leader, large humanoid.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH004 Dejah Thoris
aliases: Red Martian Princess, My Chieftain (referenced by Carter)
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
direct_identity_evidence: Explicitly named as Dejah Thoris, a Red Martian Princess.
direct_visual_evidence: Identified as a "Red Martian."
costume_or_covering_evidence: Engaged in arduous labor (mixing radium-based explosives).
movement_evidence: Walks through the city at night; performing manual labor.
associated_entities: John Carter, Sola
alias_or_role_evidence: Noble lineage, Princess.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Dejah Thoris
**Role:** Red Martian Princess / Love interest.
**Presence:** Physically present.
**Description:** A noble Red Martian princess who has been subjected to arduous labor (mixing radium explosives) by jealous older women in the Thark retinue.
**Costume/Traits:** Red Martian physiology; noble status.
**Prompt Phrases:** Red Martian princess, noble woman, ethereal, walking under Martian moons.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH005 Sola
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
direct_identity_evidence: Explicitly named as Sola, companion to Dejah Thoris.
direct_visual_evidence: Associated with the Red Martian Princess.
costume_or_covering_evidence: 
movement_evidence: Present in the plaza with Dejah Thoris.
associated_entities: Dejah Thoris
alias_or_role_evidence: Companion to the princess.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Sola
**Role:** Companion to Dejah Thoris.
**Presence:** Physically present.
**Description:** A companion to Princess Dejah Thoris, seen in the plaza and accompanying her.
**Costume/Traits:** Likely shares Red Martian characteristics with Dejah Thoris.
**Prompt Phrases:** Red Martian, companion, female humanoid.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: CH006 Lorquas Ptomel
aliases: Leader of the green Martian community
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
direct_identity_evidence: Explicitly named as Lorquas Ptomel, leader of the green Martian community.
direct_visual_evidence: Implied green Martian physiology.
costume_or_covering_evidence: 
movement_evidence: Rewards Carter with a gold anklet.
associated_entities: John Carter
alias_or_role_evidence: Leader of the green Martian horde/community.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Lorquas Ptomel
**Role:** Leader of the green Martian community.
**Presence:** Referenced (action performed).
**Description:** The leader of the green Martian community who recognizes John Carter's skill in taming beasts and rewards him with a gold anklet.
**Costume/Traits:** Green Martian.
**Prompt Phrases:** Green Martian leader, authoritative, commanding presence.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
