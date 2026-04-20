# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T16:57:47.548401+00:00
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

**Characters:**
* **The Protagonist:** A human captive with exceptional jumping abilities and an adventurous spirit.
* **Sola:** A Martian female who shows the protagonist kindness, sympathy, and care.
* **The Watchdog:** A ferocious, incredibly fast, and loyal Martian beast used for hunting and protection.
* **The Ape-like Creature:** A massive, white, hairless, and intimidating creature encountered at the end of the chapter.

**Settings:**
* **The Prisoner's Chamber:** A room decorated with beautiful murals depicting Martian landscapes (mountains, rivers, gardens) but devoid of living creatures.
* **Martian City Streets:** Deserted streets characterized by sudden temperature shifts and illuminated by moons or primitive oil lamps.
* **Building Ledge/Window:** A high vantage point thirty feet above the ground used during an escape attempt.

**Key Events:**
1. **The Guarded Captivity:** After Sola leaves him, the protagonist is left alone with a ferocious Martian watchdog that guards the threshold of his room.
2. **Observations of Mars:** While alone, the protagonist examines the room's murals and learns about Martian biology, specifically a large plant that produces milk-like liquid. He also notes the extreme cold of Martian nights and the influence of the two moons on nocturnal illumination.
3. **The Escape Attempt:** Seeking to test the watchdog's temperament, the protagonist attempts to leave the room. The dog follows him through the streets but suddenly turns to block his exit from the city limits with a ferocious charge.
4. **The High-Speed Chase:** A pursuit ensues where the protagonist uses his agility to evade the incredibly fast beast, eventually leaping into a high window of a nearby building.
5. **The Ambush:** Just as the protagonist believes he has reached safety on the windowsill, he is violently grabbed and dragged back into a room by a colossal, white, ape-like creature.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

* [Protagonist](#protagonist)
* [Sola](#sola)
* [Watchdog](#watchdog)
* [Ape-like Creature](#ape-like-creature)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH005 Protagonist

aliases: []

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical features, facial details, hair, or clothing are described.

clarification_required: true

clarification_reason: Needs visual identification for character design.

clarification_question: What is the protagonist's physical appearance, age, and attire?

[[SECTION markdown]]

# Protagonist

**Role:** Human captive and escapee.

**Presence:** Physically present.

**Description:** A human with exceptional jumping abilities and an adventurous spirit.

**Uncertainty Notes:** Physical phenotype, clothing, and facial features are entirely unstated in this chapter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH005 Sola

aliases: []

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical features, skin color, or clothing are described.

clarification_required: true

clarification_reason: Needs visual identification for character design.

clarification_question: What does Sola look like (skin, eyes, hair) and what is she wearing?

[[SECTION markdown]]

# Sola

**Role:** Martian female; provider of care/kindness.

**Presence:** Referenced (leaves the protagonist at the start of the chapter).

**Description:** A Martian female characterized by her kindness, sympathy, and care toward the protagonist.

**Uncertainty Notes:** No visual or biological details are provided beyond her species and temperament.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: watchdog

canonical_character_id: CH005 Watchdog

aliases: []

is_fully_identified: false

manual_description_required: true

manual_description_reason: No visual description of size, color, or anatomy is provided.

clarification_required: true

clarification_reason: Needs physical traits for creature design.

clarification_question: What are the physical characteristics (size, color, texture, species-like features) of the Martian watchdog?

[[SECTION markdown]]

# Watchdog

**Role:** Guard and hunter.

**Presence:** Physically present.

**Description:** A ferocious, incredibly fast, and loyal Martian beast used for hunting and protection.

**Uncertainty Notes:** While its behavior (ferocity/speed) is known, its visual appearance is completely unknown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: ape_like_creature

canonical_character_id: CH005 Ape-like Creature

aliases: []

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_question: ""

[[SECTION markdown]]

# Ape-like Creature

**Role:** Ambush predator.

**Presence:** Physically present.

**Description:** A massive, white, hairless, and intimidating creature.

**Uncertainty Notes:** None; physical traits (size, color, texture) are sufficiently established.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
