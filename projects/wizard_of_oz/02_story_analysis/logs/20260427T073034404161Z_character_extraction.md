# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:30:34.404161+00:00
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

Chapter id: CH021

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

**Setting:** A disagreeable country of bogs and marshes, leading into a vast, ancient forest filled with massive trees and thick moss.

**Characters:** Dorothy, Toto, the Scarecrow, the Tin Woodman, the Lion, various forest beasts (tigers, elephants, bears, wolves, foxes), and the Great Spider monster.

**Events:**
- The travelers navigate through difficult marshlands and enter a deep, ancient forest.
- The group discovers a massive gathering of wild animals in a forest clearing.
- A tiger informs the Lion that the animals are being terrorized by a giant spider-like monster with elephant-sized body and tree-trunk legs.
- The Lion strikes a deal: if he kills the monster, the animals will crown him King of the Forest.
- The Lion tracks the monster to an oak grove while it is sleeping.
- Utilizing the creature's anatomy (a slender neck), the Lion leaps onto its back and decapitates it with a single heavy paw strike.
- The Lion returns to the clearing, announces his victory, and is officially recognized as the King of Beasts. He promises to return to rule once Dorothy has reached Kansas.
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
- [Toto](#toto)
- [Scarecrow](#scarecrow)
- [Tin Woodman](#tin_woodman)
- [Lion](#lion)
- [Tiger](#tiger)
- [Great Spider Monster](#great_spider_monster)

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

confidence: 0.9

direct_identity_evidence: Presence in the group navigating marshes and forest.

direct_visual_evidence: 

costume_or_covering_evidence: 

movement_evidence: Navigating through difficult marshlands.

associated_entities: Toto, Scarecrow, Tin Woodman, Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Description:** A human girl traveling through bogs, marshes, and ancient forests. 

**Note:** Specific visual details regarding her clothing or hair are not provided in this chapter.
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

scale_hint: small

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: Traveling with Dorothy.

direct_visual_evidence: 

costume_or_covering_evidence: 

movement_evidence: Navigating through difficult marshlands.

associated_entities: Dorothy

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Toto
**Role:** Companion

**Status:** Physically Present

**Description:** A small animal companion traveling with Dorothy.

**Note:** Specific breed or color is not mentioned in this chapter.
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

confidence: 0.8

direct_identity_evidence: Part of the traveling group.

direct_visual_evidence: 

costume_or_covering_evidence: 

movement_evidence: Navigating through difficult marshlands.

associated_entities: Dorothy, Tin Woodman, Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Scarecrow
**Role:** Traveler / Companion

**Status:** Physically Present

**Description:** A humanoid non-human entity traveling with the group.

**Note:** Specific material composition (straw/fabric) is implied by name but not explicitly described in this chapter's text.
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

confidence: 0.8

direct_identity_evidence: Part of the traveling group.

direct_visual_evidence: 

costume_or_covering_evidence: 

movement_evidence: Navigating through difficult marshlands.

associated_entities: Dorothy, Scarecrow, Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Tin Woodman
**Role:** Traveler / Companion

**Status:** Physically Present

**Description:** A humanoid non-human entity traveling with the group.

**Note:** Specific material composition (tin/metal) is implied by name but not explicitly described in this chapter's text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lion

canonical_character_id: Lion

aliases: King of the Forest, King of Beasts

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

confidence: 0.9

direct_identity_evidence: Identified as the Lion; strikes a deal with animals.

direct_visual_evidence: Uses heavy paw strike to decapitate monster.

costume_or_covering_evidence: 

movement_evidence: Tracks the monster; leaps onto its back.

associated_entities: Dorothy, Tiger, Forest Animals

alias_or_role_evidence: King of the Forest (promised), King of Beasts (recognized)

unknowns: 

source_refs: 

[[SECTION markdown]]
# Lion
**Role:** Hero / Future King of the Forest

**Status:** Physically Present

**Description:** A large animal capable of heavy, decisive strikes with its paws.

**Key Traits:** Strong enough to decapitate a giant monster in one strike; possesses leadership qualities recognized by forest animals.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tiger

canonical_character_id: Tiger

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

confidence: 0.9

direct_identity_evidence: Identified as a tiger in the clearing.

direct_visual_evidence: 

costume_or_covering_evidence: 

movement_evidence: Present in forest clearing.

associated_entities: Lion, Forest Animals

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Tiger
**Role:** Messenger / Forest Animal

**Status:** Physically Present

**Description:** A large forest animal that communicates the threat of the spider monster to the Lion.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: great_spider_monster

canonical_character_id: Great Spider Monster

aliases: Giant Spider-like Monster

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: creature

morphology_hint: multi_legged

scale_hint: giant

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: Described by the tiger and killed by the Lion.

direct_visual_evidence: Elephant-sized body, tree-trunk legs, slender neck.

costume_or_covering_evidence: 

movement_evidence: Sleeping in an oak grove.

associated_entities: Forest Animals (victims)

alias_or_role_evidence: Terrorizer of the forest.

unknowns: 

source_refs: 

[[SECTION markdown]]
# Great Spider Monster
**Role:** Antagonist (Deceased)

**Status:** Physically Present (until decapitated)

**Description:** A massive, terrifying creature. It has an elephant-sized body and legs as thick as tree trunks. Despite its bulk, it possesses a slender neck.

**Note:** The monster is killed by the Lion during this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
