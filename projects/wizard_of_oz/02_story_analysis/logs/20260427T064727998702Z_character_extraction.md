# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:47:27.998702+00:00
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

**Setting:** A small, one-room farmhouse situated in the middle of the vast, gray, and sun-bleached Kansas prairies. The landscape is flat and devoid of color or trees.

**Characters:**
- **Dorothy:** An orphan girl who maintains a sense of joy and laughter despite her surroundings.
- **Aunt Em:** Dorothy's aunt; once pretty, she has become thin, gaunt, and gray due to the harsh life on the farm.
- **Uncle Henry:** Dorothy's uncle; a hardworking, stern, and solemn farmer.
- **Toto:** Dorothy's small, energetic black dog.

**Events:**
- The family lives in a state of constant vigilance against the weather, specifically cyclones.
- A massive storm approaches from both the north and south, signaling an imminent cyclone.
- As Uncle Henry goes to tend to the livestock, Aunt Em directs Dorothy to seek shelter in the underground cyclone cellar.
- Before Dorothy can reach the trap door, a powerful cyclone hits the house, lifting it off the ground and carrying it into the air.
- Inside the flying house, Dorothy experiences the terrifying but eventually rhythmic motion of being carried by the wind.
- After a brief moment of panic where Toto nearly falls through the open trap door, Dorothy secures him and settles down.
- As the hours pass, Dorothy overcomes her initial fright and eventually falls asleep while the house is carried miles away by the storm.
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

canonical_character_id: Dorothy

aliases: orphan girl

is_fully_identified: true

manual_description_required: true

manual_description_reason: No specific physical features (hair color, eye color, clothing) are provided in the text.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: human

morphology_hint: biped

scale_hint: small

renderability_hint: renderable

confidence: 0.9

associated_entities: aunt_em, uncle_henry, toto

alias_or_role_evidence: orphan girl

unknowns: hair color, eye color, specific clothing style

source_refs: chapter summary

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Orphan Girl

**Presence:** Physically Present

**Description:** 
A young girl living on a Kansas farm. She is characterized by her temperament—maintaining joy and laughter despite the harsh, gray environment.

**Visual Notes:**
- **Physicality:** Human child.
- **Uncertainty:** Specific facial features, hair color, and clothing are not described in this chapter. 

**Prompt Phrases:** young girl, joyful expression, Kansas farm orphan.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: aunt_em

canonical_character_id: Aunt Em

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

associated_entities: dorothy, uncle_henry

alias_or_role_evidence: 

unknowns: clothing details

source_refs: chapter summary

[[SECTION markdown]]

# Aunt Em
**Role:** Dorothy's Aunt

**Presence:** Physically Present

**Description:** 
A woman who has been weathered by the harsh life on the farm.

**Visual Notes:**
- **Physicality:** Thin, gaunt, and gray appearance. Once pretty, but now aged by hardship.
- **Silhouette:** Likely worn or practical farm attire (not specified).

**Prompt Phrases:** thin gaunt woman, graying complexion, weathered farmer's wife.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: uncle_henry

canonical_character_id: Uncle Henry

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

associated_entities: dorothy, aunt_em

alias_or_role_evidence: 

unknowns: specific clothing details

source_refs: chapter summary

[[SECTION markdown]]

# Uncle Henry
**Role:** Dorothy's Uncle / Farmer

**Presence:** Physically Present

**Description:** 
A hardworking and stern farmer.

**Visual Notes:**
- **Physicality:** Stern, solemn demeanor.
- **Silhouette:** Likely rugged farm laborer clothing.

**Prompt Phrases:** stern man, solemn expression, hardworking farmer, rugged appearance.
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

associated_entities: dorothy

alias_or_role_evidence: 

unknowns: breed (though color is known)

source_refs: chapter summary

[[SECTION markdown]]

# Toto
**Role:** Dorothy's Pet

**Presence:** Physically Present

**Description:** 
A small, energetic dog.

**Visual Notes:**
- **Color:** Black.
- **Physicality:** Small quadruped, high energy.

**Prompt Phrases:** small black dog, energetic puppy, small canine.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
