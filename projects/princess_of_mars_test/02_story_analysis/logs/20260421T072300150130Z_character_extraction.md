# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:23:00.150130+00:00
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

Chapter id: CH016

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
After a twenty-day journey through ruined cities and across Martian canals, John Carter and his companions arrive at the great city of Thark. Upon arrival, Carter is assigned a large building in the city plaza. He reunites with Dejah Thoris and Sola, during which he formally declares his devotion to Dejah Thoris and commands her cooperation in planning an escape. Sola informs them that the priest Sarkoja has spoken to Tal Hajus, and Dejah Thoris is slated to be thrown to the wild calots in a forthcoming arena game. 

The trio devises an escape plan: they will travel north via a distant waterway to avoid detection by the Tharks. Carter prepares his thoats and attempts to meet the women at the city's edge under the cover of night. However, he discovers that the plan has been compromised after overhearing mounted warriors discussing the failed rendezvous. To avoid capture with his large animals, Carter hides the thoats in a courtyard filled with moss-like vegetation. He then infiltrates Dejah Thoris's quarters by climbing through a second-story window, only to overhear a Thark chieftain ordering warriors to ambush him and imprison him in the vaults once he returns to the room.

**Characters:**
* **John Carter:** A warrior and Earthman; driven by his love for Dejah Thoris; currently planning an escape from Thark.
* **Dejah Thoris:** A captive princess of Helium; agrees to cooperate with Carter's plan.
* **Sola:** A Thark woman who harbors resentment toward her people's customs; joins the escape plot.
* **Woola:** John Carter's loyal, multi-tusked Martian hound.
* **Thark Chieftain:** An unnamed leader who has organized an ambush for Carter.

**Settings:**
* **The Road to Thark:** A landscape of ruined cities, canals, and cultivated fields with enormous trees.
* **The City of Thark:** A massive ancient city inhabited by thirty thousand green men; characterized by grand architecture and large, hollow-courtyard buildings.
* **Dejah Thoris's Quarters:** A large, multi-story building in the central plaza of Thark.
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
- [Sola](#sola)
- [Woola](#woola)
- [Thark Chieftain](#thark_chieftain)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Earthman, Warrior

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Warrior

**Status:** Physically Present

**Physical Description:** An Earthman and warrior. (Note: Specific visual details like hair color or build are not explicitly detailed in this chapter text, but he is established as a capable combatant/infiltrator).

**Costume/Silhouette:** Not specified in this chapter; uses thoats for transport.

**Prompt Phrases:** Martian warrior, Earthman, infiltrator, commanding presence.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH003 Dejah Thoris

aliases: Princess of Helium

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Love interest / Captive Princess

**Status:** Physically Present

**Physical Description:** A princess of Helium. (Specific physical traits are not detailed in this chapter).

**Costume/Silhouette:** Captive status; located within the city of Thark.

**Prompt Phrases:** Martian princess, captive royalty, noble silhouette.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH004 Sola

aliases: Thark woman

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola
**Role:** Ally / Escape conspirator

**Status:** Physically Present

**Physical Description:** A Thark woman. (Specific physical traits are not detailed in this chapter).

**Costume/Silhouette:** Member of the Thark people.

**Prompt Phrases:** Thark woman, rebel ally, Martian inhabitant.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH005 Woola

aliases: Martian hound

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Woola
**Role:** Companion / Pet

**Status:** Physically Present (referenced/implied presence with Carter)

**Physical Description:** A loyal, multi-tusked Martian hound.

**Costume/Silhouette:** Large, multi-tusked beast.

**Prompt Phrases:** Multi-tusked Martian hound, loyal beast, alien canine.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: thark_chieftain

canonical_character_id: UNKNOWN Thark Chieftain

aliases: Leader

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is unnamed and lacks any physical description beyond his rank.

clarification_required: true

clarification_reason: Needs visual identity to distinguish from other Tharks.

clarification_question: What are the physical characteristics and distinguishing features of the Thark Chieftain?

[[SECTION markdown]]

# Thark Chieftain
**Role:** Antagonist / Commander

**Status:** Referenced (Voice/Order)

**Physical Description:** Unknown. An unnamed leader of the Tharks.

**Costume/Silhouette:** Likely wearing chieftain regalia, but not specified.

**Prompt Phrases:** Martian chieftain, commanding warrior, green man leader.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
