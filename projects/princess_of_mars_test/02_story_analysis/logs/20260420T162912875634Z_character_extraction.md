# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T16:29:12.875634+00:00
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

Chapter id: CH001

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

### Summary
Following the end of the Civil War, Captain John Carter and Captain James K. Powell discover a massive gold vein in the Arizona mountains. When Powell leaves to secure mining machinery, Carter witnesses suspicious movement on the trail and suspects an Apache ambush. Driven by a sense of duty, Carter pursues the trail, discovers a large Apache camp, and launches a solo charge that scatters the warriors. However, the raid reveals that Powell has been killed by arrows. In a desperate attempt to escape the pursuing Apache party, Carter flees into the mountains, eventually stumbling upon a large, ancient cave. Upon entering the cave to scout, an inexplicable and overwhelming drowsiness overcomes him.

### Characters
* **John Carter (Captain Jack Carter):** A former Confederate cavalry captain and veteran of the Sioux wars; a man driven by duty who possesses mysterious knowledge regarding Mars.
* **Captain James K. Powell:** A mining engineer and Carter's partner in prospecting; killed during an Apache ambush.

### Settings
* **Arizona Mountains/Hills:** The rugged, desolate landscape where the gold mine is located and where the pursuit takes place.
* **The Apache Camp:** A large plateau filled with hundreds of tepees and warriors.
* **The Cave:** A large, ancient-looking chamber found at the end of a high cliff trail, characterized by a smooth floor and mysterious shadows.

### Key Events
* **The Discovery:** Carter and Powell locate a million-dollar gold vein in 1865.
* **The Ambush:** Carter observes suspicious tracks and pursues what he believes is an attack on Powell.
* **The Charge:** Carter singlehandedly attacks the Apache camp, causing a rout.
* **The Death of Powell:** Carter finds his friend dead from arrow wounds.
* **The Flight and the Cave:** While fleeing pursuit, Carter enters a mysterious cave and falls into a sudden, deep sleep.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

- [John Carter](#john-carter)
- [James K. Powell](#james-k-powell)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Captain Jack Carter, Captain Carter

is_fully_identified: false

manual_description_required: true

manual_description_reason: Lacks specific facial features, build, or detailed clothing description.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter

**Role:** Protagonist; Former Confederate Cavalry Captain.

**Presence:** Physically present in Chapter 1.

**Physical Description:** A veteran of the Sioux wars; characterized by a strong sense of duty.

**Costume & Silhouette:** Implied mid-19th century cavalry attire (Confederate era).

**Uncertainty Notes:** No specific facial features, eye color, hair texture, or precise physical build are provided in the text.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: james_k_powell

canonical_character_id: CH001 James K. Powell

aliases: Captain Powell, Powell

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description or visual traits provided in the text.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# James K. Powell

**Role:** Mining Engineer; Partner to John Carter.

**Presence:** Referenced (Deceased).

**Physical Description:** No visual description available in the text.

**Uncertainty Notes:** Character is deceased within the chapter; no physical traits are established for visual continuity.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
