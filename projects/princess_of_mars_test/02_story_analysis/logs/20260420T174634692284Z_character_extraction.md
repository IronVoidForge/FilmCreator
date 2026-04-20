# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:46:34.692783+00:00
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

Chapter id: CH006

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

**Setting:** An interior chamber within a Martian building, overlooking a plaza.

**Characters:**
- **The Protagonist:** An Earthman fighting for survival.
- **The Watch-thing:** The protagonist's loyal, multi-legged, beast-like guardian.
- **The Ape-creatures:** Two massive, ten-to-fifteen-foot tall, four-armed creatures resembling gorillas.
- **Tars Tarkas:** A Martian warrior who respects physical prowess.
- **Sola:** A Martian woman who shows compassion and solicitude toward the protagonist.
- **Martian Warriors:** A group of warriors observing the combat.

**Events:**
- The protagonist is pinned by one massive ape-creature while its mate approaches with a stone cudgel to kill him.
- The protagonist's "watch-thing" intervenes, engaging the second ape in a brutal, life-or-death struggle.
- As the watch-thing begins to lose the fight due to the ape's superior strength, the protagonist seizes the fallen cudgel and kills the first ape by crushing its skull.
- The second ape, enraged by its mate's death, charges the protagonist. Despite the overwhelming odds, the protagonist stays to defend his dying watch-thing.
- Using earthly combat tactics (striking the chin and stomach), the protagonist incapacitates the second ape and kills it with the cudgel.
- Tars Tarkas, Sola, and a group of warriors arrive, having witnessed the fight. They applaud the protagonist's bravery, viewing his combat as a display of high status.
- While Sola shows genuine concern for the protagonist's well-being, the other Martians laugh at the spectacle.
- A Martian warrior attempts to execute the wounded watch-thing; the protagonist intervenes by striking the warrior's arm, preventing the shot.
- Tars Tarkas allows the protagonist to keep his beast, and the protagonist departs into the plaza with Sola and his loyal creature.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH006

- [Protagonist](#protagonist)
- [The Watch-thing](#the-watch-thing)
- [Ape-creature 1](#ape-creature-1)
- [Ape-creature 2](#ape-creature-2)
- [Tars Tarkas](#tars-tarkas)
- [Sola](#sola)
- [Martian Warriors](#martian-warriors)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH001 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance, clothing, and specific facial features are not described in this chapter.

clarification_required: true

clarification_reason: Identity and physical traits need confirmation for visual consistency.

clarification_question: What is the protagonist's hair color, eye color, build, and current attire?

[[SECTION markdown]]

# Protagonist
**Role:** Central combatant / Survivor

**Status:** Physically Present

**Physical Description:** An Earthman of significant physical prowess and combat skill. He demonstrates high endurance and tactical intelligence in hand-to-hand combat.

**Costume/Silhouette:** Unknown.

**Descriptive Noun Phrases:** Earthman survivor, skilled combatant, defender of the watch-thing.

**Uncertainty Notes:** No specific visual details regarding his face or clothing are provided in this text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: watch_thing

canonical_character_id: CH003 Watch-thing

aliases: Beast, Guardian, Loyal creature

is_fully_identified: false

manual_description_required: true

manual_description_reason: While described as multi-legged and beast-like, specific colors, textures, or exact anatomy are missing.

clarification_required: true

clarification_reason: Needs more detail for consistent rendering of the creature's skin/fur and limb structure.

clarification_question: What is the color, texture (fur vs scales), and specific number of legs for the watch-thing?

[[SECTION markdown]]

# The Watch-thing
**Role:** Protagonist's guardian

**Status:** Physically Present (Wounded)

**Physical Description:** A multi-legged, beast-like creature. It is capable of engaging massive creatures in brutal combat.

**Costume/Silhouette:** Multi-legged beast silhouette.

**Descriptive Noun Phrases:** Multi-legged guardian, loyal beast, wounded Martian pet.

**Uncertainty Notes:** Specific biological details (scales, fur, color) are not specified.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: ape_creature_1

canonical_character_id: CH004 Ape-creature

aliases: First ape

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Ape-creature 1
**Role:** Antagonist (Deceased)

**Status:** Physically Present (Dead)

**Physical Description:** A massive, ten-to-fifteen-foot tall creature with four arms. Resembles a giant gorilla.

**Costume/Silhouette:** Massive, four-armed primate silhouette.

**Descriptive Noun Phrases:** Giant four-armed ape, massive gorilla-like creature, heavy combatant.

**Uncertainty Notes:** None.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: ape_creature_2

canonical_character_id: CH004 Ape-creature

aliases: Second ape, mate

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Ape-creature 2
**Role:** Antagonist (Deceased)

**Status:** Physically Present (Dead)

**Physical Description:** A massive, ten-to-fifteen-foot tall creature with four arms. Resembles a giant gorilla. Enraged by the death of its mate.

**Costume/Silhouette:** Massive, four-armed primate silhouette.

**Descriptive Noun Phrases:** Enraged four-armed ape, massive gorilla-like creature.

**Uncertainty Notes:** None.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH005 Tars Tarkas

aliases: Martian warrior

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance of the Martian is not described.

clarification_required: true

clarification_reason: Needs visual description for Martian physiology and armor.

clarification_question: What does Tars Tarkas look like (skin color, facial features, clothing/armor)?

[[SECTION markdown]]

# Tars Tarkas
**Role:** Martian observer / Leader figure

**Status:** Physically Present

**Physical Description:** A Martian warrior who values physical prowess and bravery. He shows respect to the protagonist's combat skills.

**Costume/Silhouette:** Unknown.

**Descriptive Noun Phrases:** Respected Martian warrior, combat observer.

**Uncertainty Notes:** No visual details provided for his specific appearance or attire.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH006 Sola

aliases: Martian woman

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided.

clarification_required: true

clarification_reason: Needs visual details for character design.

clarification_question: What is Sola's appearance, hair, and clothing?

[[SECTION markdown]]

# Sola
**Role:** Compassionate Martian observer

**Status:** Physically Present

**Physical Description:** A Martian woman who displays compassion and solicitude toward the protagonist.

**Costume/Silhouette:** Unknown.

**Descriptive Noun Phrases:** Compassionate Martian woman, caring observer.

**Uncertainty Notes:** No physical or costume details are present in the text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_warriors

canonical_character_id: CH007 Martian Warriors

aliases: Group of warriors

is_fully_identified: false

manual_description_required: true

manual_description_reason: They are a collective group with no individual descriptions.

clarification_required: true

clarification_reason: General aesthetic for the warrior class is needed.

clarification_question: What is the standard appearance and armor of the Martian warrior class?

[[SECTION markdown]]

# Martian Warriors
**Role:** Observers / Crowd

**Status:** Physically Present

**Physical Description:** A group of Martians who observe the combat, some laughing at the spectacle and others applauding.

**Costume/Silhouette:** Unknown.

**Descriptive Noun Phrases:** Group of Martian warriors, observing crowd.

**Uncertainty Notes:** No specific visual details for the group or their equipment.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
