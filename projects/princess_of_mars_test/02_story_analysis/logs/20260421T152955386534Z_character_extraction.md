# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:29:55.387033+00:00
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

**Setting:** An Arizona cave (Earth) and a study overlooking the Hudson River (Earth).

**Characters:**
- **John Carter:** The protagonist, now living on Earth, reflecting on his past.
- **The Mummified Woman:** A deceased figure found in the cave.
- **Dejah Thoris (Mentioned):** Carter's lost love on Mars.
- **A Little Boy and a Black-Haired Woman (Vision/Imagination):** Possible manifestations of Dejah Thoris and a child.

**Events:**
- John Carter awakens in a dark cave in Arizona, wearing strange, stiff garments.
- He discovers the mummified remains of an old woman huddled over a charcoal burner containing green powder, surrounded by hanging human skeletons.
- Upon exiting the cave, Carter realizes he is back on Earth, looking out over the Arizona landscape.
- A temporal jump occurs: Carter reflects on his life twenty years after his arrival on Mars. He has become wealthy from an untouched mine but remains consumed by longing for Mars and Dejah Thoris.
- In his study by the Hudson, Carter experiences a vision or a profound feeling that Dejah Thoris and a child are waiting for him across space, suggesting a potential reunion or spiritual connection.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH028

- [john_carter](#john_carter)
- [mummified_woman](#mummified_woman)
- [dejah_thoris](#dejah_thoris)
- [visionary_child](#visionary_child)
- [black_haired_woman](#black_haired_woman)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: John Carter

aliases: Protagonist

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

**Description:** A man living on Earth, currently wealthy and residing in a study overlooking the Hudson River. He has experienced significant time passing (reflecting on life twenty years after Mars).

**Visual Cues:** Wealthy attire (implied by setting), reflective/melancholic expression.

**Prompt Phrases:** middle-aged man, wealthy gentleman, contemplative, Hudson River study setting.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: mummified_woman

canonical_character_id: The Mummified Woman

aliases: Old woman, deceased figure

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only described as a mummified remains of an old woman.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Mummified Woman
**Role:** Found Object / Deceased Figure

**Status:** Physically Present (as remains)

**Description:** An old woman found in a dark Arizona cave, mummified. She was discovered huddled over a charcoal burner containing green powder.

**Visual Cues:** Mummified skin, ancient clothing/remains, huddled posture.

**Uncertainty Note:** Specific facial features and exact clothing are lost to mummification; visual representation should focus on the desiccated, ancient state.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: Lost love

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is mentioned/envisioned but no specific physical traits are provided in this chapter.

clarification_required: true

clarification_reason: Physical appearance is not detailed in the text.

clarification_question: What are the canonical physical characteristics of Dejah Thoris (hair color, eye color, build)?

[[SECTION markdown]]

# Dejah Thoris
**Role:** Referenced / Visionary Figure

**Status:** Referenced / Uncertain (Vision)

**Description:** The lost love of John Carter from Mars. She appears in a vision or profound feeling experienced by Carter.

**Visual Cues:** Associated with a "black-haired woman" in the vision.

**Uncertainty Note:** Physical details are highly dependent on established lore not present in this specific text segment.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: visionary_child

canonical_character_id: Visionary Child

aliases: The child

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only identified as a "child" in a vision.

clarification_required: true

clarification_reason: No age, gender, or physical traits provided.

clarification_question: What is the approximate age and appearance of the child in the vision?

[[SECTION markdown]]

# Visionary Child
**Role:** Visionary Figure

**Status:** Uncertain (Vision/Imagination)

**Description:** A child appearing in a vision alongside a black-haired woman, suggesting a connection to Dejah Thoris.

**Visual Cues:** None provided.

**Uncertainty Note:** Character is purely conceptual/visionary in this chapter; appearance is unknown.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: black_haired_woman

canonical_character_id: Black-Haired Woman

aliases: Vision of Dejah Thoris

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only identified by hair color in a vision.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Black-Haired Woman
**Role:** Visionary Figure

**Status:** Uncertain (Vision/Imagination)

**Description:** A woman with black hair appearing in a vision or profound feeling experienced by Carter. Likely represents Dejah Thoris.

**Visual Cues:** Black hair.

**Uncertainty Note:** Very sparse description; facial features and clothing are not specified.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
