# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:48:03.402729+00:00
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

Chapter id: CH007

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
The protagonist accompanies Sola and a massive military cavalcade—consisting of two hundred decorated chariots drawn by enormous beasts—to a remote incubator located on a dead sea bottom. Upon arrival, the chieftain Lorquas Ptomel and Tars Tarkas oversee the hatching process. The protagonist demonstrates his physical prowess by leaping over parked chariots to impress the leaders. As the young Martians emerge from the incubator, they are captured in a ritualistic gauntlet formed by women and youths. The protagonist observes the cold, utilitarian nature of Martian child-rearing: offspring are communal, raised by foster mothers to be warriors, and any defective specimens are promptly killed. Following the ceremony, the community returns to their territory, and the protagonist spends time under Sola's tutelage, learning the language and honing his telepathic skills.

**Characters:**
* **Protagonist:** An Earthman who has mastered Martian walking and is rapidly learning the language and telepathy; he discovers his mind is unreadable by Martians.
* **Sola:** A female Martian who acts as a guide and foster mother to a newly hatched male Martian, while also caring for the protagonist.
* **Tars Tarkas:** A Martian warrior/leader who interacts with the protagonist.
* **Lorquas Ptomel (Jed):** An enormous chieftain who oversees the incubator ceremony.
* **The Young Martian:** A physically perfect, four-foot-tall male captured by Sola; he becomes a rival to the protagonist in their shared education.

**Settings:**
* **The Plaza:** The central hub of the Martian community where chariots are harnessed.
* **The Dead Sea Bottom:** A level expanse where the incubator is located and where the hatching ceremony takes place.
* **The Incubator:** A remote, specialized structure used to hatch eggs via solar rays after a five-year incubation period.
* **The Dead City:** The location where the protagonist resides during his periods of idleness and education.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter CH007

- [Protagonist](#protagonist)
- [Sola](#sola)
- [Tars Tarkas](#tars-tarkas)
- [Lorquas Ptomel](#lorquas-ptomel)
- [The Young Martian](#the-young-martian)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH001 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance, clothing, and specific human features are not described in this chapter.

clarification_required: true

clarification_reason: Needs physical profile for consistent rendering.

clarification_question: What is the protagonist's hair color, eye color, build, and current attire?

[[SECTION markdown]]

# Protagonist
**Role:** Main Character / Observer

**Status:** Physically Present

**Physical Description:** 
An Earthman capable of significant physical feats (leaping over chariots). He has mastered Martian walking styles. His mind is noted as being unreadable by the local Martians.

**Costume/Silhouette:** 
Unknown.

**Prompting Phrases:** 
Human male, athletic build, Earthling, telepathic capability.

**Uncertainty Notes:** 
No visual details regarding facial features or clothing are provided in this text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH002 Sola

aliases: Guide, Foster Mother

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical traits or clothing details provided.

clarification_required: true

clarification_reason: Needs visual identification for Martian female phenotype.

clarification_question: What is Sola's physical appearance, height, and typical attire?

[[SECTION markdown]]

# Sola
**Role:** Guide and Mentor

**Status:** Physically Present

**Physical Description:** 
A female Martian. She acts as a guide to the protagonist and serves as a foster mother to a newly hatched male.

**Costume/Silhouette:** 
Unknown.

**Prompting Phrases:** 
Martian female, caregiver, mentor, telepathic.

**Uncertainty Notes:** 
Specific Martian anatomy or clothing is not detailed in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH003 Tars Tarkas

aliases: Martian Leader

is_fully_identified: false

manual_description_required: true

manual_description_reason: While identified as a warrior/leader, no specific physical description is provided.

clarification_required: true

clarification_reason: Needs visual details of his Martian physiology and armor/clothing.

clarification_question: What does Tars Tarkas look like physically?

[[SECTION markdown]]

# Tars Tarkas
**Role:** Martian Warrior/Leader

**Status:** Physically Present

**Physical Description:** 
A Martian warrior and leader who oversees the incubator hatching process.

**Costume/Silhouette:** 
Unknown.

**Prompting Phrases:** 
Martian warrior, authoritative, leader, high-ranking Martian.

**Uncertainty Notes:** 
Visual details of his specific Martian species traits are missing.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: CH004 Lorquas Ptomel

aliases: Jed, Chieftain

is_fully_identified: false

manual_description_required: true

manual_description_reason: Described as "enormous," but lacks specific facial or textural details.

clarification_required: false

clarification_reason: ""

clarification_question: ""

[[SECTION markdown]]

# Lorquas Ptomel
**Role:** Chieftain

**Status:** Physically Present

**Physical Description:** 
An enormous Martian chieftain who oversees the incubator ceremony at the dead sea bottom.

**Costume/Silhouette:** 
Unknown, but likely ceremonial or high-status.

**Prompting Phrases:** 
Enormous Martian, chieftain, imposing presence, ritual leader.

**Uncertainty Notes:** 
"Enormous" is the only scale descriptor provided; specific features are unknown.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: young_martian

canonical_character_id: CH005 Young Martian

aliases: Rival

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

[[SECTION markdown]]

# The Young Martian
**Role:** Protagonist's Rival / Student

**Status:** Physically Present

**Physical Description:** 
A physically perfect male Martian, approximately four feet tall. He is a newly hatched specimen from the incubator.

**Costume/Silhouette:** 
Likely unclothed or minimally dressed as a newborn/youth.

**Prompting Phrases:** 
Four-foot-tall Martian, physically perfect, young male Martian, newly hatched.

**Uncertainty Notes:** 
Specific species morphology (e.g., number of limbs, skin texture) is not explicitly detailed in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
