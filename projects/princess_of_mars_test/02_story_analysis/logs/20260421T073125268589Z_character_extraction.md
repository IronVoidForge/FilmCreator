# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:31:25.268589+00:00
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

Chapter id: CH020

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
After two weeks of wandering through the Barsoomian wilderness, surviving attacks by wild beasts with the help of his telepathic warnings and his faithful calot, Woola, the protagonist reaches a massive Atmosphere Factory. He is admitted by an invisible host who uses advanced technology to scan him. The protagonist meets an elderly Martian caretaker who reveals that the plant uses "the ninth ray" to generate the planet's atmosphere via radium pumps. 

The protagonist discovers through telepathy that the caretaker intends to murder him to protect the secret of the plant and prevent any potential disruption to the atmosphere. Using his newfound ability to mimic the nine specific thought-waves required for the facility's locks, the protagonist escapes the factory with Woola. He eventually encounters a group of hospitable Red Martian government officers on a farm. They provide him with food, rest, and disguise him (using reddish oil and a specific haircut) to look like a local Red Martian. They also provide him with a bullthoat for transport and Zodangan money, advising him to seek military service in Zodanga to establish his credibility.

**Characters:**
* **The Protagonist:** A man from Earth, physically distinct from Martians, possessing telepathic abilities that allow him to read thoughts and manipulate thought-wave locks.
* **Woola:** The protagonist's faithful, large calot who protects him from wild beasts.
* **The Caretaker:** An elderly, dried-up Martian living in isolation at the Atmosphere Factory; he is highly skilled in mental control but views the protagonist as a threat to Barsoom.
* **The Ptor Family:** A group of Red Martian government officers who provide hospitality and disguise to the protagonist.

**Settings:**
* **The Barsoomian Wilderness:** A dangerous landscape filled with strange beasts and scarce resources.
* **The Atmosphere Factory:** A massive, unassailable concrete structure (four square miles) containing the machinery and radium pumps that sustain the Martian atmosphere.
* **The Ptor Farm:** A collection of Red Martian homes raised on metal shafts to protect against danger, situated near a broad white turnpike.
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
- [Woola](#woola)
- [The Caretaker](#the-caretaker)
- [The Ptor Family](#the-ptor-family)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH020 Protagonist

aliases: Man from Earth

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance is only described in terms of being "distinct from Martians" and receiving a disguise; specific facial features, build, or hair color are not detailed.

clarification_required: true

clarification_reason: Need to establish baseline physical traits before the Red Martian disguise is applied.

clarification_question: What are the protagonist's specific Earth-based physical characteristics (height, build, hair/eye color) prior to his disguise?

[[SECTION markdown]]

# Protagonist
**Role:** Main Character / Wanderer

**Status:** Physically Present

**Physical Description:** 
A man from Earth. He is physically distinct from the native Martian populations. He possesses telepathic abilities, specifically the ability to read thoughts and mimic specific thought-wave patterns used for technological locks.

**Costume/Silhouette:** 
Initially described as a wanderer in the wilderness; later disguised by Red Martians using reddish oil and a specific local haircut to appear as a native Red Martian.

**Descriptive Noun Phrases:** 
Earthman, telepathic wanderer, disguised traveler.

**Uncertainty Notes:** 
Specific facial features and body type are unknown. Appearance is subject to change based on the "Red Martian" disguise provided by the Ptor family.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH020 Woola

aliases: Calot

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Woola
**Role:** Companion / Protector

**Status:** Physically Present

**Physical Description:** 
A large, faithful calot. Acts as a protector against wild beasts.

**Costume/Silhouette:** 
Large canine-like silhouette.

**Descriptive Noun Phrases:** 
Large calot, faithful beast, protective companion.

**Uncertainty Notes:** 
Specific color or breed-specific markings are not detailed beyond being a "large calot."

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: caretaker

canonical_character_id: CH020 Caretaker

aliases: Elderly Martian

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Caretaker
**Role:** Antagonist / Facility Worker

**Status:** Physically Present

**Physical Description:** 
An elderly, "dried-up" Martian. He is highly skilled in mental control and telepathy.

**Costume/Silhouette:** 
Lives in isolation within the Atmosphere Factory; appearance suggests long-term seclusion.

**Descriptive Noun Phrases:** 
Elderly caretaker, dried-up Martian, telepathic hermit.

**Uncertainty Notes:** 
Specific clothing or exact age is not provided beyond "elderly."

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: ptor_family

canonical_character_id: CH020 Ptor Family

aliases: Red Martian Officers

is_fully_identified: false

manual_description_required: true

manual_description_reason: They are described as a group/family of officers rather than specific individuals with distinct visual traits.

clarification_required: true

clarification_reason: Need to know if they should be rendered as a uniform group or if individual members have distinguishing features.

clarification_question: Are there specific visual distinctions between the members of the Ptor family, or should they be treated as a collective unit of Red Martian officers?

[[SECTION markdown]]

# The Ptor Family
**Role:** Supporting Characters / Hosts

**Status:** Physically Present

**Physical Description:** 
A group of hospitable Red Martian government officers.

**Costume/Silhouette:** 
Red Martian attire; they are associated with a farm consisting of homes raised on metal shafts.

**Descriptive Noun Phrases:** 
Red Martian officers, hospitable hosts, government officials.

**Uncertainty Notes:** 
Individual physical descriptions for members of the family are not provided.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
