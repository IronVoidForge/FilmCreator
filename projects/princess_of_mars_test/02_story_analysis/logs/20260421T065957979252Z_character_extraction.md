# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:59:57.979252+00:00
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

Chapter id: CH005

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question sections=markdown



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

**Setting:** A captive's chamber decorated with masterfully painted murals of Martian landscapes; a deserted street in a Martian city; the exterior of a building overlooking a valley.

**Characters:**
- **The Protagonist:** An adventurous human captive attempting to test his physical limits and escape his guards.
- **Sola:** A female Martian who shows uncharacteristic sympathy, kindness, and care for the protagonist, providing him with food and warmth.
- **The Watch Dog:** A ferocious, short-legged but incredibly fast Martian beast used for protection and hunting; it serves as the protagonist's constant guardian.
- **The Colossal Creature:** A large, white, hairless, ape-like being that captures the protagonist during his escape attempt.

**Key Events:**
- **Observation of Captivity:** The protagonist observes his guard dog and examines the room's murals, noting the absence of living creatures in the art.
- **Martian Biology & Environment:** Through Sola’s care, the protagonist learns about Martian food (milk from a large plant), the extreme cold of the nights, and the mechanics of the two Martian moons which provide nocturnal light.
- **The Escape Attempt:** Seeking to test the watch dog's limits, the protagonist leaves his room. He discovers that despite its short legs, the beast is incredibly fast and intelligent.
- **The Chase:** The protagonist engages in a high-stakes chase through the city, using his jumping ability to evade the beast.
- **Capture:** After leaping into a window thirty feet above the ground to escape the dog, the protagonist is grabbed from behind by a massive, ape-like creature and dragged into a room.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [protagonist](#protagonist)
- [sola](#sola)
- [the_watch_dog](#the_watch_dog)
- [the_colossal_creature](#the_colossal_creature)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Human Captive

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical features, age, or clothing details provided beyond being a human.

clarification_required: true

clarification_reason: Physical appearance and attire are unknown.

clarification_question: What is the protagonist's physical build, hair color, eye color, and what kind of clothing is he wearing?

[[SECTION markdown]]

# Protagonist
**Role:** Main Character / Captive

**Presence:** Physically Present

**Description:** An adventurous human currently held captive in a Martian chamber. He possesses high jumping ability and an active, testing nature.

**Visual Notes:** Physical appearance is currently undefined. 

**Uncertainty Notes:** Specific facial features, hair, and clothing are not described in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH003 Sola

aliases: Female Martian

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description of her appearance, skin, or clothing provided.

clarification_required: true

clarification_reason: Needs visual identification for Martian biology and attire.

clarification_question: What does Sola look like (skin color, facial features, height) and what is her typical attire?

[[SECTION markdown]]

# Sola
**Role:** Supporting Character / Caretaker

**Presence:** Physically Present

**Description:** A female Martian who shows sympathy and kindness toward the protagonist. She provides food and warmth.

**Visual Notes:** Described as a Martian, but specific biological traits are missing.

**Uncertainty Notes:** No details regarding her physical form or clothing are available.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: the_watch_dog

canonical_character_id: CH004 The Watch Dog

aliases: Martian Beast, Guard Dog

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Watch Dog
**Role:** Antagonist / Guardian

**Presence:** Physically Present

**Description:** A ferocious Martian beast used for protection and hunting. It is characterized by short legs but incredible speed and intelligence.

**Visual Notes:** Short-legged, fast-moving predator.

**Uncertainty Notes:** Specific textures (fur, scales, skin) or color are not explicitly stated.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: the_colossal_creature

canonical_character_id: CH005 The Colossal Creature

aliases: Massive Ape-like Being

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Colossal Creature
**Role:** Antagonist / Captor

**Presence:** Physically Present

**Description:** A massive, large-scale being that captures the protagonist during his escape.

**Visual Notes:** Large, white, hairless, ape-like silhouette.

**Uncertainty Notes:** None; physical traits are clearly defined.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
