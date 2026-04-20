# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:14:59.366366+00:00
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

Chapter id: CH023

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

**Setting:**
The city of Zodanga (specifically the barracks, the streets, and the sky above) and the vast expanse of a dead sea bottom during flight.

**Characters:**
* **John Carter:** An air-scout/warrior attempting to reach Helium while evading Zodangan authorities.
* **Kantos Kan:** A Heliumite air-scout who pledges his sword to assist John Carter and Sab Than.
* **Sab Than:** The ruler of Zodanga (mentioned/target).
* **Dejah Thoris:** The Princess of Helium (mentioned as the motivation for the protagonists).
* **Zodangan Sentry:** A guard at the barracks intercepted by Carter.

**Events:**
* **The Secret Meeting:** John Carter infiltrates the quarters of Kantos Kan to inform him of Dejah Thoris's engagement to Sab Than. 
* **The Pact:** Distraught by the news, Kantos Kan vows to assassinate Sab Than via a secret palace entrance known only to the ruler. The two men devise a plan: Kantos Kan will strike the palace while Carter heads for Helium.
* **The Infiltration of the Barracks:** Carter performs a perilous climb up the side of the Zodangan barracks and uses a leather strap and hook to swing onto the roof. He subdues a sentry, binds him, and hangs him over the edge to delay discovery.
* **The Aerial Chase:** After retrieving two machines from the sheds, Carter and Kantos Kan depart. As they approach the palace, they are spotted by a patrol. Carter engages in a high-speed chase through the Martian sky, utilizing Heliumite gearing to increase his machine's speed.
* **The Crash and Disorientation:** A projectile from a Zodangan cruiser hits Carter's craft, causing him to plunge toward the ground. Though he regains control, the explosion destroys his compass and speedometer.
* **Lost in the Sky:** After six hours of flight, Carter realizes he is lost. He passes several large cities but fails to find Helium, noting that he cannot identify the city by its lack of the characteristic twin scarlet and yellow towers.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH023

- [John Carter](#john_carter)
- [Kantos Kan](#kantos_kan)
- [Sab Than](#sab_than)
- [Dejah Thoris](#dejah_thoris)
- [Zodangan Sentry](#zodangan_sentry)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: John Carter

aliases: Air-scout, Warrior

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Air-scout

**Status:** Physically Present

**Description:** An air-scout and warrior. He is capable of high-stakes infiltration, climbing vertical surfaces (Zodangan barracks), and piloting aerial machines under combat conditions. 

**Traits:** Skilled climber, pilot, agile, tactical.

**Prompt Phrases:** Martian air-scout, warrior in flight gear, pilot of a small aerial machine, agile infiltrator.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: kantos_kan

canonical_character_id: Kantos Kan

aliases: Heliumite air-scout

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Kantos Kan
**Role:** Supporting Character / Ally

**Status:** Physically Present

**Description:** A Heliumite air-scout who pledges his sword to assist John Carter and Sab Than. He is motivated by the news of Dejah Thoris's engagement.

**Traits:** Vengeful, loyal to Helium, skilled with a sword.

**Prompt Phrases:** Heliumite air-scout, warrior, swordsman, pilot.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sab_than

canonical_character_id: Sab Than

aliases: Ruler of Zodanga

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned as a target/ruler; no physical description provided.

clarification_required: true

clarification_reason: Character is only referenced in dialogue and plot context.

clarification_question: What is the physical appearance and regalia of Sab Than?

[[SECTION markdown]]

# Sab Than
**Role:** Antagonist (Target)

**Status:** Referenced

**Description:** The ruler of Zodanga. He is currently engaged to Dejah Thoris, which serves as the catalyst for the chapter's conflict.

**Uncertainty Note:** No physical description or visual traits are provided in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: Princess of Helium

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned as a motivation; no physical description provided.

clarification_required: true

clarification_reason: Character is only referenced in dialogue and plot context.

clarification_question: What are the visual characteristics of Dejah Thoris?

[[SECTION markdown]]

# Dejah Thoris
**Role:** Motivation / Princess

**Status:** Referenced

**Description:** The Princess of Helium. Her engagement to Sab Than drives the actions of Kantos Kan and John Carter.

**Uncertainty Note:** No physical description or visual traits are provided in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: zodangan_sentry

canonical_character_id: Zodangan Sentry

aliases: Guard

is_fully_identified: false

manual_description_required: true

manual_description_reason: Generic guard role; no specific physical or costume details provided.

clarification_required: true

clarification_reason: Character is a generic background entity with no distinguishing features.

clarification_question: What is the standard uniform and appearance of a Zodangan Sentry?

[[SECTION markdown]]

# Zodangan Sentry
**Role:** Minor Obstacle

**Status:** Physically Present (Subdued)

**Description:** A guard at the Zodangan barracks who is intercepted and bound by John Carter.

**Uncertainty Note:** Specific physical appearance, armor, or uniform details are not described in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
