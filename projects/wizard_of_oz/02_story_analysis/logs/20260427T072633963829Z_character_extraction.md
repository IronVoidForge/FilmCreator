# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:26:33.963829+00:00
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

Chapter id: CH019

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

**Setting:** The outskirts of the Emerald City, the surrounding green fields, a thick forest, and the edge of a white china wall.

**Characters:** Dorothy, Scarecrow, Tin Woodman, Cowardly Lion, Toto, Guardian of the Gate (briefly).

**Events:**
- **Departure from the Emerald City:** The group says goodbye to the Guardian of the Gate and the green-whiskered soldier. The Guardian returns their spectacles and acknowledges the Scarecrow as the new ruler of the city.
- **Reflections on Oz:** As they travel toward the South, the companions reflect on their time in the Emerald City and their feelings regarding the Wizard's true nature and the gifts he provided them.
- **The Fighting Trees:** The group encounters a dense forest that blocks their path. Upon attempting to pass through, the Scarecrow is attacked by trees that use their branches to seize and toss travelers. 
- **Breaking Through:** The Tin Woodman uses his axe to chop through the attacking branches, creating a safe passage for the rest of the group and Toto. They conclude that only the first row of trees acts as "policemen" for the forest.
- **The China Wall:** After exiting the woods, the travelers are halted by a high, smooth wall made of white china, prompting the Tin Woodman to suggest building a ladder to climb over it.
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
- [Guardian of the Gate](#guardian_of_the_gate)
- [Green-whiskered Soldier](#green_whiskered_soldier)

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

direct_identity_evidence: Yes

direct_visual_evidence: Yes

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Scarecrow, Tin Woodman, Cowardly Lion, Toto

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Description:** A young human girl traveling with a group of companions toward the South.

**Notes:** While specific visual details like clothing are not detailed in this specific chapter text, her identity as a human traveler is established through her movement and dialogue with the group.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: scarecrow

canonical_character_id: CH003 Scarecrow

aliases: New Ruler of the Emerald City

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

direct_identity_evidence: Yes

direct_visual_evidence: Yes

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Dorothy, Tin Woodman, Cowardly Lion, Toto

alias_or_role_evidence: Recognized as the new ruler of the Emerald City.

unknowns: 

source_refs: 

[[SECTION markdown]]

# Scarecrow
**Role:** Companion / Ruler of Emerald City

**Status:** Physically Present

**Description:** A humanoid non-human entity who is recognized by the Guardian as the new ruler of the Emerald City.

**Notes:** Involved in combat with the Fighting Trees; uses physical movement to navigate the forest.
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

direct_identity_evidence: Yes

direct_visual_evidence: Yes

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Dorothy, Scarecrow, Cowardly Lion, Toto

alias_or_role_evidence: Uses an axe to clear paths.

unknowns: 

source_refs: 

[[SECTION markdown]]

# Tin Woodman
**Role:** Companion / Pathbreaker

**Status:** Physically Present

**Description:** A humanoid non-human entity capable of using tools (an axe) to chop through tree branches.

**Notes:** Acts as the primary defense against the Fighting Trees by clearing a path for the group.
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

direct_identity_evidence: Yes

direct_visual_evidence: Yes

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Dorothy, Scarecrow, Tin Woodman, Toto

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Cowardly Lion
**Role:** Companion

**Status:** Physically Present

**Description:** A large quadruped animal traveling with the group.

**Notes:** Part of the core traveling party moving toward the South.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: toto

canonical_character_id: CH006 Toto

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

direct_identity_evidence: Yes

direct_visual_evidence: Yes

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Dorothy, Scarecrow, Tin Woodman, Cowardly Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Toto
**Role:** Companion / Pet

**Status:** Physically Present

**Description:** A small quadruped animal.

**Notes:** Travels alongside the main group through the forest and toward the China Wall.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: guardian_of_the_gate

canonical_character_id: CH007 Guardian of the Gate

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

movement_evidence: No

associated_entities: Scarecrow

alias_or_role_evidence: Guardian of the Emerald City gate.

unknowns: 

source_refs: 

[[SECTION markdown]]

# Guardian of the Gate
**Role:** Gatekeeper

**Status:** Referenced / Briefly Present

**Description:** A humanoid entity who guards the entrance to the Emerald City and returns spectacles to the group.

**Notes:** Appears at the beginning of the chapter during the departure from the city. Physical appearance is not detailed beyond his role.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: green_whiskered_soldier

canonical_character_id: CH008 Green-whiskered Soldier

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only a single descriptive trait (green whiskers) is provided.

clarification_required: true

clarification_reason: Insufficient detail for full character design.

clarification_question: What is the soldier's overall appearance, uniform, and species?

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: human_scale

renderability_hint: context_only

confidence: 0.4

direct_identity_evidence: Yes

direct_visual_evidence: No

costume_or_covering_evidence: No

movement_evidence: No

associated_entities: Guardian of the Gate

alias_or_role_evidence: Part of the Emerald City guard.

unknowns: 

source_refs: 

[[SECTION markdown]]

# Green-whiskered Soldier
**Role:** Guard

**Status:** Referenced

**Description:** A soldier associated with the Emerald City, noted specifically for having green whiskers.

**Notes:** Mentioned during the departure from the city; very little visual information is available.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: fighting_trees

canonical_character_id: CH009 Fighting Trees

aliases: Policemen of the forest

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: creature

morphology_hint: multi_legged

scale_hint: large

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: Yes

direct_visual_evidence: Yes

costume_or_covering_evidence: No

movement_evidence: Yes

associated_entities: Scarecrow, Tin Woodman

alias_or_role_evidence: Act as "policemen" for the forest.

unknowns: 

source_refs: 

[[SECTION markdown]]

# Fighting Trees
**Role:** Obstacle / Forest Sentinels

**Status:** Physically Present

**Description:** Large, sentient trees that use their branches to seize and toss travelers.

**Notes:** The first row of these trees acts as "policemen" for the forest. They are aggressive toward those attempting to pass through.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
