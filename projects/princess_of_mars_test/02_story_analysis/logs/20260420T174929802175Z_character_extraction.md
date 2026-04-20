# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:49:29.802175+00:00
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

Chapter id: CH008

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

**Setting:** A deserted Martian city and its surrounding hills/valleys.

**Events:**
- As the protagonist and Sola attempt to return home after an incubator ceremony, a sudden retreat is ordered by the green Martians as twenty large, gray aerial craft approach the city.
- A fierce battle ensues between the green Martian warriors (utilizing high-accuracy ground fire from buildings) and the approaching fleet. The Martian warriors target specific components of the ships: sighting apparatus, gunners, officers, and steering gear.
- The fleet is routed, leaving only one crippled, unmanned vessel drifting erratically toward the city.
- Green Martian warriors intercept the drifting craft, haul it to the ground using grappling hooks, and systematically loot it of weapons, silks, jewels, and food/water.
- After looting, the warriors set the vessel ablaze, sending it drifting away as a "floating funeral pyre."
- The protagonist experiences a profound sense of melancholy and empathy for the defeated crew, despite their status as enemies.
- Upon returning to the city plaza, the protagonist spots the prisoner taken from the craft: a beautiful, slender, copper-skinned woman with black hair who resembles Earthly women in form.
- The woman makes a silent gesture toward the protagonist, seeking help; however, due to his ignorance of Martian customs, he fails to respond, leading her to look upon him with dejection and contempt before she is taken away.

**Characters:**
- **The Protagonist:** Observes the battle from a window; feels an unexpected empathy for the defeated aerial crew.
- **Sola:** A green Martian accompanying the protagonist.
- **Green Martian Warriors:** Highly disciplined, tactical combatants with specialized roles in warfare.
- **The Prisoner:** A beautiful, slender, copper-skinned female captive from the aerial craft; she appears to be of a different, perhaps more "humanoid" race than the green Martians.
- **Woola:** The Martian hound following the protagonist.

**Key Elements for Extraction:**
- The tactical volley of the green Martian warriors against the airships.
- The looting and subsequent destruction (burning) of the derelict craft.
- The visual encounter/eye contact between the Protagonist and the female prisoner.
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
- [Green Martian Warriors](#green-martian-warriors)
- [The Prisoner](#the-prisoner)
- [Woola](#woola)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description or specific attire provided in this chapter.

clarification_required: true

clarification_reason: Physical appearance and species/origin are unknown.

clarification_question: What is the protagonist's physical appearance, race, and clothing?

[[SECTION markdown]]

# Protagonist
**Role:** Observer / Narrator

**Status:** Physically Present

**Physical Description:** 
Unknown. The character observes the battle from a window and experiences internal emotional shifts (melancholy/empathy), but no visual traits are provided in this text.

**Costume/Silhouette:** 
Unknown.

**Uncertainty Notes:** 
Extremely high uncertainty regarding visual identity. Character is defined by their perspective and empathy rather than physical presence.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH003 Sola

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is identified as a "green Martian" but lacks specific physical details, height, or clothing.

clarification_required: true

clarification_reason: Needs specific visual traits to distinguish from generic warriors.

clarification_question: What are Sola's specific physical features and what is she wearing?

[[SECTION markdown]]

# Sola
**Role:** Companion to the Protagonist

**Status:** Physically Present

**Physical Description:** 
Identified as a green Martian. No further details on facial structure, build, or specific shade of green are provided.

**Costume/Silhouette:** 
Unknown.

**Uncertainty Notes:** 
Visuals are limited to species type; requires more detail for consistent rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: green_martian_warriors

canonical_character_id: CH004 Green Martian Warriors

aliases: Martian warriors

is_fully_identified: false

manual_description_required: true

manual_description_reason: While their color is known, their specific armor, weaponry, and physical build are not described.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Green Martian Warriors
**Role:** Combatants / Defenders of the city

**Status:** Physically Present (Group)

**Physical Description:** 
Green-skinned Martians. They exhibit high discipline and tactical coordination.

**Costume/Silhouette:** 
Not explicitly described, but they utilize high-accuracy ground fire from buildings and use grappling hooks for looting.

**Uncertainty Notes:** 
The specific aesthetic of their warfare gear (armor, weapons) is missing.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: the_prisoner

canonical_character_id: CH005 The Prisoner

aliases: Female captive

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Prisoner
**Role:** Captive from the aerial craft

**Status:** Physically Present

**Physical Description:** 
A beautiful, slender woman with copper-colored skin and black hair. Her form is noted to resemble Earthly women.

**Costume/Silhouette:** 
Not explicitly described, but she is a prisoner taken from an aerial vessel.

**Useful Phrases:** 
Copper-skinned woman, slender humanoid, black hair, Earth-like features.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH006 Woola

aliases: Martian hound

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is identified as a "Martian hound" but lacks specific size, color, or breed-like descriptions.

clarification_required: true

clarification_reason: Needs visual specification for animal design.

clarification_question: What does Woola look like (size, color, fur texture)?

[[SECTION markdown]]

# Woola
**Role:** Companion / Pet

**Status:** Physically Present

**Physical Description:** 
A Martian hound that follows the protagonist.

**Costume/Silhouette:** 
Unknown.

**Uncertainty Notes:** 
Visual appearance is limited to species designation; specific morphology is unknown.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
