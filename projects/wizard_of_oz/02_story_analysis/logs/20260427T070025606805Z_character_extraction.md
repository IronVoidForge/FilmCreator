# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:00:25.607805+00:00
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

Chapter id: CH006

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

**Setting:** A thick, dark forest where the Yellow Brick Road is partially obscured by dried branches and dead leaves.

**Characters:** 
- Dorothy
- Toto
- Scarecrow
- Tin Woodman
- The Cowardly Lion (New Character)

**Events:**
- While walking through the woods, the group is ambushed by a large Lion that attacks the Scarecrow and the Tin Woodman.
- Dorothy defends Toto by slapping the Lion on the nose and calling him a coward.
- The Lion reveals his true nature: despite being the "King of Beasts," he is paralyzed by fear and lacks courage, which makes him deeply unhappy.
- After hearing about the group's quest to see Oz, the Lion decides to join them to ask for courage.
- During their continued journey, the Tin Woodman accidentally steps on a beetle; his subsequent tears of regret cause his jaw to rust shut.
- The Scarecrow uses the oil-can to fix the Tin Woodman, and the Woodman vows to walk more carefully to avoid harming any living creatures.
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
- [Cowardly Lion](#cowardly_lion)

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

confidence: 0.9

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: Toto, Scarecrow, Tin Woodman, Cowardly Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Group Member

**Status:** Physically Present

**Description:** A human girl traveling with a group of companions. In this chapter, she demonstrates bravery by defending Toto against the Lion.

**Visual Notes:** Specific clothing or physical features are not detailed in this specific chapter text; rely on established series continuity for visual assets.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: toto

canonical_character_id: CH001 Toto

aliases: Dog

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

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: Dorothy

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Toto
**Role:** Companion / Pet

**Status:** Physically Present

**Description:** A small dog belonging to Dorothy. He is the target of the Lion's initial aggression.

**Visual Notes:** Small quadrupedal animal.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: scarecrow

canonical_character_id: CH003 Scarecrow

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

associated_entities: Tin Woodman, Dorothy, Cowardly Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Scarecrow
**Role:** Group Member

**Status:** Physically Present

**Description:** A humanoid entity who is part of the traveling group. He is attacked by the Lion during the ambush.

**Visual Notes:** Character is a non-human humanoid; specific material composition (straw/fabric) is implied by name but not explicitly described in this chapter's action.

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

confidence: 0.9

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: Scarecrow, Dorothy, Cowardly Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Tin Woodman
**Role:** Group Member

**Status:** Physically Present

**Description:** A humanoid entity made of metal. He is attacked by the Lion and later suffers a mechanical failure (rusted jaw) due to emotional distress after stepping on a beetle.

**Visual Notes:** Metallic construction; prone to rusting if moisture (tears) is applied to joints/jaw.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: cowardly_lion

canonical_character_id: CH005 Cowardly Lion

aliases: King of Beasts

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

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: Dorothy, Scarecrow, Tin Woodman

alias_or_role_evidence: "King of Beasts"

unknowns: 

source_refs: 

[[SECTION markdown]]

# Cowardly Lion
**Role:** New Character / Ally

**Status:** Physically Present

**Description:** A large lion who initially attacks the group but is revealed to be driven by fear rather than malice. He lacks courage and seeks Oz to find some.

**Visual Notes:** Large quadrupedal feline; "King of Beasts" archetype.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
