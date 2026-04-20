# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:00:00.985617+00:00
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

John Carter attempts to retrieve keys from his dead jailer but discovers they are gone, realizing Dejah Thoris and Sola have been taken by the Tharks to be devoured. He meets Kantos Kan, a fellow prisoner and Helium Navy Lieutenant, who shares details about the failed expedition and the ongoing search for the princess. Both are dragged to the Thark amphitheater for the arena games. Carter fights through various beasts and warriors, eventually facing Kantos Kan in the final match. They collude to escape; Carter pretends to die so Kan can claim freedom. Carter escapes into the hills east of the city while Kan leaves him there.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- **John Carter** - Protagonist, physically referenced and present in arena sequence
- **Dejah Thoris** - Princess of Helium, mentioned as taken by Tharks
- **Sola** - Companion of Dejah Thoris, mentioned as taken by Tharks  
- **Kantos Kan** - Helium Navy Lieutenant, fellow prisoner and final match opponent

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# John Carter

**Chapter Role:** Protagonist, arena fighter, escapee

**Physical Presence:** Referenced and present in chapter sequence

**Description:** Main character attempting to retrieve keys from dead jailer, meets Kantos Kan as fellow prisoner, fights through beasts and warriors in Thark amphitheater arena games. Colludes with Kantos Kan to escape; pretends to die so Kan can claim freedom. Escapes into hills east of city.

**Continuity Notes:** Central figure in failed expedition aftermath, Helium Navy connection implied through Kantos Kan's introduction.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH002 Dejah Thoris

aliases: Princess of Helium, Sola's companion

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned as taken by Tharks; no physical description in chapter.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is Dejah Thoris's physical form and origin?

[[SECTION markdown]]

# Dejah Thoris

**Chapter Role:** Princess of Helium, mentioned character

**Physical Presence:** Referenced only (taken by Tharks)

**Description:** Princess of Helium who has been taken by the Tharks to be devoured. Mentioned alongside Sola as victims of the Thark expedition aftermath.

**Continuity Notes:** Central figure in failed expedition narrative; captured status drives chapter tension.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH003 Sola

aliases: Dejah Thoris's companion, Princess's attendant

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned as taken by Tharks; no physical description in chapter.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is Sola's physical form and origin?

[[SECTION markdown]]

# Sola

**Chapter Role:** Dejah Thoris's companion, mentioned character

**Physical Presence:** Referenced only (taken by Tharks)

**Description:** Companion of Dejah Thoris who has been taken by the Tharks to be devoured. Mentioned alongside Dejah Thoris as victims of the Thark expedition aftermath.

**Continuity Notes:** Associated with Dejah Thoris in captivity narrative; both mentioned together as taken prisoners.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: kantos_kan

canonical_character_id: CH004 Kantos Kan

aliases: Helium Navy Lieutenant, fellow prisoner

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is Kantos Kan's physical form and origin?

[[SECTION markdown]]

# Kantos Kan

**Chapter Role:** Helium Navy Lieutenant, fellow prisoner, final match opponent

**Physical Presence:** Referenced and present in chapter sequence

**Description:** Fellow prisoner and Helium Navy Lieutenant who shares details about failed expedition. Opponent in final arena match against John Carter. Colludes with Carter to escape; claims freedom while Carter pretends to die. Leaves Carter in hills east of city.

**Continuity Notes:** Connected to failed expedition narrative through shared knowledge; serves as both antagonist and ally in escape sequence.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_PACKET]]
````
