# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:54:38.400306+00:00
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

**Setting:** A captive's chamber decorated with beautiful murals of Martian landscapes; later, the deserted streets and outskirts of a Martian city.

**Characters:**
- **The Protagonist:** A human male, an adventurer and skilled jumper, currently held captive.
- **Sola:** A female Martian who shows kindness and sympathy toward the protagonist, providing him with food (cheese-like substance) and milk from a large plant, and tending to him during the cold Martian nights.
- **The Watch Dog:** A ferocious, short-legged but incredibly fast Martian beast used for protection and hunting; it guards the protagonist's door.
- **The Colossal Ape-like Creature:** A large, white, hairless creature with a shock of bristly hair that captures the protagonist after his attempted escape.

**Events:**
- Sola leaves the protagonist under the guard of a ferocious Martian watchdog.
- The protagonist observes the room's murals and learns about the Martian environment, including the extreme cold at night and the influence of Mars' two moons.
- Sola returns to feed the protagonist and provides furs to protect him from the sudden temperature drops during the night.
- Seeking to test the limits of his guard, the protagonist attempts to escape the room. The watchdog follows him cautiously until they reach the edge of the city.
- The watchdog suddenly turns aggressive, charging at the protagonist with incredible speed.
- The protagonist uses his jumping ability to evade the beast, eventually leaping toward a window thirty feet above the ground.
- After successfully pulling himself onto a windowsill, the protagonist is grabbed from behind by a massive, white, ape-like creature and dragged into a building.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter CH005

- [Protagonist](#protagonist)
- [Sola](#sola)
- [The Watch Dog](#the-watch-dog)
- [The Colossal Ape-like Creature](#the-colossal-ape-like-creature)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Adventurer, Skilled Jumper

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

**Physical Description:** A human male. He is characterized by his high agility and "skilled jumping" ability, capable of leaping thirty feet vertically to reach a windowsill.

**Costume/Traits:** Currently held captive; uses furs provided by Sola for warmth against Martian night temperatures.

**Prompt Phrases:** Human male adventurer, agile jumper, athletic build, escaping captive.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH003 Sola

aliases: Female Martian

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical features (hair, eyes, skin, clothing) are described beyond her being a "female Martian."

clarification_required: true

clarification_reason: Physical appearance is entirely absent from the text.

clarification_question: What is Sola's physical appearance and what does her Martian attire look like?

[[SECTION markdown]]

# Sola
**Role:** Sympathetic Caretaker

**Status:** Physically Present

**Physical Description:** A female Martian. She shows kindness to the protagonist by providing food (cheese-like substance), milk from a large plant, and furs for warmth.

**Costume/Traits:** Unknown.

**Prompt Phrases:** Female Martian, kind expression, provider, caretaker.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: watchdog

canonical_character_id: CH004 Watch Dog

aliases: Ferocious Beast, Guard

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Watch Dog
**Role:** Guardian / Antagonist

**Status:** Physically Present

**Physical Description:** A ferocious Martian beast. It is characterized by being short-legged but possessing incredible, sudden speed.

**Costume/Traits:** Aggressive hunter/guard behavior.

**Prompt Phrases:** Ferocious Martian beast, short-legged predator, incredibly fast runner, aggressive guard animal.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: colossal_ape_creature

canonical_character_id: CH005 Colossal Ape-like Creature

aliases: Massive White Creature

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Colossal Ape-like Creature
**Role:** Captor

**Status:** Physically Present

**Physical Description:** A massive, white, hairless creature. It possesses a shock of bristly hair. It is large enough to grab the protagonist from behind and drag him easily.

**Costume/Traits:** White skin, hairless body with a patch of bristles, ape-like silhouette.

**Prompt Phrases:** Colossal white ape-like creature, massive hairless humanoid beast, bristly hair shock, powerful limbs.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
