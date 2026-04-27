# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:51:59.756056+00:00
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

Chapter id: CH001

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

**Setting:** A small, one-room farmhouse situated in the middle of the vast, colorless Kansas prairies. The landscape is characterized by gray grass and baked earth.

**Characters:**
- **Dorothy:** An orphaned young girl who maintains a sense of joy despite her surroundings.
- **Aunt Em:** Dorothy's aunt; once pretty, now hardened and gray from the harsh prairie life.
- **Uncle Henry:** Dorothy's uncle; a stern, hardworking farmer.
- **Toto:** Dorothy's small, energetic black dog.

**Events:**
- The family lives in a state of constant vigilance due to the threat of cyclones.
- A massive storm approaches from both the north and south, signaling an imminent cyclone.
- As Uncle Henry goes to tend to the livestock, Aunt Em directs Dorothy to seek shelter in the underground cyclone cellar.
- Before Dorothy can reach the trap door, a powerful cyclone hits the house, lifting it off the ground.
- The house becomes the center of the storm, carried high into the air by intense wind pressure.
- Inside the floating house, Dorothy manages to rescue Toto after he nearly falls through the open trap door.
- As the hours pass, the initial terror subsides into a rhythmic swaying; Dorothy and Toto eventually fall asleep as the house is carried miles away.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [dorothy](dorothy)
- [aunt_em](aunt_em)
- [uncle_henry](uncle_henry)
- [toto](toto)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dorothy

canonical_character_id: CH001 Dorothy

aliases: orphaned young girl

is_fully_identified: true

manual_description_required: true

manual_description_reason: No specific clothing, hair color, or facial features are described in the text.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: human

morphology_hint: biped

scale_hint: small

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: Dorothy is named as the orphan girl living in the farmhouse.

direct_visual_evidence: None provided regarding specific appearance.

costume_or_covering_evidence: None.

movement_evidence: Moves to seek shelter; rescues Toto.

associated_entities: Aunt Em, Uncle Henry, Toto

alias_or_role_evidence: 

unknowns: hair color, eye color, clothing style, age (exact), height.

source_refs: Chapter 1

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Orphaned girl

**Presence:** Physically present.

**Description:** A young girl living on a Kansas farm. She is characterized by her resilient and joyful temperament despite the harsh, colorless environment of the prairies.

**Costume/Silhouette:** Unknown. No specific clothing details are provided in this chapter.

**Descriptive Noun Phrases:** Young girl, orphan, resilient child.

**Uncertainty Notes:** Physical appearance (hair, eyes, clothing) is completely unstated.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: aunt_em

canonical_character_id: CH001 Aunt Em

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

confidence: 0.8

direct_identity_evidence: Identified as Dorothy's aunt.

direct_visual_evidence: Once pretty, now hardened and gray from prairie life.

costume_or_covering_evidence: None.

movement_evidence: Directs Dorothy to the cellar.

associated_entities: Dorothy, Uncle Henry

alias_or_role_evidence: 

unknowns: specific facial features, clothing.

source_refs: Chapter 1

[[SECTION markdown]]

# Aunt Em
**Role:** Supporting character / Dorothy's aunt

**Presence:** Physically present.

**Description:** A woman who has been weathered and hardened by the harshness of life on the Kansas prairies. She is described as having once been pretty but now appearing gray/worn.

**Costume/Silhouette:** Unknown.

**Descriptive Noun Phrases:** Hardened woman, prairie aunt, weathered woman.

**Uncertainty Notes:** Specific clothing or detailed facial structure is not provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: uncle_henry

canonical_character_id: CH001 Uncle Henry

aliases: 

is_fully_identified: true

manual_description_required: true

manual_description_reason: Only described as "stern" and "hardworking"; no physical morphology or clothing details.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: human

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.7

direct_identity_evidence: Identified as Dorothy's uncle and a farmer.

direct_visual_evidence: Stern demeanor.

costume_or_covering_evidence: None.

movement_evidence: Goes to tend livestock.

associated_entities: Aunt Em, Dorothy

alias_or_role_evidence: 

unknowns: physical build, age, clothing, facial features.

source_refs: Chapter 1

[[SECTION markdown]]

# Uncle Henry
**Role:** Supporting character / Farmer

**Presence:** Physically present.

**Description:** A stern and hardworking farmer living on the prairie.

**Costume/Silhouette:** Unknown.

**Descriptive Noun Phrases:** Stern farmer, hardworking man, prairie uncle.

**Uncertainty Notes:** Physical appearance is limited to personality traits (sternness).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: toto

canonical_character_id: CH001 Toto

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

direct_identity_evidence: Named as Dorothy's dog.

direct_visual_evidence: Small, energetic, black.

costume_or_covering_evidence: Black fur.

movement_evidence: Energetic; nearly falls through a trap door; rescued by Dorothy.

associated_entities: Dorothy

alias_or_role_evidence: 

unknowns: breed (specific).

source_refs: Chapter 1

[[SECTION markdown]]

# Toto
**Role:** Companion / Pet

**Presence:** Physically present.

**Description:** A small, energetic black dog belonging to Dorothy.

**Costume/Silhouette:** Small quadruped with black fur.

**Descriptive Noun Phrases:** Small black dog, energetic puppy-like dog.

**Uncertainty Notes:** Specific breed is not mentioned.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
