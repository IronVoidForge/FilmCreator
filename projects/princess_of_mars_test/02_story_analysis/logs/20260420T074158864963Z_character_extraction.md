# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:41:58.864963+00:00
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

In this chapter, John Carter recovers consciousness after being stabbed by Zad, a weapon wielded by Sarkoja. He removes the blade and tends to his wounds using Martian healing agents provided by Dejah Thoris's women. Upon visiting Sola and Dejah, he learns Dejah is weeping in grief, believing him dead due to her prideful nature. Carter promises to respect her feelings until she speaks. Later, while traveling with Tars Tarkas in the massive silent caravan of chariots and animals across the mossy sea bottom, Carter meets Sola again at night. She requests he listen to her story about her parents. Sola recounts how her mother, a small and compassionate green Martian woman, fell in love with a warrior named Tars Tarkas while hiding an egg in an ancient tower. They kept their love secret for years until Sarkoja discovered them. To save the child, the mother lied about the father's identity to Sarkoja before escaping with Sola into the returning caravan of young Tharks. The mother was subsequently imprisoned and tortured by Tal Hajus, dying without revealing the father's name. Sola reveals that her father is indeed Tars Tarkas, who has been waiting for his chance to avenge his wife and kill Tal Hajus. She entrusts Carter with this secret, trusting his discretion despite his reputation for truthfulness.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

## John Carter (protagonist)
- **Asset ID:** protagonist
- **Canonical Character ID:** CH002 Protagonist
- **Aliases:** Narrator, Conscious Entity
- **Fully Identified:** false
- **Manual Description Required:** true
- **Clarification Required:** true

## Zad (weapon wielder)
- **Asset ID:** zad_weapon_wielder
- **Canonical Character ID:** CH015 Zad
- **Aliases:** None
- **Fully Identified:** false
- **Manual Description Required:** true
- **Clarification Required:** true

## Sarkoja (mentioned antagonist)
- **Asset ID:** sarkoja_antagonist
- **Canonical Character ID:** CH015 Sarkoja
- **Aliases:** None
- **Fully Identified:** false
- **Manual Description Required:** true
- **Clarification Required:** true

## Dejah Thoris (weeping figure)
- **Asset ID:** dejah_thoris_weeping
- **Canonical Character ID:** CH015 Dejah Thoris
- **Aliases:** None
- **Fully Identified:** false
- **Manual Description Required:** true
- **Clarification Required:** true

## Sola (storyteller)
- **Asset ID:** sola_storyteller
- **Canonical Character ID:** CH015 Sola
- **Aliases:** None
- **Fully Identified:** false
- **Manual Description Required:** true
- **Clarification Required:** true

## Tars Tarkas (mentioned father figure)
- **Asset ID:** tars_tarkas_father
- **Canonical Character ID:** CH015 Tars Tarkas
- **Aliases:** None
- **Fully Identified:** false
- **Manual Description Required:** true
- **Clarification Required:** true

## Tal Hajus (mentioned torturer)
- **Asset ID:** tal_hajus_torturer
- **Canonical Character ID:** CH015 Tal Hajus
- **Aliases:** None
- **Fully Identified:** false
- **Manual Description Required:** true
- **Clarification Required:** true

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter text.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# Protagonist (John Carter)

**Chapter Role:** Main character recovering consciousness after being stabbed by Zad.

**Physical Presence:** Referenced throughout chapter, not visually detailed.

**Physical Description:** Sparse information provided in source material. Character appears to be male based on narrative context but lacks specific physical descriptors.

**Costume/Silhouette:** No costume details available in chapter text.

**Continuity-Critical Traits:** Central figure in Dejah Thoris's grief storyline and Sola's parent story revelation.

**Uncertainty Notes:** Physical form, appearance, and origin remain undefined in this chapter. Manual description required for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: zad_weapon_wielder

canonical_character_id: CH015 Zad

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Minimal physical description provided in chapter text.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the weapon wielder's physical form and appearance?

[[SECTION markdown]]

# Zad (Weapon Wielder)

**Chapter Role:** Character who stabbed John Carter with a blade.

**Physical Presence:** Referenced as weapon wielder, not visually detailed.

