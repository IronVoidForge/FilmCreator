# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:28:22.163917+00:00
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

**Setting:** A subterranean amphitheater within a ruined, ancient city inhabited by the Warhoon horde; later, the hills east of the city.

**Characters:**
- **John Carter:** A prisoner of the Warhoons, fighting for survival in the arena.
- **Kantos Kan:** A padwar (lieutenant) from Helium and a fellow prisoner; he provides intelligence on the search for Dejah Thoris.
- **Dak Kova:** The leader of the Warhoon horde, presiding over the games.
- **Warhoon Horde:** A bloodthirsty green Martian community hosting gladiatorial games.

**Events:**
- **Loss of Keys:** John Carter realizes his jailer's keys have been stolen by creatures in the darkness.
- **Meeting Kantos Kan:** Carter meets a fellow prisoner, Kantos Kan, who reveals that Helium has launched massive fleets to find Dejah Thoris and explains how he was captured while scouting the Warhoon city.
- **The Arena Games:** The prisoners are taken to an immense, excavated amphitheater for a ten-day tournament where only one survivor is granted freedom. Carter witnesses brutal contests between women and beasts.
- **Combat Success:** Carter dominates his matches using his superior strength and agility, eventually becoming one of the final three combatants alongside Kantos Kan and a massive northern green warrior.
- **The Final Duel:** Kantos Kan uses a specialized Martian swordsmanship technique to kill the giant warrior. 
- **The Escape Plan:** To avoid killing each other, Carter and Kantos Kan stage a fake death. Kantos Kan appears to deliver a fatal blow to Carter, but the blade misses vital organs. Kantos Kan claims his freedom, while Carter uses the cover of darkness to escape the arena and head toward the eastern hills.
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

**Physical Description:** Possesses superior Martian strength and agility compared to local inhabitants. Capable of dominating combat matches against beasts and warriors.

**Costume/Silhouette:** Likely wearing gladiatorial or prisoner attire suitable for arena combat; silhouette is athletic and powerful.

**Prompt Phrases:** Powerful human warrior, agile fighter, gladiator, survivor, intense combatant.

**Uncertainty Notes:** Specific clothing details for this specific arena sequence are not detailed beyond the context of being a prisoner/gladiator.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: kantos_kan

canonical_character_id: CH003 Kantos Kan

aliases: Padwar from Helium, Fellow Prisoner

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Kantos Kan
**Role:** Supporting Character / Padwar

**Status:** Physically Present

**Physical Description:** A Martian padwar from Helium. Skilled in specialized Martian swordsmanship techniques.

**Costume/Silhouette:** Prisoner/Gladiator attire; carries weaponry capable of lethal precision.

**Prompt Phrases:** Martian padwar, skilled swordsman, Helium soldier, agile combatant, tactical fighter.

**Uncertainty Notes:** Specific physical features (color of skin/hair) are implied by Martian biology but not explicitly detailed in this chapter text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dak_kova

canonical_character_id: CH004 Dak Kova

aliases: Leader of the Warhoon Horde

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical description or costume details provided for this leader.

clarification_required: true

clarification_reason: Needs visual identification to distinguish from general horde members.

clarification_question: What is Dak Kova's physical appearance and distinctive attire?

[[SECTION markdown]]

# Dak Kova
**Role:** Antagonist / Horde Leader

**Status:** Physically Present (Presiding)

**Physical Description:** Unknown. Identified as the leader of the Warhoon horde presiding over the games.

**Costume/Silhouette:** Unknown; likely more ornate or distinct than standard Warhoon warriors to denote leadership.

**Prompt Phrases:** Warhoon leader, presiding warlord, overseer of the arena.

**Uncertainty Notes:** Character is identified by rank and role but lacks any visual descriptors in this text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: warhoon_horde

canonical_character_id: CH005 Warhoon Horde

aliases: Green Martian Community

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Warhoon Horde
**Role:** Faction / Antagonists

**Status:** Physically Present

**Physical Description:** A bloodthirsty community of green-skinned Martians.

**Costume/Silhouette:** Aggressive, tribal, or gladiatorial aesthetic consistent with a horde inhabiting a ruined city.

**Prompt Phrases:** Green-skinned Martians, bloodthirsty horde, ancient city inhabitants, aggressive warriors.

**Uncertainty Notes:** Individual variations within the horde are not specified.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
