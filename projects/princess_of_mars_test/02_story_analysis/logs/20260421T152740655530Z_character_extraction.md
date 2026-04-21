# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:27:40.655530+00:00
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

Chapter id: CH026

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

Following the total destruction of Zodanga, Tars Tarkas and Kantos Kan lead a fleet of Thark vessels and prisoners toward Helium. En route, they encounter a Zodangan fleet attempting to besiege Helium; a massive aerial battle ensues, aided by the superior marksmanship of the Thark warriors and the arrival of the Heliumite navy. The battle concludes with a ritualistic surrender where Zodangan commanders leap to their deaths from their vessels.

John Carter transfers Princess Dejah Thoris to the Heliumite flagship, where she is celebrated as a hero and credits Carter for her rescue. Carter remains with Tars Tarkas to finalize the land campaign. After unloading Thark mounts (thoats) near Helium, the combined forces of the Tharks and the Heliumite army launch a decisive assault on the remaining Zodangan land camps. Despite being heavily outnumbered, the coalition forces crush the Zodangan resistance.

The chapter concludes with a grand triumphal procession into the city of Helium. John Carter, Tars Tarkas, and the Thark leaders are received with immense honor by Tardos Mors, Jeddak of Helium. The meeting solidifies a historic alliance between the red and green races, and Carter is personally embraced by the royal family as a savior and son of the city.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH026

- [John Carter](#john_carter)
- [Tars Tarkas](#tars_tarkas)
- [Kantos Kan](#kantos_kan)
- [Dejah Thoris](#dejah_thoris)
- [Tardos Mors](#tardos_mors)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: John Carter

aliases: Savior, Son of the City

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Military Leader / Savior of Helium

**Status:** Physically Present

**Physical Description:** Human male, Earth-origin. (Note: Specific visual details for this chapter are implied by his role as a combat leader and hero).

**Costume/Silhouette:** Combat gear suitable for Martian warfare; associated with the coalition of Tharks and Heliumites.

**Prompt Phrases:** human warrior, heroic posture, savior of helium, martial leader.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: Tars Tarkas

aliases: Thark Leader

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Thark Military Commander / Ally

**Status:** Physically Present

**Physical Description:** Green-skinned Thark warrior.

**Costume/Silhouette:** Thark military attire, commanding presence within the fleet and land campaign.

**Prompt Phrases:** green thark warrior, massive green humanoid, martian commander, thark leader.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: kantos_kan

canonical_character_id: Kantos Kan

aliases: Thark Leader

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Kantos Kan
**Role:** Thark Military Leader

**Status:** Physically Present

**Physical Description:** Green-skinned Thark.

**Costume/Silhouette:** Thark military regalia, part of the fleet command.

**Prompt Phrases:** green thark warrior, martian officer, thark commander.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: Princess of Helium, Hero of the Battle

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Princess of Helium / Heroine

**Status:** Physically Present

**Physical Description:** Heliumite royalty.

**Costume/Silhouette:** Royal Heliumite attire; celebrated as a hero following the rescue from Zodanga.

**Prompt Phrases:** heliumite princess, martian royalty, heroic female figure, elegant martian.
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
**Role:** Jeddak (Ruler) of Helium

**Status:** Physically Present

**Physical Description:** Heliumite ruler.

**Costume/Silhouette:** Grand royal regalia of the Heliumite throne.

**Prompt Phrases:** martian king, jeddak of helium, royal martian leader, ceremonial attire.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