**Physical Description:** Sparse information provided in source material. Character appears to be associated with weapon but lacks specific physical descriptors.

**Costume/Silhouette:** No costume details available in chapter text.

**Continuity-Critical Traits:** Associated with Sarkoja's weapon and John Carter's wound recovery.

**Uncertainty Notes:** Physical form, appearance, and origin remain undefined in this chapter. Manual description required for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja_antagonist

canonical_character_id: CH015 Sarkoja

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Mentioned in relation to weapon but no physical description provided.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the antagonist's physical form and appearance?

[[SECTION markdown]]

# Sarkoja (Antagonist)

**Chapter Role:** Character whose weapon was used to stab John Carter.

**Physical Presence:** Referenced in chapter summary, not visually detailed.

**Physical Description:** Sparse information provided in source material. Character appears to be antagonist but lacks specific physical descriptors.

**Costume/Silhouette:** No costume details available in chapter text.

**Continuity-Critical Traits:** Associated with weapon wielder and Tal Hajus imprisonment storyline.

**Uncertainty Notes:** Physical form, appearance, and origin remain undefined in this chapter. Manual description required for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris_weeping

canonical_character_id: CH015 Dejah Thoris

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Mentioned as weeping figure but no physical description provided.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the weeping figure's physical form and appearance?

[[SECTION markdown]]

# Dejah Thoris (Weeping Figure)

**Chapter Role:** Character who is weeping in grief, believing John Carter dead.

**Physical Presence:** Referenced as weeping figure, not visually detailed.

**Physical Description:** Sparse information provided in source material. Character appears to be female based on narrative context but lacks specific physical descriptors.

**Costume/Silhouette:** No costume details available in chapter text.

**Continuity-Critical Traits:** Central to John Carter's emotional storyline and pride-driven grief.

**Uncertainty Notes:** Physical form, appearance, and origin remain undefined in this chapter. Manual description required for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola_storyteller

canonical_character_id: CH015 Sola

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Storyteller role mentioned but no physical description provided.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the storyteller's physical form and appearance?

[[SECTION markdown]]

# Sola (Storyteller)

**Chapter Role:** Character who tells story about her parents to John Carter.

**Physical Presence:** Referenced as storyteller, not visually detailed.

**Physical Description:** Sparse information provided in source material. Character appears to be female based on narrative context but lacks specific physical descriptors.

**Costume/Silhouette:** No costume details available in chapter text.

**Continuity-Critical Traits:** Reveals her father is Tars Tarkas and mother's imprisonment by Tal Hajus.

**Uncertainty Notes:** Physical form, appearance, and origin remain undefined in this chapter. Manual description required for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas_father

canonical_character_id: CH015 Tars Tarkas

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Mentioned as father figure but no physical description provided.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the father figure's physical form and appearance?

[[SECTION markdown]]

# Tars Tarkas (Father Figure)

**Chapter Role:** Character mentioned as Sola's father, warrior who waited to avenge wife.

**Physical Presence:** Referenced in story context, not visually detailed.

**Physical Description:** Sparse information provided in source material. Character appears to be male based on narrative context but lacks specific physical descriptors.

**Costume/Silhouette:** No costume details available in chapter text.

**Continuity-Critical Traits:** Associated with Sola's mother's imprisonment and Tal Hajus storyline.

**Uncertainty Notes:** Physical form, appearance, and origin remain undefined in this chapter. Manual description required for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tal_hajus_torturer

canonical_character_id: CH015 Tal Hajus

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Mentioned as torturer but no physical description provided.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the torturer's physical form and appearance?

[[SECTION markdown]]

# Tal Hajus (Torturer)

**Chapter Role:** Character who imprisoned and tortured Sola's mother.

**Physical Presence:** Referenced in story context, not visually detailed.

**Physical Description:** Sparse information provided in source material. Character appears to be antagonist but lacks specific physical descriptors.

**Costume/Silhouette:** No costume details available in chapter text.

**Continuity-Critical Traits:** Associated with Sola's mother's imprisonment and death without revealing father's name.

**Uncertainty Notes:** Physical form, appearance, and origin remain undefined in this chapter. Manual description required for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
