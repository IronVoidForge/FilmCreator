# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:44:54.381949+00:00
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

**Setting:** A captive's chamber decorated with beautiful murals of Martian landscapes; a deserted Martian city street; and an overlooking building.

**Characters:**
- **The Protagonist:** A human male, adventurous and physically agile (a "jumper"), currently held captive.
- **Sola:** A kind and sympathetic female Martian who provides the protagonist with food, drink, and warmth.
- **The Watch Dog:** A ferocious, short-legged but incredibly fast Martian beast used for guarding and hunting.
- **The Colossal Creature:** A large, white, hairless, ape-like being encountered at the end of the chapter.

**Events:**
- Sola leaves the protagonist under the guard of a ferocious Martian watchdog that blocks the room's exit.
- The protagonist observes the room's murals and learns about Martian biology, specifically a milk-producing plant and the extreme temperature fluctuations caused by the thin atmosphere and dual moons.
- Sola returns to feed him (cheese-like substance and plant-milk) and provides furs for warmth during the cold Martian night.
- The protagonist decides to test the watchdog's temperament by attempting to leave the room.
- The watchdog follows him at a distance until they reach the edge of the city, where it suddenly turns aggressive and charges.
- The protagonist uses his jumping ability to evade the beast, eventually leaping into a window thirty feet above the ground to escape.
- Upon entering the building through the window, the protagonist is violently grabbed by the neck and thrown to the floor by a massive, white, ape-like creature.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [Protagonist](#protagonist)
- [Sola](#sola)
- [The Watch Dog](#the-watch-dog)
- [The Colossal Creature](#the-colossal-creature)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Human male, Jumper

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Protagonist
**Role:** Captive / Adventurer

**Status:** Physically Present

**Physical Description:** A human male described as physically agile and capable of high leaps ("a jumper").

**Costume/Traits:** Not explicitly detailed in this chapter, but possesses high mobility.

**Prompt Phrases:** Human male, athletic build, agile, jumper, escaping predator.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH003 Sola

aliases: Kind Martian, Sympathetic female

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical features (hair, eyes, skin, clothing) are provided beyond her species and temperament.

clarification_required: true

clarification_reason: Physical appearance is entirely absent from the text.

clarification_question: What does Sola look like? Please provide details on her Martian physiology, hair, eye color, and typical attire.

[[SECTION markdown]]

# Sola
**Role:** Caretaker / Sympathetic Martian

**Status:** Physically Present

**Physical Description:** A female Martian; described as kind and sympathetic. No specific visual traits provided.

**Costume/Traits:** Provides furs and food to the protagonist.

**Prompt Phrases:** Female Martian, kind expression, sympathetic, caretaker.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: watchdog

canonical_character_id: CH004 Watch Dog

aliases: Ferocious beast, Guarding Martian beast

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Watch Dog
**Role:** Guard / Predator

**Status:** Physically Present

**Physical Description:** A ferocious Martian beast with short legs but incredible speed.

**Costume/Traits:** Aggressive temperament; used for guarding and hunting.

**Prompt Phrases:** Ferocious Martian beast, short-legged, extremely fast, predatory animal, aggressive hunter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: colossal_creature

canonical_character_id: CH005 Colossal Creature

aliases: Massive white ape-like creature

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Colossal Creature
**Role:** Antagonist / Encountered Threat

**Status:** Physically Present

**Physical Description:** A massive, large, white, hairless, ape-like being.

**Costume/Traits:** Extremely strong (capable of grabbing the protagonist by the neck and throwing him).

**Prompt Phrases:** Colossal creature, massive white ape, hairless primate, giant white beast, powerful limbs.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
