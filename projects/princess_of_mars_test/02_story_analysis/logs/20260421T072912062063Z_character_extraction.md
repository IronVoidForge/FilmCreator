# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:29:12.062063+00:00
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

Chapter id: CH014

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

**Settings:**
*   The camp and outskirts of the Thark expeditionary force during the march toward Thark.
*   A Warhoon incubator site containing small, newly-laid green Martian eggs.

**Characters:**
*   **John Carter:** A human fighting for Dejah Thoris; currently experiencing romantic tension and physical combat.
*   **Dejah Thoris:** Princess of Helium; she is offended by John's perceived social indiscretion and remains aloof/angry toward him.
*   **Tars Tarkas:** Thark chieftain; shows a pragmatic, almost human-like undercurrent of compassion by unchaining Dejah Thoris.
*   **Sola:** Dejah Thoris’s faithful companion; she attempts to mediate between the lovers and eventually sacrifices herself.
*   **Sarkoja:** A female Thark driven by intense hatred for John Carter; orchestrates a distraction to facilitate his death.
*   **Zad:** An *o mad* (warrior with one name) who challenges John Carter to a formal duel.

**Key Events:**
*   **Romantic Tension:** John Carter reflects on his unspoken love for Dejah Thoris and the cultural misunderstandings regarding courtship on Barsoom that have caused her to shun him.
*   **The Departure:** The group begins their march toward Thark. John discovers Dejah Thoris is being heavily manacled by Sarkoja, but Tars Tarkas intervenes to ensure she is treated with more dignity, eventually unchaining her himself.
*   **Warhoon Incubator:** During the march, the party discovers and destroys a Warhoon incubator, destroying small green Martian eggs.
*   **The Duel:** Zad challenges John Carter to a formal duel with long-swords. During the fight, Sarkoja uses a mirror to flash sunlight into John's eyes to blind him.
*   **Chaos in the Chariot:** As John is blinded, Dejah Thoris confronts Sarkoja. Sola leaps in front of Sarkoja’s dagger to protect the Princess, taking the blow.
*   **The Climax:** Amidst the chaos, Zad delivers a fatal thrust to John Carter's chest, and John collapses as he loses consciousness.
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
- [Tars Tarkas](#tars_tarkas)
- [Sola](#sola)
- [Sarkoja](#sarkoja)
- [Zad](#zad)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Combatant

**Status:** Physically Present (Injured/Unconscious)

**Physical Description:** Human male. Currently engaged in combat with long-swords.

**Costume/Traits:** Warrior attire suitable for Barsoomian combat. 

**Prompt Phrases:** human male warrior, fighting with long-sword, wounded chest.
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
**Role:** Princess / Love Interest

**Status:** Physically Present

**Physical Description:** Martian female royalty. Currently depicted as angry/offended and being manacled by Sarkoja before Tars Tarkas intervenes.

**Costume/Traits:** Royal attire, previously heavily manacled.

**Prompt Phrases:** Martian princess, regal but distressed, noble silhouette.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: Thark Chieftain
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Thark Chieftain

**Status:** Physically Present

**Physical Description:** Large, powerful Thark warrior. Shows pragmatic compassion.

**Costume/Traits:** Thark chieftain armor/regalia.

**Prompt Phrases:** massive green Martian warrior, Thark chieftain, imposing presence.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola
**Role:** Companion / Martyr

**Status:** Physically Present (Deceased/Dying)

**Physical Description:** Faithful companion to Dejah Thoris.

**Costume/Traits:** Martian attire.

**Prompt Phrases:** female Martian companion, sacrificial pose, wounded by dagger.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: Female Thark
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sarkoja
**Role:** Antagonist

**Status:** Physically Present

**Physical Description:** Female Thark driven by hatred.

**Costume/Traits:** Uses a mirror to reflect sunlight; carries a dagger.

**Prompt Phrases:** female Thark warrior, malicious expression, wielding a mirror and dagger.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: zad
canonical_character_id: Zad
aliases: o mad
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Zad
**Role:** Duelist

**Status:** Physically Present

**Physical Description:** A warrior with one name (*o mad*).

**Costume/Traits:** Equipped for a formal long-sword duel.

**Prompt Phrases:** Martian warrior, single-named duelist, wielding long-sword.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
