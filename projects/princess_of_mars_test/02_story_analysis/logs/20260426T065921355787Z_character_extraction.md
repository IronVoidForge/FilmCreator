# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:59:21.355787+00:00
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

Chapter id: CH020

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
After two weeks of wandering through the Martian wilderness, during which he is attacked by wild beasts and aided by his faithful calot Woola, John Carter reaches a massive Atmosphere Factory. Inside, he is hosted by an elderly man who possesses a diadem with a unique "ninth ray" stone. Through his telepathic abilities, Carter learns that this facility is vital to the survival of all life on Mars, as it produces the planet's atmosphere. 

The host, sensing Carter is an outsider, secretly plots to kill him to protect the plant's secrets. However, Carter uses his telepathy to intercept the nine thought-waves required to operate the factory's massive doors, allowing him and Woola to escape. Following his escape, Carter is found by a group of hospitable Red Martian government officers on a farm. They provide him with food, rest, and assistance in disguising himself as a local Red Martian—anointing his skin with red oil and cutting his hair to match the fashion—to help him blend in as he travels toward Zodanga.

**Characters:**
- **John Carter:** Exhausted and starving, but increasingly proficient in using telepathy to read minds and manipulate technology.
- **Woola:** Carter's loyal calot who saves him from a multi-legged beast and accompanies him on his journey.
- **The Old Man (Atmosphere Plant Host):** A solitary guardian of the atmosphere machinery who views Carter as a threat to Barsoom's stability.
- **The Ptor Family:** A group of Red Martian government officers who provide Carter with hospitality, supplies, and a disguise.

**Settings:**
- **The Atmosphere Factory:** A massive, unassailable concrete structure containing radium pumps and the machinery that generates the Martian atmosphere using the ninth ray.
- **The Ptor Farm:** A collection of Red Martian homes raised on metal shafts to avoid danger, located near a broad white turnpike.
- **The Martian Wilderness:** A harsh landscape filled with strange beasts and vegetation providing "vegetable milk."
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH020

- [John Carter](#john_carter)
- [Woola](#woola)
- [The Old Man](#the_old_man)
- [The Ptor Family](#the_ptor_family)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH020 John Carter

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

confidence: 0.9

direct_identity_evidence: true

direct_visual_evidence: true

costume_or_covering_evidence: true

movement_evidence: true

associated_entities: Woola, The Old Man, The Ptor Family

alias_or_role_evidence: true

unknowns: 

source_refs: 

[[SECTION markdown]]
# John Carter
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:** An exhausted and starving man. Later in the chapter, his appearance is modified to blend in with Red Martians; his skin is anointed with red oil and his hair is cut to match local fashion. He possesses telepathic abilities capable of intercepting thought-waves.

**Costume/Silhouette:** Initially traveling through wilderness; later disguised as a local Red Martian using red oils and specific hair styling.

**Prompt Phrases:** exhausted man, starving traveler, skin coated in red oil, short cropped Martian hair, telepathic expression.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH020 Woola

aliases: Calot

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

confidence: 0.8

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
**Role:** Companion / Loyal Beast

**Status:** Physically Present

**Physical Description:** A loyal calot. Described as a beast that protects the protagonist from multi-legged predators.

**Costume/Silhouette:** Quadrupedal Martian creature.

**Prompt Phrases:** loyal calot, large Martian quadruped, faithful beast, protective animal.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: the_old_man

canonical_character_id: CH020 The Old Man

aliases: Atmosphere Plant Host

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only described as "elderly" with no specific physical features or clothing details provided.

clarification_required: true

clarification_reason: Physical appearance is extremely sparse.

clarification_question: What are the specific facial features, build, and clothing style of the elderly host?

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.5

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: false

associated_entities: John Carter

alias_or_role_evidence: true

unknowns: facial features, build, clothing

source_refs: 

[[SECTION markdown]]
# The Old Man
**Role:** Antagonist / Guardian of the Atmosphere Factory

**Status:** Physically Present

**Physical Description:** An elderly man. He is a solitary guardian who possesses a diadem with a unique "ninth ray" stone.

**Costume/Silhouette:** Wears a diadem containing a ninth-ray stone. Specific clothing details are unknown.

**Prompt Phrases:** elderly man, solitary guardian, wearing a diadem with a glowing ninth-ray stone, secretive expression.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: ptor_family

canonical_character_id: CH020 The Ptor Family

aliases: Red Martian government officers

is_fully_identified: false

manual_description_required: true

manual_description_reason: Characterized as a group/family rather than individuals; specific physical traits for members are not detailed.

clarification_required: true

clarification_reason: Individual appearances within the group are unknown.

clarification_question: What is the typical appearance and attire of the Ptor family members?

character_type_hint: group

morphology_hint: biped

scale_hint: human_scale

renderability_hint: context_only

confidence: 0.6

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: false

associated_entities: John Carter

alias_or_role_evidence: true

unknowns: individual features, specific clothing

source_refs: 

[[SECTION markdown]]
# The Ptor Family
**Role:** Supporting Characters / Hosts

**Status:** Physically Present

**Physical Description:** A group of hospitable Red Martian government officers. They reside on a farm with homes raised on metal shafts.

**Costume/Silhouette:** Likely dressed in local Red Martian fashion (consistent with the disguise provided to Carter).

**Prompt Phrases:** group of Red Martians, hospitable officers, living on a raised farm, Martian government officials.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
