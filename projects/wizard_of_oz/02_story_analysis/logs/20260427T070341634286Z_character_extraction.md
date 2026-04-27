# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:03:41.634286+00:00
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

Chapter id: CH008

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

**Setting:** A sunny country featuring a wide river with a swift current, a grassy riverbank, and a vast meadow filled with scarlet poppies.

**Characters:** Dorothy, Toto, Scarecrow, Tin Woodman, Cowardly Lion, and a Stork.

**Events:**
- **The River Crossing:** The group attempts to cross a wide river on a makeshift raft. During the crossing, the current sweeps them downstream, causing the Scarecrow to become stuck on his pole in the middle of the river.
- **The Rescue of the Scarecrow:** After the raft reaches the shore, the group realizes they have lost the Scarecrow. A passing Stork agrees to help and flies out to retrieve the Scarecrow, carrying him back to the group.
- **The Poppy Field:** As the travelers walk along the riverbank toward the Yellow Brick Road, they enter a massive meadow of scarlet poppies. The scent of these flowers is deadly, causing anyone who breathes it to fall into an eternal sleep.
- **The Sleeping Danger:** Dorothy and Toto succumb to the scent and fall asleep in the field. The Cowardly Lion also falls asleep because he is too heavy for the others to carry. 
- **The Escape:** Because they are not made of flesh, the Scarecrow and Tin Woodman are immune to the scent. They form a "human chair" to carry the sleeping Dorothy and Toto out of the field. They manage to reach safety, but they are forced to leave the Cowardly Lion behind in the poppy field, fearing he will sleep forever.
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
- [Stork](#stork)

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

direct_identity_evidence: Yes

direct_visual_evidence: No

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Toto, Scarecrow, Tin Woodman, Cowardly Lion

alias_or_role_evidence: 

unknowns: Specific clothing details not provided in this chapter.

source_refs: 

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present (falls asleep in poppy field)

**Physical Description:** Human female.

**Costume/Silhouette:** Not explicitly described in this chapter.

**Descriptive Phrases:** Young girl, human traveler, sleeping figure.

**Uncertainty Notes:** Specific attire and hair color are not mentioned in this text segment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: toto

canonical_character_id: CH003 Toto

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

direct_identity_evidence: Yes

direct_visual_evidence: No

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Dorothy

alias_or_role_evidence: 

unknowns: Breed/color not specified.

source_refs: 

[[SECTION markdown]]

# Toto
**Role:** Companion / Pet

**Status:** Physically Present (falls asleep in poppy field)

**Physical Description:** Small animal.

**Costume/Silhouette:** N/A

**Descriptive Phrases:** Small dog, companion animal.

**Uncertainty Notes:** Specific breed or color is not mentioned.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: scarecrow

canonical_character_id: CH004 Scarecrow

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

direct_identity_evidence: Yes

direct_visual_evidence: No

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Dorothy, Tin Woodman, Cowardly Lion

alias_or_role_evidence: 

unknowns: Specific material texture (straw vs fabric) is implied but not detailed.

source_refs: 

[[SECTION markdown]]

# Scarecrow
**Role:** Traveler / Rescuer

**Status:** Physically Present (stuck on pole, then rescued)

**Physical Description:** Non-flesh entity; immune to poppy scent.

**Costume/Silhouette:** Bipedal humanoid form.

**Descriptive Phrases:** Straw-based humanoid, non-flesh traveler, resilient entity.

**Uncertainty Notes:** Specific facial features or clothing are not described.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tin_woodman

canonical_character_id: CH005 Tin Woodman

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

direct_identity_evidence: Yes

direct_visual_evidence: No

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Dorothy, Scarecrow, Cowardly Lion

alias_or_role_evidence: 

unknowns: Specific metal texture or joints.

source_refs: 

[[SECTION markdown]]

# Tin Woodman
**Role:** Traveler / Rescuer

**Status:** Physically Present (immune to poppy scent)

**Physical Description:** Non-flesh entity; immune to poppy scent.

**Costume/Silhouette:** Bipedal humanoid form.

**Descriptive Phrases:** Metal man, non-flesh traveler, mechanical humanoid.

**Uncertainty Notes:** Specific metal type or level of articulation is not described.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: cowardly_lion

canonical_character_id: CH006 Cowardly Lion

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

direct_identity_evidence: Yes

direct_visual_evidence: No

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Dorothy, Scarecrow, Tin Woodman

alias_or_role_evidence: 

unknowns: Specific fur color/pattern.

source_refs: 

[[SECTION markdown]]

# Cowardly Lion
**Role:** Traveler

**Status:** Physically Present (falls asleep in poppy field)

**Physical Description:** Large animal; too heavy to be carried by the others.

**Costume/Silhouette:** Quadrupedal feline silhouette.

**Descriptive Phrases:** Large lion, heavy animal, sleeping predator.

**Uncertainty Notes:** Specific coloration or mane details are not provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: stork

canonical_character_id: CH007 Stork

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: winged

scale_hint: large

renderability_hint: renderable

confidence: 0.8

direct_identity_evidence: Yes

direct_visual_evidence: No

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Scarecrow

alias_or_role_evidence: 

unknowns: Specific plumage colors.

source_refs: 

[[SECTION markdown]]

# Stork
**Role:** Helper / Messenger

**Status:** Physically Present (flies through scene)

**Physical Description:** Winged bird capable of carrying a humanoid.

**Costume/Silhouette:** Avian silhouette, large scale.

**Descriptive Phrases:** Large flying stork, rescue bird.

**Uncertainty Notes:** Specific color patterns of feathers are not mentioned.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
