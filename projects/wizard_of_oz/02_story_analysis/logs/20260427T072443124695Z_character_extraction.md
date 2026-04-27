# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:24:43.124695+00:00
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
Project slug: wizard_of_oz

Chapter id: CH018

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

**Setting:** The Throne Room in the Emerald City.

**Characters:** Dorothy, Scarecrow (now ruler of the Emerald City), Tin Woodman, Cowardly Lion, the Monkey King and his band of Winged Monkeys, and a Soldier with green whiskers.

**Events:**
- Following Oz's departure via balloon, the group mourns his loss; the Tin Woodman is comforted by Dorothy to prevent rusting.
- The Scarecrow, now the official ruler of the Emerald City, convenes a meeting with the travelers in the Throne Room.
- Dorothy expresses her desire to return to Kansas, prompting the Scarecrow to suggest using the Golden Cap to summon the Winged Monkeys for transport.
- The Monkey King appears but refuses to fly Dorothy across the desert, stating that Winged Monkeys are bound to their own country and cannot leave it.
- Seeking an alternative, the group summons a soldier who suggests seeking help from Glinda, the Good Witch of the South, who lives on the edge of the desert.
- The soldier warns that the road south is dangerous, filled with wild beasts and hostile people.
- Despite the risks, Dorothy, the Lion, the Tin Woodman, and the Scarecrow decide to depart for the South the following morning to seek Glinda's aid.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [Dorothy](#dorothy)
- [Scarecrow](#scarecrow)
- [Tin Woodman](#tin_woodman)
- [Cowardly Lion](#cowardly_lion)
- [Monkey King](#monkey_king)
- [Winged Monkeys](#winged_monkeys)
- [Soldier](#soldier)
- [Glinda](#glinda)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dorothy

canonical_character_id: CH001 Dorothy

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

direct_identity_evidence: Presence in the throne room and dialogue regarding her desire to return home.

direct_visual_evidence: 

costume_or_covering_evidence: 

movement_evidence: 

associated_entities: Scarecrow, Tin Woodman, Cowardly Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Description:** A young girl traveling with the Scarecrow, Tin Woodman, and Cowardly Lion. She is currently mourning the departure of Oz and seeking a way back to Kansas.

**Descriptive Phrases:** Young girl, traveler, seeker of Glinda.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: scarecrow

canonical_character_id: CH003 Scarecrow

aliases: Ruler of the Emerald City

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

direct_identity_evidence: Identified as the ruler of the Emerald City convening a meeting.

direct_visual_evidence: 

costume_or_covering_evidence: 

movement_evidence: 

associated_entities: Dorothy, Tin Woodman, Cowardly Lion

alias_or_role_evidence: Ruler of the Emerald City

unknowns: 

source_refs: 

[[SECTION markdown]]

# Scarecrow
**Role:** Ruler of the Emerald City / Companion

**Status:** Physically Present

**Description:** The current official ruler of the Emerald City. He is a companion to Dorothy and suggests using the Golden Cap to solve their transport issues.

**Descriptive Phrases:** Straw-filled humanoid, ruler of the emerald city, decision-maker.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tin_woodman

canonical_character_id: CH004 Tin Woodman

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

direct_identity_evidence: Identified as part of the traveling group.

direct_visual_evidence: Needs comfort from Dorothy to prevent rusting.

costume_or_covering_evidence: Metal/Tin body.

movement_evidence: 

associated_entities: Dorothy, Scarecrow, Cowardly Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Tin Woodman
**Role:** Companion

**Status:** Physically Present

**Description:** A metal/tin humanoid companion to Dorothy. He is susceptible to rusting and requires care from Dorothy.

**Descriptive Phrases:** Tin man, metallic humanoid, rust-prone traveler.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: cowardly_lion

canonical_character_id: CH005 Cowardly Lion

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: quadruped

scale_hint: large

renderability_hint: renderable

confidence: 1.0

direct_identity_evidence: Identified as part of the traveling group.

direct_visual_evidence: 

costume_or_covering_evidence: 

movement_evidence: 

associated_entities: Dorothy, Scarecrow, Tin Woodman

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Cowardly Lion
**Role:** Companion

**Status:** Physically Present

**Description:** A large animal companion traveling with Dorothy and the others.

**Descriptive Phrases:** Large lion, traveling beast.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: monkey_king

canonical_character_id: CH006 Monkey King

aliases: 

is_fully_identified: true

manual_description_required: true

manual_description_reason: Specific physical appearance of the king (beyond being a monkey) is not detailed.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: quadruped

scale_hint: small

renderability_hint: renderable

confidence: 0.7

direct_identity_evidence: Identified as the leader of the Winged Monkeys summoned by the Golden Cap.

direct_visual_evidence: 

costume_or_covering_evidence: 

movement_evidence: 

associated_entities: Winged Monkeys

alias_or_role_evidence: King of the monkeys

unknowns: Specific facial features or unique markings.

source_refs: 

[[SECTION markdown]]

# Monkey King
**Role:** Summoned Entity / Obstacle

**Status:** Physically Present

**Description:** The leader of the Winged Monkeys. He refuses to fly Dorothy across the desert due to the territorial nature of his kind.

**Descriptive Phrases:** Monkey king, winged monkey leader.

**Uncertainty Note:** Specific physical details or regalia are not provided in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: winged_monkeys

canonical_character_id: CH007 Winged Monkeys

aliases: Band of Winged Monkeys

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: winged

scale_hint: small

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: Identified as the group summoned by the Golden Cap.

direct_visual_evidence: They are winged monkeys.

costume_or_covering_evidence: 

movement_evidence: Flight capability implied.

associated_entities: Monkey King

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Winged Monkeys
**Role:** Summoned Entities

**Status:** Physically Present (as a group)

**Description:** A band of monkeys with wings. They are bound to their own country and cannot fly Dorothy across the desert.

**Descriptive Phrases:** Flying monkeys, winged primates.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: soldier

canonical_character_id: CH008 Soldier

aliases: 

is_fully_identified: true

manual_description_required: true

manual_description_reason: Only one specific visual trait (green whiskers) is mentioned.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.8

direct_identity_evidence: Summoned to assist the group in the throne room.

direct_visual_evidence: Has green whiskers.

costume_or_covering_evidence: Soldier's uniform (implied).

movement_evidence: 

associated_entities: 

alias_or_role_evidence: 

unknowns: Full facial structure, body type, or specific uniform details.

source_refs: 

[[SECTION markdown]]

# Soldier
**Role:** Informant

**Status:** Physically Present

**Description:** A soldier summoned to the throne room who provides guidance on how to reach Glinda.

**Physical Traits:** Green whiskers.

**Descriptive Phrases:** Soldier with green whiskers, guide.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: glinda

canonical_character_id: CH009 Glinda

aliases: Glinda the Good Witch of the South

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is only mentioned/referenced, no physical description provided.

clarification_required: true

clarification_reason: Character has not appeared in the chapter.

clarification_question: What is Glinda's physical appearance and magical aesthetic?

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: human_scale

renderability_hint: context_only

confidence: 0.5

direct_identity_evidence: Referenced by the soldier as a potential source of help.

direct_visual_evidence: 

costume_or_covering_evidence: 

movement_evidence: 

associated_entities: 

alias_or_role_evidence: Glinda, the Good Witch of the South

unknowns: Physical appearance, clothing, magical effects.

source_refs: 

[[SECTION markdown]]

# Glinda
**Role:** Referenced Goal/Helper

**Status:** Referenced

**Description:** The Good Witch of the South who lives on the edge of the desert. Dorothy's group intends to seek her aid.

**Descriptive Phrases:** Good Witch of the South, magical guide.

**Uncertainty Note:** No physical description is available in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
