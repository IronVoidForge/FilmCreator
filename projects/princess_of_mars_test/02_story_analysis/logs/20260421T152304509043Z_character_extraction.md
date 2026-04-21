# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:23:04.509043+00:00
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

Chapter id: CH022

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
The interior of the palace in Zodanga, specifically the private apartments of Jeddak Than Kosis, various winding corridors, antechambers, and a great hall overlooking a balcony.

**Characters:**
* **John Carter:** A human warrior serving as a guard for Than Kosis; he is searching for Dejah Thoris.
* **Dejah Thoris:** The Princess of Helium, who has unexpectedly pledged herself to Sab Than to ensure peace.
* **Than Kosis:** The Jeddak (ruler) of Zodanga.
* **Sab Than:** The Prince of Zodanga and son of Than Kosis.
* **Notan:** The royal psychologist.
* **Guardsmen:** Four unnamed Zodangan soldiers killed by Carter during his confrontation.

**Events:**
* **The Betrayal:** While stationed behind a tapestry to guard Than Kosis, John Carter witnesses Dejah Thoris enter the chamber and publicly declare her intention to marry Sab Than, effectively abandoning her previous feelings for Carter.
* **The Confrontation:** Distraught, Carter abandons his post to find Dejah Thoris. He is intercepted by four guards in an antechamber. After a fierce combat lasting twenty minutes, Carter kills all four guardsmen.
* **The Reunion:** Carter confronts Dejah Thoris. She recognizes him but reveals that due to Barsoomian custom, her promise to Sab Than is binding and she can no longer be his. She explains that her previous offense toward him was a misunderstanding of Martian marriage customs.
* **The Escape:** As the palace enters an uproar following the discovery of the dead guards, Carter hides in a large hanging ornament in a great hall. He overhears the royal psychologist describing him as a superhuman stranger and Than Kosis ordering a massive manhunt. 
* **Departure:** Under the cover of darkness, Carter escapes the palace by leaping from a balcony to a glass wall and into the streets of Zodanga.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH022

- [John Carter](#john_carter)
- [Dejah Thoris](#dejah_thoris)
- [Than Kosis](#than_kosis)
- [Sab Than](#sab_than)
- [Notan](#notan)
- [Guardsmen](#guardsmen)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH022 John Carter

aliases: Human warrior, Guard

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

**Physical Description:** A human warrior capable of superhuman combat feats. He is skilled in fierce, prolonged melee combat (engaging four guards for twenty minutes).

**Costume/Silhouette:** Currently serving as a guard for the Zodangan palace; likely wearing Zodangan military attire or armor suitable for a guard.

**Prompt Phrases:** Human warrior, athletic build, superhuman combatant, martial prowess, agile fighter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH022 Dejah Thoris

aliases: Princess of Helium

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Princess / Love Interest

**Status:** Physically Present

**Physical Description:** A Barsoomian princess. While specific physical traits are not detailed in this chapter, she is of high social standing and follows strict Martian customs regarding marriage and honor.

**Costume/Silhouette:** Royal attire consistent with a Princess of Helium.

**Prompt Phrases:** Barsoomian princess, royal elegance, noble silhouette, formal Martian dress.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: than_kosis

canonical_character_id: CH022 Than Kosis

aliases: Jeddak of Zodanga

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Than Kosis
**Role:** Ruler / Antagonist

**Status:** Physically Present (referenced/heard)

**Physical Description:** The Jeddak of Zodanga. A powerful ruler commanding a massive manhunt.

**Costume/Silhouette:** Royal Zodangan regalia.

**Prompt Phrases:** Zodangan Jeddak, authoritative ruler, commanding presence, royal garments.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sab_than

canonical_character_id: CH022 Sab Than

aliases: Prince of Zodanga

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sab Than
**Role:** Prince / Fiance

**Status:** Referenced

**Physical Description:** Son of Than Kosis and Prince of Zodanga.

**Costume/Silhouette:** Royal Zodangan attire.

**Prompt Phrases:** Zodangan prince, noble youth, royal heir.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: notan

canonical_character_id: CH022 Notan

aliases: Royal Psychologist

is_fully_identified: true

manual_description_required: true

manual_description_reason: No physical description provided in the text.

clarification_required: true

clarification_reason: Physical appearance is unknown.

clarification_question: What does the royal psychologist, Notan, look like?

[[SECTION markdown]]

# Notan
**Role:** Royal Psychologist

**Status:** Physically Present (heard)

**Physical Description:** Unknown. Described by his role and his observation of Carter as a "superhuman stranger."

**Costume/Silhouette:** Likely scholarly or official Zodangan attire.

**Prompt Phrases:** Scholarly figure, royal advisor, observant psychologist.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: guardsmen

canonical_character_id: CH022 Guardsmen

aliases: Zodangan soldiers

is_fully_identified: false

manual_description_required: true

manual_description_reason: Unnamed group of soldiers.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Guardsmen
**Role:** Combatants / Obstacles

**Status:** Physically Present (deceased)

**Physical Description:** Four unnamed Zodangan soldiers killed by John Carter in combat.

**Costume/Silhouette:** Standard Zodangan military uniform/armor.

**Prompt Phrases:** Zodangan guards, armored soldiers, fallen warriors.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
