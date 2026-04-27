# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:28:48.151099+00:00
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

**Setting:** The Dainty China Country, a land characterized by a smooth, white, platter-like floor, tiny colorful china houses, and inhabitants made entirely of fragile porcelain.

**Characters:** 
- Dorothy
- Scarecrow
- Tin Woodman
- Cowardly Lion
- Toto
- A China Milkmaid (and her cow)
- A beautiful China Princess
- Mr. Joker (a cracked, foolish China Clown)

**Events:**
- The travelers use a wooden ladder built by the Tin Woodman to climb over a high wall into the Dainty China Country.
- Upon entering, they realize the extreme fragility of the land. Dorothy and her friends must move with extreme caution to avoid breaking anything or anyone.
- A mishap occurs when Dorothy startles a china cow, causing it to kick over a milkmaid; the cow breaks a leg and the milkmaid suffers a nick in her elbow.
- Dorothy meets a beautiful China Princess who explains that while they are pretty, being mended after a break ruins their beauty. The Princess also explains that if they are taken away from their country, they become stiff and lose their ability to move freely.
- They encounter Mr. Joker, a clown covered in cracks from standing on his head too often.
- After traveling through the country for an hour, the group reaches the far wall. While climbing over it, the Lion accidentally smashes a china church with his tail.
- The group successfully exits the China Country, reflecting on the perils of traveling through such a brittle land.
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
- [China Milkmaid](#china_milkmaid)
- [China Cow](#china_cow)
- [China Princess](#china_princess)
- [Mr. Joker](#mr_joker)

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

direct_identity_evidence: Dorothy is explicitly named as a traveler in the group.

direct_visual_evidence: Present in the scene.

costume_or_covering_evidence: 

movement_evidence: Moves with extreme caution to avoid breaking china.

associated_entities: Scarecrow, Tin Woodman, Cowardly Lion, Toto

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Description:** A human girl traveling through the Dainty China Country. She must move with extreme caution to avoid breaking the fragile porcelain inhabitants and structures.

**Descriptive Noun Phrases:** Human girl, cautious traveler.
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

direct_identity_evidence: Scarecrow is explicitly named as part of the traveling group.

direct_visual_evidence: Present in the scene.

costume_or_covering_evidence: 

movement_evidence: Part of the group climbing the ladder and moving through the country.

associated_entities: Dorothy, Tin Woodman, Cowardly Lion, Toto

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Scarecrow
**Role:** Traveler

**Status:** Physically Present

**Description:** A member of the traveling group.

**Descriptive Noun Phrases:** Straw-filled humanoid, traveling companion.
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

direct_identity_evidence: Tin Woodman is explicitly named as part of the traveling group.

direct_visual_evidence: Present in the scene.

costume_or_covering_evidence: Constructed of tin.

movement_evidence: Built a wooden ladder for the group to climb.

associated_entities: Dorothy, Scarecrow, Cowardly Lion, Toto

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Tin Woodman
**Role:** Traveler / Builder

**Status:** Physically Present

**Description:** A metal humanoid who provides utility to the group, such as building a wooden ladder.

**Descriptive Noun Phrases:** Tin man, metallic humanoid, articulated metal construct.
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

direct_identity_evidence: Cowardly Lion is explicitly named as part of the traveling group.

direct_visual_evidence: Present in the scene.

costume_or_covering_evidence: 

movement_evidence: Accidentally smashes a china church with his tail while climbing out of the country.

associated_entities: Dorothy, Scarecrow, Tin Woodman, Toto

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Cowardly Lion
**Role:** Traveler

**Status:** Physically Present

**Description:** A large animal traveler. His size and tail cause accidental destruction in the fragile environment.

**Descriptive Noun Phrases:** Large lion, heavy-tailed predator.
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

confidence: 1.0

direct_identity_evidence: Toto is explicitly named as part of the traveling group.

direct_visual_evidence: Present in the scene.

costume_or_covering_evidence: 

movement_evidence: Traveling with the group.

associated_entities: Dorothy, Scarecrow, Tin Woodman, Cowardly Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Toto
**Role:** Companion

**Status:** Physically Present

**Description:** A small animal traveling with Dorothy.

**Descriptive Noun Phrases:** Small dog, canine companion.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: china_milkmaid

canonical_character_id: China Milkmaid

aliases: 

is_fully_identified: true

manual_description_required: true

manual_description_reason: Physical appearance is limited to being made of porcelain and having a "nick in her elbow." Specific facial features or clothing patterns are not described.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: small

renderability_hint: renderable

confidence: 0.8

direct_identity_evidence: Explicitly named as a China Milkmaid.

direct_visual_evidence: Present in the scene (suffers an injury).

costume_or_covering_evidence: Implied milkmaid attire, but made of porcelain.

movement_evidence: Kicked over by a china cow.

associated_entities: China Cow

alias_or_role_evidence: 

unknowns: Specific facial features, color patterns, or clothing details beyond "china."

source_refs: 

[[SECTION markdown]]

# China Milkmaid
**Role:** Inhabitant of Dainty China Country

**Status:** Physically Present

**Description:** A fragile inhabitant made entirely of porcelain. She suffers a nick in her elbow after being kicked by a china cow.

**Descriptive Noun Phrases:** Porcelain milkmaid, fragile china figure, chipped ceramic woman.

**Uncertainty Note:** Specific visual details regarding her face or clothing patterns are unknown.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: china_cow

canonical_character_id: China Cow

aliases: 

is_fully_identified: true

manual_description_required: true

manual_description_reason: Only described as a "china cow" that can kick. No specific markings or porcelain patterns are provided.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: quadruped

scale_hint: small

renderability_hint: renderable

confidence: 0.8

direct_identity_evidence: Explicitly named as a china cow.

direct_visual_evidence: Present in the scene (kicks the milkmaid).

costume_or_covering_evidence: Made of porcelain.

movement_evidence: Kicks over the milkmaid and breaks its own leg.

associated_entities: China Milkmaid

alias_or_role_evidence: 

unknowns: Specific patterns, colors, or size relative to a real cow.

source_refs: 

[[SECTION markdown]]

# China Cow
**Role:** Inhabitant of Dainty China Country

**Status:** Physically Present

**Description:** A small animal made entirely of porcelain. It is prone to breaking; it breaks its own leg during a mishap.

**Descriptive Noun Phrases:** Porcelain cow, ceramic bovine, fragile china animal.

**Uncertainty Note:** Visual patterns (spots/colors) are not specified in the text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: china_princess

canonical_character_id: China Princess

aliases: 

is_fully_identified: true

manual_description_required: true

manual_description_reason: Described only as "beautiful," with no specific physical features, colors, or porcelain patterns provided.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: small

renderability_hint: renderable

confidence: 0.8

direct_identity_evidence: Explicitly named as a China Princess.

direct_visual_evidence: Present in the scene (explains the nature of their existence).

costume_or_covering_evidence: Implied royal porcelain attire.

movement_evidence: Moves, but notes that they become "stiff" if taken from their country.

associated_entities: 

alias_or_role_evidence: 

unknowns: Facial features, hair/crown details, specific porcelain colors or patterns.

source_refs: 

[[SECTION markdown]]

# China Princess
**Role:** Inhabitant / Informant

**Status:** Physically Present

**Description:** A beautiful inhabitant of the Dainty China Country made of porcelain. She explains that mending breaks ruins their beauty and that they lose mobility if removed from their land.

**Descriptive Noun Phrases:** Beautiful porcelain princess, ceramic royal, fragile china lady.

**Uncertainty Note:** Specific visual details (colors, patterns, facial features) are not provided.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: mr_joker

canonical_character_id: Mr. Joker

aliases: China Clown

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: small

renderability_hint: renderable

confidence: 1.0

direct_identity_evidence: Explicitly named as Mr. Joker.

direct_visual_evidence: Present in the scene.

costume_or_covering_evidence: A clown, covered in cracks.

movement_evidence: Known to stand on his head.

associated_entities: 

alias_or_role_evidence: Referred to as a "foolish China Clown."

unknowns: Specific colors or patterns of the clown makeup/clothing.

source_refs: 

[[SECTION markdown]]

# Mr. Joker
**Role:** Inhabitant of Dainty China Country

**Status:** Physically Present

**Description:** A foolish China Clown made of porcelain. He is characterized by being covered in cracks, a result of standing on his head too often.

**Descriptive Noun Phrases:** Cracked china clown, foolish porcelain joker, ceramic entertainer.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
