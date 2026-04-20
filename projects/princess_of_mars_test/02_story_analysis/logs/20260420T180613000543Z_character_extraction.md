# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:06:13.000543+00:00
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

Chapter id: CH019

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

**Setting:** A subterranean amphitheater within a ruined green Martian city; later, the hills east of the city.

**Characters:**
- **John Carter:** A prisoner of the Warhoon, fighting for survival in the arena.
- **Kantos Kan:** A padwar (lieutenant) from Helium and a fellow prisoner; becomes a close ally to Carter.
- **Dak Kova:** The leader/chieftain of the Warhoon horde.
- **Warhoon Horde:** A bloodthirsty green Martian community hosting gladiatorial games.

**Events:**
- **Loss of Keys:** After being left in darkness, John Carter realizes his jailer's keys have been stolen by creatures from the nearby lair.
- **Meeting Kantos Kan:** Carter meets a fellow prisoner, Kantos Kan of Helium. Kan provides intelligence regarding Dejah Thoris, noting that she and Sola likely escaped into the hills near a waterway. He also details the failed search efforts by Helium's fleets.
- **The Gladiatorial Games:** The prisoners are taken to an immense, excavated amphitheater for a ten-day tournament. The games involve pitting humans, green warriors, and ferocious Martian beasts against one another until only one victor remains.
- **Arena Combat:** Carter survives multiple bouts against men and beasts using his superior strength and agility. Kantos Kan survives by using a specialized long-distance sword throw to kill a massive sixteen-foot northern warrior.
- **The Escape Plan:** As the final two combatants, Carter and Kantos Kan conspire to fake Carter's death. Under the cover of darkness, Kantos Kan performs a staged killing blow that fails to strike a vital organ. 
- **Escape:** Believing Carter dead, the crowd disperses. Carter crawls from the arena and successfully reaches the hills east of the city to begin his escape.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH019

- [john_carter](#john_carter)
- [kantos_kan](#kantos_kan)
- [dak_kova](#dak_kova)
- [warhoon_horde](#warhoon_horde)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Prisoner, Gladiator

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Gladiator

**Status:** Physically Present

**Physical Description:** Possesses superior strength and agility compared to local Martians. Capable of surviving multiple bouts against men and beasts in an arena setting.

**Costume/Silhouette:** Likely wearing gladiatorial or prisoner attire suitable for combat; specific details not provided in this chapter.

**Prompt Phrases:** agile human warrior, powerful physique, survivor, gladiator.

**Uncertainty Notes:** Specific clothing/armor details are absent from this text segment.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: kantos_kan

canonical_character_id: CH020 Kantos Kan

aliases: Padwar of Helium, Fellow Prisoner

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Kantos Kan
**Role:** Ally / Padwar of Helium

**Status:** Physically Present

**Physical Description:** A warrior capable of high-skill combat; utilizes a specialized long-distance sword throw.

**Costume/Silhouette:** Prisoner attire during the games.

**Prompt Phrases:** skilled helium padwar, long-distance swordsman, tactical warrior.

**Uncertainty Notes:** Specific facial features or physical build are not detailed in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dak_kova

canonical_character_id: CH021 Dak Kova

aliases: Chieftain of the Warhoon

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided in text.

clarification_required: true

clarification_reason: Physical appearance and stature are unknown.

clarification_question: What is Dak Kova's physical appearance and what does his Warhoon chieftain attire look like?

[[SECTION markdown]]

# Dak Kova
**Role:** Antagonist / Chieftain

**Status:** Referenced (Leader of the horde)

**Physical Description:** Unknown.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** Warhoon chieftain, leader of the horde.

**Uncertainty Notes:** Character is mentioned as a leader but lacks any visual descriptors in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: warhoon_horde

canonical_character_id: CH022 Warhoon Horde

aliases: Green Martian community, Gladiators

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Warhoon Horde
**Role:** Antagonists / Spectators

**Status:** Physically Present (as a group)

**Physical Description:** A bloodthirsty green Martian community.

**Costume/Silhouette:** Gladiatorial and tribal warrior attire.

**Prompt Phrases:** green martian warriors, bloodthirsty horde, subterranean amphitheater crowd.

**Uncertainty Notes:** Individual variations within the horde are not specified.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
