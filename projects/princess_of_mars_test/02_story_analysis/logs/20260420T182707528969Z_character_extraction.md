# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:27:07.528969+00:00
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

Chapter id: CH028

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

The protagonist awakens in a dark cave wearing strange, stiff garments. Upon exploring with a match, he discovers the mummified remains of an old woman tending a charcoal burner and a gruesome display of human skeletons hanging from the cave ceiling by rawhide thongs. 

Emerging from the cave onto a ledge, he realizes with shock that he is back on Earth in Arizona, not Mars. He reflects on his ten-year separation from Mars and his enduring love for Dejah Thoris, wondering if she survived the atmospheric crisis on her planet. The narrative shifts to twenty years after his arrival on Mars, as an older version of the protagonist sits in his study overlooking the Hudson, experiencing a vision of Dejah Thoris, a young boy, and a creature with a heart of gold, sensing that he will soon be reunited with them.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [Protagonist](#protagonist)
- [Old Woman (Mummified)](#old-woman-mummified)
- [Dejah Thoris](#dejah-thoris)
- [Young Boy](#young-boy)
- [Creature with a Heart of Gold](#creature-with-a-heart-of-gold)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: Protagonist

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance is not described in the present, only his clothing (strange, stiff garments) and his age progression from young to old.

clarification_required: true

clarification_reason: Identity and physical features are unknown.

clarification_question: What is the protagonist's specific physical appearance and facial features?

[[SECTION markdown]]

# Protagonist
**Role:** Main Character / Narrator

**Status:** Physically Present (Young and Old)

**Physical Description:** 
- Young version: Wearing "strange, stiff garments."
- Older version: Sitting in a study overlooking the Hudson.

**Costume/Silhouette:** Stiff, unusual clothing during the cave sequence.

**Uncertainty Notes:** No facial features, hair color, or specific body type are provided for either age stage.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: old_woman_mummified

canonical_character_id: Old Woman (Mummified)

aliases: Charcoal burner

is_fully_identified: true

manual_description_required: true

manual_description_reason: Character is a mummified corpse; specific facial or body details are absent.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Old Woman (Mummified)
**Role:** Background/Environmental Detail

**Status:** Physically Present (Deceased)

**Physical Description:** Mummified remains of an old woman.

**Costume/Silhouette:** Associated with charcoal burning activities.

**Uncertainty Notes:** Specific clothing or mummification state details are not provided.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is only referenced/envisioned; no physical description provided.

clarification_required: true

clarification_reason: No visual data available for character design.

clarification_question: What are the physical characteristics and attire of Dejah Thoris?

[[SECTION markdown]]

# Dejah Thoris
**Role:** Love Interest / Visionary Figure

**Status:** Referenced / Envisioned

**Physical Description:** Unknown.

**Costume/Silhouette:** Unknown.

**Uncertainty Notes:** Character exists only in the protagonist's memory and visions.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: young_boy

canonical_character_id: Young Boy

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is a vague vision with no descriptive traits.

clarification_required: true

clarification_reason: No visual information provided.

clarification_question: What does the young boy look like?

[[SECTION markdown]]

# Young Boy
**Role:** Visionary Figure

**Status:** Envisioned

**Physical Description:** A young boy.

**Costume/Silhouette:** Unknown.

**Uncertainty Notes:** Extremely sparse information; part of a vision.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: creature_heart_of_gold

canonical_character_id: Creature with a Heart of Gold

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is an abstract concept/vision without physical form.

clarification_required: true

clarification_reason: No visual information provided.

clarification_question: What species or physical form does this creature take?

[[SECTION markdown]]

# Creature with a Heart of Gold
**Role:** Visionary Figure

**Status:** Envisioned

**Physical Description:** Unknown; described only by temperament/metaphor.

**Costume/Silhouette:** Unknown.

**Uncertainty Notes:** Character is purely conceptual in this chapter.

[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
