# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:28:51.655721+00:00
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
The palace of Helium and the Atmosphere Plant on Barsoom. The environment shifts from a period of peace and prosperity to one of extreme atmospheric thinning and impending asphyxiation.

**Characters:**
- **John Carter:** Prince of Helium, driven by his love for Dejah Thoris to save the planet.
- **Dejah Thoris:** Princess of Helium, facing death alongside John.
- **Tardos Mors:** Jeddak of Helium, leader during the planetary crisis.
- **Sola & Tars Tarkas:** Mentioned in the context of the recent peace between Thark and Helium.
- **Woola:** The loyal Martian hound.
- **The Assistant Keeper/Assassin:** (Mentioned) The catalyst for the atmospheric failure.

**Events:**
- **Peaceful Transition:** Following a period of celebration, the Tharks return to their lands, and John Carter and Dejah Thoris enjoy several years of happiness in Helium, awaiting the hatching of their egg.
- **The Crisis:** News arrives that the keeper of the atmosphere plant has been murdered and the engine has stopped. Air pressure begins to drop rapidly across Barsoom.
- **The Descent into Death:** As the air thins, the people of Helium succumb to asphyxiation. In a sunken garden, the royal family prepares for death. Dejah Thoris falls into a coma.
- **The Revelation:** In a moment of desperation, John Carter recalls nine "thought waves"—the secret auditory key required to operate the atmosphere plant's locks.
- **The Race Against Time:** John commandeers a high-speed air-scout machine, stripping it of all weight to reach the plant faster. He flies through the thinning atmosphere at extreme velocity.
- **The Atmosphere Plant:** John arrives at the plant to find most workers dead or unconscious. Using his mental "thought waves," he successfully unlocks the three great doors. He instructs a surviving worker to restart the pumps before collapsing from exhaustion and lack of oxygen.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [John Carter](#john-carter)
- [Dejah Thoris](#dejah-thoris)
- [Tardos Mors](#tardos-mors)
- [Sola](#sola)
- [Tars Tarkas](#tars-tarkas)
- [Woola](#woola)
- [Assistant Keeper/Assassin](#assistant-keeper-assassin)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: John Carter

aliases: Prince of Helium

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist, Prince of Helium.
**Status:** Physically Present.
**Physical Description:** Driven and desperate; seen piloting a stripped-down high-speed air-scout machine through thinning atmosphere.
**Costume/Silhouette:** Not specifically detailed in this chapter beyond his role as a pilot/warrior.
**Prompt Phrases:** Martian prince, pilot of air-scout, determined expression, gasping for air.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: Princess of Helium

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Supporting Protagonist, Princess of Helium.
**Status:** Physically Present.
**Physical Description:** Succumbing to asphyxiation; enters a coma due to lack of oxygen in the sunken garden.
**Costume/Silhouette:** Royal attire (implied by status).
**Prompt Phrases:** Martian princess, unconscious, pale, lying in sunken garden.
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
**Role:** Supporting Character, Jeddak of Helium.
**Status:** Physically Present.
**Physical Description:** Leading during the planetary crisis; part of the royal group in the sunken garden.
**Costume/Silhouette:** Royal Martian leader.
**Prompt Phrases:** Jeddak, Martian ruler, elder statesman, facing atmospheric collapse.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: Sola

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned as part of the recent peace; no physical description provided in this chapter.

clarification_required: true

clarification_reason: Character is only referenced via context of a past event.

clarification_question: What are Sola's visual characteristics and current status?

[[SECTION markdown]]

# Sola
**Role:** Referenced Character.
**Status:** Referenced.
**Physical Description:** Unknown in this chapter.
**Costume/Silhouette:** Unknown.
**Prompt Phrases:** Martian woman, Thark ally (contextual).
**Uncertainty Note:** Character is mentioned only as part of the peace between Tharks and Helium; no visual details provided.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: Tars Tarkas

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Mentioned in the context of peace, but no specific physical description for this chapter's scene.

clarification_required: true

clarification_reason: Character is referenced via historical/political context rather than active presence.

clarification_question: Can you confirm Tars Tarkas's current visual state or location?

[[SECTION markdown]]

# Tars Tarkas
**Role:** Referenced Character.
**Status:** Referenced.
**Physical Description:** Unknown in this chapter.
**Costume/Silhouette:** Unknown.
**Prompt Phrases:** Thark leader, Martian warrior (contextual).
**Uncertainty Note:** Mentioned as part of the peace treaty context; no active physical presence described.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: Woola

aliases: Martian hound

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Woola
**Role:** Supporting Character, Loyal Hound.
**Status:** Physically Present (implied/mentioned).
**Physical Description:** Loyal Martian hound.
**Costume/Silhouette:** Large Martian canine.
**Prompt Phrases:** Great Martian hound, loyal beast, Barsoomian dog.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: assistant_keeper_assassin

canonical_character_id: Assistant Keeper/Assassin

aliases: The Murderer

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is defined only by their action (murder) and role (assassin); no physical description.

clarification_required: true

clarification_reason: Identity and appearance are unknown.

clarification_question: What does the assassin look like?

[[SECTION markdown]]

# Assistant Keeper/Assassin
**Role:** Antagonist (Catalyst).
**Status:** Referenced.
**Physical Description:** Unknown; responsible for the murder of the atmosphere plant keeper.
**Costume/Silhouette:** Unknown.
**Prompt Phrases:** Assassin, saboteur, killer of the keeper.
**Uncertainty Note:** Character is a shadow figure whose identity and appearance are not established in this text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
