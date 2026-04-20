# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:00:12.087960+00:00
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

Chapter id: CH015

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

After surviving a near-fatal sword thrust from Zad, John Carter is treated by his retinue of Martian women. He discovers that Dejah Thoris is in deep mourning, believing him to be dead. As the massive caravan moves silently across a moss-covered sea bottom toward a range of hills, Carter meets with Sola.

Sola shares the tragic and unconventional history of her parentage. She reveals that her mother, a sensitive Thark woman who felt alienated from her cruel society, fell in love with a warrior and raised Sola in secret within an ancient tower to protect her from the judgment of their people. The secrecy was shattered when Sarkoja discovered them; despite torture by Tal Hajus, Sola's mother remained silent to protect her daughter, eventually dying after successfully hiding Sola among a group of young Tharks. Sola concludes her story by revealing that her father—a man driven by a desire for vengeance against Tal Hajus—is none other than Tars Tarkas.
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
- [Zad](#zad)
- [Dejah Thoris](#dejah_thoris)
- [Sola](#sola)
- [Sola's Mother](#sola_mother)
- [Sarkoja](#sarkoja)
- [Tal Hajus](#tal_hajus)
- [Tars Tarkas](#tars_tarkas)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist

**Status:** Physically Present

**Description:** A survivor of a near-fatal sword thrust. Currently being treated by Martian women.

**Prompt Phrases:** Human male, wounded warrior, survivor.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: zad

canonical_character_id: UNKNOWN Zad

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned as the attacker; no physical description provided.

clarification_required: true

clarification_reason: Identity and appearance unknown.

clarification_question: What is Zad's physical appearance and affiliation?

[[SECTION markdown]]

# Zad
**Role:** Antagonist (referenced)

**Status:** Referenced

**Description:** An individual who attempted to kill John Carter with a sword thrust.

**Prompt Phrases:** Sword wielder, attacker.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH003 Dejah Thoris

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Supporting Character

**Status:** Physically Present (referenced in scene)

**Description:** Currently in a state of deep mourning, believing John Carter to be dead.

**Prompt Phrases:** Mourning woman, Martian noblewoman.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH004 Sola

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola
**Role:** Supporting Character

**Status:** Physically Present

**Description:** Daughter of a Thark woman and Tars Tarkas. Raised in secrecy within an ancient tower.

**Prompt Phrases:** Half-Thark, daughter of Tars Tarkas, secret upbringing.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola_mother

canonical_character_id: UNKNOWN Sola's Mother

aliases: Sensitive Thark woman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Described only by temperament (sensitive/alienated); no physical traits provided.

clarification_required: true

clarification_reason: Physical appearance is unknown.

clarification_question: What did Sola's mother look like?

[[SECTION markdown]]

# Sola's Mother
**Role:** Referenced Character

**Status:** Referenced (deceased)

**Description:** A sensitive Thark woman who felt alienated from her society. She died after protecting Sola from the judgment of her people.

**Prompt Phrases:** Sensitive Thark, martyr, deceased mother.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: UNKNOWN Sarkoja

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Mentioned as the one who discovered Sola's mother; no physical description.

clarification_required: true

clarification_reason: Appearance unknown.

clarification_question: What is Sarkoja's appearance?

[[SECTION markdown]]

# Sarkoja
**Role:** Referenced Character

**Status:** Referenced

**Description:** The individual who discovered the secret relationship between Sola's mother and her father.

**Prompt Phrases:** Discoverer, antagonist figure.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tal_hajus

canonical_character_id: UNKNOWN Tal Hajus

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Mentioned as a torturer; no physical description.

clarification_required: true

clarification_reason: Appearance unknown.

clarification_question: What is Tal Hajus's appearance?

[[SECTION markdown]]

# Tal Hajus
**Role:** Referenced Character

**Status:** Referenced

**Description:** A character who tortured Sola's mother; the object of Tars Tarkas's vengeance.

**Prompt Phrases:** Torturer, vengeful target.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH005 Tars Tarkas

aliases: Sola's Father

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Supporting Character

**Status:** Referenced

**Description:** A warrior driven by a desire for vengeance against Tal Hajus; father of Sola.

**Prompt Phrases:** Thark warrior, vengeful father.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
