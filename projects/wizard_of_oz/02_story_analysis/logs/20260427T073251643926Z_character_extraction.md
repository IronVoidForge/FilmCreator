# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:32:51.643926+00:00
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

**Setting:** A rocky hill inhabited by Hammer-Heads and the lush, red-themed Country of the Quadlings.

**Characters:** Dorothy, Scarecrow, Tin Woodman, Cowardly Lion, Toto, Hammer-Heads (armless creatures with projectile heads), Winged Monkeys, a Farmer's Wife, Castle Guards, and Glinda (mentioned).

**Events:**
- The travelers attempt to climb a rocky hill but are intercepted by the Hammer-Heads, who guard the territory.
- The Scarecrow and the Lion are both knocked down the hill by the Hammer-Heads' ability to shoot their heads forward like projectiles.
- Realizing they cannot fight the creatures physically, Dorothy uses the Golden Cap to summon the Winged Monkeys.
- The Winged Monkeys fly the travelers over the hill, bypassing the frustrated Hammer-Heads, and deposit them in the Country of the Quadlings.
- Upon arrival, the group observes the red-colored aesthetic of the Quadling land and receives a meal from a kind farmer's wife.
- The travelers follow directions to Glinda's castle, where they are met by guards in red uniforms and granted immediate entry to see the Good Witch.
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
- [Toto](#toto)
- [Hammer-Heads](#hammer_heads)
- [Winged Monkeys](#winged_monkeys)
- [Farmer's Wife](#farmers_wife)
- [Castle Guards](#castle_guards)
- [Glinda](#glinda)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dorothy

canonical_character_id: Dorothy

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

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: Scarecrow, Tin Woodman, Cowardly Lion, Toto, Winged Monkeys

alias_or_role_evidence: 

unknowns: physical appearance details in this specific chapter

source_refs: 

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Description:** A young human girl traveling with a group of companions. In this chapter, she demonstrates agency by using the Golden Cap to summon the Winged Monkeys to bypass obstacles.

**Descriptive Nouns:** Young girl, traveler, user of the Golden Cap.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: scarecrow

canonical_character_id: Scarecrow

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

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: Dorothy, Tin Woodman, Cowardly Lion

alias_or_role_evidence: 

unknowns: specific fabric textures or facial features

source_refs: 

[[SECTION markdown]]

# Scarecrow
**Role:** Companion / Traveler

**Status:** Physically Present

**Description:** A humanoid entity made of straw. He is part of the traveling group and is physically knocked down a hill by the Hammer-Heads.

**Descriptive Nouns:** Straw man, humanoid construct, companion.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tin_woodman

canonical_character_id: Tin Woodman

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

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: Dorothy, Scarecrow, Cowardly Lion

alias_or_role_evidence: 

unknowns: specific metal sheen or joint details

source_refs: 

[[SECTION markdown]]

# Tin Woodman
**Role:** Companion / Traveler

**Status:** Physically Present

**Description:** A humanoid entity constructed of tin. He travels with Dorothy and the others through the rocky hills and into the Quadling country.

**Descriptive Nouns:** Tin man, metal construct, humanoid.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: cowardly_lion

canonical_character_id: Cowardly Lion

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

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: Dorothy, Scarecrow, Tin Woodman

alias_or_role_evidence: 

unknowns: specific fur patterns or mane details

source_refs: 

[[SECTION markdown]]

# Cowardly Lion
**Role:** Companion / Traveler

**Status:** Physically Present

**Description:** A large quadrupedal animal. He is part of the traveling group and is knocked down a hill by the Hammer-Heads' projectile attacks.

**Descriptive Nouns:** Large lion, quadruped, companion.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: toto

canonical_character_id: Toto

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: quadruped

scale_hint: tiny

renderability_hint: renderable

confidence: 1.0

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: Dorothy

alias_or_role_evidence: 

unknowns: specific breed details

source_refs: 

[[SECTION markdown]]

# Toto
**Role:** Companion / Pet

**Status:** Physically Present

**Description:** A small quadrupedal animal traveling with Dorothy.

**Descriptive Nouns:** Small dog, companion, pet.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: hammer_heads

canonical_character_id: Hammer-Heads

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

movement_evidence: true

associated_entities: 

alias_or_role_evidence: 

unknowns: specific skin texture or facial features beyond the head mechanism

source_refs: 

[[SECTION markdown]]

# Hammer-Heads

**Role:** Antagonists / Territory Guards

**Status:** Physically Present

**Description:** Armless creatures that inhabit a rocky hill. They possess the unique ability to shoot their heads forward like projectiles to knock down intruders.

**Descriptive Nouns:** Armless humanoids, projectile-headed creatures, hill guards.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: winged_monkeys

canonical_character_id: Winged Monkeys

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: creature

morphology_hint: winged

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: Dorothy (summoned by)

alias_or_role_evidence: 

unknowns: specific monkey species or wing structure details

source_refs: 

[[SECTION markdown]]

# Winged Monkeys
**Role:** Servants / Transporters

**Status:** Physically Present

**Description:** Flying creatures summoned via the Golden Cap. They fly the travelers over the rocky hill and deposit them in the Country of the Quadlings.

**Descriptive Nouns:** Flying monkeys, winged creatures, summoned entities.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: farmers_wife

canonical_character_id: Farmer's Wife

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided other than her role as a provider of food.

clarification_required: true

clarification_reason: Physical appearance is entirely unstated.

clarification_question: What does the farmer's wife look like?

character_type_hint: human

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.5

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: false

associated_entities: 

alias_or_role_evidence: 

unknowns: appearance, age, clothing

source_refs: 

[[SECTION markdown]]

# Farmer's Wife
**Role:** Supporting Character / Provider

**Status:** Physically Present

**Description:** A kind woman in the Country of the Quadlings who provides a meal to the travelers.

**Uncertainty Note:** Physical appearance and specific clothing are unknown.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: castle_guards

canonical_character_id: Castle Guards

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: group

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: true

direct_visual_evidence: true

costume_or_covering_evidence: true

movement_evidence: false

associated_entities: Glinda

alias_or_role_evidence: 

unknowns: individual facial features

source_refs: 

[[SECTION markdown]]

# Castle Guards
**Role:** Security / Gatekeepers

**Status:** Physically Present

**Description:** A group of guards stationed at Glinda's castle. They wear red uniforms and grant the travelers immediate entry.

**Descriptive Nouns:** Red-uniformed guards, castle security.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: glinda

canonical_character_id: Glinda

aliases: Good Witch

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned by name; no physical description provided in this chapter.

clarification_required: true

clarification_reason: Identity is known, but visual appearance is missing.

clarification_question: What is Glinda's physical appearance and attire?

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.4

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: false

associated_entities: Castle Guards

alias_or_role_evidence: true

unknowns: appearance, magic style, clothing

source_refs: 

[[SECTION markdown]]

# Glinda
**Role:** Destination / Authority Figure

**Status:** Referenced

**Description:** Known as the Good Witch. The travelers are traveling to her castle to see her.

**Uncertainty Note:** No visual information is available in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
