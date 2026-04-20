# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:25:43.882143+00:00
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

Chapter id: CH027

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
The palace in Helium (including the rooftop shrine and sunken garden) and the massive, fortified Atmosphere Plant.

**Characters:**
* **John Carter:** Prince of Helium; hero of Barsoom.
* **Dejah Thoris:** Princess of Helium; John Carter's wife.
* **Tardos Mors:** Jeddak (Ruler) of Helium.
* **Woola:** The loyal Martian hound.
* **Sola & Tars Tarkas:** Mentioned in the context of the recent peace treaty.
* **The Assistant Keeper/Assassin:** Mentioned as the cause of the crisis.
* **A surviving technician:** An unnamed man at the Atmosphere Plant.

**Events:**
* **Peace and Prosperity:** Following a period of peace with the Tharks, John Carter and Dejah Thoris live in happiness for nine years, awaiting the hatching of their egg in a golden incubator.
* **The Crisis:** A dispatch bearer arrives with news that the keeper of the Atmosphere Plant has been murdered and the plant's engine has stopped. Air pressure across Barsoom begins to drop rapidly.
* **The Approaching Death:** As the air thins, the people of Helium face mass asphyxiation. In a sunken garden, the royal family prepares for death. Dejah Thoris falls into a coma near their egg incubator.
* **The Revelation:** In a moment of desperation, John Carter recalls nine "thought waves"—a mental key to the Atmosphere Plant's locks.
* **The Race Against Time:** John Carter commandeers a high-speed air-scout machine, stripping it of all weight to maximize speed. He flies through the thinning atmosphere toward the plant.
* **The Breach:** Arriving at the plant, John finds most workers dead or unconscious. Using his mental "thought waves," he successfully unlocks the three great doors. He instructs a surviving technician to restart the pumps before collapsing from exhaustion and lack of oxygen.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [John Carter](#john_carter)
- [Dejah Thoris](#dejah_thoris)
- [Tardos Mors](#tardos_mors)
- [Woola](#woola)
- [Sola](#sola)
- [Tars Tarkas](#tars_tarkas)
- [Assistant Keeper/Assassin](#assistant_keeper_assassin)
- [Surviving Technician](#surviving_technician)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: John Carter

aliases: Prince of Helium, Hero of Barsoom

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist; Prince of Helium.
**Presence:** Physically present.
**Physical Description:** Heroic Martian figure, capable of high-speed flight and mental "thought wave" manipulation.
**Costume/Silhouette:** Not explicitly detailed in this chapter, but associated with royal status and air-scout piloting.
**Prompt Phrases:** Martian hero, pilot of air-scout machine, intense focus, mental projection.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: Princess of Helium, John Carter's wife

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Supporting Character; Princess of Helium.
**Presence:** Physically present.
**Physical Description:** Royal Martian woman; currently in a coma due to oxygen deprivation.
**Costume/Silhouette:** Associated with the royal palace and golden egg incubator.
**Prompt Phrases:** Martian princess, regal, unconscious, lying near golden incubator.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tardos_mors

canonical_character_id: Tardos Mors

aliases: Jeddak of Helium

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tardos Mors
**Role:** Supporting Character; Jeddak (Ruler) of Helium.
**Presence:** Physically present.
**Physical Description:** Martian ruler, part of the royal family in the sunken garden.
**Costume/Silhouette:** Royal attire.
**Prompt Phrases:** Martian ruler, Jeddak, elder statesman.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: Woola

aliases: The loyal Martian hound

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Woola
**Role:** Supporting Character; Loyal Martian hound.
**Presence:** Physically present.
**Physical Description:** Large, loyal Martian canine.
**Costume/Silhouette:** Animal form.
**Prompt Phrases:** Giant Martian hound, loyal beast, Barsoomian dog.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: Sola

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Mentioned only in context of a treaty; no physical description provided.

clarification_required: true

clarification_reason: Character is referenced but not visually described in this chapter.

clarification_question: What are Sola's physical characteristics and appearance?

[[SECTION markdown]]

# Sola
**Role:** Referenced Character.
**Presence:** Referenced.
**Physical Description:** Unknown.
**Costume/Silhouette:** Unknown.
**Prompt Phrases:** Martian woman (uncertain details).
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: Tars Tarkas

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Mentioned only in context of a treaty; no physical description provided.

clarification_required: true

clarification_reason: Character is referenced but not visually described in this chapter.

clarification_question: What are Tars Tarkas's physical characteristics and appearance?

[[SECTION markdown]]

# Tars Tarkas
**Role:** Referenced Character.
**Presence:** Referenced.
**Physical Description:** Unknown.
**Costume/Silhouette:** Unknown.
**Prompt Phrases:** Thark warrior (uncertain details).
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: assistant_keeper_assassin

canonical_character_id: The Assistant Keeper/Assassin

aliases: Murderer, Killer of the keeper

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is identified by role/action but lacks any physical description.

clarification_required: true

clarification_reason: Identity and appearance are unknown.

clarification_question: What does the assassin look like?

[[SECTION markdown]]

# Assistant Keeper/Assassin
**Role:** Antagonist (referenced).
**Presence:** Referenced.
**Physical Description:** Unknown; responsible for the murder at the Atmosphere Plant.
**Costume/Silhouette:** Unknown.
**Prompt Phrases:** Mysterious assassin, killer of the keeper.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: surviving_technician

canonical_character_id: Surviving Technician

aliases: Unnamed man

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is an unnamed worker with no physical description.

clarification_required: true

clarification_reason: No visual details provided beyond occupation.

clarification_question: What is the appearance and age of the surviving technician?

[[SECTION markdown]]

# Surviving Technician
**Role:** Minor Character.
**Presence:** Physically present (briefly).
**Physical Description:** Unnamed man, worker at the Atmosphere Plant; exhausted/struggling with low oxygen.
**Costume/Silhouette:** Worker's attire.
**Prompt Phrases:** Martian technician, gasping for air, worker in atmosphere plant.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
