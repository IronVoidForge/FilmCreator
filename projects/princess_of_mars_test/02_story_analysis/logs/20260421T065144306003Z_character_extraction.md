# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:51:44.306003+00:00
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

Chapter id: CH004

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

**Events:**
The protagonist and his captor, Tars Tarkas, travel across a rising landscape toward a massive, deserted city situated on a table land. Upon entering the city, they find it inhabited by hundreds of Green Martians living in ruins that appear much older and more sophisticated than the current inhabitants. The party arrives at a magnificent marble edifice to meet with the local chieftain. After an introduction involving customary greetings, the protagonist is forced to perform for the assembled warriors. He initially struggles with movement, causing amusement among the Martians, but he earns their respect by striking a Martian who treated him roughly. The chapter concludes with a demonstration of "sak" (jumping), where the protagonist successfully performs a massive leap. Seeking food and water, he is led by a female Martian named Sola to a sleeping chamber, where he encounters a small, ten-legged creature resembling a frog-like pony.

**Characters:**
* **The Protagonist:** A human survivor, currently a prisoner, attempting to navigate Martian customs through observation and physical prowess.
* **Tars Tarkas:** A high-ranking Green Martian (vice-chieftain) who acts as the protagonist's escort and statesman.
* **The Chieftain:** The ruler of the local community, adorned in elaborate metal and feather ornaments.
* **Sola:** A young female Martian of Tars Tarkas's retinue; she is light olive-green and serves as the protagonist's guide to his quarters.
* **The Warriors/Martians:** A violent, highly physical race characterized by their tusks, varying heights (10-12 feet for females), and a culture that finds humor in death and struggle.

**Settings:**
* **The Deserted City:** An enormous, ancient city on a table land featuring ruins of a much older, more advanced civilization.
* **The Audience Chamber:** A massive marble building inlaid with gold and jewels, containing human-sized furniture that is incongruously small for the large Martians.
* **The Plaza:** A central open area used for public demonstrations and gatherings.
* **Sola's Quarters:** A spacious, well-lit room decorated with murals and mosaics, filled with silks and furs.
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
- [Tars Tarkas](#tars-tarkas)
- [The Chieftain](#the-chieftain)
- [Sola](#sola)
- [Green Martians](#green-martians)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH004 Protagonist

aliases: Human survivor, Prisoner

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical description (hair color, eye color, build, clothing) is provided in this chapter.

clarification_required: true

clarification_reason: Physical appearance and current attire are unknown.

clarification_question: What is the protagonist's hair/eye color, build, and what is he wearing?

[[SECTION markdown]]

# Protagonist

**Role:** Human survivor and prisoner.

**Status:** Physically present.

**Physical Description:** Unknown. He is capable of performing "sak" (massive leaps) and possesses enough strength to strike a Martian warrior.

**Costume/Silhouette:** Not described.

**Descriptive Noun Phrases:** Human survivor, leaping prisoner, struggling outsider.

**Uncertainty Notes:** Complete lack of visual data regarding facial features or clothing.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH004 Tars Tarkas

aliases: Vice-chieftain, Escort

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas

**Role:** High-ranking Green Martian (vice-chieftain) and escort to the protagonist.

**Status:** Physically present.

**Physical Description:** A Green Martian; high-ranking status implied by his role as a statesman/escort.

**Costume/Silhouette:** Not explicitly detailed in this chapter, but carries the authority of a vice-chieftain.

**Descriptive Noun Phrases:** Green Martian leader, vice-chieftain, statesman.

**Uncertainty Notes:** Specific facial features or clothing details are not provided in this text segment.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: chieftain

canonical_character_id: CH004 Chieftain

aliases: Local ruler

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Chieftain

**Role:** Ruler of the local Martian community.

**Status:** Physically present.

**Physical Description:** A large Green Martian.

**Costume/Silhouette:** Adorned in elaborate metal and feather ornaments.

**Descriptive Noun Phrases:** Ornately dressed chieftain, feathered ruler, Martian leader.

**Uncertainty Notes:** Specific patterns of the metal or feathers are not described.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH004 Sola

aliases: Guide

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola

**Role:** Young female Martian; guide to the protagonist.

**Status:** Physically present.

**Physical Description:** Light olive-green skin. Part of Tars Tarkas's retinue.

**Costume/Silhouette:** Not explicitly described.

**Descriptive Noun Phrases:** Light olive-green female Martian, young guide.

**Uncertainty Notes:** Specific clothing or height relative to others is not detailed.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: green_martians

canonical_character_id: CH004 Green Martians

aliases: Warriors, Martians

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Green Martians

**Role:** The local inhabitants and warrior class.

**Status:** Physically present (hundreds).

**Physical Description:** Large-statured beings with tusks. Females are noted to be between 10-12 feet tall. Skin is green.

**Costume/Silhouette:** Characterized by a violent, highly physical culture; presence in ruins of an older civilization.

**Descriptive Noun Phrases:** Tusked warriors, giant green humanoids, 12-foot females.

**Uncertainty Notes:** Specific clothing styles for the general population are not detailed.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
